import urllib
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_mail import Mail
from itsdangerous import URLSafeTimedSerializer

# ==============================
# Configuración de la conexión
# ==============================
params = urllib.parse.quote_plus(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=JEFF\\SQLEXPRESS;"
    "Database=Hotel;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

# ==============================
# Inicialización de la app
# ==============================
app = Flask(__name__, static_folder='public')

# ==============================
# Configuraciones de Flask
# ==============================
app.config['SECRET_KEY'] = '1234segura'
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME='jeffgomez489@gmail.com',
    MAIL_PASSWORD='nroucqifwegcrrpi',  # contraseña de app de Gmail
    SQLALCHEMY_DATABASE_URI=f"mssql+pyodbc:///?odbc_connect={params}",
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    SQLALCHEMY_ECHO=True
)

# ==============================
# Inicialización de extensiones
# ==============================
db = SQLAlchemy(app)
csrf = CSRFProtect(app)
mail = Mail(app)
serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])

# ==============================
# Prueba de conexión a la DB
# ==============================
with app.app_context():
    try:
        with db.engine.connect() as conn:
            print("✅ Conexión exitosa a SQL Server")
    except Exception as e:
        print("❌ Error de conexión a SQL Server:", e)

# ==============================
# Importar modelos
# ==============================
from app.models import reservacion, usuario, login, habitacion, fecha_bloqueada

# ==============================
# Importar blueprints y registrarlos
# ==============================
from app.routes.public_routes import public_bp
from app.routes.auth_routes import auth_bp
from app.routes.reservacion_routes import reservacion_bp
from app.routes.admin_routes import admin_bp

app.register_blueprint(public_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(reservacion_bp)
app.register_blueprint(admin_bp, url_prefix='/admin')
