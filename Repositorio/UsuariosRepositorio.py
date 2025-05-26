import pyodbc
from Utilidades.Configuracion import strConnection
from Entidades.Usuarios import Usuarios
from Utilidades.Encriptar import EncriptarAES 
class UsuariosRepositorio:

    @staticmethod
    def listar():
        try:
            conexion = pyodbc.connect(strConnection)
            consulta = "SELECT id_usuario, nombre, correo, contrasena FROM usuarios"
            cursor = conexion.cursor()
            cursor.execute(consulta)

            encriptador = EncriptarAES()

            usuarios = []
            for fila in cursor.fetchall():
                usuario = Usuarios(
                    id_usuario=fila[0],
                    nombre=fila[1],
                    correo=encriptador.decifrar(fila[2]),
                    contrasena=encriptador.decifrar(fila[3]),
                )
                usuarios.append(usuario)

            cursor.close()
            conexion.close()
            return usuarios

        except Exception as ex:
            print("Error al listar usuarios:", str(ex))
            return []

        # with pyodbc.connect(strConnection) as conexion:
        #     cursor = conexion.cursor()
        #     cursor.execute("SELECT * FROM usuarios")
        #     return [Usuarios(*fila) for fila in cursor.fetchall()]

    @staticmethod
    def crear(usuario: Usuarios):
        try:
            conexion = pyodbc.connect(strConnection)
            cursor = conexion.cursor()

            encriptador = EncriptarAES()
            cifradoE = encriptador.cifrar(usuario.correo)
            cifrado = encriptador.cifrar(usuario.contrasena)

            consulta = "INSERT INTO usuarios (nombre, correo, contrasena) VALUES (?, ?, ?)"
            cursor.execute(consulta, (usuario.nombre, cifradoE, cifrado))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Usuario guardado correctamente con contraseña cifrada.")

        except Exception as ex:
            print("Error al guardar usuario:", str(ex))



    # def crear(usuario: Usuarios):
    #     with pyodbc.connect(strConnection) as conexion:
    #         cursor = conexion.cursor()
    #         cursor.execute("""
    #             INSERT INTO usuarios (nombre, correo, contrasena)
    #             VALUES (?, ?, ?)""", (usuario.nombre, usuario.correo, usuario.contrasena))
    #         conexion.commit()

    @staticmethod
    def actualizar(usuario: Usuarios):
        try:
            conexion = pyodbc.connect(strConnection)
            cursor = conexion.cursor()

            encriptador = EncriptarAES()
            cifradoE = encriptador.cifrar(usuario.correo)
            cifrado = encriptador.cifrar(usuario.contrasena)

            consulta = """
                UPDATE usuarios SET nombre=?, correo=?, contrasena=? WHERE id_usuario=?
            """
            cursor.execute(consulta, (usuario.nombre, cifradoE, cifrado, usuario.id_usuario))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Usuario actualizado correctamente.")

        except Exception as ex:
            print("Error al actualizar usuario:", str(ex))
        # with pyodbc.connect(strConnection) as conexion:
        #     cursor = conexion.cursor()
        #     cursor.execute("""
        #         UPDATE usuarios SET nombre=?, correo=?, contrasena=? WHERE id_usuario=?""",
        #         (usuario.nombre, usuario.correo, usuario.contrasena, usuario.id_usuario))
        #     conexion.commit()

    @staticmethod
    def eliminar(id_usuario):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM usuarios WHERE id_usuario=?", (id_usuario,))
            conexion.commit()
