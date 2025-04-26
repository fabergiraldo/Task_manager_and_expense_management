import pyodbc
from Entidades.Gastos import Gastos
from Utilidades.Configuracion import Configuracion

class GastosRepositorio:

    def listar(self):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            consulta = """
                SELECT g.id_gasto, g.id_usuario, g.id_categoria, g.monto, g.descripcion, 
                       g.fecha, g.id_metodo_pago, g.id_proveedor, g.estado
                FROM gastos g
            """
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista = []
            for elemento in cursor:
                gasto = Gastos(
                    id_gasto=elemento[0],
                    id_usuario=elemento[1],
                    id_categoria=elemento[2],
                    monto=elemento[3],
                    descripcion=elemento[4],
                    fecha=elemento[5],
                    id_metodo_pago=elemento[6],
                    id_proveedor=elemento[7],
                    estado=elemento[8]
                )
                lista.append(gasto)

            cursor.close()
            conexion.close()

            return lista

        except Exception as ex:
            print("Error al listar gastos:", str(ex))
            return []

    def guardar(self, id_usuario, id_categoria, monto, descripcion, fecha, id_metodo_pago, id_proveedor, estado):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = """
                INSERT INTO gastos (id_usuario, id_categoria, monto, descripcion, 
                                  fecha, id_metodo_pago, id_proveedor, estado)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(consulta, (id_usuario, id_categoria, monto, descripcion, 
                                    fecha, id_metodo_pago, id_proveedor, estado))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Gasto guardado correctamente")

        except Exception as ex:
            print("Error al guardar gasto:", str(ex))

    def actualizar(self, id_gasto, id_usuario, id_categoria, monto, descripcion, 
                  fecha, id_metodo_pago, id_proveedor, estado):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = """
                UPDATE gastos 
                SET id_usuario = ?, id_categoria = ?, monto = ?, descripcion = ?,
                    fecha = ?, id_metodo_pago = ?, id_proveedor = ?, estado = ?
                WHERE id_gasto = ?
            """
            cursor.execute(consulta, (id_usuario, id_categoria, monto, descripcion,
                                    fecha, id_metodo_pago, id_proveedor, estado, id_gasto))
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