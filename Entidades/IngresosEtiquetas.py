# No aplica encriptacion, Solo contiene IDs de relación
class IngresosEtiquetas:
    def __init__(self, id_ingreso: int = 0, id_etiqueta: int = 0):
        self.id_ingreso = id_ingreso
        self.id_etiqueta = id_etiqueta
    
    def GetId_ingreso(self) -> int:
        return self.id_ingreso
    def SetId_ingreso(self, value: int) -> None:
        self.id_ingreso = value

    def GetId_etiqueta(self) -> int:
        return self.id_etiqueta
    def SetId_etiqueta(self, value: int) -> None:
        self.id_etiqueta = value

    def __str__(self):
        return f"id_ingreso: {self.GetId_ingreso()}, id_etiqueta: {self.GetId_etiqueta()}"
    
    def serialize(self):
        return {
            "id_ingreso": self.id_ingreso,
            "id_etiqueta": self.id_etiqueta
        }