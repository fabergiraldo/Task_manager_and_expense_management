from datetime import date, datetime
from Utilidades.Encriptar import EncriptarAES
class Transacciones:
    def __init__(self, id_transaccion=None, id_usuario=None, tipo=None, id_categoria=None,
                 id_moneda=None, id_cuenta=None, id_metodo_pago=None, fecha=None):
        self.id_transaccion = id_transaccion
        self.id_usuario = id_usuario
        self.tipo = tipo
        self.id_categoria = id_categoria
        self.id_moneda = id_moneda
        self.id_cuenta = id_cuenta
        self.id_metodo_pago = id_metodo_pago
        self.fecha = fecha

    id_transaccion: int = 0
    def GetIdTransaccion(self) -> int:
        return self.id_transaccion
    def SetIdTransaccion(self, value: int) -> None:
        self.id_transaccion = value

    id_usuario: int = 0
    def GetIdUsuario(self) -> int:
        return self.id_usuario
    def SetIdUsuario(self, value: int) -> None:
        self.id_usuario = value

    tipo: str = None
    def GetTipo(self) -> str:
        return EncriptarAES.decifrar(self.tipo) if self.tipo else None
    def SetTipo(self, value: str) -> None:
        self.tipo = EncriptarAES.cifrar(value) if value else None

    id_categoria: int = 0
    def GetIdCategoria(self) -> int:
        return self.id_categoria
    def SetIdCategoria(self, value: int) -> None:
        self.id_categoria = value

    id_moneda: int = 0
    def GetIdMoneda(self) -> int:
        return self.id_moneda
    def SetIdMoneda(self, value: int) -> None:
        self.id_moneda = value

    id_cuenta: int = 0
    def GetIdCuenta(self) -> int:
        return self.id_cuenta
    def SetIdCuenta(self, value: int) -> None:
        self.id_cuenta = value

    id_metodo_pago: int = 0
    def GetIdMetodoPago(self) -> int:
        return self.id_metodo_pago
    def SetIdMetodoPago(self, value: int) -> None:
        self.id_metodo_pago = value

    fecha: str = None
    def GetFecha(self) -> str:
        return self.fecha
    def SetFecha(self, value: str) -> None:
        self.fecha = value


    def serialize(self):
        return {
            "id_transaccion": self.id_transaccion,
            "id_usuario": self.id_usuario,
            "tipo": self.tipo,
            "id_categoria": self.id_categoria,
            "id_moneda": self.id_moneda,
            "id_cuenta": self.id_cuenta,
            "id_metodo_pago": self.id_metodo_pago,
            "fecha": self.fecha.isoformat() if isinstance(self.fecha, datetime) else str(self.fecha)
        }