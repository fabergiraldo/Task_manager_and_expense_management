class Facturas:
    def __init__(self, id_factura=None, id_gasto=None, id_proveedor=None, ruta_archivo=None):
        self.id_factura = id_factura
        self.id_gasto = id_gasto
        self.id_proveedor = id_proveedor
        self.ruta_archivo = ruta_archivo
        
    def serialize(self):
        return {
            "id_factura": self.id_factura,
            "id_gasto": self.id_gasto,
            "id_proveedor": self.id_proveedor,
            "ruta_archivo": self.ruta_archivo
        }