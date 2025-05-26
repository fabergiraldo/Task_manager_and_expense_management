import pyodbc
from Utilidades.Configuracion import strConnection
from Entidades.CuentasBancarias import CuentasBancarias
from Utilidades.Encriptar import EncriptarAES

class CuentasBancariasRepositorio:

    @staticmethod
    def listar():
        try:
            conexion = pyodbc.connect(strConnection)
            consulta = "SELECT id_cuenta, id_usuario, nombre_banco, numero_cuenta, saldo, id_moneda FROM cuentas_bancarias"
            cursor = conexion.cursor()
            cursor.execute(consulta)

            encriptador = EncriptarAES()

            cuentas = []
            for fila in cursor.fetchall():
                cuenta = CuentasBancarias(
                    id_cuenta=fila[0],
                    id_usuario=fila[1],
                    nombre_banco=fila[2],
                    numero_cuenta=encriptador.decifrar(fila[3]),
                    saldo=fila[4],
                    id_moneda=fila[5]
                )
                cuentas.append(cuenta)

            cursor.close()
            conexion.close()
            return cuentas

        except Exception as ex:
            print("Error al listar cuentas bancarias:", str(ex))
            return []
        # with pyodbc.connect(strConnection) as conexion:
        #     cursor = conexion.cursor()
        #     cursor.execute(
        #         "SELECT id_cuenta, id_usuario, nombre_banco, numero_cuenta, saldo, id_moneda FROM cuentas_bancarias"
        #     )
        #     return [CuentasBancarias(*fila) for fila in cursor.fetchall()]

    @staticmethod
    def crear(cuenta: CuentasBancarias):
        try:
            conexion = pyodbc.connect(strConnection)
            cursor = conexion.cursor()

            encriptador = EncriptarAES()
            cifrado = encriptador.cifrar(cuenta.numero_cuenta)

            consulta = "INSERT INTO cuentas_bancarias (id_usuario, nombre_banco, numero_cuenta, saldo, id_moneda) VALUES (?, ?, ?, ?, ?)"
            cursor.execute(consulta, (cuenta.id_usuario, cuenta.nombre_banco, cifrado, cuenta.saldo, cuenta.id_moneda))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("✅ Cuenta bancaria guardada correctamente con número cifrado.")

        except Exception as ex:
            print("❌ Error al guardar cuenta bancaria:", str(ex))
        # with pyodbc.connect(strConnection) as conexion:
        #     cursor = conexion.cursor()
        #     cursor.execute(
        #         "INSERT INTO cuentas_bancarias (id_usuario, nombre_banco, numero_cuenta, saldo, id_moneda) VALUES (?, ?, ?, ?, ?)",
        #         (cuenta.id_usuario, cuenta.nombre_banco, cuenta.numero_cuenta, cuenta.saldo, cuenta.id_moneda)
        #     )
        #     conexion.commit()

    @staticmethod
    def actualizar(cuenta: CuentasBancarias):
        try:
            conexion = pyodbc.connect(strConnection)
            cursor = conexion.cursor()

            encriptador = EncriptarAES()
            cifrado = encriptador.cifrar(cuenta.numero_cuenta)

            consulta = """
                UPDATE cuentas_bancarias SET id_usuario=?, nombre_banco=?, numero_cuenta=?, saldo=?, id_moneda=? WHERE id_cuenta=?
            """
            cursor.execute(consulta, (cuenta.id_usuario, cuenta.nombre_banco, cifrado, cuenta.saldo, cuenta.id_moneda, cuenta.id_cuenta))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("✅ Cuenta bancaria actualizada correctamente.")

        except Exception as ex:
            print("❌ Error al actualizar cuenta bancaria:", str(ex))
        # with pyodbc.connect(strConnection) as conexion:
        #     cursor = conexion.cursor()
        #     cursor.execute(
        #         "UPDATE cuentas_bancarias SET id_usuario=?, nombre_banco=?, numero_cuenta=?, saldo=?, id_moneda=? WHERE id_cuenta=?",
        #         (cuenta.id_usuario, cuenta.nombre_banco, cuenta.numero_cuenta, cuenta.saldo, cuenta.id_moneda, cuenta.id_cuenta)
        #     )
        #     conexion.commit()

    @staticmethod
    def eliminar(id_cuenta):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM cuentas_bancarias WHERE id_cuenta=?", (id_cuenta,))
            conexion.commit()
