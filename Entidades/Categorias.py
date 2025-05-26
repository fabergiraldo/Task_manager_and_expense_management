from Utilidades.Encriptar import EncriptarAES
class Categorias:
	def __init__(self, id_categoria: int = 0, nombre: str = None, descripcion: str = None):
		self.id_categoria = id_categoria
		self.nombre = nombre
		self.descripcion = descripcion
		
	def GetIdCategoria(self) -> int:
		return self.id_categoria
	def SetIdCategoria(self, value: int) -> None:
		self.id_categoria = value
 
	
	def GetNombre(self) -> str:
		return self.nombre
	def SetNombre(self, value: str) -> None:
		self.nombre = value
 
	
	def GetDescripcion(self) -> str:
		return self.descripcion
	def SetDescripcion(self, value: str) -> None:
		self.descripcion = value

	def __str__(self):
		return f"ID: {self.GetIdCategoria()}, nombre: {self.GetNombre()}, descripcion: {self.GetDescripcion()}"
	
	def serialize(self):
		return {
            "id_categoria": self.id_categoria,
            "nombre": self.nombre,
            "descripcion": self.descripcion}