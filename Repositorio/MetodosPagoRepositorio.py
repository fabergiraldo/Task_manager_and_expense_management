import pyodbc
from Entidades.MetodosPago import MetodosPago
from Utilidades.Configuracion import Configuracion

class MetodosPagoRepositorio:
    def listar(self):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            cursor.execute("SELECT id_metodo_pago, metodo FROM metodos_pago")
            lista = [MetodosPago(id_metodo_pago=row[0], metodo=row[1]) for row in cursor]
            cursor.close()
            conexion.close()
            return lista
        except Exception as ex:
            print("Error al listar métodos de pago:", ex)
            return []

    def guardar(self, metodo):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO metodos_pago (metodo) VALUES (?)", (metodo,))
            conexion.commit()
            cursor.close()
            conexion.close()
            print("Método de pago guardado correctamente")
        except Exception as ex:
            print("Error al guardar método de pago:", ex)

    def actualizar(self, id_metodo_pago, metodo):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            cursor.execute("UPDATE metodos_pago SET metodo = ? WHERE id_metodo_pago = ?", (metodo, id_metodo_pago))
            conexion.commit()
            cursor.close()
            conexion.close()
            print("Método de pago actualizado correctamente")
        except Exception as ex:
            print("Error al actualizar método de pago:", ex)

    def eliminar(self, id_metodo_pago):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM metodos_pago WHERE id_metodo_pago = ?", (id_metodo_pago,))
            conexion.commit()
            cursor.close()
            conexion.close()
            print("Método de pago eliminado correctamente")
        except Exception as ex:
            print("Error al eliminar método de pago:", ex)