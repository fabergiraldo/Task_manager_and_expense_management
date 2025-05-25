import pyodbc
from Entidades.Monedas import Monedas
from Utilidades.Configuracion import Configuracion
from Utilidades.Encriptar import EncriptarAES

class MonedasRepositorio:
    def __init__(self):
        self.encriptarAES = EncriptarAES() 
    def listar(self):
        respuesta: dict = {};
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            consulta = "SELECT id_moneda, nombre, codigo, simbolo FROM monedas"
            cursor = conexion.cursor()
            cursor.execute(consulta)

            contador = 0;
            for elemento in cursor:
                lista: dict = {};                
                lista["id_moneda"]=elemento[0];
                lista["nombre"]=elemento[1];
                lista["codigo"]=elemento[2];
                lista["simbolo"]=elemento[3];
                respuesta[str(contador)] = lista;
                contador = contador + 1;

            cursor.close()
            conexion.close()
            return respuesta;
        except Exception as ex:
            print("Error al listar monedas:", str(ex))
            return respuesta;

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