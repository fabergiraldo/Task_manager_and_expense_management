import pyodbc
from Entidades.Transacciones import Transacciones
from Utilidades.Configuracion import Configuracion
from Utilidades.Encriptar import EncriptarAES 

class TransaccionesRepositorio:
    def __init__(self):
        self.encriptarAES = EncriptarAES() 

    def listar(self):
        respuesta: dict = {}
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            consulta = "SELECT id_transaccion, id_usuario, tipo, id_categoria, id_moneda, id_cuenta, id_metodo_pago, fecha FROM transacciones"
            cursor = conexion.cursor()
            cursor.execute(consulta)

            contador = 0
            for elemento in cursor:
                lista: dict = {}                
                lista["id_transaccion"] = elemento[0]
                lista["id_usuario"] = elemento[1]
                lista["tipo"] = self.encriptarAES.decifrar(elemento[2])
                lista["id_categoria"] = elemento[3]
                lista["id_moneda"] = elemento[4]
                lista["id_cuenta"] = elemento[5]
                lista["id_metodo_pago"] = elemento[6]
                lista["fecha"] = elemento[7]
                respuesta[str(contador)] = lista
                contador += 1  

            cursor.close()
            conexion.close()
            return respuesta

        except Exception as ex:
            print("Error al listar transacciones:", str(ex))
            return respuesta

    def guardar(self, id_usuario, tipo, id_categoria, id_moneda, id_cuenta, id_metodo_pago, fecha):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            encriptador = EncriptarAES()
            cifrado = encriptador.cifrar(tipo)

            consulta = """
                INSERT INTO transacciones (id_usuario, tipo, id_categoria, id_moneda, id_cuenta, id_metodo_pago, fecha) 
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(consulta, (id_usuario, cifrado, id_categoria, id_moneda, id_cuenta, id_metodo_pago, fecha))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Transacción guardada correctamente")

        except Exception as ex:
            print("Error al guardar transacción:", str(ex))

    def actualizar(self, id_transaccion, id_usuario, tipo, id_categoria, id_moneda, id_cuenta, id_metodo_pago, fecha):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            cifrado = self.encriptarAES.cifrar(tipo)

            consulta = """
                UPDATE transacciones 
                SET id_usuario = ?, tipo = ?, id_categoria = ?, id_moneda = ?, id_cuenta = ?, id_metodo_pago = ?, fecha = ? 
                WHERE id_transaccion = ?
            """
            cursor.execute(consulta, (id_usuario, cifrado, id_categoria, id_moneda, id_cuenta, id_metodo_pago, fecha, id_transaccion))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Transacción actualizada correctamente")

        except Exception as ex:
            print("Error al actualizar transacción:", str(ex))

    def eliminar(self, id_transaccion):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = "DELETE FROM transacciones WHERE id_transaccion = ?"
            cursor.execute(consulta, (id_transaccion,))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Transacción eliminada correctamente")

        except Exception as ex:
            print("Error al eliminar transacción:", str(ex))
