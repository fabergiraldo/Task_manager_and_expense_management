import pyodbc
from Entidades.Ingresos import Ingresos
from Utilidades.Configuracion import Configuracion
from Utilidades.Encriptar import EncriptarAES

class IngresosRepositorio:
    def __init__(self):
        self.encriptarAES = EncriptarAES()

    def listar(self):
        respuesta: dict = {};
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            consulta = "SELECT i.id_ingreso, i.id_usuario, i.fecha, i.monto, i.descripcion, i.id_moneda, i.id_cuenta, i.id_metodo_pago FROM ingresos i"
            cursor = conexion.cursor()
            cursor.execute(consulta)

            contador = 0;
            for elemento in cursor:
                lista: dict = {};                
                lista["id_ingreso"]=elemento[0];
                lista["id_usuario"]=elemento[1];
                lista["fecha"]=elemento[2];
                lista["monto"]=elemento[3];
                lista["descripcion"]=self.encriptarAES.decifrar(elemento[4]);
                lista["id_moneda"]=elemento[5];
                lista["id_cuenta"]=elemento[6];
                lista["id_metodo_pago"]=elemento[7];
                respuesta[str(contador)] = lista;
                contador = contador + 1; 


            cursor.close()
            conexion.close()

            return respuesta;

        except Exception as ex:
            print("Error al listar ingresos:", str(ex))
            return respuesta;

    def guardar(self, id_usuario, fecha, monto, descripcion, id_moneda, id_cuenta, id_metodo_pago):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            encriptador = EncriptarAES()
            cifrado = encriptador.cifrar(descripcion)

            consulta = """
                INSERT INTO ingresos (id_usuario, fecha, monto, descripcion, id_moneda, id_cuenta, id_metodo_pago)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(consulta, (id_usuario, fecha, monto, cifrado, id_moneda, id_cuenta, id_metodo_pago))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Ingreso guardado correctamente")

        except Exception as ex:
            print("Error al guardar ingreso:", str(ex))

    def actualizar(self, id_usuario, fecha, monto, descripcion, id_moneda, id_cuenta, id_metodo_pago):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = """
                UPDATE ingresos 
                SET id_usuario = ?, fecha = ?, monto = ?, descripcion = ?, 
                    id_moneda = ?, id_cuenta = ?, id_metodo_pago = ?
                WHERE id_ingreso = ?
            """
            cursor.execute(consulta, (id_usuario, fecha, monto, descripcion, id_moneda, id_cuenta, id_metodo_pago))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Ingreso actualizado correctamente")

        except Exception as ex:
            print("Error al actualizar ingreso:", str(ex))

    def eliminar(self, id_ingreso):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = "DELETE FROM ingresos WHERE id_ingreso = ?"
            cursor.execute(consulta, (id_ingreso,))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Ingreso eliminado correctamente")

        except Exception as ex:
            print("Error al eliminar ingreso:", str(ex)) 