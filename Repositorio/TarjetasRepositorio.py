import pyodbc
from Entidades.Tarjetas import Tarjetas
from Utilidades.Configuracion import Configuracion

class TarjetasRepositorio:
    def listar(self):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            consulta = ("SELECT id_tarjeta, id_usuario, nombre_tarjeta, tipo, numero_tarjeta, "
                        "vencimiento FROM tarjetas")
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista = []
            for e in cursor:
                tarjeta = Tarjetas(
                    id_tarjeta=e[0],
                    id_usuario=e[1],
                    nombre_tarjeta=e[2],
                    tipo=e[3],
                    numero_tarjeta=e[4],
                    vencimiento=e[5]
                )
                lista.append(tarjeta)

            cursor.close()
            conexion.close()
            return lista
        except Exception as ex:
            print("Error al listar tarjetas:", str(ex))
            return []

    def guardar(self, id_usuario, nombre_tarjeta, tipo, numero_tarjeta, vencimiento):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = ("INSERT INTO tarjetas (id_usuario, nombre_tarjeta, tipo, numero_tarjeta, vencimiento) "
                        "VALUES (?, ?, ?, ?, ?)")
            cursor.execute(consulta, (id_usuario, nombre_tarjeta, tipo, numero_tarjeta, vencimiento))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Tarjeta guardada correctamente")
        except Exception as ex:
            print("Error al guardar tarjeta:", str(ex))

    def actualizar(self, id_tarjeta, id_usuario, nombre_tarjeta, tipo, numero_tarjeta, vencimiento):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = ("UPDATE tarjetas SET id_usuario = ?, nombre_tarjeta = ?, tipo = ?, "
                        "numero_tarjeta = ?, vencimiento = ? WHERE id_tarjeta = ?")
            cursor.execute(consulta, (id_usuario, nombre_tarjeta, tipo, numero_tarjeta, vencimiento, id_tarjeta))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Tarjeta actualizada correctamente")
        except Exception as ex:
            print("Error al actualizar tarjeta:", str(ex))

    def eliminar(self, id_tarjeta):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = "DELETE FROM tarjetas WHERE id_tarjeta = ?"
            cursor.execute(consulta, (id_tarjeta,))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Tarjeta eliminada correctamente")
        except Exception as ex:
            print("Error al eliminar tarjeta:", str(ex))