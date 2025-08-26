from app import db

class habitacion(db.Model):
    __tablename__ = 'habitaciones'

    id = db.Column('id', db.Integer, primary_key=True)
    tipo_habitacion = db.Column('tipo_habitacion', db.String(50), nullable=False)
    precio = db.Column('precio', db.Float, nullable=False)
    descripcion = db.Column('descripcion', db.String(255), nullable=True)

    def __repr__(self):
        return f"<Habitacion {self.tipo_habitacion} - {self.precio}>"
