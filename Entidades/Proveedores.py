from Utilidades.Encriptar import EncriptarAES
class Proveedores:
    def __init__(self, id_proveedor: int = 0, nombre: str = None, contacto: str = None, telefono: str = None, correo: str = None):
        self.id_proveedor = id_proveedor
        self.nombre = nombre
        self.contacto = contacto
        self.telefono = telefono
        self.correo = correo

    def GetId_proveedor(self) -> int:
        return self.id_proveedor
    def SetId_proveedor(self, value: int) -> None:
        self.id_proveedor = value

    def GetNombre(self) -> str:
        return self.nombre
    def SetNombre(self, value: str) -> None:
        self.nombre = value

    def GetContacto(self) -> str:
        return EncriptarAES.decifrar(self.contacto) if self.contacto else None
    def SetContacto(self, value: str) -> None:
        self.contacto = EncriptarAES.cifrar(value) if value else None

    def GetTelefono(self) -> str:
        return EncriptarAES.decifrar(self.telefono) if self.telefono else None
    def SetTelefono(self, value: str) -> None:
        self.telefono = EncriptarAES.cifrar(value) if value else None

    def GetCorreo(self) -> str:
        return EncriptarAES.decifrar(self.correo) if self.correo else None
    def SetCorreo(self, value: str) -> None:
        self.correo = EncriptarAES.cifrar(value) if value else None

    def __str__(self):
        return f"id_proveedor: {self.GetId_proveedor()}, nombre: {self.GetNombre()}, contacto: {self.GetContacto()}, telefono: {self.GetTelefono()}, correo: {self.GetCorreo()}"