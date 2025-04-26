import pyodbc
from Entidades.Facturas import Facturas
from Utilidades.Configuracion import Configuracion

class FacturasRepositorio:

    def listar(self):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            consulta = """
                SELECT id_factura, id_gasto, numero_factura, fecha_emision, 
                       fecha_vencimiento, monto_total, estado
                FROM facturas
            """
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista = []
            for elemento in cursor:
                factura = Facturas(
                    id_factura=elemento[0],
                    id_gasto=elemento[1],
                    numero_factura=elemento[2],
                    fecha_emision=elemento[3],
                    fecha_vencimiento=elemento[4],
                    monto_total=elemento[5],
                    estado=elemento[6]
                )
                lista.append(factura)

            cursor.close()
            conexion.close()

            return lista

        except Exception as ex:
            print("Error al listar facturas:", str(ex))
            return []

    def guardar(self, id_gasto, numero_factura, fecha_emision, fecha_vencimiento, 
                monto_total, estado):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = """
                INSERT INTO facturas (id_gasto, numero_factura, fecha_emision, 
                                    fecha_vencimiento, monto_total, estado)
                VALUES (?, ?, ?, ?, ?, ?)
            """
            cursor.execute(consulta, (id_gasto, numero_factura, fecha_emision, 
                                    fecha_vencimiento, monto_total, estado))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Factura guardada correctamente")

        except Exception as ex:
            print("Error al guardar factura:", str(ex))

    def actualizar(self, id_factura, id_gasto, numero_factura, fecha_emision, 
                  fecha_vencimiento, monto_total, estado):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = """
                UPDATE facturas 
                SET id_gasto = ?, numero_factura = ?, fecha_emision = ?, 
                    fecha_vencimiento = ?, monto_total = ?, estado = ?
                WHERE id_factura = ?
            """
            cursor.execute(consulta, (id_gasto, numero_factura, fecha_emision, 
                                    fecha_vencimiento, monto_total, estado, 
                                    id_factura))
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