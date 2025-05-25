import pyodbc
from Entidades.CuentasBancarias import CuentasBancarias
from Utilidades.Configuracion import Configuracion
from Utilidades.Encriptar import EncriptarAES

class CuentasBancariasRepositorio:
    def __init__(self):
        self.encriptarAES = EncriptarAES() 
    def listar(self):
        respuesta: dict = {};
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            consulta = "SELECT id_cuenta, id_usuario, nombre_banco, numero_cuenta, saldo, id_moneda FROM cuentas_bancarias"
            cursor = conexion.cursor()
            cursor.execute(consulta)

            contador = 0;
            for elemento in cursor:
                lista: dict = {};                
                lista["id_cuenta"]=elemento[0];
                lista["id_usuario"]=elemento[1];
                lista["nombre_banco"]=elemento[2];
                lista["numero_cuenta"]=self.encriptarAES.decifrar(elemento[3]);
                lista["saldo"]=elemento[4];
                lista["id_moneda"]=elemento[5];
                respuesta[str(contador)] = lista;
                contador = contador + 1;

            cursor.close()
            conexion.close()

            return respuesta;

        except Exception as ex:
            print("Error al listar cuentas bancarias:", str(ex))
            return respuesta;

    def guardar(self, id_usuario, nombre_banco, numero_cuenta, saldo, id_moneda):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            encriptador = EncriptarAES()
            cifrado = encriptador.cifrar(numero_cuenta)

            consulta = "INSERT INTO cuentas_bancarias (id_usuario, nombre_banco, numero_cuenta, saldo, id_moneda) VALUES (?, ?, ?, ?, ?)"
            cursor.execute(consulta, (id_usuario, nombre_banco, cifrado, saldo, id_moneda))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Cuenta bancaria guardada correctamente")

        except Exception as ex:
            print("Error al guardar cuenta bancaria:", str(ex))

    def actualizar(self, id_usuario, nombre_banco, numero_cuenta, saldo, id_moneda):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = "UPDATE cuentas_bancarias SET id_usuario = ?, nombre_banco = ?, numero_cuenta = ?, saldo = ?, id_moneda = ? WHERE id_cuenta = ?"
            cursor.execute(consulta, ( nombre_banco, numero_cuenta, saldo, id_moneda))
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