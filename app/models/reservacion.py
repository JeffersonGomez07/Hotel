from app import db
from datetime import datetime

class reservacion(db.Model): # db.model define un modelo de base de datos
    __tablename__ = 'reservaciones' # Nombre de la tabla en la base de datos

    id = db.Column('id', db.Integer, primary_key=True) # Campo ID, clave primaria
    nombre_cliente = db.Column('nombre_cliente', db.String(100), nullable=False)
    email = db.Column('email', db.String(100), nullable=False) # Email del cliente, campo obligatorio
    fecha_llegada = db.Column('fecha_llegada', db.Date, nullable=False) # Fecha de llegada, campo obligatorio
    fecha_salida = db.Column('fecha_salida', db.Date, nullable=False) # Fecha de salida, campo obligatorio
    tipo_habitacion = db.Column('tipo_habitacion', db.String(50), nullable=False) # Tipo de habitación, campo obligatorio
    adultos = db.Column('adultos', db.Integer, nullable=False) # Cantidad de adultos, campo obligatorio
    ninos = db.Column('ninos', db.Integer, nullable=False) # Cantidad de adultos y niños, campos obligatorios
    fecha_registro = db.Column('fecha_registro', db.DateTime, default=datetime.utcnow) # Fecha de registro, por defecto es la fecha actual
    estado = db.Column('estado', db.String(20), default='Pendiente') # Estado de la reservación, por defecto es 'Pendiente'
    
    def __repr__(self): 
        return f"<reservacion {self.nombre_cliente} {self.fecha_llegada} - {self.fecha_salida}>" # Representación del objeto para facilitar la depuración
