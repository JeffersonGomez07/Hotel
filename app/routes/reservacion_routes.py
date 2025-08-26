from flask import Blueprint, render_template, request, jsonify, session, flash, redirect, url_for
from app import db, csrf
from app.models import reservacion, fecha_bloqueada
from datetime import datetime, timedelta

reservacion_bp = Blueprint('reservacion', __name__)

@csrf.exempt
@reservacion_bp.route('/reservaciones', methods=['GET', 'POST'])
def reservaciones():
    # Validar que el usuario esté logueado
    if 'usuario_id' not in session:
        flash('Debes iniciar sesión para hacer una reservación.', 'warning')
        return redirect(url_for('auth.login'))

    if request.method == 'GET':
        return render_template('reservaciones.html')

    # POST: recibir JSON con datos de reservación
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Datos no válidos'}), 400

    nombre = data.get('nombre') 
    email = data.get('email')
    fecha_llegada = data.get('checkin')
    fecha_salida = data.get('checkout')
    tipo_habitacion = data.get('habitacion')
    adultos = data.get('adultos')
    ninos = data.get('ninos')

    campos_requeridos = [nombre, email, fecha_llegada, fecha_salida, tipo_habitacion]
    if not all(campos_requeridos) or adultos is None or ninos is None:
        return jsonify({'error': 'Faltan campos requeridos'}), 400

    try:
        fecha_llegada_dt = datetime.strptime(fecha_llegada, '%Y-%m-%d').date()
        fecha_salida_dt = datetime.strptime(fecha_salida, '%Y-%m-%d').date()
        adultos_int = int(adultos)
        ninos_int = int(ninos)

        if fecha_llegada_dt < datetime.today().date():
            return jsonify({'error': 'La fecha de llegada no puede ser anterior a hoy.'}), 400

        if fecha_salida_dt <= fecha_llegada_dt:
            return jsonify({'error': 'La fecha de salida debe ser posterior a la de llegada.'}), 400

        # Validar que ninguna fecha en el rango esté bloqueada
        fechas_en_rango = [fecha_llegada_dt + timedelta(days=i) for i in range((fecha_salida_dt - fecha_llegada_dt).days)]

        fecha_bloqueada = fecha_bloqueada.query.filter(fecha_bloqueada.fecha.in_(fechas_en_rango)).first()
        if fecha_bloqueada:
            return jsonify({'error': f'La fecha {fecha_bloqueada.fecha.strftime("%Y-%m-%d")} está bloqueada y no puede reservarse.'}), 400

        # Crear la nueva reservación
        nueva_reserva = reservacion(
            nombre_cliente=nombre,
            email=email,
            fecha_llegada=fecha_llegada_dt,
            fecha_salida=fecha_salida_dt,
            tipo_habitacion=tipo_habitacion,
            adultos=adultos_int,
            ninos=ninos_int
        )

        db.session.add(nueva_reserva)
        db.session.commit()

        return jsonify({'mensaje': 'Reservación registrada correctamente.'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Error al guardar la reservación: {str(e)}'}), 500