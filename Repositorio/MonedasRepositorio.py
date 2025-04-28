import pyodbc
from Entidades.Monedas import Monedas
from Utilidades.Configuracion import Configuracion

class MonedasRepositorio:
    def listar(self):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            consulta = "SELECT id_moneda, nombre, codigo, simbolo FROM monedas"
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista = []
            for elemento in cursor:
                moneda = Monedas(
                    id_moneda=elemento[0],
                    nombre=elemento[1],
                    codigo=elemento[2],
                    simbolo=elemento[3]
                )
                lista.append(moneda)

            cursor.close()
            conexion.close()
            return lista
        except Exception as ex:
            print("Error al listar monedas:", str(ex))
            return []

    def guardar(self, nombre, codigo, simbolo):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = "INSERT INTO monedas (nombre, codigo, simbolo) VALUES (?, ?, ?)"
            cursor.execute(consulta, (nombre, codigo, simbolo))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Moneda guardada correctamente")
        except Exception as ex:
            print("Error al guardar moneda:", str(ex))

    def actualizar(self, id_moneda, nombre, codigo, simbolo):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = "UPDATE monedas SET nombre = ?, codigo = ?, simbolo = ? WHERE id_moneda = ?"
            cursor.execute(consulta, (nombre, codigo, simbolo, id_moneda))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Moneda actualizada correctamente")
        except Exception as ex:
            print("Error al actualizar moneda:", str(ex))

    def eliminar(self, id_moneda):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = "DELETE FROM monedas WHERE id_moneda = ?"
            cursor.execute(consulta, (id_moneda,))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Moneda eliminada correctamente")
        except Exception as ex:
            print("Error al eliminar moneda:", str(ex))