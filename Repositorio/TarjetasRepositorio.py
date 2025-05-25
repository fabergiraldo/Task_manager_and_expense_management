import pyodbc
from Entidades.Tarjetas import Tarjetas
from Utilidades.Configuracion import Configuracion
from Utilidades.Encriptar import EncriptarAES

class TarjetasRepositorio:
    def __init__(self):
        self.encriptarAES = EncriptarAES()
    def listar(self):
        respuesta: dict = {};    
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            consulta = "SELECT id_tarjeta, id_usuario, nombre_tarjeta, tipo, numero_tarjeta, vencimiento FROM tarjetas"
            cursor = conexion.cursor()
            cursor.execute(consulta)

            contador = 0;
            for elemento in cursor:
                lista: dict = {};                
                lista["id_tarjeta"]=elemento[0];
                lista["id_usuario"]=elemento[1];
                lista["nombre_tarjeta"]=elemento[2];
                lista["tipo"]=elemento[3];
                lista["numero_tarjeta"]=self.encriptarAES.decifrar(elemento[5]);
                lista["vencimiento"]=elemento[5];
                respuesta[str(contador)] = lista;
                contador = contador + 1;  


            cursor.close()
            conexion.close()
            return respuesta;
        except Exception as ex:
            print("Error al listar tarjetas:", str(ex))
            return respuesta;

    def guardar(self, id_usuario, nombre_tarjeta, tipo, numero_tarjeta, vencimiento):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            encriptador = EncriptarAES()
            cifrado = encriptador.cifrar(numero_tarjeta)

            consulta = "INSERT INTO tarjetas (id_usuario, nombre_tarjeta, tipo, numero_tarjeta, vencimiento) VALUES (?, ?, ?, ?, ?)"
            cursor.execute(consulta, (id_usuario, nombre_tarjeta, tipo, cifrado, vencimiento))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Tarjeta guardada correctamente")
        except Exception as ex:
            print("Error al guardar tarjeta:", str(ex))

    def actualizar(self, id_tarjeta, id_usuario, nombre_tarjeta, tipo, numero_tarjeta, vencimiento):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = ("UPDATE tarjetas SET id_usuario = ?, nombre_tarjeta = ?, tipo = ?, "
                        "numero_tarjeta = ?, vencimiento = ? WHERE id_tarjeta = ?")
            cursor.execute(consulta, (id_usuario, nombre_tarjeta, tipo, numero_tarjeta, vencimiento, id_tarjeta))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Tarjeta actualizada correctamente")
        except Exception as ex:
            print("Error al actualizar tarjeta:", str(ex))

    def eliminar(self, id_tarjeta):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = "DELETE FROM tarjetas WHERE id_tarjeta = ?"
            cursor.execute(consulta, (id_tarjeta,))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Tarjeta eliminada correctamente")
        except Exception as ex:
            print("Error al eliminar tarjeta:", str(ex))