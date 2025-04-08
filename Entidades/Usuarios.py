class Usuarios:
	id_usuario: int = 0
	def GetIdUsuario(self) -> int:
		return self.id_usuario
	def SetIdUsuario(self, value: int) -> None:
		self.id_usuario = value
 
	nombre: str = None
	def GetNombre(self) -> str:
		return self.nombre
	def SetNombre(self, value: str) -> None:
		self.nombre = value
 
	correo: str = None
	def GetCorreo(self) -> str:
		return self.correo
	def SetCorreo(self, value: str) -> None:
		self.correo = value
 
	contrasena: str = None
	def GetContrasena(self) -> str:
		return self.contrasena
	def SetContrasena(self, value: str) -> None:
		self.contrasena = value
 
	fecha_registro: str = None
	def GetFechaRegistro(self) -> str:
		return self.fecha_registro
	def SetFechaRegistro(self, value: str) -> None:
		self.fecha_registro = value