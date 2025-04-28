import pyodbc
from Entidades.Transacciones import Transacciones
from Utilidades.Configuracion import Configuracion

class TransaccionesRepositorio:
    def listar(self):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            cursor.execute(
                "SELECT id_transaccion, tipo, id_gasto, id_ingreso, fecha FROM transacciones"
            )
            lista = [
                Transacciones(
                    id_transaccion=row[0],
                    tipo=row[1],
                    id_gasto=row[2],
                    id_ingreso=row[3],
                    fecha=row[4]
                ) for row in cursor
            ]
            cursor.close()
            conexion.close()
            return lista
        except Exception as ex:
            print("Error al listar transacciones:", ex)
            return []

    def guardar(self, tipo, id_gasto=None, id_ingreso=None):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO transacciones (tipo, id_gasto, id_ingreso) VALUES (?, ?, ?)",
                (tipo, id_gasto, id_ingreso)
            )
            conexion.commit()
            cursor.close()
            conexion.close()
            print("Transacción guardada correctamente")
        except Exception as ex:
            print("Error al guardar transacción:", ex)

    def actualizar(self, id_transaccion, tipo, id_gasto=None, id_ingreso=None):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            cursor.execute(
                "UPDATE transacciones SET tipo = ?, id_gasto = ?, id_ingreso = ? WHERE id_transaccion = ?",
                (tipo, id_gasto, id_ingreso, id_transaccion)
            )
            conexion.commit()
            cursor.close()
            conexion.close()
            print("Transacción actualizada correctamente")
        except Exception as ex:
            print("Error al actualizar transacción:", ex)

    def eliminar(self, id_transaccion):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM transacciones WHERE id_transaccion = ?", (id_transaccion,))
            conexion.commit()
            cursor.close()
            conexion.close()
            print("Transacción eliminada correctamente")
        except Exception as ex:
            print("Error al eliminar transacción:", ex)
