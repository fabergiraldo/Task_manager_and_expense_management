import pyodbc
from Utilidades.Configuracion import strConnection
from Entidades.Facturas import Facturas

class FacturasRepositorio:

    @staticmethod
    def listar():
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "SELECT id_factura, id_gasto, id_proveedor, ruta_archivo FROM facturas"
            )
            return [Facturas(*fila) for fila in cursor.fetchall()]

    @staticmethod
    def crear(factura: Facturas):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO facturas (id_gasto, id_proveedor, ruta_archivo) VALUES (?, ?, ?)",
                (factura.id_gasto, factura.id_proveedor, factura.ruta_archivo)
            )
            conexion.commit()

    @staticmethod
    def actualizar(factura: Facturas):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "UPDATE facturas SET id_gasto=?, id_proveedor=?, ruta_archivo=? WHERE id_factura=?",
                (factura.id_gasto, factura.id_proveedor, factura.ruta_archivo, factura.id_factura)
            )
            conexion.commit()

    @staticmethod
    def eliminar(id_factura):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM facturas WHERE id_factura=?", (id_factura,))
            conexion.commit()
