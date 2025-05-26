# No aplica encriptacion Solo contiene nombres de etiquetas
class Etiquetas:
    def __init__(self, id_etiqueta: int = 0, nombre: str = None):
        self.id_etiqueta = id_etiqueta
        self.nombre = nombre

    def GetId_etiqueta(self) -> int:
        return self.id_etiqueta
    def SetId_etiqueta(self, value: int) -> None:
        self.id_etiqueta = value

    def GetNombre(self) -> str:
        return self.nombre
    def SetNombre(self, value: str) -> None:
        self.nombre = value

    def __str__(self):
        return f"ID: {self.GetId_etiqueta()}, nombre: {self.GetNombre()}"
    
    def serialize(self):
        return {
            "id_etiqueta": self.id_etiqueta,
            "nombre": self.nombre
        }