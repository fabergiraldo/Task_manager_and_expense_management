CREATE USER 'user_ptyhon'@'localhost' IDENTIFIED BY 'Clas3s1Nt2024_!';
GRANT CREATE, INSERT, UPDATE, DELETE, SELECT, FILE, EXECUTE ON *.* TO 'user_ptyhon'@'localhost' WITH GRANT OPTION;

-- Creación de la base de datos
drop database if exists gestion_gastos;
create database gestion_gastos;
use gestion_gastos;

-- Tabla Usuarios
CREATE TABLE usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) UNIQUE NOT NULL,
    contrasena VARCHAR(255) NOT NULL,
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Tabla Categorías
CREATE TABLE categorias (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(255)
);

-- Tabla Monedas
CREATE TABLE monedas (
    id_moneda INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    codigo VARCHAR(10),
    simbolo VARCHAR(10)
);

-- Tabla Cuentas Bancarias
CREATE TABLE cuentas_bancarias (
    id_cuenta INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    nombre_banco VARCHAR(100),
    numero_cuenta VARCHAR(50),
    saldo DECIMAL(12,2),
    id_moneda INT,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_moneda) REFERENCES monedas(id_moneda)
);

-- Tabla Tarjetas
CREATE TABLE tarjetas (
    id_tarjeta INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    nombre_tarjeta VARCHAR(100),
    tipo ENUM('Debito','Credito'),
    numero_tarjeta VARCHAR(20),
    vencimiento DATE,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);

