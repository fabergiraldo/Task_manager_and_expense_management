class Transacciones:
    id_transaccion: int = 0
    tipo: str = None
    id_gasto: int = 0
    id_ingreso: int = 0
    fecha: str = None

    def GetId_transaccion(self) -> int:
        return self.id_transaccion
    def SetId_transaccion(self, value: int) -> None:
        self.id_transaccion = value

    def GetTipo(self) -> str:
        return self.tipo
    def SetTipo(self, value: str) -> None:
        self.tipo = value

    def GetId_gasto(self) -> int:
        return self.id_gasto
    def SetId_gasto(self, value: int) -> None:
        self.id_gasto = value

    def GetId_ingreso(self) -> int:
        return self.id_ingreso
    def SetId_ingreso(self, value: int) -> None:
        self.id_ingreso = value

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