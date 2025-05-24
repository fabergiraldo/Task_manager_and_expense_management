import pyodbc
from Utilidades.Configuracion import strConnection
from Entidades.Gastos import Gastos

class GastosRepositorio:

    @staticmethod
    def listar():
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "SELECT id_gasto, id_usuario, fecha, monto, descripcion, id_categoria, id_moneda, id_cuenta, id_tarjeta, id_proveedor, id_metodo_pago FROM gastos"
            )
            return [Gastos(*fila) for fila in cursor.fetchall()]

    @staticmethod
    def crear(gasto: Gastos):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO gastos (id_usuario, fecha, monto, descripcion, id_categoria, id_moneda, id_cuenta, id_tarjeta, id_proveedor, id_metodo_pago) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (gasto.id_usuario, gasto.fecha, gasto.monto, gasto.descripcion, gasto.id_categoria,
                 gasto.id_moneda, gasto.id_cuenta, gasto.id_tarjeta, gasto.id_proveedor,
                 gasto.id_metodo_pago)
            )
            conexion.commit()

    @staticmethod
    def actualizar(gasto: Gastos):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "UPDATE gastos SET id_usuario=?, fecha=?, monto=?, descripcion=?, id_categoria=?, id_moneda=?, id_cuenta=?, id_tarjeta=?, id_proveedor=?, id_metodo_pago=? WHERE id_gasto=?",
                (gasto.id_usuario, gasto.fecha, gasto.monto, gasto.descripcion, gasto.id_categoria,
                 gasto.id_moneda, gasto.id_cuenta, gasto.id_tarjeta, gasto.id_proveedor,
                 gasto.id_metodo_pago, gasto.id_gasto)
            )
            conexion.commit()

    @staticmethod
    def eliminar(id_gasto):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM gastos WHERE id_gasto=?", (id_gasto,))
            conexion.commit()
