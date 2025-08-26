from app import db
from datetime import datetime

class fecha_bloqueada(db.Model):
    __tablename__ = 'fechas_bloqueadas'
    
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False, unique=True)
    motivo = db.Column(db.String(255), nullable=False)
    bloqueada_por = db.Column(db.String(100))
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
