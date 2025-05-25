import pyodbc
from Entidades.Etiquetas import Etiquetas
from Utilidades.Configuracion import Configuracion
from Utilidades.Encriptar import EncriptarAES

class EtiquetasRepositorio:
    def __init__(self):
        self.encriptarAES = EncriptarAES() 
    def listar(self):
        respuesta: dict = {};
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            consulta = "SELECT id_etiqueta, nombre FROM etiquetas"
            cursor = conexion.cursor()
            cursor.execute(consulta)

            contador = 0;
            for elemento in cursor:
                lista: dict = {};                
                lista["id_etiqueta"]=elemento[0];
                lista["nombre"]=elemento[1];
                respuesta[str(contador)] = lista;
                contador = contador + 1;

            cursor.close()
            conexion.close()
            return respuesta;

        except Exception as ex:
            print("Error al listar etiquetas:", str(ex))
            return respuesta;

    def guardar(self, nombre):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = "INSERT INTO etiquetas (nombre) VALUES (?)"
            cursor.execute(consulta, (nombre,))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Etiqueta guardada correctamente")

        except Exception as ex:
            print("Error al guardar etiqueta:", str(ex))

    def actualizar(self, id_etiqueta, nombre):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = "UPDATE etiquetas SET nombre = ? WHERE id_etiqueta = ?"
            cursor.execute(consulta, (nombre, id_etiqueta))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Etiqueta actualizada correctamente")

        except Exception as ex:
            print("Error al actualizar etiqueta:", str(ex))

    def eliminar(self, id_etiqueta):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = "DELETE FROM etiquetas WHERE id_etiqueta = ?"
            cursor.execute(consulta, (id_etiqueta,))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Etiqueta eliminada correctamente")

        except Exception as ex:
            print("Error al eliminar etiqueta:", str(ex)) 