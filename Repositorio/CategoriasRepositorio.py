import pyodbc
from Entidades.Categorias import Categorias
from Utilidades.Configuracion import Configuracion

class CategoriasRepositorio:

    def listar(self):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            consulta = "SELECT id_categoria, nombre, descripcion FROM categorias"
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista = []
            for elemento in cursor:
                categoria = Categorias(
                    id_categoria=elemento[0],
                    nombre=elemento[1],
                    descripcion=elemento[2]
                )
                lista.append(categoria)

            cursor.close()
            conexion.close()

            return lista

        except Exception as ex:
            print("Error al listar categorías:", str(ex))
            return []

    def guardar(self, nombre, descripcion):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = "INSERT INTO categorias (nombre, descripcion) VALUES (?, ?)"
            cursor.execute(consulta, (nombre, descripcion))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Categoría guardada correctamente")

        except Exception as ex:
            print("Error al guardar categoría:", str(ex))

    def actualizar(self, id_categoria, nombre, descripcion):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = "UPDATE categorias SET nombre = ?, descripcion = ? WHERE id_categoria = ?"
            cursor.execute(consulta, (nombre, descripcion, id_categoria))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Categoría actualizada correctamente")

        except Exception as ex:
            print("Error al actualizar categoría:", str(ex))

    def eliminar(self, id_categoria):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = "DELETE FROM categorias WHERE id_categoria = ?"
            cursor.execute(consulta, (id_categoria,))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Categoría eliminada correctamente")

        except Exception as ex:
            print("Error al eliminar categoría:", str(ex)) 