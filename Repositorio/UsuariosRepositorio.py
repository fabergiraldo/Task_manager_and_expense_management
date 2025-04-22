import pyodbc
from Entidades.Usuarios import Usuarios
from Utilidades.Configuracion import Configuracion

class UsuariosRepositorio:

    def listar(self):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            consulta = "SELECT id_usuario, nombre, correo, fecha_registro FROM usuarios"
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista = []
            for elemento in cursor:
                usuario = Usuarios(
                    id_usuario=elemento[0],
                    nombre=elemento[1],
                    correo=elemento[2],
                    fecha_registro=elemento[3]
                )
                lista.append(usuario)

            cursor.close()
            conexion.close()

            return lista

        except Exception as ex:
            print("Error al listar usuarios:", str(ex))
            return []  # Devuelve una lista vacía si ocurre un error


    def guardar(self, nombre, correo, contrasena):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = "INSERT INTO usuarios (nombre, correo, contrasena) VALUES (?, ?, ?)"
            cursor.execute(consulta, (nombre, correo, contrasena))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Usuario guardado correctamente")

        except Exception as ex:
            print("Error al guardar usuario:", str(ex))

    def actualizar(self, id_usuario, nombre, correo):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = "UPDATE usuarios SET nombre = ?, correo = ? WHERE id_usuario = ?"
            cursor.execute(consulta, (nombre, correo, id_usuario))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Usuario actualizado correctamente")

        except Exception as ex:
            print("Error al actualizar usuario:", str(ex))

    def eliminar(self, id_usuario):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = "DELETE FROM usuarios WHERE id_usuario = ?"
            cursor.execute(consulta, (id_usuario,))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Usuario eliminado correctamente")

        except Exception as ex:
            print("Error al eliminar usuario:", str(ex))
