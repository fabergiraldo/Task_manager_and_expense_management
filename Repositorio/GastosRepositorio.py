import pyodbc
from Entidades.Gastos import Gastos
from Utilidades.Configuracion import Configuracion
from Utilidades.Encriptar import EncriptarAES

class GastosRepositorio:
    def __init__(self):
        self.encriptarAES = EncriptarAES() 

    def listar(self):
        respuesta: dict = {};
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            consulta = "SELECT g.id_gasto, g.id_usuario, g.fecha, g.monto, g.descripcion, g.id_categoria, g.id_moneda, g.id_cuenta, g.id_tarjeta, g.id_proveedor, g.id_metodo_pago FROM gastos g"
            cursor = conexion.cursor()
            cursor.execute(consulta)

            contador = 0;
            for elemento in cursor:
                lista: dict = {};                
                lista["id_gasto"]=elemento[0];
                lista["id_usuario"]=elemento[1];
                lista["fecha"]=elemento[2];
                lista["monto"]=elemento[3];
                lista["descripcion"]=self.encriptarAES.decifrar(elemento[4]);
                lista["id_categoria"]=elemento[5];
                lista["id_moneda"]=elemento[6];
                lista["id_cuenta"]=elemento[7];
                lista["id_tarjeta"]=elemento[8];
                lista["id_proveedor"]=elemento[9];
                lista["id_metodo_pago"]=elemento[10];
                respuesta[str(contador)] = lista;
                contador = contador + 1;

            cursor.close()
            conexion.close()

            return respuesta;

        except Exception as ex:
            print("Error al listar gastos:", str(ex))
            return respuesta;

    def guardar(self, id_usuario, fecha, monto, descripcion, id_categoria, id_moneda, id_cuenta, id_tarjeta, id_proveedor, id_metodo_pago):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            encriptador = EncriptarAES()
            cifrado = encriptador.cifrar(descripcion)

            consulta = """
                INSERT INTO gastos (id_usuario, fecha, monto, descripcion, id_categoria, id_moneda, id_cuenta, id_tarjeta, id_proveedor, id_metodo_pago)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(consulta, (id_usuario, fecha, monto, cifrado, id_categoria, id_moneda, id_cuenta, id_tarjeta, id_proveedor, id_metodo_pago))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Gasto guardado correctamente")

        except Exception as ex:
            print("Error al guardar gasto:", str(ex))

    def actualizar(self, id_usuario, fecha, monto, descripcion, id_categoria, id_moneda, id_cuenta, id_tarjeta, id_proveedor, id_metodo_pago):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = "UPDATE gastos SET id_usuario = ?, fecha = ?, monto = ?, descripcion = ?, id_categoria = ?, id_moneda = ?, id_cuenta = ?, id_tarjeta = ?, id_proveedor = ?, id_metodo_pago = ? WHERE id_gasto = ?"
            cursor.execute(consulta, (id_usuario, fecha, monto, descripcion, id_categoria, id_moneda, id_cuenta, id_tarjeta, id_proveedor, id_metodo_pago))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Gasto actualizado correctamente")

        except Exception as ex:
            print("Error al actualizar gasto:", str(ex))

    def eliminar(self, id_gasto):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = "DELETE FROM gastos WHERE id_gasto = ?"
            cursor.execute(consulta, (id_gasto,))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Gasto eliminado correctamente")

        except Exception as ex:
            print("Error al eliminar gasto:", str(ex)) 