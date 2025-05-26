import pyodbc
from Utilidades.Configuracion import strConnection
from Entidades.Ingresos import Ingresos
from Utilidades.Encriptar import EncriptarAES

class IngresosRepositorio:

    @staticmethod
    def listar():
        try:
            conexion = pyodbc.connect(strConnection)
            consulta = """
                SELECT i.id_ingreso, i.id_usuario, i.fecha, i.monto, i.descripcion, 
                    i.id_moneda, i.id_cuenta, i.id_metodo_pago 
                FROM ingresos i
            """
            cursor = conexion.cursor()
            cursor.execute(consulta)

            encriptador = EncriptarAES()

            ingresos = []
            for fila in cursor.fetchall():
                ingreso = Ingresos(
                    id_ingreso=fila[0],
                    id_usuario=fila[1],
                    fecha=fila[2],
                    monto=fila[3],
                    descripcion=encriptador.decifrar(fila[4]),  # ✅ Corrección en desencriptado
                    id_moneda=fila[5],
                    id_cuenta=fila[6],
                    id_metodo_pago=fila[7]
                )
                ingresos.append(ingreso)

            cursor.close()
            conexion.close()
            return ingresos

        except Exception as ex:
            print("Error al listar ingresos:", str(ex))
            return []
        # with pyodbc.connect(strConnection) as conexion:
        #     cursor = conexion.cursor()
        #     cursor.execute(
        #         "SELECT id_ingreso, id_usuario, fecha, monto, descripcion, id_moneda, id_cuenta, id_metodo_pago FROM ingresos"
        #     )
        #     return [Ingresos(*fila) for fila in cursor.fetchall()]

    @staticmethod
    def crear(ingreso: Ingresos):
        try:
            conexion = pyodbc.connect(strConnection)
            cursor = conexion.cursor()

            encriptador = EncriptarAES()
            cifrado = encriptador.cifrar(ingreso.descripcion)

            consulta = """
                INSERT INTO ingresos (id_usuario, fecha, monto, descripcion, id_moneda, id_cuenta, id_metodo_pago)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(consulta, (ingreso.id_usuario, ingreso.fecha, ingreso.monto, cifrado, ingreso.id_moneda, ingreso.id_cuenta, ingreso.id_metodo_pago))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("✅ Ingreso guardado correctamente con descripción cifrada.")

        except Exception as ex:
            print("Error al guardar ingreso:", str(ex))
        # with pyodbc.connect(strConnection) as conexion:
        #     cursor = conexion.cursor()
        #     cursor.execute(
        #         "INSERT INTO ingresos (id_usuario, fecha, monto, descripcion, id_moneda, id_cuenta, id_metodo_pago) VALUES (?, ?, ?, ?, ?, ?, ?)",
        #         (ingreso.id_usuario, ingreso.fecha, ingreso.monto, ingreso.descripcion,
        #          ingreso.id_moneda, ingreso.id_cuenta, ingreso.id_metodo_pago)
        #     )
        #     conexion.commit()

    @staticmethod
    def actualizar(ingreso: Ingresos):
        try:
            conexion = pyodbc.connect(strConnection)
            cursor = conexion.cursor()

            encriptador = EncriptarAES()
            cifrado = encriptador.cifrar(ingreso.descripcion)

            consulta = """
                UPDATE ingresos SET id_usuario=?, fecha=?, monto=?, descripcion=?, id_moneda=?, id_cuenta=?, id_metodo_pago=? WHERE id_ingreso=?
            """
            cursor.execute(consulta, (ingreso.id_usuario, ingreso.fecha, ingreso.monto, cifrado, ingreso.id_moneda, ingreso.id_cuenta, ingreso.id_metodo_pago, ingreso.id_ingreso))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Ingreso actualizado correctamente con descripción cifrada.")

        except Exception as ex:
            print("Error al actualizar ingreso:", str(ex))
        # with pyodbc.connect(strConnection) as conexion:
        #     cursor = conexion.cursor()
        #     cursor.execute(
        #         "UPDATE ingresos SET id_usuario=?, fecha=?, monto=?, descripcion=?, id_moneda=?, id_cuenta=?, id_metodo_pago=? WHERE id_ingreso=?",
        #         (ingreso.id_usuario, ingreso.fecha, ingreso.monto, ingreso.descripcion,
        #          ingreso.id_moneda, ingreso.id_cuenta, ingreso.id_metodo_pago, ingreso.id_ingreso)
        #     )
        #     conexion.commit()

    @staticmethod
    def eliminar(id_ingreso):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM ingresos WHERE id_ingreso=?", (id_ingreso,))
            conexion.commit()