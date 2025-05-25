import pyodbc
from Entidades.MetodosPago import MetodosPago
from Utilidades.Configuracion import Configuracion

class MetodosPagoRepositorio:
    def listar(self):
        respuesta: dict = {}
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            consulta = "SELECT id_metodo_pago, metodo FROM metodos_pago"
            cursor = conexion.cursor()
            cursor.execute(consulta)

            contador = 0
            for elemento in cursor:
                lista: dict = {}                
                lista["id_metodo_pago"] = elemento[0]
                lista["metodo"] = elemento[1]
                respuesta[str(contador)] = lista
                contador += 1

            cursor.close()
            conexion.close()
            return respuesta

        except Exception as ex:
            print("Error al listar métodos de pago:", str(ex))
            return respuesta

    def guardar(self, metodo):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = "INSERT INTO metodos_pago (metodo) VALUES (?)"
            cursor.execute(consulta, (metodo,))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Método de pago guardado correctamente")

        except Exception as ex:
            print("Error al guardar método de pago:", str(ex))

    def actualizar(self, id_metodo_pago, metodo):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = "UPDATE metodos_pago SET metodo = ? WHERE id_metodo_pago = ?"
            cursor.execute(consulta, (metodo, id_metodo_pago))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Método de pago actualizado correctamente")

        except Exception as ex:
            print("Error al actualizar método de pago:", str(ex))

    def eliminar(self, id_metodo_pago):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = "DELETE FROM metodos_pago WHERE id_metodo_pago = ?"
            cursor.execute(consulta, (id_metodo_pago,))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Método de pago eliminado correctamente")

        except Exception as ex:
            print("Error al eliminar método de pago:", str(ex))
