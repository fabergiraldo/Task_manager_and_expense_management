import pyodbc
from Utilidades.Configuracion import strConnection
from Entidades.Usuarios import Usuarios

class UsuariosRepositorio:

    @staticmethod
    def listar():
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM usuarios")
            return [Usuarios(*fila) for fila in cursor.fetchall()]

    @staticmethod
    def crear(usuario: Usuarios):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute("""
                INSERT INTO usuarios (nombre, correo, contrasena)
                VALUES (?, ?, ?)""", (usuario.nombre, usuario.correo, usuario.contrasena))
            conexion.commit()

    @staticmethod
    def actualizar(usuario: Usuarios):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute("""
                UPDATE usuarios SET nombre=?, correo=?, contrasena=? WHERE id_usuario=?""",
                (usuario.nombre, usuario.correo, usuario.contrasena, usuario.id_usuario))
            conexion.commit()

    @staticmethod
    def eliminar(id_usuario):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM usuarios WHERE id_usuario=?", (id_usuario,))
            conexion.commit()
