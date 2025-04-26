import pyodbc
from Entidades.Etiquetas import Etiquetas
from Utilidades.Configuracion import Configuracion

class EtiquetasRepositorio:

    def listar(self):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            consulta = "SELECT id_etiqueta, nombre FROM etiquetas"
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista = []
            for elemento in cursor:
                etiqueta = Etiquetas(
                    id_etiqueta=elemento[0],
                    nombre=elemento[1]
                )
                lista.append(etiqueta)

            cursor.close()
            conexion.close()

            return lista

        except Exception as ex:
            print("Error al listar etiquetas:", str(ex))
            return []

    def guardar(self, nombre):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = "INSERT INTO etiquetas (nombre) VALUES (?)"
            cursor.execute(consulta, (nombre,))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Etiqueta guardada correctamente")

        except Exception as ex:
            print("Error al guardar etiqueta:", str(ex))

    def actualizar(self, id_etiqueta, nombre):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = "UPDATE etiquetas SET nombre = ? WHERE id_etiqueta = ?"
            cursor.execute(consulta, (nombre, id_etiqueta))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Etiqueta actualizada correctamente")

        except Exception as ex:
            print("Error al actualizar etiqueta:", str(ex))

    def eliminar(self, id_etiqueta):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = "DELETE FROM etiquetas WHERE id_etiqueta = ?"
            cursor.execute(consulta, (id_etiqueta,))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Etiqueta eliminada correctamente")

        except Exception as ex:
            print("Error al eliminar etiqueta:", str(ex)) 