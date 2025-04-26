class GastosEtiquetas:
    def __init__(self, id_gasto: int = 0, id_etiqueta: int = 0):
        self.id_gasto = id_gasto
        self.id_etiqueta = id_etiqueta

    def GetId_gasto(self) -> int:
        return self.id_gasto
    def SetId_gasto(self, value: int) -> None:
        self.id_gasto = value

    def GetId_etiqueta(self) -> int:
        return self.id_etiqueta
    def SetId_etiqueta(self, value: int) -> None:
        self.id_etiqueta = value

    def __str__(self):
        return f"id_gasto: {self.GetId_gasto()}, id_etiqueta: {self.GetId_etiqueta()}"