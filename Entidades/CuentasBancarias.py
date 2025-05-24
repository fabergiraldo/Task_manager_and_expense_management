class CuentasBancarias:
	def __init__(self, id_cuenta: int = 0, id_usuario: int = 0, nombre_banco: str = None, numero_cuenta: str = None, saldo: float = 0.0, id_moneda: int = 0):
		self.id_cuenta = id_cuenta
		self.id_usuario = id_usuario
		self.nombre_banco = nombre_banco
		self.numero_cuenta = numero_cuenta
		self.saldo = saldo
		self.id_moneda = id_moneda
	
	def GetIdCuenta(self) -> int:
		return self.id_cuenta
	def SetIdCuenta(self, value: int) -> None:
		self.id_cuenta = value
 
	
	def GetIdUsuario(self) -> int:
		return self.id_usuario
	def SetIdUsuario(self, value: int) -> None:
		self.id_usuario = value
 
	
	def GetNombreBanco(self) -> str:
		return self.nombre_banco
	def SetNombreBanco(self, value: str) -> None:
		self.nombre_banco = value
 
	
	def GetNumeroCuenta(self) -> str:
		return self.numero_cuenta
	def SetNumeroCuenta(self, value: str) -> None:
		self.numero_cuenta = value
 
	
	def GetSaldo(self) -> float:
		return self.saldo
	def SetSaldo(self, value: float) -> None:
		self.saldo = value
 
	
	def GetIdMoneda(self) -> int:
		return self.id_moneda
	def SetIdMoneda(self, value: int) -> None:
		self.id_moneda = value

	def __str__(self):
		return f"id_cuenta: {self.GetIdCuenta()}, id_usuario: {self.GetIdUsuario()}, nombre_banco: {self.GetNombreBanco()}, numero_cuenta: {self.GetNumeroCuenta()}, saldo: {self.GetSaldo()}, id_moneda: {self.GetIdMoneda()}"
	
	def serialize(self):
		return {
            "id_cuenta": self.id_cuenta,
            "id_usuario": self.id_usuario,
            "nombre_banco": self.nombre_banco,
            "numero_cuenta": self.numero_cuenta,
            "saldo": float(self.saldo) if self.saldo is not None else None,
            "id_moneda": self.id_moneda
        }