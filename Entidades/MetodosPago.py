# MetodosPago: Solo contiene nombres de métodos de pago
class MetodosPago:
    def __init__(self, id_metodo_pago: int = 0, metodo: str = None):
        self.id_categoria = id_metodo_pago
        self.metodo = metodo

    def GetId_metodo_pago(self) -> int:
        return self.id_metodo_pago
    def SetId_metodo_pago(self, value: int) -> None:
        self.id_metodo_pago = value

    def GetMetodo(self) -> str:
        return self.metodo
    def SetMetodo(self, value: str) -> None:
        self.metodo = value

    def __str__(self):
        return f"id_metodo_pago: {self.GetId_metodo_pago()}, metodo: {self.GetMetodo()}"