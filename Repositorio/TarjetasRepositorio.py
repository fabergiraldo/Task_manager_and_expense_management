import pyodbc
from Utilidades.Configuracion import strConnection
from Entidades.Tarjetas import Tarjetas

class TarjetasRepositorio:

    @staticmethod
    def listar():
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "SELECT id_tarjeta, id_usuario, nombre_tarjeta, tipo, numero_tarjeta, vencimiento FROM tarjetas"
            )
            rows = cursor.fetchall()
            tarjetas = []
            for fila in rows:
                # vencimiento comes as datetime.date or datetime.datetime
                tarjetas.append(Tarjetas(*fila))
            return tarjetas

    @staticmethod
    def crear(tarjeta: Tarjetas):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO tarjetas (id_usuario, nombre_tarjeta, tipo, numero_tarjeta, vencimiento) VALUES (?, ?, ?, ?, ?)",
                (tarjeta.id_usuario, tarjeta.nombre_tarjeta, tarjeta.tipo, tarjeta.numero_tarjeta, tarjeta.vencimiento)
            )
            conexion.commit()

    @staticmethod
    def actualizar(tarjeta: Tarjetas):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "UPDATE tarjetas SET id_usuario=?, nombre_tarjeta=?, tipo=?, numero_tarjeta=?, vencimiento=? WHERE id_tarjeta=?",
                (tarjeta.id_usuario, tarjeta.nombre_tarjeta, tarjeta.tipo, tarjeta.numero_tarjeta, tarjeta.vencimiento, tarjeta.id_tarjeta)
            )
            conexion.commit()

    @staticmethod
    def eliminar(id_tarjeta):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM tarjetas WHERE id_tarjeta=?", (id_tarjeta,))
            conexion.commit()