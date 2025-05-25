from Repositorio.UsuariosRepositorio import UsuariosRepositorio
# from Repositorio.CategoriasRepositorio import CategoriasRepositorio
# from Repositorio.MonedasRepositorio import MonedasRepositorio
# from Repositorio.CuentasBancariasRepositorio import CuentasBancariasRepositorio
# from Repositorio.TarjetasRepositorio import TarjetasRepositorio
# from Repositorio.MetodosPagoRepositorio import MetodosPagoRepositorio
# from Repositorio.GastosRepositorio import GastosRepositorio
# from Repositorio.GastosEtiquetasRepositorio import GastosEtiquetasRepositorio
# from Repositorio.FacturasRepositorio import FacturasRepositorio
# from Repositorio.EtiquetasRepositorio import EtiquetasRepositorio
# from Repositorio.ProveedoresRepositorio import ProveedoresRepositorio
# from Repositorio.IngresosRepositorio import IngresosRepositorio
# from Repositorio.IngresosEtiquetasRepositorio import IngresosEtiquetasRepositorio
# from Repositorio.NotificacionesRepositorio import NotificacionesRepositorio
# from Repositorio.PresupuestosRepositorio import PresupuestosRepositorio
# from Repositorio.TransaccionesRepositorio import TransaccionesRepositorio
from Utilidades.Encriptar import EncriptarAES


#Crear instancias de los repositorios
usuarios_repo = UsuariosRepositorio()
# categorias_repo = CategoriasRepositorio()
# cuentas_bancarias_repo = CuentasBancariasRepositorio()
# TarjetasRepositorio_repo = TarjetasRepositorio()
# metodos_pago_repo = MetodosPagoRepositorio()
# gastos_repo = GastosRepositorio()
# gastos_etiquetas_repo = GastosEtiquetasRepositorio()
# monedas_repo = MonedasRepositorio()
# etiquetas_repo = EtiquetasRepositorio()
# proveedores_repo = ProveedoresRepositorio()
# ingresos_repo = IngresosRepositorio()
# ingresos_etiquetas_repo = IngresosEtiquetasRepositorio()
# facturas_repo = FacturasRepositorio()
# Notificaciones_repo = NotificacionesRepositorio()
# Presupuesto_repo = PresupuestosRepositorio()
# Transacciones_repo = TransaccionesRepositorio()

encriptador = EncriptarAES()
print("🔐 Clave AES usada:", encriptador.secretKey)

# # Pruebas para UsuariosRepositorio
# print("\n=== Pruebas UsuariosRepositorio ===")
# # Guardar un usuario nuevo
# usuarios_repo.guardar("juan Castro", "juan@example.com", "juan14235")

#Actualizar categoría
usuarios_repo.actualizar(2, "Carlos Castro", "castro2@example.com", "carlos14235")

# # Listar usuarios
# print("\nListando usuarios:")
# usuarios = usuarios_repo.Listar({}) 
# # Verificar si hubo error antes de iterar
# if "Error" in usuarios:
#     print("❌ Error al listar usuarios:", usuarios["Error"])
# else:
#     for u in usuarios.values():
#         print(u)


# # Pruebas para CategoriasRepositorio
# print("\n=== Pruebas CategoriasRepositorio ===")
# # Guardar una categoría nueva
# categorias_repo.guardar("Leche bebe", "Gastos relacionados con la bebe de la casa")

# #Listar categorías
# print("\nListando categorías:")
# categorias = categorias_repo.listar()
# for c in categorias.values():
#      print(c)

# Actualizar categoría
#categorias_repo.actualizar(1, "Comida", "Gastos en restaurantes y supermercados")

# Eliminar categoría
#categorias_repo.eliminar(2)

# #Pruebas para MonedasRepositorio
# print("\n=== Pruebas MonedasRepositorio ===")
# #Guardar una moneda nueva
# monedas_repo.guardar("Dólar Estadounidense", "USD","$")

# # Listar monedas
# print("\nListando monedas:")
# monedas = monedas_repo.listar()
# for m in monedas.values():  # ✅ Iterar sobre los valores en lugar de las claves
#     print(m)  # Esto imprimirá cada diccionario con los datos


# # Actualizar moneda
# #monedas_repo.actualizar(1, "Dólar Estadounidense", "USD_S","$")

# # Eliminar moneda
# #monedas_repo.eliminar(2)

# #Pruebas para CuentasBancariasRepositorio
# print("\n=== Pruebas CuentasBancariasRepositorio ===")
# #Guardar una cuenta bancaria nueva
# cuentas_bancarias_repo.guardar(
#    id_usuario=2,
#    nombre_banco="Banco XYZ",
#    numero_cuenta="1234567890",
#    saldo=1000000,
#    id_moneda=1
# )

# Listar cuentas bancarias
# print("\nListando cuentas bancarias:")
# cuentas = cuentas_bancarias_repo.listar()
# for c in cuentas.values():
#     print(c)

# # Actualizar cuenta bancaria
# #cuentas_bancarias_repo.actualizar(
# #    id_cuenta=1,
# #    id_usuario=1,
# #    numero_cuenta="1234567890",
# #    tipo_cuenta="Corriente",
# #    nombre_banco="Banco XYZ",
# #    saldo=1500000,
# #    estado="Activa"
# #)

# # Eliminar cuenta bancaria
# #cuentas_bancarias_repo.eliminar(2)

#Pruebas para EtiquetasRepositorio
# print("\n=== Pruebas EtiquetasRepositorio ===")
# #Guardar una etiqueta nueva
# etiquetas_repo.guardar("Urgente")

# Listar etiquetas
# print("\nListando etiquetas:")
# etiquetas = etiquetas_repo.listar()
# for e in etiquetas.values():
#     print(e)

# # Actualizar etiqueta
# #etiquetas_repo.actualizar(1, "Prioritario")

# # Eliminar etiqueta
# #etiquetas_repo.eliminar(2)


# #Pruebas para ProveedoresRepositorio
# print("\n=== Pruebas ProveedoresRepositorio ===")
# #Guardar un proveedor nuevo
# proveedores_repo.guardar(
#    nombre="Supermercado XYZ",
#    contacto="Gabriela Giraldo",
#    telefono="1234567890",
#    correo="contacto@superxyz.com"
# )

# # Listar proveedores
# print("\nListando proveedores:")
# proveedores = proveedores_repo.listar()
# for p in proveedores.values():
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


# #Pruebas para TarjetasRepositorio
# print("\n=== Pruebas TarjetasRepositorio ===")
# #Guardar una tarjeta nuevo
# TarjetasRepositorio_repo.guardar(
#    id_usuario=2,
#    nombre_tarjeta="visa",
#    tipo="credito",
#    numero_tarjeta="1000908090",
#    vencimiento="Diciembre 2026"
# )

# # Listar Tarjetas
# print("\nListando tarjetas:")
# tarjetas = TarjetasRepositorio_repo.listar()
# for t in tarjetas.values():
#     print(t)

# #Pruebas para MetodosPagoRepositorio
# print("\n=== Pruebas MetodosPagoRepositorio ===")
# #Guardar un método de pago nuevo
# metodos_pago_repo.guardar("Transferencia Bancaria")

# # Listar métodos de pago
# print("\nListando métodos de pago:")
# metodos = metodos_pago_repo.listar()
# for m in metodos.values():
#     print(m)

# # Actualizar método de pago
# #metodos_pago_repo.actualizar(1, "Transferencia Bancaria Internacional")

# # Eliminar método de pago
# #metodos_pago_repo.eliminar(2)

# #Pruebas para GastosRepositorio
# print("\n=== Pruebas GastosRepositorio ===")
# #Guardar un gasto nuevo
# gastos_repo.guardar(
#    id_usuario=2,
#    fecha="2024-04-26",
#    monto=50000,
#    descripcion="Compra en el supermercado",
#    id_categoria=4,
#    id_moneda=1,
#    id_cuenta=6,
#    id_tarjeta=2,
#    id_proveedor=6,
#    id_metodo_pago=1
# )

# # Listar gastos
# print("\nListando gastos:")
# gastos = gastos_repo.listar()
# for g in gastos.values():
#     print(g)

# # Actualizar gasto
# #gastos_repo.actualizar(
# #  id_usuario=2,
#    fecha="2024-04-26",
#    monto=50000,
#    descripcion="Compra en el D1",
#    id_categoria=4,
#    id_moneda=1,
#    id_cuenta=6,
#    id_tarjeta=2,
#    id_proveedor=6,
#    id_metodo_pago=1
# #)

# # Eliminar gasto
# #gastos_repo.eliminar(2)


# #Pruebas para GastosEtiquetasRepositorio
# print("\n=== Pruebas GastosEtiquetasRepositorio ===")
# #Guardar una relación gasto-etiqueta nueva
# gastos_etiquetas_repo.guardar(1,1)

# # Listar relaciones gasto-etiqueta
# print("\nListando relaciones gasto-etiqueta:")
# gastos_etiquetas = gastos_etiquetas_repo.listar()
# for ge in gastos_etiquetas.values():
#     print(ge)

# # Actualizar relación gasto-etiqueta
# #gastos_etiquetas_repo.actualizar(1, 1, 2)

# # Eliminar relación gasto-etiqueta
# #gastos_etiquetas_repo.eliminar(2)


# #Pruebas para FacturasRepositorio
# print("\n=== Pruebas FacturasRepositorio ===")
# #Guardar una factura nueva
# facturas_repo.guardar(
#    id_gasto=1,
#    id_proveedor=6,
#    ruta_archivo="C:User/User1/Desktop/Facturas"
# )

# # Listar facturas
# print("\nListando facturas:")
# facturas = facturas_repo.listar()
# for f in facturas.values():
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

# #Pruebas para IngresosRepositorio
# print("\n=== Pruebas IngresosRepositorio ===")
# #Guardar un ingreso nuevo
# ingresos_repo.guardar(
#    id_usuario=2,
#    fecha="2024-04-26",
#    monto=1000000,
#    descripcion="Salario mensual",
#    id_moneda=1,
#    id_cuenta=6,
#    id_metodo_pago=1
# )

# # Listar ingresos
# print("\nListando ingresos:")
# ingresos = ingresos_repo.listar()
# for i in ingresos.values():
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

# #Pruebas para IngresosEtiquetasRepositorio
# print("\n=== Pruebas IngresosEtiquetasRepositorio ===")
# #Guardar una relación ingreso-etiqueta nueva
# ingresos_etiquetas_repo.guardar(2,1)

# # Listar relaciones ingreso-etiqueta
# print("\nListando relaciones ingreso-etiqueta:")
# ingresos_etiquetas = ingresos_etiquetas_repo.listar()
# for ie in ingresos_etiquetas.values():
#     print(ie)

# # Actualizar relación ingreso-etiqueta
# #ingresos_etiquetas_repo.actualizar(1, 1, 2)

# # Eliminar relación ingreso-etiqueta
# #ingresos_etiquetas_repo.eliminar(2)

# # Pruebas para NotificacionesRepositorio
# print("\n=== Pruebas NotificacionesRepositorio ===")
# # Guardar una NOtificacion
# Notificaciones_repo.guardar(
#     id_usuario=2,
#     mensaje="El pago en supermercado fue exitoso",
#     fecha="2024-04-26",
#     leido=False
# )

# # Listar relaciones NotificacionesRepositorio
# print("\nListando NotificacionesRepositorio:")
# Notificaciones = Notificaciones_repo.listar()
# for n in Notificaciones.values():
#     print(n)


# # Pruebas para PresupuestoRepositorio
# print("\n=== Pruebas PresupuestoRepositorio ===")
# # Guardar un presupuesto
# Presupuesto_repo.guardar(
#     id_usuario=2,
#     id_categoria=4,
#     mes="Junio",
#     monto=4000000
# )

# # Listar relaciones PresupuestoRepositorio
# print("\nListando PresupuestoRepositorio:")
# Presupuesto = Presupuesto_repo.listar()
# for p in Presupuesto.values():
#     print(p)


# # Pruebas para Transacciones
# print("\n=== Pruebas TransaccionesRepositorio ===")
# # Guardar un presupuesto
# Transacciones_repo.guardar(
#     id_usuario=2,
#     tipo='Ingreso',
#     id_categoria=4,
#     id_moneda=1,
#     id_cuenta=6,
#     id_metodo_pago=1,
#     fecha="2024-04-26"
# )

# # Listar relaciones TransaccionesRepositorio
# print("\nListando TransaccionesRepositorio:")
# Transacciones = Transacciones_repo.listar()
# for t in Transacciones.values():
#     print(t)
