USE gestion_gastos;

-- 1) Usuarios
INSERT INTO usuarios (nombre, correo, contrasena) VALUES
  ('Usuario1',  'usuario1@example.com',  'contrasena1'),
  ('Usuario2',  'usuario2@example.com',  'contrasena2'),
  ('Usuario3',  'usuario3@example.com',  'contrasena3'),
  ('Usuario4',  'usuario4@example.com',  'contrasena4'),
  ('Usuario5',  'usuario5@example.com',  'contrasena5'),
  ('Usuario6',  'usuario6@example.com',  'contrasena6'),
  ('Usuario7',  'usuario7@example.com',  'contrasena7'),
  ('Usuario8',  'usuario8@example.com',  'contrasena8'),
  ('Usuario9',  'usuario9@example.com',  'contrasena9'),
  ('Usuario10', 'usuario10@example.com', 'contrasena10');

-- 2) Categorías
INSERT INTO categorias (nombre, descripcion) VALUES
  ('Transporte',      'Gastos de transporte'),
  ('Alimentación',    'Gastos de comida y bebida'),
  ('Oficina',         'Suministros de oficina'),
  ('Entretenimiento', 'Ocio y entretenimiento'),
  ('Salud',           'Servicios médicos'),
  ('Educación',       'Cursos y capacitación'),
  ('Viajes',          'Hotel y pasajes'),
  ('Tecnología',      'Equipos y software'),
  ('Servicios',       'Servicios varios'),
  ('Misceláneo',      'Gastos diversos');

-- 3) Monedas
INSERT INTO monedas (nombre, codigo, simbolo) VALUES
  ('Peso Colombiano', 'COP', '$'),
  ('Dólar Americano', 'USD', 'US$'),
  ('Euro',            'EUR', '€'),
  ('Libra Esterlina','GBP', '£'),
  ('Yen',             'JPY', '¥'),
  ('Peso Mexicano',   'MXN', 'MX$'),
  ('Real Brasileño',  'BRL', 'R$'),
  ('Franco Suizo',    'CHF', 'Fr.'),
  ('Dólar Canadiense','CAD', 'C$'),
  ('Dólar Australiano','AUD','A$');

-- 4) Cuentas Bancarias
INSERT INTO cuentas_bancarias (id_usuario, nombre_banco, numero_cuenta, saldo, id_moneda) VALUES
  (1, 'Banco A', '000111222', 1500.00, 1),
  (2, 'Banco B', '000333444',  800.50, 2),
  (3, 'Banco C', '000555666', 3200.75, 3),
  (4, 'Banco D', '000777888',  450.00, 4),
  (5, 'Banco E', '000999000', 2100.00, 5),
  (6, 'Banco F', '001111222',  600.00, 6),
  (7, 'Banco G', '001333444', 1700.20, 7),
  (8, 'Banco H', '001555666',  900.00, 8),
  (9, 'Banco I', '001777888', 2400.40, 9),
  (10,'Banco J', '001999000', 1100.00,10);

-- 5) Tarjetas
INSERT INTO tarjetas (id_usuario, nombre_tarjeta, tipo, numero_tarjeta, vencimiento) VALUES
  (1, 'Visa Platinum',   'Credito', '4111111111111111','2025-12-31'),
  (2, 'Mastercard Gold', 'Debito',  '5500000000000004','2025-11-30'),
  (3, 'Amex Green',      'Credito', '340000000000009', '2026-01-31'),
  (4, 'Visa Classic',    'Debito',  '4111111111111129','2026-02-28'),
  (5, 'Mastercard MC',   'Credito', '5500000000000012','2025-10-31'),
  (6, 'Visa Electron',   'Debito',  '4026000000000002','2026-03-31'),
  (7, 'Discover It',     'Credito', '6011000000000004','2025-09-30'),
  (8, 'Visa Infinite',   'Credito', '4917610000000000','2026-04-30'),
  (9, 'Mastercard MC2',  'Debito',  '5555555555554444','2026-05-31'),
  (10,'Amex Gold',       'Credito', '378282246310005','2025-08-31');

-- 6) Proveedores
INSERT INTO proveedores (nombre, contacto, telefono, correo) VALUES
  ('Proveedor A','Juan Pérez',  '+571234567890','provA@empresa.com'),
  ('Proveedor B','María Gómez', '+571234567891','provB@empresa.com'),
  ('Proveedor C','Luis Díaz',   '+571234567892','provC@empresa.com'),
  ('Proveedor D','Ana Ruiz',    '+571234567893','provD@empresa.com'),
  ('Proveedor E','Carlos Mora', '+571234567894','provE@empresa.com'),
  ('Proveedor F','Sofía León',  '+571234567895','provF@empresa.com'),
  ('Proveedor G','Pedro Soto',  '+571234567896','provG@empresa.com'),
  ('Proveedor H','Laura Vega',  '+571234567897','provH@empresa.com'),
  ('Proveedor I','Diego Ríos',  '+571234567898','provI@empresa.com'),
  ('Proveedor J','Elena Castillo','+571234567899','provJ@empresa.com');

-- 7) Métodos de Pago
INSERT INTO metodos_pago (metodo) VALUES
  ('Efectivo'),
  ('Tarjeta Débito'),
  ('Tarjeta Crédito'),
  ('Transferencia'),
  ('Cheque'),
  ('PayPal'),
  ('Cripto'),
  ('Pago Móvil'),
  ('Depósito'),
  ('Contra Entrega');

-- 8) Gastos
INSERT INTO gastos (
  id_usuario, fecha, monto, descripcion,
  id_categoria, id_moneda, id_cuenta, id_tarjeta, id_proveedor, id_metodo_pago
) VALUES
  (1, '2025-05-01', 120.00, 'Taxi aeropuerto', 1, 1, 1, 1, 1, 1),
  (2, '2025-05-02',  75.50, 'Almuerzo cliente', 2, 2, 2, 2, 2, 2),
  (3, '2025-05-03', 300.00, 'Papelería',       3, 3, 3, 3, 3, 3),
  (4, '2025-05-04',  50.00, 'Cine empresa',    4, 4, 4, 4, 4, 4),
  (5, '2025-05-05', 200.00, 'Consulta médica', 5, 5, 5, 5, 5, 5),
  (6, '2025-05-06', 500.00, 'Curso Python',    6, 6, 6, 6, 6, 6),
  (7, '2025-05-07', 850.00, 'Boleto avión',    7, 7, 7, 7, 7, 7),
  (8, '2025-05-08', 1200.00,'Laptop',          8, 8, 8, 8, 8, 8),
  (9, '2025-05-09',  95.00, 'Servicios varios',9, 9, 9, 9, 9, 9),
  (10,'2025-05-10', 400.00,'Gasto misceláneo',10,10,10,10,10,10);

-- 9) Ingresos
INSERT INTO ingresos (
  id_usuario, fecha, monto, descripcion,
  id_moneda, id_cuenta, id_metodo_pago
) VALUES
  (1, '2025-05-01', 1000.00, 'Pago cliente A',  1, 1, 1),
  (2, '2025-05-02', 1500.00, 'Pago cliente B',  2, 2, 2),
  (3, '2025-05-03',  800.00, 'Reembolso',       3, 3, 3),
  (4, '2025-05-04', 1200.00,'Venta equipo',     4, 4, 4),
  (5, '2025-05-05',  950.00, 'Honorarios',       5, 5, 5),
  (6, '2025-05-06', 1100.00,'Pago proyecto',    6, 6, 6),
  (7, '2025-05-07',  700.00,'Servicios',        7, 7, 7),
  (8, '2025-05-08', 1300.00,'Bonus',            8, 8, 8),
  (9, '2025-05-09',  500.00,'Devolución',       9, 9, 9),
  (10,'2025-05-10', 2000.00,'Ingreso misceláneo',10,10,10);

-- 10) Presupuestos
INSERT INTO presupuestos (id_usuario, id_categoria, mes, monto) VALUES
  (1,  1, 2025, 1000.00),
  (2,  2, 2025, 1500.00),
  (3,  3, 2025, 1200.00),
  (4,  4, 2025,  800.00),
  (5,  5, 2025, 2000.00),
  (6,  6, 2025, 1800.00),
  (7,  7, 2025, 2200.00),
  (8,  8, 2025, 2500.00),
  (9,  9, 2025,  900.00),
  (10,10, 2025, 1100.00);

-- 11) Facturas
INSERT INTO facturas (id_gasto, id_proveedor, ruta_archivo) VALUES
  (1,  1, '/files/recibo1.pdf'),
  (2,  2, '/files/recibo2.pdf'),
  (3,  3, '/files/recibo3.pdf'),
  (4,  4, '/files/recibo4.pdf'),
  (5,  5, '/files/recibo5.pdf'),
  (6,  6, '/files/recibo6.pdf'),
  (7,  7, '/files/recibo7.pdf'),
  (8,  8, '/files/recibo8.pdf'),
  (9,  9, '/files/recibo9.pdf'),
  (10,10,'/files/recibo10.pdf');

-- 12) Notificaciones
INSERT INTO notificaciones (id_usuario, mensaje) VALUES
  (1, 'Notificación 1'),
  (2, 'Notificación 2'),
  (3, 'Notificación 3'),
  (4, 'Notificación 4'),
  (5, 'Notificación 5'),
  (6, 'Notificación 6'),
  (7, 'Notificación 7'),
  (8, 'Notificación 8'),
  (9, 'Notificación 9'),
  (10,'Notificación 10');

-- 13) Transacciones
INSERT INTO transacciones (
  id_usuario, tipo, id_categoria, id_moneda, id_cuenta, id_metodo_pago
) VALUES
  (1, 'Gasto',    1, 1, 1, 1),
  (2, 'Ingreso',  2, 2, 2, 2),
  (3, 'Gasto',    3, 3, 3, 3),
  (4, 'Ingreso',  4, 4, 4, 4),
  (5, 'Gasto',    5, 5, 5, 5),
  (6, 'Ingreso',  6, 6, 6, 6),
  (7, 'Gasto',    7, 7, 7, 7),
  (8, 'Ingreso',  8, 8, 8, 8),
  (9, 'Gasto',    9, 9, 9, 9),
  (10,'Ingreso', 10,10,10,10);

-- 14) Etiquetas
INSERT INTO etiquetas (nombre) VALUES
  ('Etiqueta1'),
  ('Etiqueta2'),
  ('Etiqueta3'),
  ('Etiqueta4'),
  ('Etiqueta5'),
  ('Etiqueta6'),
  ('Etiqueta7'),
  ('Etiqueta8'),
  ('Etiqueta9'),
  ('Etiqueta10');

-- 15) Gastos_Etiquetas
INSERT INTO gastos_etiquetas (id_gasto, id_etiqueta) VALUES
  (1,1),
  (2,2),
  (3,3),
  (4,4),
  (5,5),
  (6,6),
  (7,7),
  (8,8),
  (9,9),
  (10,10);

-- 16) Ingresos_Etiquetas
INSERT INTO ingresos_etiquetas (id_ingreso, id_etiqueta) VALUES
  (1,1),
  (2,2),
  (3,3),
  (4,4),
  (5,5),
  (6,6),
  (7,7),
  (8,8),
  (9,9),
  (10,10);
