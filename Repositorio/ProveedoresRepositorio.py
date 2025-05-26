import pyodbc
from Utilidades.Configuracion import strConnection
from Entidades.Proveedores import Proveedores
from Utilidades.Encriptar import EncriptarAES 

class ProveedoresRepositorio:

    @staticmethod
    def listar():
        try:
            conexion = pyodbc.connect(strConnection)
            consulta = "SELECT id_proveedor, nombre, contacto, telefono, correo FROM proveedores"
            cursor = conexion.cursor()
            cursor.execute(consulta)

            encriptador = EncriptarAES()

            proveedores = []
            for fila in cursor.fetchall():
                proveedor = Proveedores(
                    id_proveedor=fila[0],
                    nombre=fila[1],
                    contacto=encriptador.decifrar(fila[2]),
                    telefono=encriptador.decifrar(fila[3]),
                    correo=encriptador.decifrar(fila[4]),
                )
                proveedores.append(proveedor)

            cursor.close()
            conexion.close()
            return proveedores

        except Exception as ex:
            print("Error al listar proveedores:", str(ex))
            return []
        # with pyodbc.connect(strConnection) as conexion:
        #     cursor = conexion.cursor()
        #     cursor.execute(
        #         "SELECT id_proveedor, nombre, contacto, telefono, correo FROM proveedores"
        #     )
        #     return [Proveedores(*fila) for fila in cursor.fetchall()]

    @staticmethod
    def crear(proveedor: Proveedores):
        try:
            conexion = pyodbc.connect(strConnection)
            cursor = conexion.cursor()

            encriptador = EncriptarAES()
            cifradoC = encriptador.cifrar(proveedor.contacto)
            cifradoT = encriptador.cifrar(proveedor.telefono)
            cifradoE = encriptador.cifrar(proveedor.correo)

            consulta = "INSERT INTO proveedores (nombre, contacto, telefono, correo) VALUES (?, ?, ?, ?)"
            cursor.execute(consulta, (proveedor.nombre, cifradoC, cifradoT, cifradoE))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Proveedor guardado correctamente con datos cifrados.")

        except Exception as ex:
            print("Error al guardar proveedor:", str(ex))
        # with pyodbc.connect(strConnection) as conexion:
        #     cursor = conexion.cursor()
        #     cursor.execute(
        #         "INSERT INTO proveedores (nombre, contacto, telefono, correo) VALUES (?, ?, ?, ?)",
        #         (proveedor.nombre, proveedor.contacto, proveedor.telefono, proveedor.correo)
        #     )
        #     conexion.commit()

    @staticmethod
    def actualizar(proveedor: Proveedores):
        try:
            conexion = pyodbc.connect(strConnection)
            cursor = conexion.cursor()

            encriptador = EncriptarAES()
            cifradoC = encriptador.cifrar(proveedor.contacto)
            cifradoT = encriptador.cifrar(proveedor.telefono)
            cifradoE = encriptador.cifrar(proveedor.correo)

            consulta = """
                UPDATE proveedores SET nombre=?, contacto=?, telefono=?, correo=? WHERE id_proveedor=?
            """
            cursor.execute(consulta, (proveedor.nombre, cifradoC, cifradoT, cifradoE, proveedor.id_proveedor))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Proveedor actualizado correctamente con datos cifrados.")

        except Exception as ex:
            print("Error al actualizar proveedor:", str(ex))
        # with pyodbc.connect(strConnection) as conexion:
        #     cursor = conexion.cursor()
        #     cursor.execute(
        #         "UPDATE proveedores SET nombre=?, contacto=?, telefono=?, correo=? WHERE id_proveedor=?",
        #         (proveedor.nombre, proveedor.contacto, proveedor.telefono, proveedor.correo, proveedor.id_proveedor)
        #     )
        #     conexion.commit()

    @staticmethod
    def eliminar(id_proveedor):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM proveedores WHERE id_proveedor=?", (id_proveedor,))
            conexion.commit()