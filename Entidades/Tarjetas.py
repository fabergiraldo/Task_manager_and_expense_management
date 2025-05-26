from Utilidades.Encriptar import EncriptarAES
class Tarjetas:
    def __init__(self, id_tarjeta=None, id_usuario=None, nombre_tarjeta=None, tipo=None, numero_tarjeta=None, vencimiento=None):
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

    def serialize(self):
        return {
            "id_tarjeta": self.id_tarjeta,
            "id_usuario": self.id_usuario,
            "nombre_tarjeta": self.nombre_tarjeta,
            "tipo": self.tipo,
            "numero_tarjeta": self.numero_tarjeta,
            "vencimiento": self.vencimiento.isoformat() if self.vencimiento else None
        }