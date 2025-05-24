import pyodbc
from Utilidades.Configuracion import strConnection
from Entidades.Etiquetas import Etiquetas

class EtiquetasRepositorio:

    @staticmethod
    def listar():
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "SELECT id_etiqueta, nombre FROM etiquetas"
            )
            return [Etiquetas(*fila) for fila in cursor.fetchall()]

    @staticmethod
    def crear(etiqueta: Etiquetas):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO etiquetas (nombre) VALUES (?)",
                (etiqueta.nombre,)
            )
            conexion.commit()

    @staticmethod
    def actualizar(etiqueta: Etiquetas):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "UPDATE etiquetas SET nombre=? WHERE id_etiqueta=?",
                (etiqueta.nombre, etiqueta.id_etiqueta)
            )
            conexion.commit()

    @staticmethod
    def eliminar(id_etiqueta):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM etiquetas WHERE id_etiqueta=?", (id_etiqueta,))
            conexion.commit()