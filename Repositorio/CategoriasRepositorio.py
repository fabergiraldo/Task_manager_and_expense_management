import pyodbc
from Utilidades.Configuracion import strConnection
from Entidades.Categorias import Categorias

class CategoriasRepositorio:

    @staticmethod
    def listar():
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT id_categoria, nombre, descripcion FROM categorias")
            return [Categorias(*fila) for fila in cursor.fetchall()]

    @staticmethod
    def crear(categoria: Categorias):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO categorias (nombre, descripcion) VALUES (?, ?)",
                (categoria.nombre, categoria.descripcion)
            )
            conexion.commit()

    @staticmethod
    def actualizar(categoria: Categorias):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "UPDATE categorias SET nombre=?, descripcion=? WHERE id_categoria=?",
                (categoria.nombre, categoria.descripcion, categoria.id_categoria)
            )
            conexion.commit()

    @staticmethod
    def eliminar(id_categoria):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM categorias WHERE id_categoria=?", (id_categoria,))
            conexion.commit()