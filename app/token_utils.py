# tokenUtils.py

from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadSignature
from app import app  # importar la instancia de Flask para usar app.secret_key

serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])

def generar_token(email):
    # Salt unificado para restablecer contraseña
    return serializer.dumps(email, salt='password-reset-salt')

def validar_token(token, expiracion=3600):
    try:
        # Usamos el mismo salt que en generar_token
        email = serializer.loads(token, salt='password-reset-salt', max_age=expiracion)
        return email
    except (SignatureExpired, BadSignature):
        return None
