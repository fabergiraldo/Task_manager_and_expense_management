from Repositorio.UsuariosRepositorio import UsuariosRepositorio
from Repositorio.CategoriasRepositorio import CategoriasRepositorio
from Repositorio.CuentasBancariasRepositorio import CuentasBancariasRepositorio
from Repositorio.EtiquetasRepositorio import EtiquetasRepositorio
from Repositorio.FacturasRepositorio import FacturasRepositorio
from Repositorio.GastosEtiquetasRepositorio import GastosEtiquetasRepositorio
from Repositorio.GastosRepositorio import GastosRepositorio
from Repositorio.IngresosEtiquetasRepositorio import IngresosEtiquetasRepositorio
from Repositorio.IngresosRepositorio import IngresosRepositorio


# Crear instancias de los repositorios
# usuarios_repo = UsuariosRepositorio()
# categorias_repo = CategoriasRepositorio()
# gastos_repo = GastosRepositorio()
# ingresos_repo = IngresosRepositorio()
# metodos_pago_repo = MetodosPagoRepositorio()
# proveedores_repo = ProveedoresRepositorio()
# etiquetas_repo = EtiquetasRepositorio()
# ingresos_etiquetas_repo = IngresosEtiquetasRepositorio()
# gastos_etiquetas_repo = GastosEtiquetasRepositorio()
# facturas_repo = FacturasRepositorio()
# monedas_repo = MonedasRepositorio()
cuentas_bancarias_repo = CuentasBancariasRepositorio()

# Pruebas para UsuariosRepositorio
#print("\n=== Pruebas UsuariosRepositorio ===")
# Guardar un usuario nuevo
#usuarios_repo.guardar("Faber Giraldo", "faber@example.com", "14235")

# # Listar usuarios
# print("\nListando usuarios:")
# usuarios = usuarios_repo.listar()
# for u in usuarios:
#     print(u)

# # Actualizar usuario
# #usuarios_repo.actualizar(1, "Juan P. Gómez", "juanp@example.com")

# # Eliminar usuario
# #usuarios_repo.eliminar(2)

# # Pruebas para CategoriasRepositorio
# print("\n=== Pruebas CategoriasRepositorio ===")
# # Guardar una categoría nueva
# categorias_repo.guardar("Leche bebe", "Gastos relacionados con la bebe de la casa")

# Listar categorías
# print("\nListando categorías:")
# categorias = categorias_repo.listar()
# for c in categorias:
#      print(c)

# Actualizar categoría
#categorias_repo.actualizar(1, "Comida", "Gastos en restaurantes y supermercados")

# Eliminar categoría
#categorias_repo.eliminar(2)

# # Pruebas para GastosRepositorio
# print("\n=== Pruebas GastosRepositorio ===")
# # Guardar un gasto nuevo
# #gastos_repo.guardar(
# #    id_usuario=1,
# #    id_categoria=1,
# #    monto=50000,
# #    descripcion="Compra en el supermercado",
# #    fecha="2024-04-26",
# #    id_metodo_pago=1,
# #    id_proveedor=1,
# #    estado="Pendiente"
# #)

# # Listar gastos
# print("\nListando gastos:")
# gastos = gastos_repo.listar()
# for g in gastos:
#     print(g)

# # Actualizar gasto
# #gastos_repo.actualizar(
# #    id_gasto=1,
# #    id_usuario=1,
# #    id_categoria=1,
# #    monto=55000,
# #    descripcion="Compra en el supermercado actualizada",
# #    fecha="2024-04-26",
# #    id_metodo_pago=1,
# #    id_proveedor=1,
# #    estado="Pagado"
# #)

# # Eliminar gasto
# #gastos_repo.eliminar(2)

# # Pruebas para IngresosRepositorio
# print("\n=== Pruebas IngresosRepositorio ===")
# # Guardar un ingreso nuevo
# #ingresos_repo.guardar(
# #    id_usuario=1,
# #    monto=1000000,
# #    descripcion="Salario mensual",
# #    fecha="2024-04-26",
# #    id_metodo_pago=1,
# #    estado="Recibido"
# #)

# # Listar ingresos
# print("\nListando ingresos:")
# ingresos = ingresos_repo.listar()
# for i in ingresos:
#     print(i)

# # Actualizar ingreso
# #ingresos_repo.actualizar(
# #    id_ingreso=1,
# #    id_usuario=1,
# #    monto=1200000,
# #    descripcion="Salario mensual con bonificación",
# #    fecha="2024-04-26",
# #    id_metodo_pago=1,
# #    estado="Recibido"
# #)

# # Eliminar ingreso
# #ingresos_repo.eliminar(2)

# # Pruebas para MetodosPagoRepositorio
# print("\n=== Pruebas MetodosPagoRepositorio ===")
# # Guardar un método de pago nuevo
# #metodos_pago_repo.guardar("Transferencia Bancaria")

# # Listar métodos de pago
# print("\nListando métodos de pago:")
# metodos = metodos_pago_repo.listar()
# for m in metodos:
#     print(m)

# # Actualizar método de pago
# #metodos_pago_repo.actualizar(1, "Transferencia Bancaria Internacional")

# # Eliminar método de pago
# #metodos_pago_repo.eliminar(2)

# # Pruebas para ProveedoresRepositorio
# print("\n=== Pruebas ProveedoresRepositorio ===")
# # Guardar un proveedor nuevo
# #proveedores_repo.guardar(
# #    nombre="Supermercado XYZ",
# #    direccion="Calle 123 #45-67",
# #    telefono="1234567890",
# #    correo="contacto@superxyz.com",
# #    estado="Activo"
# #)

# # Listar proveedores
# print("\nListando proveedores:")
# proveedores = proveedores_repo.listar()
# for p in proveedores:
#     print(p)

# # Actualizar proveedor
# #proveedores_repo.actualizar(
# #    id_proveedor=1,
# #    nombre="Supermercado XYZ Plus",
# #    direccion="Calle 123 #45-67",
# #    telefono="1234567890",
# #    correo="contacto@superxyz.com",
# #    estado="Activo"
# #)

# # Eliminar proveedor
# #proveedores_repo.eliminar(2)

# # Pruebas para EtiquetasRepositorio
# print("\n=== Pruebas EtiquetasRepositorio ===")
# # Guardar una etiqueta nueva
# #etiquetas_repo.guardar("Urgente")

# # Listar etiquetas
# print("\nListando etiquetas:")
# etiquetas = etiquetas_repo.listar()
# for e in etiquetas:
#     print(e)

# # Actualizar etiqueta
# #etiquetas_repo.actualizar(1, "Prioritario")

# # Eliminar etiqueta
# #etiquetas_repo.eliminar(2)

# # Pruebas para IngresosEtiquetasRepositorio
# print("\n=== Pruebas IngresosEtiquetasRepositorio ===")
# # Guardar una relación ingreso-etiqueta nueva
# #ingresos_etiquetas_repo.guardar(1, 1)

# # Listar relaciones ingreso-etiqueta
# print("\nListando relaciones ingreso-etiqueta:")
# ingresos_etiquetas = ingresos_etiquetas_repo.listar()
# for ie in ingresos_etiquetas:
#     print(ie)

# # Actualizar relación ingreso-etiqueta
# #ingresos_etiquetas_repo.actualizar(1, 1, 2)

# # Eliminar relación ingreso-etiqueta
# #ingresos_etiquetas_repo.eliminar(2)

# # Pruebas para GastosEtiquetasRepositorio
# print("\n=== Pruebas GastosEtiquetasRepositorio ===")
# # Guardar una relación gasto-etiqueta nueva
# #gastos_etiquetas_repo.guardar(1, 1)

# # Listar relaciones gasto-etiqueta
# print("\nListando relaciones gasto-etiqueta:")
# gastos_etiquetas = gastos_etiquetas_repo.listar()
# for ge in gastos_etiquetas:
#     print(ge)

# # Actualizar relación gasto-etiqueta
# #gastos_etiquetas_repo.actualizar(1, 1, 2)

# # Eliminar relación gasto-etiqueta
# #gastos_etiquetas_repo.eliminar(2)

# # Pruebas para FacturasRepositorio
# print("\n=== Pruebas FacturasRepositorio ===")
# # Guardar una factura nueva
# #facturas_repo.guardar(
# #    id_gasto=1,
# #    numero_factura="FAC-001",
# #    fecha_emision="2024-04-26",
# #    fecha_vencimiento="2024-05-26",
# #    monto_total=50000,
# #    estado="Pendiente"
# #)

# # Listar facturas
# print("\nListando facturas:")
# facturas = facturas_repo.listar()
# for f in facturas:
#     print(f)

# # Actualizar factura
# #facturas_repo.actualizar(
# #    id_factura=1,
# #    id_gasto=1,
# #    numero_factura="FAC-001-A",
# #    fecha_emision="2024-04-26",
# #    fecha_vencimiento="2024-05-26",
# #    monto_total=55000,
# #    estado="Pagada"
# #)

# # Eliminar factura
# #facturas_repo.eliminar(2)

# # Pruebas para MonedasRepositorio
# print("\n=== Pruebas MonedasRepositorio ===")
# # Guardar una moneda nueva
# #monedas_repo.guardar("USD", "Dólar Estadounidense", "$", 1.0)

# # Listar monedas
# print("\nListando monedas:")
# monedas = monedas_repo.listar()
# for m in monedas:
#     print(m)

# # Actualizar moneda
# #monedas_repo.actualizar(1, "USD", "Dólar Estadounidense", "$", 1.05)

# # Eliminar moneda
# #monedas_repo.eliminar(2)

# # Pruebas para CuentasBancariasRepositorio
# print("\n=== Pruebas CuentasBancariasRepositorio ===")
# #Guardar una cuenta bancaria nueva
# cuentas_bancarias_repo.guardar(
#    id_usuario=1,
#    banco="Banco XYZ",
#    numero_cuenta="1234567890",
#    saldo=1000000,
#    id_moneda=1
# )

# # Listar cuentas bancarias
# print("\nListando cuentas bancarias:")
# cuentas = cuentas_bancarias_repo.listar()
# for c in cuentas:
#     print(c)

# # Actualizar cuenta bancaria
# #cuentas_bancarias_repo.actualizar(
# #    id_cuenta=1,
# #    id_usuario=1,
# #    numero_cuenta="1234567890",
# #    tipo_cuenta="Corriente",
# #    banco="Banco XYZ",
# #    saldo=1500000,
# #    estado="Activa"
# #)

# # Eliminar cuenta bancaria
# #cuentas_bancarias_repo.eliminar(2)