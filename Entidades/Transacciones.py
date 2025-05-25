from datetime import date, datetime

class Transacciones:
    def __init__(self, id_transaccion=None, id_usuario=None, tipo=None, id_categoria=None,
                 id_moneda=None, id_cuenta=None, id_metodo_pago=None, fecha=None):
        self.id_transaccion = id_transaccion
        self.id_usuario = id_usuario
        self.tipo = tipo
        self.id_categoria = id_categoria
        self.id_moneda = id_moneda
        self.id_cuenta = id_cuenta
        self.id_metodo_pago = id_metodo_pago
        self.fecha = fecha

    def serialize(self):
        return {
            "id_transaccion": self.id_transaccion,
            "id_usuario": self.id_usuario,
            "tipo": self.tipo,
            "id_categoria": self.id_categoria,
            "id_moneda": self.id_moneda,
            "id_cuenta": self.id_cuenta,
            "id_metodo_pago": self.id_metodo_pago,
            "fecha": self.fecha.isoformat() if isinstance(self.fecha, datetime) else str(self.fecha)
        }