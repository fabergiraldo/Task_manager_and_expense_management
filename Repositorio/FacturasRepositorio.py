import pyodbc
from Utilidades.Configuracion import strConnection
from Entidades.Facturas import Facturas
from Utilidades.Encriptar import EncriptarAES

class FacturasRepositorio:

    @staticmethod
    def listar():
        try:
            conexion = pyodbc.connect(strConnection)
            consulta = "SELECT id_factura, id_gasto, id_proveedor, ruta_archivo FROM facturas"
            cursor = conexion.cursor()
            cursor.execute(consulta)

            encriptador = EncriptarAES()

            facturas = []
            for fila in cursor.fetchall():
                factura = Facturas(
                    id_factura=fila[0],
                    id_gasto=fila[1],
                    id_proveedor=fila[2],
                    ruta_archivo=encriptador.decifrar(fila[3])
                )
                facturas.append(factura)

            cursor.close()
            conexion.close()
            return facturas

        except Exception as ex:
            print("Error al listar facturas:", str(ex))
            return []
        # with pyodbc.connect(strConnection) as conexion:
        #     cursor = conexion.cursor()
        #     cursor.execute(
        #         "SELECT id_factura, id_gasto, id_proveedor, ruta_archivo FROM facturas"
        #     )
        #     return [Facturas(*fila) for fila in cursor.fetchall()]

    @staticmethod
    def crear(factura: Facturas):
        try:
            conexion = pyodbc.connect(strConnection)
            cursor = conexion.cursor()

            encriptador = EncriptarAES()
            cifrado = encriptador.cifrar(factura.ruta_archivo)

            consulta = "INSERT INTO facturas (id_gasto, id_proveedor, ruta_archivo) VALUES (?, ?, ?)"
            cursor.execute(consulta, (factura.id_gasto, factura.id_proveedor, cifrado))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("✅ Factura guardada correctamente con ruta cifrada.")

        except Exception as ex:
            print("❌ Error al guardar factura:", str(ex))
        # with pyodbc.connect(strConnection) as conexion:
        #     cursor = conexion.cursor()
        #     cursor.execute(
        #         "INSERT INTO facturas (id_gasto, id_proveedor, ruta_archivo) VALUES (?, ?, ?)",
        #         (factura.id_gasto, factura.id_proveedor, factura.ruta_archivo)
        #     )
        #     conexion.commit()

    @staticmethod
    def actualizar(factura: Facturas):
        try:
            conexion = pyodbc.connect(strConnection)
            cursor = conexion.cursor()

            encriptador = EncriptarAES()
            cifrado = encriptador.cifrar(factura.ruta_archivo)

            consulta = """
                UPDATE facturas SET id_gasto=?, id_proveedor=?, ruta_archivo=? WHERE id_factura=?
            """
            cursor.execute(consulta, (factura.id_gasto, factura.id_proveedor, cifrado, factura.id_factura))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Factura actualizada correctamente con ruta cifrada.")

        except Exception as ex:
            print("Error al actualizar factura:", str(ex))
        # with pyodbc.connect(strConnection) as conexion:
        #     cursor = conexion.cursor()
        #     cursor.execute(
        #         "UPDATE facturas SET id_gasto=?, id_proveedor=?, ruta_archivo=? WHERE id_factura=?",
        #         (factura.id_gasto, factura.id_proveedor, factura.ruta_archivo, factura.id_factura)
        #     )
        #     conexion.commit()

    @staticmethod
    def eliminar(id_factura):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM facturas WHERE id_factura=?", (id_factura,))
            conexion.commit()
