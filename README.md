Sistema de Reservaciones de Hotel

Aplicación web para la gestión de reservaciones de un hotel.
El sistema permite a los usuarios registrarse, iniciar sesión y realizar reservaciones de habitaciones, mientras que la aplicación administra la información utilizando una base de datos relacional.

El proyecto está desarrollado utilizando Python con Flask para el backend, junto con HTML, CSS y JavaScript para el frontend, y SQL para la gestión de la base de datos.

Tecnologías utilizadas

Python

Flask

HTML5

CSS3

JavaScript

SQL

SQLAlchemy

Estructura del proyecto
reservaciones_app/
│
├── app/                    # Carpeta principal de la aplicación Flask
│
│   ├── static/             # Archivos estáticos
│   │   ├── css/            # Estilos personalizados
│   │   └── js/             # JavaScript del lado del cliente
│
│   ├── templates/          # Plantillas HTML renderizadas por Flask
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── dashboard.html
│   │   └── reservar.html
│
│   ├── __init__.py         # Inicializa la aplicación Flask
│   ├── routes.py           # Definición de las rutas/endpoints
│   ├── models.py           # Modelos de base de datos con SQLAlchemy
│   └── forms.py            # Formularios usando Flask-WTF
│
├── database/
│   └── schema.sql          # Script para crear las tablas en la base de datos
│
├── run.py                  # Punto de entrada para ejecutar la aplicación
└── requirements.txt        # Dependencias del proyecto
Modelos de Datos

Los modelos definen la estructura de los datos y cómo se almacenan en la base de datos.

Usuario

Representa a los usuarios del sistema.

Incluye campos como:

nombre

correo

contraseña encriptada

También contiene métodos para:

establecer contraseña

verificar contraseña

Reservación

Representa las reservaciones realizadas en el hotel.

Campos principales:

nombre del cliente

correo electrónico

fechas de reservación

habitación seleccionada

cantidad de personas

LoginForm

Define el formulario utilizado para el proceso de inicio de sesión del usuario.

Rutas (Routes)

Las rutas definen los endpoints de la aplicación y controlan la lógica de interacción entre el usuario y el sistema.

Ejemplos de rutas:

/login → inicio de sesión

/dashboard → panel principal del usuario

/reservar → formulario para realizar una reservación

Cada ruta procesa la solicitud del usuario, interactúa con los modelos de datos y renderiza las plantillas HTML correspondientes.

Base de Datos

El sistema utiliza una base de datos relacional administrada mediante SQLAlchemy.

El archivo:

database/schema.sql

contiene las instrucciones SQL necesarias para crear las tablas requeridas por la aplicación.

Ejecución del proyecto

Clonar el repositorio

git clone https://github.com/tu-usuario/reservaciones_app.git

Acceder al directorio del proyecto

cd reservaciones_app

Instalar dependencias

pip install -r requirements.txt

Ejecutar la aplicación

python run.py

Autor

Jefferson Gómez
Estudiante de Ingeniería en Sistemas
Desarrollador de Software
