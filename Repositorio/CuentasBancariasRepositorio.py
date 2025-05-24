import pyodbc
from Utilidades.Configuracion import strConnection
from Entidades.CuentasBancarias import CuentasBancarias

class CuentasBancariasRepositorio:

    @staticmethod
    def listar():
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "SELECT id_cuenta, id_usuario, nombre_banco, numero_cuenta, saldo, id_moneda FROM cuentas_bancarias"
            )
            return [CuentasBancarias(*fila) for fila in cursor.fetchall()]

    @staticmethod
    def crear(cuenta: CuentasBancarias):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO cuentas_bancarias (id_usuario, nombre_banco, numero_cuenta, saldo, id_moneda) VALUES (?, ?, ?, ?, ?)",
                (cuenta.id_usuario, cuenta.nombre_banco, cuenta.numero_cuenta, cuenta.saldo, cuenta.id_moneda)
            )
            conexion.commit()

    @staticmethod
    def actualizar(cuenta: CuentasBancarias):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "UPDATE cuentas_bancarias SET id_usuario=?, nombre_banco=?, numero_cuenta=?, saldo=?, id_moneda=? WHERE id_cuenta=?",
                (cuenta.id_usuario, cuenta.nombre_banco, cuenta.numero_cuenta, cuenta.saldo, cuenta.id_moneda, cuenta.id_cuenta)
            )
            conexion.commit()

    @staticmethod
    def eliminar(id_cuenta):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM cuentas_bancarias WHERE id_cuenta=?", (id_cuenta,))
            conexion.commit()
