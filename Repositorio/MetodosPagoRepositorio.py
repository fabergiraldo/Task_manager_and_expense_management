import pyodbc
from Utilidades.Configuracion import strConnection
from Entidades.MetodosPago import MetodosPago

class MetodosPagoRepositorio:

    @staticmethod
    def listar():
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "SELECT id_metodo_pago, metodo FROM metodos_pago"
            )
            return [MetodosPago(*fila) for fila in cursor.fetchall()]

    @staticmethod
    def crear(metodo_pago: MetodosPago):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO metodos_pago (metodo) VALUES (?)",
                (metodo_pago.metodo,)
            )
            conexion.commit()

    @staticmethod
    def actualizar(metodo_pago: MetodosPago):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "UPDATE metodos_pago SET metodo=? WHERE id_metodo_pago=?",
                (metodo_pago.metodo, metodo_pago.id_metodo_pago)
            )
            conexion.commit()

    @staticmethod
    def eliminar(id_metodo_pago):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM metodos_pago WHERE id_metodo_pago=?", (id_metodo_pago,))
            conexion.commit()