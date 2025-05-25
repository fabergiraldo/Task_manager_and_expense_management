import pyodbc
from Entidades.Facturas import Facturas
from Utilidades.Configuracion import Configuracion
from Utilidades.Encriptar import EncriptarAES

class FacturasRepositorio:
    def __init__(self):
        self.encriptarAES = EncriptarAES() 
    def listar(self):
        respuesta: dict = {};
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            consulta = "SELECT id_factura, id_gasto, id_proveedor, ruta_archivo FROM facturas"
            cursor = conexion.cursor()
            cursor.execute(consulta)

            contador = 0;
            for elemento in cursor:
                lista: dict = {};                
                lista["id_factura"]=elemento[0];
                lista["id_gasto"]=elemento[1];
                lista["id_proveedor"]=elemento[2];
                lista["ruta_archivo"]=self.encriptarAES.decifrar(elemento[3]);
                respuesta[str(contador)] = lista;
                contador = contador + 1;  

            cursor.close()
            conexion.close()

            return respuesta;

        except Exception as ex:
            print("Error al listar facturas:", str(ex))
            return respuesta;

    def guardar(self, id_gasto, id_proveedor, ruta_archivo):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            encriptador = EncriptarAES()
            cifrado = encriptador.cifrar(ruta_archivo)

            consulta = "INSERT INTO facturas (id_gasto, id_proveedor, ruta_archivo) VALUES (?, ?, ?)"
            cursor.execute(consulta, (id_gasto, id_proveedor, cifrado))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Factura guardada correctamente")

        except Exception as ex:
            print("Error al guardar factura:", str(ex))

    def actualizar(self, id_gasto, id_proveedor, ruta_archivo):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = """
                UPDATE facturas 
                SET id_gasto = ?, id_proveedor = ?, ruta_archivo = ?, 
                WHERE id_factura = ?
            """
            cursor.execute(consulta, (id_gasto, id_proveedor, ruta_archivo))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Factura actualizada correctamente")

        except Exception as ex:
            print("Error al actualizar factura:", str(ex))

    def eliminar(self, id_factura):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = "DELETE FROM facturas WHERE id_factura = ?"
            cursor.execute(consulta, (id_factura,))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Factura eliminada correctamente")

        except Exception as ex:
            print("Error al eliminar factura:", str(ex)) 