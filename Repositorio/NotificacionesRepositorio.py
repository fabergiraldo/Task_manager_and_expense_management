import pyodbc
from Entidades.Notificaciones import Notificaciones
from Utilidades.Configuracion import Configuracion

class NotificacionesRepositorio:
    def listar(self):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            cursor.execute("SELECT id_notificacion, id_usuario, mensaje, fecha, leido FROM notificaciones")
            lista = [
                Notificaciones(
                    id_notificacion=row[0],
                    id_usuario=row[1],
                    mensaje=row[2],
                    fecha=row[3],
                    leido=row[4]
                ) for row in cursor
            ]
            cursor.close()
            conexion.close()
            return lista
        except Exception as ex:
            print("Error al listar notificaciones:", ex)
            return []

    def guardar(self, id_usuario, mensaje):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO notificaciones (id_usuario, mensaje) VALUES (?, ?)", (id_usuario, mensaje))
            conexion.commit()
            cursor.close()
            conexion.close()
            print("Notificación guardada correctamente")
        except Exception as ex:
            print("Error al guardar notificación:", ex)

    def actualizar(self, id_notificacion, id_usuario, mensaje, leido):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            cursor.execute(
                "UPDATE notificaciones SET id_usuario = ?, mensaje = ?, leido = ? WHERE id_notificacion = ?",
                (id_usuario, mensaje, leido, id_notificacion)
            )
            conexion.commit()
            cursor.close()
            conexion.close()
            print("Notificación actualizada correctamente")
        except Exception as ex:
            print("Error al actualizar notificación:", ex)

    def eliminar(self, id_notificacion):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM notificaciones WHERE id_notificacion = ?", (id_notificacion,))
            conexion.commit()
            cursor.close()
            conexion.close()
            print("Notificación eliminada correctamente")
        except Exception as ex:
            print("Error al eliminar notificación:", ex)