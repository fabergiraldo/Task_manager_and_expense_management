import pyodbc
from Utilidades.Configuracion import strConnection
from Entidades.GastosEtiquetas import GastosEtiquetas

class GastosEtiquetasRepositorio:

    @staticmethod
    def listar():
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT id_gasto, id_etiqueta FROM gastos_etiquetas")
            return [GastosEtiquetas(*fila) for fila in cursor.fetchall()]

    @staticmethod
    def crear(relacion: GastosEtiquetas):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO gastos_etiquetas (id_gasto, id_etiqueta) VALUES (?, ?)" ,
                (relacion.id_gasto, relacion.id_etiqueta)
            )
            conexion.commit()

    @staticmethod
    def eliminar(id_gasto, id_etiqueta):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "DELETE FROM gastos_etiquetas WHERE id_gasto=? AND id_etiqueta=?",
                (id_gasto, id_etiqueta)
            )
            conexion.commit()