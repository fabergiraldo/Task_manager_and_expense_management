import pyodbc
from Entidades.GastosEtiquetas import GastosEtiquetas
from Utilidades.Configuracion import Configuracion

class GastosEtiquetasRepositorio:

    def listar(self):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            consulta = """
                SELECT id_gasto_etiqueta, id_gasto, id_etiqueta
                FROM gastos_etiquetas
            """
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista = []
            for elemento in cursor:
                gasto_etiqueta = GastosEtiquetas(
                    id_gasto_etiqueta=elemento[0],
                    id_gasto=elemento[1],
                    id_etiqueta=elemento[2]
                )
                lista.append(gasto_etiqueta)

            cursor.close()
            conexion.close()

            return lista

        except Exception as ex:
            print("Error al listar gastos_etiquetas:", str(ex))
            return []

    def guardar(self, id_gasto, id_etiqueta):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = """
                INSERT INTO gastos_etiquetas (id_gasto, id_etiqueta)
                VALUES (?, ?)
            """
            cursor.execute(consulta, (id_gasto, id_etiqueta))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Gasto_etiqueta guardado correctamente")

        except Exception as ex:
            print("Error al guardar gasto_etiqueta:", str(ex))

    def actualizar(self, id_gasto_etiqueta, id_gasto, id_etiqueta):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = """
                UPDATE gastos_etiquetas 
                SET id_gasto = ?, id_etiqueta = ?
                WHERE id_gasto_etiqueta = ?
            """
            cursor.execute(consulta, (id_gasto, id_etiqueta, id_gasto_etiqueta))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Gasto_etiqueta actualizado correctamente")

        except Exception as ex:
            print("Error al actualizar gasto_etiqueta:", str(ex))

    def eliminar(self, id_gasto_etiqueta):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = "DELETE FROM gastos_etiquetas WHERE id_gasto_etiqueta = ?"
            cursor.execute(consulta, (id_gasto_etiqueta,))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Gasto_etiqueta eliminado correctamente")

        except Exception as ex:
            print("Error al eliminar gasto_etiqueta:", str(ex)) 