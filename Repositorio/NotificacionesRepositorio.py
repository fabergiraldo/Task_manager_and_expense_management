import pyodbc
from Entidades.Notificaciones import Notificaciones
from Utilidades.Configuracion import Configuracion
from Utilidades.Encriptar import EncriptarAES 

class NotificacionesRepositorio:
    def __init__(self):
        self.encriptarAES = EncriptarAES() 

    def listar(self):
        respuesta: dict = {}
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            consulta = "SELECT id_notificacion, id_usuario, mensaje, fecha, leido FROM notificaciones"
            cursor = conexion.cursor()
            cursor.execute(consulta)

            contador = 0
            for elemento in cursor:
                lista: dict = {}                
                lista["id_notificacion"] = elemento[0]
                lista["id_usuario"] = elemento[1]
                lista["mensaje"] = self.encriptarAES.decifrar(elemento[2])
                lista["fecha"] = elemento[3]
                lista["leido"] = elemento[4]
                respuesta[str(contador)] = lista
                contador += 1  

            cursor.close()
            conexion.close()
            return respuesta

        except Exception as ex:
            print("Error al listar notificaciones:", str(ex))
            return respuesta

    def guardar(self, id_usuario, mensaje, fecha, leido):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            cifrado = self.encriptarAES.cifrar(mensaje)

            consulta = "INSERT INTO notificaciones (id_usuario, mensaje, fecha, leido) VALUES (?, ?, ?, ?)"
            cursor.execute(consulta, (id_usuario, cifrado, fecha, leido))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Notificación guardada correctamente")

        except Exception as ex:
            print("Error al guardar notificación:", str(ex))

    def actualizar(self, id_notificacion, id_usuario, mensaje, leido):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            cifrado = self.encriptarAES.cifrar(mensaje)

            consulta = "UPDATE notificaciones SET id_usuario = ?, mensaje = ?, leido = ? WHERE id_notificacion = ?"
            cursor.execute(consulta, (id_usuario, cifrado, leido, id_notificacion))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Notificación actualizada correctamente")

        except Exception as ex:
            print("Error al actualizar notificación:", str(ex))

    def eliminar(self, id_notificacion):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = "DELETE FROM notificaciones WHERE id_notificacion = ?"
            cursor.execute(consulta, (id_notificacion,))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Notificación eliminada correctamente")

        except Exception as ex:
            print("Error al eliminar notificación:", str(ex))
