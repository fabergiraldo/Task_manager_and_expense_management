class Facturas:
    id_factura: int = 0
    id_gasto: int = 0
    ruta_archivo: str = None

    def GetId_factura(self) -> int:
        return self.id_factura
    def SetId_factura(self, value: int) -> None:
        self.id_factura = value

    def GetId_gasto(self) -> int:
        return self.id_gasto
    def SetId_gasto(self, value: int) -> None:
        self.id_gasto = value

    def GetRuta_archivo(self) -> str:
        return self.ruta_archivo
    def SetRuta_archivo(self, value: str) -> None:
        self.ruta_archivo = value