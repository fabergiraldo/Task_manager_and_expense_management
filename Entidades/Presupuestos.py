from Utilidades.Encriptar import EncriptarAES
class Presupuestos:
    def __init__(self, id_presupuesto: int = 0, id_usuario: int = 0, id_categoria: int = 0, mes: str = None, monto: float = 0.0):
        self.id_presupuesto = id_presupuesto
        self.id_usuario = id_usuario
        self.id_categoria = id_categoria
        self.mes = mes
        self.monto = monto

    id_presupuesto: int = 0
    def GetIdPresupuesto(self) -> int:
        return self.id_presupuesto
    def SetIdPresupuesto(self, value: int) -> None:
        self.id_presupuesto = value

    id_usuario: int = 0
    def GetIdUsuario(self) -> int:
        return self.id_usuario
    def SetIdUsuario(self, value: int) -> None:
        self.id_usuario = value

    id_categoria: int = 0
    def GetIdCategoria(self) -> int:
        return self.id_categoria
    def SetIdCategoria(self, value: int) -> None:
        self.id_categoria = value

    mes: str = None
    def GetMes(self) -> str:
        return EncriptarAES.decifrar(self.mes) if self.mes else None
    def SetMes(self, value: str) -> None:
        self.mes = EncriptarAES.cifrar(value) if value else None

    monto: float = 0.0
    def GetMonto(self) -> float:
        return self.monto
    def SetMonto(self, value: float) -> None:
        self.monto = value

    def __str__(self):
        return f"ID: {self.GetIdPresupuesto()}, usuario: {self.GetIdUsuario()}, categoría: {self.GetIdCategoria()}, mes: {self.GetMes()}, monto: {self.GetMonto()}"
