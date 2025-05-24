import pyodbc
from Utilidades.Configuracion import strConnection
from Entidades.Proveedores import Proveedores

class ProveedoresRepositorio:

    @staticmethod
    def listar():
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "SELECT id_proveedor, nombre, contacto, telefono, correo FROM proveedores"
            )
            return [Proveedores(*fila) for fila in cursor.fetchall()]

    @staticmethod
    def crear(proveedor: Proveedores):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO proveedores (nombre, contacto, telefono, correo) VALUES (?, ?, ?, ?)",
                (proveedor.nombre, proveedor.contacto, proveedor.telefono, proveedor.correo)
            )
            conexion.commit()

    @staticmethod
    def actualizar(proveedor: Proveedores):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "UPDATE proveedores SET nombre=?, contacto=?, telefono=?, correo=? WHERE id_proveedor=?",
                (proveedor.nombre, proveedor.contacto, proveedor.telefono, proveedor.correo, proveedor.id_proveedor)
            )
            conexion.commit()

    @staticmethod
    def eliminar(id_proveedor):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM proveedores WHERE id_proveedor=?", (id_proveedor,))
            conexion.commit()