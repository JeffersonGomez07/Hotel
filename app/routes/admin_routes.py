from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from app import db, csrf
from app.models import reservacion, habitacion, fecha_bloqueada
from datetime import datetime

admin_bp = Blueprint('admin', __name__)

# ------------------- DASHBOARD -------------------
@csrf.exempt
@admin_bp.route('/dashboard')
def dashboard():
    if 'usuario_rol' not in session or session['usuario_rol'] != 'admin':
        flash('Acceso no autorizado.', 'danger')
        return redirect(url_for('auth.login'))

    reservaciones = reservacion.query.all()
    total_reservaciones = len(reservaciones)
    total_habitaciones = habitacion.query.count()
    reservas_pendientes = reservacion.query.filter_by(estado='pendiente').count()
    reservas_confirmadas = reservacion.query.filter_by(estado='confirmada').count()

    return render_template(
        'admin/dashboard.html',
        reservaciones=reservaciones,
        total_reservaciones=total_reservaciones,
        total_habitaciones=total_habitaciones,
        reservas_pendientes=reservas_pendientes,
        reservas_confirmadas=reservas_confirmadas
    )

# ------------------- GESTIONAR RESERVAS -------------------
@csrf.exempt
@admin_bp.route('/gestionar_reservas')
def gestionar_reservas():
    if 'usuario_rol' not in session or session['usuario_rol'] != 'admin':
        flash('Acceso no autorizado.', 'danger')
        return redirect(url_for('auth.login'))

    reservaciones = reservacion.query.all()
    return render_template('admin/gestionar_reservas.html', reservaciones=reservaciones)

# ------------------- GESTIONAR FECHAS -------------------
@csrf.exempt
@admin_bp.route('/gestionar_fechas', methods=['GET'])
def gestionar_fechas():
    if 'usuario_rol' not in session or session['usuario_rol'] != 'admin':
        flash('Acceso no autorizado.', 'danger')
        return redirect(url_for('auth.login'))  # Solo redirige si no es admin

    fechas = fecha_bloqueada.query.all()
    return render_template('admin/gestionar_fechas.html', fechas=fechas)

# ------------------- BLOQUEAR FECHA -------------------
@csrf.exempt
@admin_bp.route('/admin/bloquear_fecha', methods=['POST'])
def bloquear_fecha():
    if 'usuario_rol' not in session or session['usuario_rol'] != 'admin':
        flash('Acceso no autorizado.', 'danger')
        return redirect(url_for('auth.login'))

    fecha_str = request.form.get('fecha')
    if not fecha_str:
        flash('Debe seleccionar una fecha.', 'warning')
        return redirect(url_for('admin.gestionar_fechas'))

    try:
        fecha_dt = datetime.strptime(fecha_str, '%Y-%m-%d').date()
        existente = fecha_bloqueada.query.filter_by(fecha=fecha_dt).first()
        if existente:
            flash('La fecha ya está bloqueada.', 'warning')
        else:
            nueva_fecha = fecha_bloqueada(
                fecha=fecha_dt,
                motivo=request.form.get('motivo') or 'Bloqueo administrativo',
                bloqueada_por=session.get('usuario_nombre', 'admin')
            )
            db.session.add(nueva_fecha)
            db.session.commit()
            flash('Fecha bloqueada correctamente.', 'success')
    except Exception as e:
        flash(f'Error al bloquear fecha: {str(e)}', 'danger')

    return redirect(url_for('admin.gestionar_fechas'))

# ------------------- DESBLOQUEAR FECHA -------------------
@csrf.exempt
@admin_bp.route('/admin/desbloquear_fecha/<int:fecha_id>', methods=['POST'])
def desbloquear_fecha(fecha_id):
    if 'usuario_rol' not in session or session['usuario_rol'] != 'admin':
        flash('Acceso no autorizado.', 'danger')
        return redirect(url_for('auth.login'))

    fecha = fecha_bloqueada.query.get_or_404(fecha_id)
    try:
        db.session.delete(fecha)
        db.session.commit()
        flash('Fecha desbloqueada correctamente.', 'success')
    except Exception as e:
        flash(f'Error al desbloquear fecha: {str(e)}', 'danger')

    return redirect(url_for('admin.gestionar_fechas'))

# ------------------- GESTIONAR HABITACIONES -------------------
@csrf.exempt
@admin_bp.route('/gestionar_habitaciones', methods=['GET'])
def gestionar_habitaciones():
    if 'usuario_rol' not in session or session['usuario_rol'] != 'admin':
        flash('Acceso no autorizado.', 'danger')
        return redirect(url_for('auth.login'))

    habitaciones = habitacion.query.all()
    return render_template('admin/gestionar_habitaciones.html', habitaciones=habitaciones)

@csrf.exempt
@admin_bp.route('/editar_reserva/<int:id>', methods=['GET', 'POST'])
def editar_reserva(id):
    # Buscar la reserva por su ID o devolver 404 si no existe
    reserva = reservacion.query.get_or_404(id)

    if request.method == 'POST':
        try:
            # Actualizar datos desde el formulario
            reserva.nombre_cliente = request.form['nombre_cliente']
            reserva.email = request.form['email']
            reserva.fecha_llegada = request.form['fecha_llegada']
            reserva.fecha_salida = request.form['fecha_salida']
            reserva.tipo_habitacion = request.form['tipo_habitacion']
            reserva.adultos = request.form['adultos']
            reserva.ninos = request.form['ninos']
            reserva.estado = request.form['estado']

            # Guardar cambios
            db.session.commit()
            flash('Reservación actualizada correctamente.', 'success')
            return redirect(url_for('admin.gestionar_reservas'))

        except Exception as e:
            db.session.rollback()
            flash(f'Error al actualizar la reservación: {str(e)}', 'danger')

    # Mostrar formulario con los datos actuales
    return render_template('admin/editar_reserva.html', reserva=reserva)
