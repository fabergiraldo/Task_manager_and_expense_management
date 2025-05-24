import pyodbc
from Utilidades.Configuracion import strConnection
from Entidades.Monedas import Monedas

class MonedasRepositorio:

    @staticmethod
    def listar():
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT id_moneda, nombre, codigo, simbolo FROM monedas")
            return [Monedas(*fila) for fila in cursor.fetchall()]

    @staticmethod
    def crear(moneda: Monedas):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO monedas (nombre, codigo, simbolo) VALUES (?, ?, ?)",
                (moneda.nombre, moneda.codigo, moneda.simbolo)
            )
            conexion.commit()

    @staticmethod
    def actualizar(moneda: Monedas):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "UPDATE monedas SET nombre=?, codigo=?, simbolo=? WHERE id_moneda=?",
                (moneda.nombre, moneda.codigo, moneda.simbolo, moneda.id_moneda)
            )
            conexion.commit()

    @staticmethod
    def eliminar(id_moneda):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM monedas WHERE id_moneda=?", (id_moneda,))
            conexion.commit()