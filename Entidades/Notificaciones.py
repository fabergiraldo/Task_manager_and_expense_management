from Utilidades.Encriptar import EncriptarAES

class Notificaciones:
    def __init__(self, id_notificacion: int = 0, id_usuario: int = 0, mensaje: str = None, fecha: str = None, leido: bool = False):
        self.id_notificacion = id_notificacion
        self.id_usuario = id_usuario
        self.mensaje = mensaje
        self.fecha = fecha
        self.leido = leido

    id_notificacion: int = 0
    def GetIdNotificacion(self) -> int:
        return self.id_notificacion
    def SetIdNotificacion(self, value: int) -> None:
        self.id_notificacion = value

    id_usuario: int = 0
    def GetIdUsuario(self) -> int:
        return self.id_usuario
    def SetIdUsuario(self, value: int) -> None:
        self.id_usuario = value

    mensaje: str = None
    def GetMensaje(self) -> str:
        return EncriptarAES.decifrar(self.mensaje) if self.mensaje else None
    def SetMensaje(self, value: str) -> None:
        self.mensaje = EncriptarAES.cifrar(value) if value else None

    fecha: str = None
    def GetFecha(self) -> str:
        return self.fecha
    def SetFecha(self, value: str) -> None:
        self.fecha = value

    leido: bool = False
    def GetLeido(self) -> bool:
        return self.leido
    def SetLeido(self, value: bool) -> None:
        self.leido = value

    def __str__(self):
        return f"ID: {self.GetIdNotificacion()}, usuario: {self.GetIdUsuario()}, mensaje: {self.GetMensaje()}, fecha: {self.GetFecha()}, leído: {self.GetLeido()}"
