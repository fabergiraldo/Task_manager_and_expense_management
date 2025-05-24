class Tarjetas:
    id_tarjeta: int = 0
    id_usuario: int = 0
    nombre_tarjeta: str = None
    tipo: str = None
    numero_tarjeta: str = None
    vencimiento: str = None

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
        return self.numero_tarjeta
    def SetNumero_tarjeta(self, value: str) -> None:
        self.numero_tarjeta = value

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