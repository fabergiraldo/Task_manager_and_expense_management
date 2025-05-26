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
ALTER TABLE tarjetas MODIFY COLUMN numero_tarjeta VARCHAR(255);


-- Tabla Proveedores
CREATE TABLE proveedores (
    id_proveedor INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    contacto VARCHAR(100),
    telefono VARCHAR(20),
    correo VARCHAR(100)
);

-- Tabla Métodos de Pago
CREATE TABLE metodos_pago (
    id_metodo_pago INT AUTO_INCREMENT PRIMARY KEY,
    metodo VARCHAR(50)
);

-- Tabla Gastos
CREATE TABLE gastos (
    id_gasto INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    fecha DATE,
    monto DECIMAL(12,2),
    descripcion VARCHAR(255),
    id_categoria INT,
    id_moneda INT,
    id_cuenta INT,
    id_tarjeta INT,
    id_proveedor INT,
    id_metodo_pago INT,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria),
    FOREIGN KEY (id_moneda) REFERENCES monedas(id_moneda),
    FOREIGN KEY (id_cuenta) REFERENCES cuentas_bancarias(id_cuenta),
    FOREIGN KEY (id_tarjeta) REFERENCES tarjetas(id_tarjeta),
    FOREIGN KEY (id_proveedor) REFERENCES proveedores(id_proveedor),
    FOREIGN KEY (id_metodo_pago) REFERENCES metodos_pago(id_metodo_pago)
);

-- Tabla Ingresos
CREATE TABLE ingresos (
    id_ingreso INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    fecha DATE,
    monto DECIMAL(12,2),
    descripcion VARCHAR(255),
    id_moneda INT,
    id_cuenta INT,
    id_metodo_pago INT,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_moneda) REFERENCES monedas(id_moneda),
    FOREIGN KEY (id_cuenta) REFERENCES cuentas_bancarias(id_cuenta),
    FOREIGN KEY (id_metodo_pago) REFERENCES metodos_pago(id_metodo_pago)
);

-- Tabla Presupuestos
CREATE TABLE presupuestos (
    id_presupuesto INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    id_categoria INT,
    mes YEAR(4),
    monto DECIMAL(12,2),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria)
);

-- Tabla Facturas
CREATE TABLE facturas (
    id_factura INT AUTO_INCREMENT PRIMARY KEY,
    id_gasto INT,
    id_proveedor INT,
    ruta_archivo VARCHAR(255),
    FOREIGN KEY (id_gasto) REFERENCES gastos(id_gasto),
    FOREIGN KEY (id_proveedor) REFERENCES proveedores(id_proveedor)
);

-- Tabla Notificaciones
CREATE TABLE notificaciones (
    id_notificacion INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    mensaje VARCHAR(255),
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    leido BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);

-- Tabla Transacciones
CREATE TABLE transacciones (
    id_transaccion INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    tipo ENUM('Ingreso','Gasto'),
    id_categoria INT,
    id_moneda INT,
    id_cuenta INT,
    id_metodo_pago INT,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria),
    FOREIGN KEY (id_moneda) REFERENCES monedas(id_moneda),
    FOREIGN KEY (id_cuenta) REFERENCES cuentas_bancarias(id_cuenta),
    FOREIGN KEY (id_metodo_pago) REFERENCES metodos_pago(id_metodo_pago)
);

-- Tabla Etiquetas
CREATE TABLE etiquetas (
    id_etiqueta INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50)
);

-- Tabla Gastos_Etiquetas (relación muchos a muchos)
CREATE TABLE gastos_etiquetas (
    id_gasto INT,
    id_etiqueta INT,
    PRIMARY KEY (id_gasto, id_etiqueta),
    FOREIGN KEY (id_gasto) REFERENCES gastos(id_gasto),
    FOREIGN KEY (id_etiqueta) REFERENCES etiquetas(id_etiqueta)
);

-- Tabla Ingresos_Etiquetas (relación muchos a muchos)
CREATE TABLE ingresos_etiquetas (
    id_ingreso INT,
    id_etiqueta INT,
    PRIMARY KEY (id_ingreso, id_etiqueta),
    FOREIGN KEY (id_ingreso) REFERENCES ingresos(id_ingreso),
    FOREIGN KEY (id_etiqueta) REFERENCES etiquetas(id_etiqueta)
);
