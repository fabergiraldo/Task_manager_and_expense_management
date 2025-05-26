import pyodbc
from Utilidades.Configuracion import strConnection
from Entidades.Tarjetas import Tarjetas
from Utilidades.Encriptar import EncriptarAES

class TarjetasRepositorio:

    @staticmethod
    def listar():
        try:
            conexion = pyodbc.connect(strConnection)
            consulta = "SELECT id_tarjeta, id_usuario, nombre_tarjeta, tipo, numero_tarjeta, vencimiento FROM tarjetas"
            cursor = conexion.cursor()
            cursor.execute(consulta)

            encriptador = EncriptarAES()

            tarjetas = []
            for fila in cursor.fetchall():
                tarjeta = Tarjetas(
                    id_tarjeta=fila[0],
                    id_usuario=fila[1],
                    nombre_tarjeta=fila[2],
                    tipo=fila[3],
                    numero_tarjeta=encriptador.decifrar(fila[4]),  
                    vencimiento=fila[5]  
                )
                tarjetas.append(tarjeta)

            cursor.close()
            conexion.close()
            return tarjetas

        except Exception as ex:
            print("Error al listar tarjetas:", str(ex))
            return []
        # with pyodbc.connect(strConnection) as conexion:
        #     cursor = conexion.cursor()
        #     cursor.execute(
        #         "SELECT id_tarjeta, id_usuario, nombre_tarjeta, tipo, numero_tarjeta, vencimiento FROM tarjetas"
        #     )
        #     rows = cursor.fetchall()
        #     tarjetas = []
        #     for fila in rows:
        #         # vencimiento comes as datetime.date or datetime.datetime
        #         tarjetas.append(Tarjetas(*fila))
        #     return tarjetas

    @staticmethod
    def crear(tarjeta: Tarjetas):
        try:
            conexion = pyodbc.connect(strConnection)
            cursor = conexion.cursor()

            encriptador = EncriptarAES()
            cifrado = encriptador.cifrar(tarjeta.numero_tarjeta)

            consulta = "INSERT INTO tarjetas (id_usuario, nombre_tarjeta, tipo, numero_tarjeta, vencimiento) VALUES (?, ?, ?, ?, ?)"
            cursor.execute(consulta, (tarjeta.id_usuario, tarjeta.nombre_tarjeta, tarjeta.tipo, cifrado, tarjeta.vencimiento))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Tarjeta guardada correctamente con número cifrado.")

        except Exception as ex:
            print("Error al guardar tarjeta:", str(ex))
        # with pyodbc.connect(strConnection) as conexion:
        #     cursor = conexion.cursor()
        #     cursor.execute(
        #         "INSERT INTO tarjetas (id_usuario, nombre_tarjeta, tipo, numero_tarjeta, vencimiento) VALUES (?, ?, ?, ?, ?)",
        #         (tarjeta.id_usuario, tarjeta.nombre_tarjeta, tarjeta.tipo, tarjeta.numero_tarjeta, tarjeta.vencimiento)
        #     )
        #     conexion.commit()

    @staticmethod
    def actualizar(tarjeta: Tarjetas):
        try:
            conexion = pyodbc.connect(strConnection)
            cursor = conexion.cursor()

            encriptador = EncriptarAES()
            cifrado = encriptador.cifrar(tarjeta.numero_tarjeta)

            consulta = """
                UPDATE tarjetas SET id_usuario=?, nombre_tarjeta=?, tipo=?, numero_tarjeta=?, vencimiento=? WHERE id_tarjeta=?
            """
            cursor.execute(consulta, (tarjeta.id_usuario, tarjeta.nombre_tarjeta, tarjeta.tipo, cifrado, tarjeta.vencimiento, tarjeta.id_tarjeta))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Tarjeta actualizada correctamente con número cifrado.")

        except Exception as ex:
            print("Error al actualizar tarjeta:", str(ex))
        # with pyodbc.connect(strConnection) as conexion:
        #     cursor = conexion.cursor()
        #     cursor.execute(
        #         "UPDATE tarjetas SET id_usuario=?, nombre_tarjeta=?, tipo=?, numero_tarjeta=?, vencimiento=? WHERE id_tarjeta=?",
        #         (tarjeta.id_usuario, tarjeta.nombre_tarjeta, tarjeta.tipo, tarjeta.numero_tarjeta, tarjeta.vencimiento, tarjeta.id_tarjeta)
        #     )
        #     conexion.commit()


    @staticmethod
    def eliminar(id_tarjeta):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM tarjetas WHERE id_tarjeta=?", (id_tarjeta,))
            conexion.commit()