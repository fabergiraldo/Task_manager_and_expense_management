import pyodbc
from Entidades.IngresosEtiquetas import IngresosEtiquetas
from Utilidades.Configuracion import Configuracion

class IngresosEtiquetasRepositorio:

    def listar(self):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            consulta = """
                SELECT id_ingreso_etiqueta, id_ingreso, id_etiqueta
                FROM ingresos_etiquetas
            """
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista = []
            for elemento in cursor:
                ingreso_etiqueta = IngresosEtiquetas(
                    id_ingreso_etiqueta=elemento[0],
                    id_ingreso=elemento[1],
                    id_etiqueta=elemento[2]
                )
                lista.append(ingreso_etiqueta)

            cursor.close()
            conexion.close()

            return lista

        except Exception as ex:
            print("Error al listar ingresos_etiquetas:", str(ex))
            return []

    def guardar(self, id_ingreso, id_etiqueta):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = """
                INSERT INTO ingresos_etiquetas (id_ingreso, id_etiqueta)
                VALUES (?, ?)
            """
            cursor.execute(consulta, (id_ingreso, id_etiqueta))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Ingreso_etiqueta guardado correctamente")

        except Exception as ex:
            print("Error al guardar ingreso_etiqueta:", str(ex))

    def actualizar(self, id_ingreso_etiqueta, id_ingreso, id_etiqueta):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = """
                UPDATE ingresos_etiquetas 
                SET id_ingreso = ?, id_etiqueta = ?
                WHERE id_ingreso_etiqueta = ?
            """
            cursor.execute(consulta, (id_ingreso, id_etiqueta, id_ingreso_etiqueta))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Ingreso_etiqueta actualizado correctamente")

        except Exception as ex:
            print("Error al actualizar ingreso_etiqueta:", str(ex))

    def eliminar(self, id_ingreso_etiqueta):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = "DELETE FROM ingresos_etiquetas WHERE id_ingreso_etiqueta = ?"
            cursor.execute(consulta, (id_ingreso_etiqueta,))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Ingreso_etiqueta eliminado correctamente")

        except Exception as ex:
            print("Error al eliminar ingreso_etiqueta:", str(ex)) 