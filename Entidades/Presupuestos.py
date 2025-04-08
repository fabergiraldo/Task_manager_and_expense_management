class Presupuestos:
    id_presupuesto: int = 0
    id_usuario: int = 0
    id_categoria: int = 0
    mes: str = None
    monto: float = 0.0

    def GetId_presupuesto(self) -> int:
        return self.id_presupuesto
    def SetId_presupuesto(self, value: int) -> None:
        self.id_presupuesto = value

    def GetId_usuario(self) -> int:
        return self.id_usuario
    def SetId_usuario(self, value: int) -> None:
        self.id_usuario = value

    def GetId_categoria(self) -> int:
        return self.id_categoria
    def SetId_categoria(self, value: int) -> None:
        self.id_categoria = value

    def GetMes(self) -> str:
        return self.mes
    def SetMes(self, value: str) -> None:
        self.mes = value

    def GetMonto(self) -> float:
        return self.monto
    def SetMonto(self, value: float) -> None:
        self.monto = value