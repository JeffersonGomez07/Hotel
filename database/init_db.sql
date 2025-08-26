# Script SQL para crear las tablas de la base de datos




CREATE TABLE dbo.usuarios (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nombre NVARCHAR(100) NOT NULL,
    email NVARCHAR(100) NOT NULL UNIQUE,
    password NVARCHAR(255) NOT NULL,
    rol NVARCHAR(50) NOT NULL DEFAULT 'usuario',  -- Nueva columna con valor por defecto
    fecha_registro DATETIME DEFAULT GETDATE()
);


UPDATE dbo.usuarios
SET rol = 'admin'
WHERE email = 'jeffermp40@gmail.com';


CREATE TABLE fechas_bloqueadas (
    id INT PRIMARY KEY IDENTITY(1,1),
    fecha DATE NOT NULL,
    motivo VARCHAR(255),
    bloqueada_por VARCHAR(100),
    fecha_registro DATETIME DEFAULT GETDATE()
);

CREATE TABLE habitaciones (
    id INT IDENTITY(1,1) PRIMARY KEY,
    tipo_habitacion VARCHAR(50) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    descripcion TEXT NULL
);
CREATE TABLE reservaciones (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nombre_cliente VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    fecha_llegada DATE NOT NULL,
    fecha_salida DATE NOT NULL,
    tipo_habitacion VARCHAR(50) NOT NULL,
    adultos INT NOT NULL,
    ninos INT NOT NULL,
    fecha_registro DATETIME DEFAULT GETDATE(),
    estado VARCHAR(20) DEFAULT 'Pendiente'
);
