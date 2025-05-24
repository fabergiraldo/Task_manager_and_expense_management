class Usuarios:
    def __init__(self, id_usuario: int = 0, nombre: str = None, correo: str = None, contrasena: str = None, fecha_registro: str = None):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena
        self.fecha_registro = fecha_registro

    def GetIdUsuario(self) -> int:
        return self.id_usuario

    def SetIdUsuario(self, value: int) -> None:
        self.id_usuario = value

    def GetNombre(self) -> str:
        return self.nombre

    def SetNombre(self, value: str) -> None:
        self.nombre = value

    def GetCorreo(self) -> str:
        return self.correo

    def SetCorreo(self, value: str) -> None:
        self.correo = value

    def GetContrasena(self) -> str:
        return self.contrasena

    def SetContrasena(self, value: str) -> None:
        self.contrasena = value

    def GetFechaRegistro(self) -> str:
        return self.fecha_registro

    def SetFechaRegistro(self, value: str) -> None:
        self.fecha_registro = value

    def __str__(self):
        return f"ID: {self.GetIdUsuario()}, Nombre: {self.GetNombre()}, Correo: {self.GetCorreo()}, Fecha Registro: {self.GetFechaRegistro()}"
    
    def serialize(self):
        return {
            "id_usuario": self.id_usuario,
            "nombre": self.nombre,
            "correo": self.correo,
            # normalmente no expondrías la contraseña en un JSON…
            "fecha_registro": self.fecha_registro.isoformat() if self.fecha_registro else None
        }


