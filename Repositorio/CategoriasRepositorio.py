import pyodbc
from Utilidades.Configuracion import strConnection
from Entidades.Categorias import Categorias
from Utilidades.Encriptar import EncriptarAES

class CategoriasRepositorio:

    @staticmethod
    def listar():
        try:
            conexion = pyodbc.connect(strConnection)
            consulta = "SELECT id_categoria, nombre, descripcion FROM categorias"
            cursor = conexion.cursor()
            cursor.execute(consulta)

            encriptador = EncriptarAES()

            categorias = []
            for fila in cursor.fetchall():
                categoria = Categorias(
                    id_categoria=fila[0],
                    nombre=fila[1],
                    descripcion=encriptador.decifrar(fila[2]),
                )
                categorias.append(categoria)

            cursor.close()
            conexion.close()
            return categorias

        except Exception as ex:
            print("Error al listar categorías:", str(ex))
            return []
        # with pyodbc.connect(strConnection) as conexion:
        #     cursor = conexion.cursor()
        #     cursor.execute("SELECT id_categoria, nombre, descripcion FROM categorias")
        #     return [Categorias(*fila) for fila in cursor.fetchall()]

    @staticmethod
    def crear(categoria: Categorias):
        try:
            conexion = pyodbc.connect(strConnection)
            cursor = conexion.cursor()

            encriptador = EncriptarAES()
            cifrado = encriptador.cifrar(categoria.descripcion)

            consulta = "INSERT INTO categorias (nombre, descripcion) VALUES (?, ?)"
            cursor.execute(consulta, (categoria.nombre, cifrado))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("✅ Categoría guardada correctamente con descripción cifrada.")

        except Exception as ex:
            print("Error al guardar categoría:", str(ex))
        # with pyodbc.connect(strConnection) as conexion:
        #     cursor = conexion.cursor()
        #     cursor.execute(
        #         "INSERT INTO categorias (nombre, descripcion) VALUES (?, ?)",
        #         (categoria.nombre, categoria.descripcion)
        #     )
        #     conexion.commit()

    @staticmethod
    def actualizar(categoria: Categorias):
        try:
            conexion = pyodbc.connect(strConnection)
            cursor = conexion.cursor()

            encriptador = EncriptarAES()
            cifrado = encriptador.cifrar(categoria.descripcion)

            consulta = """
                UPDATE categorias SET nombre=?, descripcion=? WHERE id_categoria=?
            """
            cursor.execute(consulta, (categoria.nombre, cifrado, categoria.id_categoria))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Categoría actualizada correctamente con descripción cifrada.")

        except Exception as ex:
            print("Error al actualizar categoría:", str(ex))
        # with pyodbc.connect(strConnection) as conexion:
        #     cursor = conexion.cursor()
        #     cursor.execute(
        #         "UPDATE categorias SET nombre=?, descripcion=? WHERE id_categoria=?",
        #         (categoria.nombre, categoria.descripcion, categoria.id_categoria)
        #     )
        #     conexion.commit()

    @staticmethod
    def eliminar(id_categoria):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM categorias WHERE id_categoria=?", (id_categoria,))
            conexion.commit()