class Gastos:
    def __init__(self, id_gasto=None, id_usuario=None, fecha=None, monto=None, descripcion=None,
                 id_categoria=None, id_moneda=None, id_cuenta=None, id_tarjeta=None,
                 id_proveedor=None, id_metodo_pago=None):
        self.id_gasto = id_gasto
        self.id_usuario = id_usuario
        self.fecha = fecha
        self.monto = monto
        self.descripcion = descripcion
        self.id_categoria = id_categoria
        self.id_moneda = id_moneda
        self.id_cuenta = id_cuenta
        self.id_tarjeta = id_tarjeta
        self.id_proveedor = id_proveedor
        self.id_metodo_pago = id_metodo_pago
    
    
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
        return self.descripcion
    def SetDescripcion(self, value: str) -> None:
        self.descripcion = value

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

    def GetId_proveedor(self) -> int:
        return self.id_proveedor
    def SetId_proveedor(self, value: int) -> None:
        self.id_proveedor = value

    def GetId_metodo_pago(self) -> int:
        return self.id_metodo_pago
    def SetId_metodo_pago(self, value: int) -> None:
        self.id_metodo_pago = value

    def __str__(self):
        return f"id_gasto: {self.GetId_gasto()}, id_usuario: {self.GetId_usuario()}, fecha: {self.GetFecha()}, monto: {self.GetMonto()}, descripcion: {self.GetDescripcion()}, id_categoria: {self.GetId_categoria()}, id.moneda: {self.GetId_moneda()}, id_cuenta: {self.GetId_cuenta()}, id_tarjeta: {self.GetId_tarjeta()}"
    
    def serialize(self):
        return {
            "id_gasto": self.id_gasto,
            "id_usuario": self.id_usuario,
            "fecha": self.fecha.isoformat() if isinstance(self.fecha, (date, datetime)) else str(self.fecha),
            "monto": float(self.monto) if self.monto is not None else None,
            "descripcion": self.descripcion,
            "id_categoria": self.id_categoria,
            "id_moneda": self.id_moneda,
            "id_cuenta": self.id_cuenta,
            "id_tarjeta": self.id_tarjeta,
            "id_proveedor": self.id_proveedor,
            "id_metodo_pago": self.id_metodo_pago
        }