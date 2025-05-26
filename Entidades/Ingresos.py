from datetime import date, datetime
from Utilidades.Encriptar import EncriptarAES
class Ingresos:
    def __init__(self, id_ingreso=None, id_usuario=None, fecha=None, monto=None, descripcion=None,
                 id_moneda=None, id_cuenta=None, id_metodo_pago=None):
        self.id_ingreso = id_ingreso
        self.id_usuario = id_usuario
        self.fecha = fecha
        self.monto = monto
        self.descripcion = descripcion
        self.id_moneda = id_moneda
        self.id_cuenta = id_cuenta
        self.id_metodo_pago = id_metodo_pago
    

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
        return EncriptarAES.decifrar(self.descripcion) if self.descripcion else None
    def SetDescripcion(self, value: str) -> None:
        self.descripcion = EncriptarAES.cifrar(value) if value else None


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
    
    def serialize(self):
        return {
            "id_ingreso": self.id_ingreso,
            "id_usuario": self.id_usuario,
            "fecha": self.fecha.isoformat() if isinstance(self.fecha, (date, datetime)) else str(self.fecha),
            "monto": float(self.monto) if self.monto is not None else None,
            "descripcion": self.descripcion,
            "id_moneda": self.id_moneda,
            "id_cuenta": self.id_cuenta,
            "id_metodo_pago": self.id_metodo_pago
        }