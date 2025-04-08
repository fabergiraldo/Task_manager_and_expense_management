class Proveedores:
    id_proveedor: int = 0
    nombre: str = None
    contacto: str = None
    telefono: str = None
    correo: str = None

    def GetId_proveedor(self) -> int:
        return self.id_proveedor
    def SetId_proveedor(self, value: int) -> None:
        self.id_proveedor = value

    def GetNombre(self) -> str:
        return self.nombre
    def SetNombre(self, value: str) -> None:
        self.nombre = value

    def GetContacto(self) -> str:
        return self.contacto
    def SetContacto(self, value: str) -> None:
        self.contacto = value

    def GetTelefono(self) -> str:
        return self.telefono
    def SetTelefono(self, value: str) -> None:
        self.telefono = value

    def GetCorreo(self) -> str:
        return self.correo
    def SetCorreo(self, value: str) -> None:
        self.correo = value