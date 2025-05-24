class MetodosPago:
    id_metodo_pago: int = 0
    metodo: str = None

    def GetId_metodo_pago(self) -> int:
        return self.id_metodo_pago
    def SetId_metodo_pago(self, value: int) -> None:
        self.id_metodo_pago = value

    def GetMetodo(self) -> str:
        return self.metodo
    def SetMetodo(self, value: str) -> None:
        self.metodo = value

    def serialize(self):
        return {
            "id_metodo_pago": self.id_metodo_pago,
            "metodo": self.metodo
        }