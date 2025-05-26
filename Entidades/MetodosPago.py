# No aplica Encriptacion, solo contiene nombres de métodos de pago
class MetodosPago:
    def __init__(self, id_metodo_pago=None, metodo=None):
        self.id_metodo_pago = id_metodo_pago
        self.metodo = metodo


    def serialize(self):
        return {
            "id_metodo_pago": self.id_metodo_pago,
            "metodo": self.metodo
        }