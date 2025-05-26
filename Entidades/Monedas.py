# entidades/moneda.py
# Solo contiene información pública sobre monedas no aplica para encriptacion
class Monedas:
    def __init__(self, id_moneda=None, nombre=None, codigo=None, simbolo=None):
        self.id_moneda = id_moneda
        self.nombre = nombre
        self.codigo = codigo
        self.simbolo = simbolo

    def serialize(self):
        return {
            "id_moneda": self.id_moneda,
            "nombre": self.nombre,
            "codigo": self.codigo,
            "simbolo": self.simbolo
        }