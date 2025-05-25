from Utilidades.Encriptar import EncriptarAES

class Categorias:
	def __init__(self, id_categoria: int = 0, nombre: str = None, descripcion: str = None):
		self.id_categoria = id_categoria
		self.nombre = nombre
		self.descripcion = descripcion
		
	id_categoria: int = 0
	def GetIdCategoria(self) -> int:
		return self.id_categoria
	def SetIdCategoria(self, value: int) -> None:
		self.id_categoria = value
 
	nombre: str = None
	def GetNombre(self) -> str:
		return self.nombre
	def SetNombre(self, value: str) -> None:
		self.nombre = value
 
	descripcion: str = None
	def GetDescripcion(self) -> str:
		return EncriptarAES.decifrar(self.descripcion) if self.descripcion else None
	def SetDescripcion(self, value: str) -> None:
		self.descripcion = EncriptarAES.cifrar(value) if value else None

	def __str__(self):
		return f"ID: {self.GetIdCategoria()}, nombre: {self.GetNombre()}, descripcion: {self.GetDescripcion()}"