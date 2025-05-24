import pyodbc
from Utilidades.Configuracion import strConnection
from Entidades.Ingresos import Ingresos

class IngresosRepositorio:

    @staticmethod
    def listar():
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "SELECT id_ingreso, id_usuario, fecha, monto, descripcion, id_moneda, id_cuenta, id_metodo_pago FROM ingresos"
            )
            return [Ingresos(*fila) for fila in cursor.fetchall()]

    @staticmethod
    def crear(ingreso: Ingresos):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO ingresos (id_usuario, fecha, monto, descripcion, id_moneda, id_cuenta, id_metodo_pago) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (ingreso.id_usuario, ingreso.fecha, ingreso.monto, ingreso.descripcion,
                 ingreso.id_moneda, ingreso.id_cuenta, ingreso.id_metodo_pago)
            )
            conexion.commit()

    @staticmethod
    def actualizar(ingreso: Ingresos):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "UPDATE ingresos SET id_usuario=?, fecha=?, monto=?, descripcion=?, id_moneda=?, id_cuenta=?, id_metodo_pago=? WHERE id_ingreso=?",
                (ingreso.id_usuario, ingreso.fecha, ingreso.monto, ingreso.descripcion,
                 ingreso.id_moneda, ingreso.id_cuenta, ingreso.id_metodo_pago, ingreso.id_ingreso)
            )
            conexion.commit()

    @staticmethod
    def eliminar(id_ingreso):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM ingresos WHERE id_ingreso=?", (id_ingreso,))
            conexion.commit()