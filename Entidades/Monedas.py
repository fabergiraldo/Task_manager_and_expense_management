# Solo contiene información pública sobre monedas no aplica para encriptacion
class Monedas:
	def __init__(self, id_moneda: int = 0, nombre: str = None, codigo: str = None, simbolo: str = None):
		self.id_moneda = id_moneda
		self.nombre = nombre
		self.codigo = codigo
		self.simbolo = simbolo

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

	def __str__(self):
		return f"id_moneda: {self.GetIdMoneda()}, nombre: {self.GetNombre()}, codigo: {self.GetCodigo()}, simbolo: {self.GetSimbolo()}"