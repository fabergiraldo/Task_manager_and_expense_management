import pyodbc
from Entidades.CuentasBancarias import CuentasBancarias
from Utilidades.Configuracion import Configuracion

class CuentasBancariasRepositorio:

    def listar(self):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            consulta = """
                SELECT id_cuenta, id_usuario, numero_cuenta, tipo_cuenta, 
                       banco, saldo, estado
                FROM cuentas_bancarias
            """
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista = []
            for elemento in cursor:
                cuenta = CuentasBancarias(
                    id_cuenta=elemento[0],
                    id_usuario=elemento[1],
                    numero_cuenta=elemento[2],
                    tipo_cuenta=elemento[3],
                    banco=elemento[4],
                    saldo=elemento[5],
                    estado=elemento[6]
                )
                lista.append(cuenta)

            cursor.close()
            conexion.close()

            return lista

        except Exception as ex:
            print("Error al listar cuentas bancarias:", str(ex))
            return []

    def guardar(self, id_usuario, numero_cuenta, tipo_cuenta, banco, saldo, estado):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = """
                INSERT INTO cuentas_bancarias (id_usuario, numero_cuenta, tipo_cuenta, 
                                             banco, saldo, estado)
                VALUES (?, ?, ?, ?, ?, ?)
            """
            cursor.execute(consulta, (id_usuario, numero_cuenta, tipo_cuenta, 
                                    banco, saldo, estado))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Cuenta bancaria guardada correctamente")

        except Exception as ex:
            print("Error al guardar cuenta bancaria:", str(ex))

    def actualizar(self, id_cuenta, id_usuario, numero_cuenta, tipo_cuenta, 
                  banco, saldo, estado):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = """
                UPDATE cuentas_bancarias 
                SET id_usuario = ?, numero_cuenta = ?, tipo_cuenta = ?, 
                    banco = ?, saldo = ?, estado = ?
                WHERE id_cuenta = ?
            """
            cursor.execute(consulta, (id_usuario, numero_cuenta, tipo_cuenta, 
                                    banco, saldo, estado, id_cuenta))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Cuenta bancaria actualizada correctamente")

        except Exception as ex:
            print("Error al actualizar cuenta bancaria:", str(ex))

    def eliminar(self, id_cuenta):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = "DELETE FROM cuentas_bancarias WHERE id_cuenta = ?"
            cursor.execute(consulta, (id_cuenta,))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Cuenta bancaria eliminada correctamente")

        except Exception as ex:
            print("Error al eliminar cuenta bancaria:", str(ex)) 