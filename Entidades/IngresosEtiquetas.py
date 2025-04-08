class IngresosEtiquetas:
    id_ingreso: int = 0
    id_etiqueta: int = 0

    def GetId_ingreso(self) -> int:
        return self.id_ingreso
    def SetId_ingreso(self, value: int) -> None:
        self.id_ingreso = value

    def GetId_etiqueta(self) -> int:
        return self.id_etiqueta
    def SetId_etiqueta(self, value: int) -> None:
        self.id_etiqueta = value