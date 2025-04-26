class Ingresos:
    def __init__(self, id_ingreso: int = 0, id_usuario: int = 0, fecha: str = None, monto: float = 0.0, descripcion: str = None, id_moneda: int = 0, id_cuenta: int = 0):
        self.id_ingreso = id_ingreso
        self.id_usuario = id_usuario
        self.fecha = fecha
        self.monto = monto
        self.descripcion = descripcion
        self.id_moneda = id_moneda
        self.id_cuenta = id_cuenta
    

    def GetId_ingreso(self) -> int:
        return self.id_ingreso
    def SetId_ingreso(self, value: int) -> None:
        self.id_ingreso = value

    def GetId_usuario(self) -> int:
        return self.id_usuario
    def SetId_usuario(self, value: int) -> None:
        self.id_usuario = value

    def GetFecha(self) -> str:
        return self.fecha
    def SetFecha(self, value: str) -> None:
        self.fecha = value

    def GetMonto(self) -> float:
        return self.monto
    def SetMonto(self, value: float) -> None:
        self.monto = value

    def GetDescripcion(self) -> str:
        return self.descripcion
    def SetDescripcion(self, value: str) -> None:
        self.descripcion = value

    def GetId_moneda(self) -> int:
        return self.id_moneda
    def SetId_moneda(self, value: int) -> None:
        self.id_moneda = value

    def GetId_cuenta(self) -> int:
        return self.id_cuenta
    def SetId_cuenta(self, value: int) -> None:
        self.id_cuenta = value

	def __str__(self):
		return f"id_ingreso: {self.GetId_ingreso()}, id_usuario: {self.GetId_usuario()}, fecha: {self.GetRuta_archivo()}, monto: {self.GetMonto()}, descripcion: {self.GetDescripcion()}, id_moneda: {self.GetId_moneda()}, id_cuenta:{self.GetId_cuenta()}"