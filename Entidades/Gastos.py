from datetime import date, datetime

class Gastos:
    def __init__(self, id_gasto=None, id_usuario=None, fecha=None, monto=None, descripcion=None,
                 id_categoria=None, id_moneda=None, id_cuenta=None, id_tarjeta=None,
                 id_proveedor=None, id_metodo_pago=None):
        self.id_gasto = id_gasto
        self.id_usuario = id_usuario
        self.fecha = fecha
        self.monto = monto
        self.descripcion = descripcion
        self.id_categoria = id_categoria
        self.id_moneda = id_moneda
        self.id_cuenta = id_cuenta
        self.id_tarjeta = id_tarjeta
        self.id_proveedor = id_proveedor
        self.id_metodo_pago = id_metodo_pago


    def serialize(self):
        return {
            "id_gasto": self.id_gasto,
            "id_usuario": self.id_usuario,
            "fecha": self.fecha.isoformat() if isinstance(self.fecha, (date, datetime)) else str(self.fecha),
            "monto": float(self.monto) if self.monto is not None else None,
            "descripcion": self.descripcion,
            "id_categoria": self.id_categoria,
            "id_moneda": self.id_moneda,
            "id_cuenta": self.id_cuenta,
            "id_tarjeta": self.id_tarjeta,
            "id_proveedor": self.id_proveedor,
            "id_metodo_pago": self.id_metodo_pago
        }