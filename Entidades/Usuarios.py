from Utilidades.Encriptar import EncriptarAES
class Usuarios:
    def __init__(self, id_usuario: int = 0, nombre: str = None, correo: str = None, contrasena: str = None):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena
        #self.fecha_registro = fecha_registro

    def GetIdUsuario(self) -> int:
        return self.id_usuario

    def SetIdUsuario(self, value: int) -> None:
        self.id_usuario = value

    def GetNombre(self) -> str:
        return self.nombre

    def SetNombre(self, value: str) -> None:
        self.nombre = value

    def GetCorreo(self) -> str:
        return EncriptarAES.decifrar(self.correo) if self.correo else None

    def SetCorreo(self, value: str) -> None:
        self.correo = EncriptarAES.cifrar(value) if value else None

    def GetContrasena(self) -> str:
        return EncriptarAES.decifrar(self.contrasena) if self.contrasena else None

    def SetContrasena(self, value: str) -> None:
        self.contrasena = EncriptarAES.cifrar(value) if value else None

    # def GetFechaRegistro(self) -> str:
    #     return self.fecha_registro

    # def SetFechaRegistro(self, value: str) -> None:
    #     self.fecha_registro = value

    def __str__(self):
        return f"ID: {self.GetIdUsuario()}, Nombre: {self.GetNombre()}, Correo: {self.GetCorreo()}"
    
    def serialize(self):
        return {
            "id_usuario": self.id_usuario,
            "nombre": self.nombre,
            "correo": self.correo
            # normalmente no expondrías la contraseña en un JSON…
            #"fecha_registro": self.fecha_registro.isoformat() if self.fecha_registro else None
        }


