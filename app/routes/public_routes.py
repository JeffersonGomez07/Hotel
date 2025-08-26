from flask import Blueprint, render_template

public_bp = Blueprint('public', __name__)

@public_bp.route('/')
def index():
    return render_template('index.html')

@public_bp.route('/habitaciones')
def habitaciones():
    return render_template('habitaciones.html')

@public_bp.route('/servicios')
def servicios():
    return render_template('servicios.html')

@public_bp.route('/contacto')
def contacto():
    return render_template('contacto.html')

@public_bp.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

@public_bp.route('/galeria')
def galeria():
    return render_template('galeria.html')

@public_bp.route('/habitacion/individual')
def habitacion_individual():
    return render_template("habitaciones/habitacion_individual.html")


@public_bp.route('/habitacion/doble')
def habitacion_doble():
    return render_template("habitaciones/habitacion_doble.html")

@public_bp.route('/habitacion/suite')
def habitacion_suite():
    return render_template("habitaciones/habitacion_suite.html")

@public_bp.route('/restaurante')
def restaurante():
    return render_template('restaurante.html')
