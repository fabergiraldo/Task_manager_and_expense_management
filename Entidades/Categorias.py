class Categorias:
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
		return self.descripcion
	def SetDescripcion(self, value: str) -> None:
		self.descripcion = value