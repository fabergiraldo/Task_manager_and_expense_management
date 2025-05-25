
class Presupuestos:
    def __init__(self, id_presupuesto=None, id_usuario=None, id_categoria=None, mes=None, monto=None):
        self.id_presupuesto = id_presupuesto
        self.id_usuario     = id_usuario
        self.id_categoria   = id_categoria
        self.mes            = mes   # año, formato YYYY
        self.monto          = monto

    def serialize(self):
        return {
            "id_presupuesto": self.id_presupuesto,
            "id_usuario":     self.id_usuario,
            "id_categoria":   self.id_categoria,
            "mes":            str(self.mes),
            "monto":          float(self.monto) if self.monto is not None else None
        }


    