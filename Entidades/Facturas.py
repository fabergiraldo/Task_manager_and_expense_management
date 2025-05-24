class Facturas:
    def __init__(self, id_factura: int = 0, id_gasto: int = 0, ruta_archivo: str = None):
        self.id_factura = id_factura
        self.id_gasto = id_gasto
        self.ruta_archivo = ruta_archivo
    
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

    def __str__(self):
        return f"ID: {self.GetId_factura()}, nombre: {self.GetId_gasto()}, descripcion: {self.GetRuta_archivo()}"

    def serialize(self):
        return {
            "id_factura": self.id_factura,
            "id_gasto": self.id_gasto,
            "id_proveedor": self.id_proveedor,
            "ruta_archivo": self.ruta_archivo
        }