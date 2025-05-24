import pyodbc
from Utilidades.Configuracion import strConnection
from Entidades.Transacciones import Transacciones

class TransaccionesRepositorio:

    @staticmethod
    def listar():
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "SELECT id_transaccion, id_usuario, tipo, id_categoria, id_moneda, id_cuenta, id_metodo_pago, fecha FROM transacciones"
            )
            return [Transacciones(*fila) for fila in cursor.fetchall()]

    @staticmethod
    def crear(transaccion: Transacciones):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO transacciones (id_usuario, tipo, id_categoria, id_moneda, id_cuenta, id_metodo_pago, fecha) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (transaccion.id_usuario, transaccion.tipo, transaccion.id_categoria,
                 transaccion.id_moneda, transaccion.id_cuenta, transaccion.id_metodo_pago,
                 transaccion.fecha)
            )
            conexion.commit()

    @staticmethod
    def actualizar(transaccion: Transacciones):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "UPDATE transacciones SET id_usuario=?, tipo=?, id_categoria=?, id_moneda=?, id_cuenta=?, id_metodo_pago=?, fecha=? WHERE id_transaccion=?",
                (transaccion.id_usuario, transaccion.tipo, transaccion.id_categoria,
                 transaccion.id_moneda, transaccion.id_cuenta, transaccion.id_metodo_pago,
                 transaccion.fecha, transaccion.id_transaccion)
            )
            conexion.commit()

    @staticmethod
    def eliminar(id_transaccion):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM transacciones WHERE id_transaccion=?", (id_transaccion,))
            conexion.commit()