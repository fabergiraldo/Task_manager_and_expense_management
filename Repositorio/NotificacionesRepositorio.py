import pyodbc
from Utilidades.Configuracion import strConnection
from Entidades.Notificaciones import Notificaciones
from Utilidades.Encriptar import EncriptarAES 
class NotificacionesRepositorio:

    @staticmethod
    def listar():
        try:
            conexion = pyodbc.connect(strConnection)
            consulta = "SELECT id_notificacion, id_usuario, mensaje, fecha, leido FROM notificaciones"
            cursor = conexion.cursor()
            cursor.execute(consulta)

            encriptador = EncriptarAES()

            notificaciones = []
            for fila in cursor.fetchall():
                notificacion = Notificaciones(
                    id_notificacion=fila[0],
                    id_usuario=fila[1],
                    mensaje=encriptador.decifrar(fila[2]),
                    fecha=fila[3],
                    leido=fila[4]
                )
                notificaciones.append(notificacion)

            cursor.close()
            conexion.close()
            return notificaciones

        except Exception as ex:
            print("Error al listar notificaciones:", str(ex))
            return []
        # with pyodbc.connect(strConnection) as conexion:
        #     cursor = conexion.cursor()
        #     cursor.execute(
        #         "SELECT id_notificacion, id_usuario, mensaje, fecha, leido FROM notificaciones"
        #     )
        #     rows = cursor.fetchall()
        #     return [Notificaciones(*fila) for fila in rows]

    @staticmethod
    def crear(notificacion: Notificaciones):
        try:
            conexion = pyodbc.connect(strConnection)
            cursor = conexion.cursor()

            encriptador = EncriptarAES()
            cifrado = encriptador.cifrar(notificacion.mensaje)

            consulta = "INSERT INTO notificaciones (id_usuario, mensaje, fecha, leido) VALUES (?, ?, ?, ?)"
            cursor.execute(consulta, (notificacion.id_usuario, cifrado, notificacion.fecha, notificacion.leido))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("✅ Notificación guardada correctamente con mensaje cifrado.")

        except Exception as ex:
            print("Error al guardar notificación:", str(ex))
        # with pyodbc.connect(strConnection) as conexion:
        #     cursor = conexion.cursor()
        #     # fecha y leido pueden usar valores por defecto en BD
        #     cursor.execute(
        #         "INSERT INTO notificaciones (id_usuario, mensaje, fecha, leido) VALUES (?, ?, ?, ?)",
        #         (notificacion.id_usuario, notificacion.mensaje, notificacion.fecha or datetime.utcnow(), notificacion.leido)
        #     )
        #     conexion.commit()

    @staticmethod
    def actualizar(notificacion: Notificaciones):
        try:
            conexion = pyodbc.connect(strConnection)
            cursor = conexion.cursor()

            encriptador = EncriptarAES()
            cifrado = encriptador.cifrar(notificacion.mensaje)

            consulta = """
                UPDATE notificaciones SET id_usuario=?, mensaje=?, fecha=?, leido=? WHERE id_notificacion=?
            """
            cursor.execute(consulta, (notificacion.id_usuario, cifrado, notificacion.fecha, notificacion.leido, notificacion.id_notificacion))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Notificación actualizada correctamente con mensaje cifrado.")

        except Exception as ex:
            print("Error al actualizar notificación:", str(ex))
        # with pyodbc.connect(strConnection) as conexion:
        #     cursor = conexion.cursor()
        #     cursor.execute(
        #         "UPDATE notificaciones SET id_usuario=?, mensaje=?, fecha=?, leido=? WHERE id_notificacion=?",
        #         (notificacion.id_usuario, notificacion.mensaje, notificacion.fecha, notificacion.leido, notificacion.id_notificacion)
        #     )
        #     conexion.commit()

    @staticmethod
    def eliminar(id_notificacion):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM notificaciones WHERE id_notificacion=?", (id_notificacion,))
            conexion.commit()