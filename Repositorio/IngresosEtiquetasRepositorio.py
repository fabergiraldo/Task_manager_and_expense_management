import pyodbc
from Utilidades.Configuracion import strConnection
from Entidades.IngresosEtiquetas import IngresosEtiquetas

class IngresosEtiquetasRepositorio:

    @staticmethod
    def listar():
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT id_ingreso, id_etiqueta FROM ingresos_etiquetas")
            return [IngresosEtiquetas(*fila) for fila in cursor.fetchall()]

    @staticmethod
    def crear(relacion: IngresosEtiquetas):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO ingresos_etiquetas (id_ingreso, id_etiqueta) VALUES (?, ?)",
                (relacion.id_ingreso, relacion.id_etiqueta)
            )
            conexion.commit()

    @staticmethod
    def eliminar(id_ingreso, id_etiqueta):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "DELETE FROM ingresos_etiquetas WHERE id_ingreso=? AND id_etiqueta=?",
                (id_ingreso, id_etiqueta)
            )
            conexion.commit()