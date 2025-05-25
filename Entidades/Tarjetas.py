class Tarjetas:
    def __init__(self, id_tarjeta=None, id_usuario=None, nombre_tarjeta=None, tipo=None, numero_tarjeta=None, vencimiento=None):
        self.id_tarjeta = id_tarjeta
        self.id_usuario = id_usuario
        self.nombre_tarjeta = nombre_tarjeta
        self.tipo = tipo
        self.numero_tarjeta = numero_tarjeta
        self.vencimiento = vencimiento

    def serialize(self):
        return {
            "id_tarjeta": self.id_tarjeta,
            "id_usuario": self.id_usuario,
            "nombre_tarjeta": self.nombre_tarjeta,
            "tipo": self.tipo,
            "numero_tarjeta": self.numero_tarjeta,
            "vencimiento": self.vencimiento.isoformat() if self.vencimiento else None
        }