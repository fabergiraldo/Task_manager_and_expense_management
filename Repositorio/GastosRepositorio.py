import pyodbc
from Utilidades.Configuracion import strConnection
from Entidades.Gastos import Gastos
from Utilidades.Encriptar import EncriptarAES
class GastosRepositorio:

    @staticmethod
    def listar():
        try:
            conexion = pyodbc.connect(strConnection)
            consulta = """
                SELECT g.id_gasto, g.id_usuario, g.fecha, g.monto, g.descripcion, 
                    g.id_categoria, g.id_moneda, g.id_cuenta, g.id_tarjeta, g.id_proveedor, g.id_metodo_pago 
                FROM gastos g
            """
            cursor = conexion.cursor()
            cursor.execute(consulta)

            encriptador = EncriptarAES()

            gastos = []
            for fila in cursor.fetchall():
                gasto = Gastos(
                    id_gasto=fila[0],
                    id_usuario=fila[1],
                    fecha=fila[2],
                    monto=fila[3],
                    descripcion=encriptador.decifrar(fila[4]),
                    id_categoria=fila[5],
                    id_moneda=fila[6],
                    id_cuenta=fila[7],
                    id_tarjeta=fila[8],
                    id_proveedor=fila[9],
                    id_metodo_pago=fila[10]
                )
                gastos.append(gasto)

            cursor.close()
            conexion.close()
            return gastos

        except Exception as ex:
            print("Error al listar gastos:", str(ex))
            return []
        #with pyodbc.connect(strConnection) as conexion:
            # cursor = conexion.cursor()
            # cursor.execute(
            #     "SELECT id_gasto, id_usuario, fecha, monto, descripcion, id_categoria, id_moneda, id_cuenta, id_tarjeta, id_proveedor, id_metodo_pago FROM gastos"
            # )
            # return [Gastos(*fila) for fila in cursor.fetchall()]

    @staticmethod
    def crear(gasto: Gastos):
        try:
            conexion = pyodbc.connect(strConnection)
            cursor = conexion.cursor()

            encriptador = EncriptarAES()
            cifrado = encriptador.cifrar(gasto.descripcion)

            consulta = """
                INSERT INTO gastos (id_usuario, fecha, monto, descripcion, id_categoria, id_moneda, id_cuenta, id_tarjeta, id_proveedor, id_metodo_pago)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(consulta, (gasto.id_usuario, gasto.fecha, gasto.monto, cifrado, gasto.id_categoria, gasto.id_moneda, gasto.id_cuenta, gasto.id_tarjeta, gasto.id_proveedor, gasto.id_metodo_pago))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Gasto guardado correctamente con descripción cifrada.")

        except Exception as ex:
            print("Error al guardar gasto:", str(ex))
        # with pyodbc.connect(strConnection) as conexion:
        #     cursor = conexion.cursor()
        #     cursor.execute(
        #         "INSERT INTO gastos (id_usuario, fecha, monto, descripcion, id_categoria, id_moneda, id_cuenta, id_tarjeta, id_proveedor, id_metodo_pago) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        #         (gasto.id_usuario, gasto.fecha, gasto.monto, gasto.descripcion, gasto.id_categoria,
        #          gasto.id_moneda, gasto.id_cuenta, gasto.id_tarjeta, gasto.id_proveedor,
        #          gasto.id_metodo_pago)
        #     )
        #     conexion.commit()

    @staticmethod
    def actualizar(gasto: Gastos):
        try:
            conexion = pyodbc.connect(strConnection)
            cursor = conexion.cursor()

            encriptador = EncriptarAES()
            cifrado = encriptador.cifrar(gasto.descripcion)

            consulta = """
                UPDATE gastos SET id_usuario=?, fecha=?, monto=?, descripcion=?, id_categoria=?, id_moneda=?, id_cuenta=?, id_tarjeta=?, id_proveedor=?, id_metodo_pago=? WHERE id_gasto=?
            """
            cursor.execute(consulta, (gasto.id_usuario, gasto.fecha, gasto.monto, cifrado, gasto.id_categoria, gasto.id_moneda, gasto.id_cuenta, gasto.id_tarjeta, gasto.id_proveedor, gasto.id_metodo_pago, gasto.id_gasto))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Gasto actualizado correctamente con descripción cifrada.")

        except Exception as ex:
            print("Error al actualizar gasto:", str(ex))
        # with pyodbc.connect(strConnection) as conexion:
        #     cursor = conexion.cursor()
        #     cursor.execute(
        #         "UPDATE gastos SET id_usuario=?, fecha=?, monto=?, descripcion=?, id_categoria=?, id_moneda=?, id_cuenta=?, id_tarjeta=?, id_proveedor=?, id_metodo_pago=? WHERE id_gasto=?",
        #         (gasto.id_usuario, gasto.fecha, gasto.monto, gasto.descripcion, gasto.id_categoria,
        #          gasto.id_moneda, gasto.id_cuenta, gasto.id_tarjeta, gasto.id_proveedor,
        #          gasto.id_metodo_pago, gasto.id_gasto)
        #     )
        #     conexion.commit()

    @staticmethod
    def eliminar(id_gasto):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM gastos WHERE id_gasto=?", (id_gasto,))
            conexion.commit()
