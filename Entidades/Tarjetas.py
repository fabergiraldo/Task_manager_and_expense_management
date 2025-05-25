from Utilidades.Encriptar import EncriptarAES
class Tarjetas:
    def __init__(self, id_tarjeta: int = 0, id_usuario: int = 0, nombre_tarjeta: str = None, tipo: str = None, numero_tarjeta: str = None, vencimiento: str = None):
        self.id_tarjeta = id_tarjeta
        self.id_usuario = id_usuario
        self.nombre_tarjeta = nombre_tarjeta
        self.tipo = tipo
        self.numero_tarjeta = numero_tarjeta
        self.vencimiento = vencimiento

    def GetId_tarjeta(self) -> int:
        return self.id_tarjeta
    def SetId_tarjeta(self, value: int) -> None:
        self.id_tarjeta = value

    def GetId_usuario(self) -> int:
        return self.id_usuario
    def SetId_usuario(self, value: int) -> None:
        self.id_usuario = value

    def GetNombre_tarjeta(self) -> str:
        return self.nombre_tarjeta
    def SetNombre_tarjeta(self, value: str) -> None:
        self.nombre_tarjeta = value

    def GetTipo(self) -> str:
        return self.tipo
    def SetTipo(self, value: str) -> None:
        self.tipo = value

    def GetNumero_tarjeta(self) -> str:
        return EncriptarAES.decifrar(self.numero_tarjeta) if self.numero_tarjeta else None
    def SetNumero_tarjeta(self, value: str) -> None:
        self.numero_tarjeta = EncriptarAES.cifrar(value) if value else None

    def GetVencimiento(self) -> str:
        return self.vencimiento
    def SetVencimiento(self, value: str) -> None:
        self.vencimiento = value

    def __str__(self):
        return f"id_tarjeta: {self.GetId_gasto()}, id_usuario: {self.GetId_usuario()}, nombre_tarjeta: {self.GetNombre_tarjeta()}, tipo: {self.GetTipo()}, numero_tarjeta: {self.GetNumero_tarjeta()}, vencimiento: {self.GetVencimiento()}"