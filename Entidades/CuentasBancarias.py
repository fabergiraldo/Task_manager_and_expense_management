class CuentasBancarias:
	id_cuenta: int = 0
	def GetIdCuenta(self) -> int:
		return self.id_cuenta
	def SetIdCuenta(self, value: int) -> None:
		self.id_cuenta = value
 
	id_usuario: int = 0
	def GetIdUsuario(self) -> int:
		return self.id_usuario
	def SetIdUsuario(self, value: int) -> None:
		self.id_usuario = value
 
	nombre_banco: str = None
	def GetNombreBanco(self) -> str:
		return self.nombre_banco
	def SetNombreBanco(self, value: str) -> None:
		self.nombre_banco = value
 
	numero_cuenta: str = None
	def GetNumeroCuenta(self) -> str:
		return self.numero_cuenta
	def SetNumeroCuenta(self, value: str) -> None:
		self.numero_cuenta = value
 
	saldo: float = 0.0
	def GetSaldo(self) -> float:
		return self.saldo
	def SetSaldo(self, value: float) -> None:
		self.saldo = value
 
	id_moneda: int = 0
	def GetIdMoneda(self) -> int:
		return self.id_moneda
	def SetIdMoneda(self, value: int) -> None:
		self.id_moneda = value