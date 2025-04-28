import pyodbc
from Entidades.Proveedores import Proveedores
from Utilidades.Configuracion import Configuracion

class ProveedoresRepositorio:
    def listar(self):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            cursor.execute("SELECT id_proveedor, nombre, contacto, telefono, correo FROM proveedores")
            lista = [
                Proveedores(
                    id_proveedor=row[0],
                    nombre=row[1],
                    contacto=row[2],
                    telefono=row[3],
                    correo=row[4]
                ) for row in cursor
            ]
            cursor.close()
            conexion.close()
            return lista
        except Exception as ex:
            print("Error al listar proveedores:", ex)
            return []

    def guardar(self, nombre, contacto, telefono, correo):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO proveedores (nombre, contacto, telefono, correo) VALUES (?, ?, ?, ?)",
                (nombre, contacto, telefono, correo)
            )
            conexion.commit()
            cursor.close()
            conexion.close()
            print("Proveedor guardado correctamente")
        except Exception as ex:
            print("Error al guardar proveedor:", ex)

    def actualizar(self, id_proveedor, nombre, contacto, telefono, correo):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            cursor.execute(
                "UPDATE proveedores SET nombre = ?, contacto = ?, telefono = ?, correo = ? WHERE id_proveedor = ?",
                (nombre, contacto, telefono, correo, id_proveedor)
            )
            conexion.commit()
            cursor.close()
            conexion.close()
            print("Proveedor actualizado correctamente")
        except Exception as ex:
            print("Error al actualizar proveedor:", ex)

    def eliminar(self, id_proveedor):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM proveedores WHERE id_proveedor = ?", (id_proveedor,))
            conexion.commit()
            cursor.close()
            conexion.close()
            print("Proveedor eliminado correctamente")
        except Exception as ex:
            print("Error al eliminar proveedor:", ex)