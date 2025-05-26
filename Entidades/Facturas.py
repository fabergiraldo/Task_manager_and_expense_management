from Utilidades.Encriptar import EncriptarAES
class Facturas:
    def __init__(self, id_factura=None, id_gasto=None, id_proveedor=None, ruta_archivo=None):
        self.id_factura = id_factura
        self.id_gasto = id_gasto
        self.id_proveedor = id_proveedor
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
        return EncriptarAES.decifrar(self.ruta_archivo) if self.ruta_archivo else None
    def SetRuta_archivo(self, value: str) -> None:
        self.ruta_archivo = EncriptarAES.cifrar(value) if value else None    
        
    def serialize(self):
        return {
            "id_factura": self.id_factura,
            "id_gasto": self.id_gasto,
            "id_proveedor": self.id_proveedor,
            "ruta_archivo": self.ruta_archivo
        }