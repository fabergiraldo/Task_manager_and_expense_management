class GastosEtiquetas:
    id_gasto: int = 0
    id_etiqueta: int = 0

    def GetId_gasto(self) -> int:
        return self.id_gasto
    def SetId_gasto(self, value: int) -> None:
        self.id_gasto = value

    def GetId_etiqueta(self) -> int:
        return self.id_etiqueta
    def SetId_etiqueta(self, value: int) -> None:
        self.id_etiqueta = value