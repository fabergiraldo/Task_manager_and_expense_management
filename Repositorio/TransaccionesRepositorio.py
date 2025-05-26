import pyodbc
from Utilidades.Configuracion import strConnection
from Entidades.Transacciones import Transacciones
from Utilidades.Encriptar import EncriptarAES 
class TransaccionesRepositorio:

    @staticmethod
    def listar():
        try:
            conexion = pyodbc.connect(strConnection)
            consulta = """
                SELECT id_transaccion, id_usuario, tipo, id_categoria, id_moneda, id_cuenta, id_metodo_pago, fecha 
                FROM transacciones
            """
            cursor = conexion.cursor()
            cursor.execute(consulta)

            encriptador = EncriptarAES()

            transacciones = []
            for fila in cursor.fetchall():
                transaccion = Transacciones(
                    id_transaccion=fila[0],
                    id_usuario=fila[1],
                    tipo=encriptador.decifrar(fila[2]),  # ✅ Corrección en desencriptado
                    id_categoria=fila[3],
                    id_moneda=fila[4],
                    id_cuenta=fila[5],
                    id_metodo_pago=fila[6],
                    fecha=fila[7]
                )
                transacciones.append(transaccion)

            cursor.close()
            conexion.close()
            return transacciones

        except Exception as ex:
            print("Error al listar transacciones:", str(ex))
            return []
        # with pyodbc.connect(strConnection) as conexion:
        #     cursor = conexion.cursor()
        #     cursor.execute(
        #         "SELECT id_transaccion, id_usuario, tipo, id_categoria, id_moneda, id_cuenta, id_metodo_pago, fecha FROM transacciones"
        #     )
        #     return [Transacciones(*fila) for fila in cursor.fetchall()]

    @staticmethod
    def crear(transaccion: Transacciones):
        try:
            conexion = pyodbc.connect(strConnection)
            cursor = conexion.cursor()

            encriptador = EncriptarAES()
            cifrado = encriptador.cifrar(transaccion.tipo)

            consulta = """
                INSERT INTO transacciones (id_usuario, tipo, id_categoria, id_moneda, id_cuenta, id_metodo_pago, fecha) 
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(consulta, (transaccion.id_usuario, cifrado, transaccion.id_categoria, transaccion.id_moneda, transaccion.id_cuenta, transaccion.id_metodo_pago, transaccion.fecha))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("✅ Transacción guardada correctamente con tipo cifrado.")

        except Exception as ex:
            print("Error al guardar transacción:", str(ex))
        # with pyodbc.connect(strConnection) as conexion:
        #     cursor = conexion.cursor()
        #     cursor.execute(
        #         "INSERT INTO transacciones (id_usuario, tipo, id_categoria, id_moneda, id_cuenta, id_metodo_pago, fecha) VALUES (?, ?, ?, ?, ?, ?, ?)",
        #         (transaccion.id_usuario, transaccion.tipo, transaccion.id_categoria,
        #          transaccion.id_moneda, transaccion.id_cuenta, transaccion.id_metodo_pago,
        #          transaccion.fecha)
        #     )
        #     conexion.commit()

    @staticmethod
    def actualizar(transaccion: Transacciones):
        try:
            conexion = pyodbc.connect(strConnection)
            cursor = conexion.cursor()

            encriptador = EncriptarAES()
            cifrado = encriptador.cifrar(transaccion.tipo)

            consulta = """
                UPDATE transacciones SET id_usuario=?, tipo=?, id_categoria=?, id_moneda=?, id_cuenta=?, id_metodo_pago=?, fecha=? WHERE id_transaccion=?
            """
            cursor.execute(consulta, (transaccion.id_usuario, cifrado, transaccion.id_categoria, transaccion.id_moneda, transaccion.id_cuenta, transaccion.id_metodo_pago, transaccion.fecha, transaccion.id_transaccion))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Transacción actualizada correctamente con tipo cifrado.")

        except Exception as ex:
            print("Error al actualizar transacción:", str(ex))
        # with pyodbc.connect(strConnection) as conexion:
        #     cursor = conexion.cursor()
        #     cursor.execute(
        #         "UPDATE transacciones SET id_usuario=?, tipo=?, id_categoria=?, id_moneda=?, id_cuenta=?, id_metodo_pago=?, fecha=? WHERE id_transaccion=?",
        #         (transaccion.id_usuario, transaccion.tipo, transaccion.id_categoria,
        #          transaccion.id_moneda, transaccion.id_cuenta, transaccion.id_metodo_pago,
        #          transaccion.fecha, transaccion.id_transaccion)
        #     )
        #     conexion.commit()

    @staticmethod
    def eliminar(id_transaccion):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM transacciones WHERE id_transaccion=?", (id_transaccion,))
            conexion.commit()