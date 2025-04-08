class Etiquetas:
    id_etiqueta: int = 0
    nombre: str = None

    def GetId_etiqueta(self) -> int:
        return self.id_etiqueta
    def SetId_etiqueta(self, value: int) -> None:
        self.id_etiqueta = value

    def GetNombre(self) -> str:
        return self.nombre
    def SetNombre(self, value: str) -> None:
        self.nombre = value