from Utilidades.Encriptar import EncriptarAES
class Gastos:
    def __init__(self, id_gasto: int = 0, id_usuario: int = 0, fecha: str = None, monto: float = 0.0, descripcion: str = None, id_categoria: int = 0, id_moneda: int = 0, id_cuenta: int = 0, id_tarjeta: int = 0):
        self.id_gasto = id_gasto
        self.id_usuario = id_usuario
        self.fecha = fecha
        self.monto = monto
        self.descripcion = descripcion
        self.id_categoria = id_categoria
        self.id_moneda = id.moneda
        self.cuenta = id_cuenta
        self.id_tarjeta = id_tarjeta
    
    
    def GetId_gasto(self) -> int:
        return self.id_gasto
    def SetId_gasto(self, value: int) -> None:
        self.id_gasto = value

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
        return EncriptarAES.decifrar(self.descripcion) if self.descripcion else None
    def SetDescripcion(self, value: str) -> None:
        self.descripcion = EncriptarAES.cifrar(value) if value else None

    def GetId_categoria(self) -> int:
        return self.id_categoria
    def SetId_categoria(self, value: int) -> None:
        self.id_categoria = value

    def GetId_moneda(self) -> int:
        return self.id_moneda
    def SetId_moneda(self, value: int) -> None:
        self.id_moneda = value

    def GetId_cuenta(self) -> int:
        return self.id_cuenta
    def SetId_cuenta(self, value: int) -> None:
        self.id_cuenta = value

    def GetId_tarjeta(self) -> int:
        return self.id_tarjeta
    def SetId_tarjeta(self, value: int) -> None:
        self.id_tarjeta = value

    def __str__(self):
        return f"id_gasto: {self.GetId_gasto()}, id_usuario: {self.GetId_usuario()}, fecha: {self.GetFecha()}, monto: {self.GetMonto()}, descripcion: {self.GetDescripcion()}, id_categoria: {self.GetId_categoria()}, id.moneda: {self.GetId_moneda()}, id_cuenta: {self.GetId_cuenta()}, id_tarjeta: {self.GetId_tarjeta()}"