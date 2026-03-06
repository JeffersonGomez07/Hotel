Sistemas de reservaciones de un hotel
JS,HTML,CSS,PYTHON Y SQL

reservaciones_app/
│
├── app/                    # Carpeta principal de la aplicación Flask
│   ├── static/             # Archivos estáticos (no cambian en el servidor)
│   │   ├── css/            # Tus estilos personalizados (ej. styles.css)
│   │   └── js/             # Archivos JavaScript del lado cliente (ej. validaciones, calendario)
│   ├── templates/          # Archivos HTML (renderizados por Flask)
│   │   ├── base.html       # Plantilla base con header/footer comunes
│   │   ├── login.html      # Formulario de inicio de sesión
│   │   ├── dashboard.html  # Página principal tras iniciar sesión (calendario, reservas)
│   │   └── reservar.html   # Formulario para hacer una reservación
│   ├── __init__.py         # Inicializa la app Flask (crea app, configura DB, etc.)
│   ├── routes.py           # Todas las rutas/endpoints de la app (ej. /login, /reservar)
│   ├── models.py           # Definición de la base de datos usando SQLAlchemy
│   └── forms.py            # Definición de formularios con Flask-WTF (login, reserva)
│
├── database/
│   └── schema.sql          # Script SQL para crear las tablas de la base de datos
│
├── app.py                  # Punto de entrada: corre la aplicación Flask
└── requirements.txt        # Lista de dependencias de Python (Flask, etc.)

Models: define la estrcutura estructura de los datos de la app y como se guardan en la BD.
Models/             
│   │   ├── __init__: funcion es inicializar los atributos del modelo cuando creas una nueva instancia     
│   │   └── LoginForm: 
│   │   ├── Reservacion: Representa las reservaciones de hotel en la base de datos, con campos como nombre, correo, fechas, habitación y cantidad de personas.
│   │   └── Usuario: El modelo Usuario representa a los usuarios del sistema, almacenando su nombre, correo y contraseña encriptada, e incluye métodos para establecer y verificar contraseñas.
Routes/             
│   │   ├── routes.py: Definicion de rutas

