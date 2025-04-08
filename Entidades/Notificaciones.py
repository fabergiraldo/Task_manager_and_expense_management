class Notificaciones:
    id_notificacion: int = 0
    id_usuario: int = 0
    mensaje: str = None
    fecha: str = None
    leido: bool = False

    def GetId_notificacion(self) -> int:
        return self.id_notificacion
    def SetId_notificacion(self, value: int) -> None:
        self.id_notificacion = value

    def GetId_usuario(self) -> int:
        return self.id_usuario
    def SetId_usuario(self, value: int) -> None:
        self.id_usuario = value

    def GetMensaje(self) -> str:
        return self.mensaje
    def SetMensaje(self, value: str) -> None:
        self.mensaje = value

    def GetFecha(self) -> str:
        return self.fecha
    def SetFecha(self, value: str) -> None:
        self.fecha = value

    def GetLeido(self) -> bool:
        return self.leido
    def SetLeido(self, value: bool) -> None:
        self.leido = value