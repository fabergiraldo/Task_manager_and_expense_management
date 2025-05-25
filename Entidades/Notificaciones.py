from datetime import date, datetime

class Notificaciones:
    def __init__(self, id_notificacion=None, id_usuario=None, mensaje=None, fecha=None, leido=False):
        self.id_notificacion = id_notificacion
        self.id_usuario = id_usuario
        self.mensaje = mensaje
        self.fecha = fecha
        self.leido = bool(leido)

    def serialize(self):
        return {
            "id_notificacion": self.id_notificacion,
            "id_usuario": self.id_usuario,
            "mensaje": self.mensaje,
            "fecha": self.fecha.isoformat() if isinstance(self.fecha, datetime) else str(self.fecha),
            "leido": self.leido
        }