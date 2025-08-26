from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from app import db, mail, csrf
from app.models import usuario
from flask_mail import Message
import uuid
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)

# ---------------- LOGIN ----------------
@csrf.exempt
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        usuario_encontrado = usuario.query.filter_by(email=email).first()

        if usuario_encontrado and check_password_hash(usuario_encontrado.password, password):
            # Guardar datos en sesión
            session['usuario_id'] = usuario_encontrado.id
            session['usuario_nombre'] = usuario_encontrado.nombre
            session['usuario_rol'] = usuario_encontrado.rol

            flash('Inicio de sesión exitoso', 'success')

            # Redirigir según rol
            if usuario_encontrado.rol == 'admin':
                return redirect(url_for('admin.dashboard'))  # Ruta del admin
            else:
                return redirect(url_for('reservacion.reservaciones'))  # Ruta del cliente
        else:
            flash('Correo o contraseña incorrectos', 'danger')

    return render_template('auth/login.html')


# ---------------- LOGOUT ----------------
@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('Has cerrado sesión correctamente', 'success')
    return redirect(url_for('auth.login'))


# ---------------- REGISTRO ----------------
@csrf.exempt
@auth_bp.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        password = request.form['password']

        usuario_existente = usuario.query.filter_by(email=email).first()
        if usuario_existente:
            flash('El correo ya está registrado', 'danger')
            return redirect(url_for('auth.registro'))

        nuevo_usuario = usuario(
            nombre=nombre,
            email=email,
            password=generate_password_hash(password),
            rol='cliente'  # Por defecto, el usuario nuevo es cliente
        )
        db.session.add(nuevo_usuario)
        db.session.commit()
        flash('Registro exitoso. Inicia sesión.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('auth/registro.html')


# ---------------- RESTABLECER CONTRASEÑA ----------------
@csrf.exempt
@auth_bp.route('/restablecer_contrasena', methods=['GET', 'POST'])
def restablecer_contrasena():
    if request.method == 'POST':
        email = request.form['email']
        usuario_recuperacion = usuario.query.filter_by(email=email).first()

        if usuario_recuperacion:
            token = str(uuid.uuid4())
            usuario_recuperacion.token_recuperacion = token
            db.session.commit()

            msg = Message(
                'Restablecer contraseña',
                sender='tu_correo@gmail.com',
                recipients=[email]
            )
            msg.body = f'Usa este enlace para restablecer tu contraseña: {url_for("auth.cambiar_contrasena", token=token, _external=True)}'
            mail.send(msg)

            flash('Se ha enviado un enlace para restablecer tu contraseña', 'success')
            return redirect(url_for('auth.login'))
        else:
            flash('Correo no encontrado', 'danger')

    return render_template('auth/restablecer_contrasena.html')


# ---------------- CAMBIAR CONTRASEÑA ----------------
@auth_bp.route('/cambiar_contrasena/<token>', methods=['GET', 'POST'])
def cambiar_contrasena(token):
    usuario_obj = usuario.query.filter_by(token_recuperacion=token).first()

    if not usuario_obj:
        flash('Token inválido o expirado', 'danger')
        return redirect(url_for('auth.login'))

    if request.method == 'POST':
        nueva_contrasena = request.form['password']
        usuario_obj.password = generate_password_hash(nueva_contrasena)
        usuario_obj.token_recuperacion = None
        db.session.commit()

        flash('Contraseña actualizada correctamente', 'success')
        return redirect(url_for('auth.login'))

    return render_template('auth/cambiar_contrasena.html', token=token)
