class Monedas:
	id_moneda: int = 0
	def GetIdMoneda(self) -> int:
		return self.id_moneda
	def SetIdMoneda(self, value: int) -> None:
		self.id_moneda = value
 
	nombre: str = None
	def GetNombre(self) -> str:
		return self.nombre
	def SetNombre(self, value: str) -> None:
		self.nombre = value
 
	codigo: str = None
	def GetCodigo(self) -> str:
		return self.codigo
	def SetCodigo(self, value: str) -> None:
		self.codigo = value
 
	simbolo: str = None
	def GetSimbolo(self) -> str:
		return self.simbolo
	def SetSimbolo(self, value: str) -> None:
		self.simbolo = value

	def serialize(self):
		return {
            "id_moneda": self.id_moneda,
            "nombre": self.nombre,
            "codigo": self.codigo,
            "simbolo": self.simbolo
        }