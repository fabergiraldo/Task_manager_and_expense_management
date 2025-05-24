import pyodbc
from Utilidades.Configuracion import strConnection
from Entidades.Notificaciones import Notificaciones

class NotificacionesRepositorio:

    @staticmethod
    def listar():
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "SELECT id_notificacion, id_usuario, mensaje, fecha, leido FROM notificaciones"
            )
            rows = cursor.fetchall()
            return [Notificaciones(*fila) for fila in rows]

    @staticmethod
    def crear(notificacion: Notificaciones):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            # fecha y leido pueden usar valores por defecto en BD
            cursor.execute(
                "INSERT INTO notificaciones (id_usuario, mensaje, fecha, leido) VALUES (?, ?, ?, ?)",
                (notificacion.id_usuario, notificacion.mensaje, notificacion.fecha or datetime.utcnow(), notificacion.leido)
            )
            conexion.commit()

    @staticmethod
    def actualizar(notificacion: Notificaciones):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "UPDATE notificaciones SET id_usuario=?, mensaje=?, fecha=?, leido=? WHERE id_notificacion=?",
                (notificacion.id_usuario, notificacion.mensaje, notificacion.fecha, notificacion.leido, notificacion.id_notificacion)
            )
            conexion.commit()

    @staticmethod
    def eliminar(id_notificacion):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM notificaciones WHERE id_notificacion=?", (id_notificacion,))
            conexion.commit()