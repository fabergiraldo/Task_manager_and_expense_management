import pyodbc
from Utilidades.Configuracion import strConnection
from Entidades.Presupuestos import Presupuestos
from Utilidades.Encriptar import EncriptarAES 
class PresupuestosRepositorio:

    @staticmethod
    def listar():
        try:
            conexion = pyodbc.connect(strConnection)
            consulta = "SELECT id_presupuesto, id_usuario, id_categoria, mes, monto FROM presupuestos"
            cursor = conexion.cursor()
            cursor.execute(consulta)

            encriptador = EncriptarAES()

            presupuestos = []
            for fila in cursor.fetchall():
                presupuesto = Presupuestos(
                    id_presupuesto=fila[0],
                    id_usuario=fila[1],
                    id_categoria=fila[2],
                    mes=encriptador.decifrar(fila[3]),
                    monto=float(fila[4]) 
                )
                presupuestos.append(presupuesto)

            cursor.close()
            conexion.close()
            return presupuestos

        except Exception as ex:
            print("Error al listar presupuestos:", str(ex))
            return []
        # with pyodbc.connect(strConnection) as conexion:
        #     cursor = conexion.cursor()
        #     cursor.execute(
        #         "SELECT id_presupuesto, id_usuario, id_categoria, mes, monto FROM presupuestos"
        #     )
        #     return [Presupuestos(*fila) for fila in cursor.fetchall()]

    @staticmethod
    def crear(presupuesto: Presupuestos):
        try:
            conexion = pyodbc.connect(strConnection)
            cursor = conexion.cursor()

            encriptador = EncriptarAES()
            cifrado = encriptador.cifrar(presupuesto.mes)

            consulta = "INSERT INTO presupuestos (id_usuario, id_categoria, mes, monto) VALUES (?, ?, ?, ?)"
            cursor.execute(consulta, (presupuesto.id_usuario, presupuesto.id_categoria, cifrado, presupuesto.monto))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Presupuesto guardado correctamente con mes cifrado.")

        except Exception as ex:
            print("Error al guardar presupuesto:", str(ex))
        # with pyodbc.connect(strConnection) as conexion:
        #     cursor = conexion.cursor()
        #     cursor.execute(
        #         "INSERT INTO presupuestos (id_usuario, id_categoria, mes, monto) VALUES (?, ?, ?, ?)",
        #         (presupuesto.id_usuario, presupuesto.id_categoria, presupuesto.mes, presupuesto.monto)
        #     )
        #     conexion.commit()

    @staticmethod
    def actualizar(presupuesto: Presupuestos):
        try:
            conexion = pyodbc.connect(strConnection)
            cursor = conexion.cursor()

            encriptador = EncriptarAES()
            cifrado = encriptador.cifrar(presupuesto.mes)

            consulta = """
                UPDATE presupuestos SET id_usuario=?, id_categoria=?, mes=?, monto=? WHERE id_presupuesto=?
            """
            cursor.execute(consulta, (presupuesto.id_usuario, presupuesto.id_categoria, cifrado, presupuesto.monto, presupuesto.id_presupuesto))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Presupuesto actualizado correctamente con mes cifrado.")

        except Exception as ex:
            print("Error al actualizar presupuesto:", str(ex))
        # with pyodbc.connect(strConnection) as conexion:
        #     cursor = conexion.cursor()
        #     cursor.execute(
        #         "UPDATE presupuestos SET id_usuario=?, id_categoria=?, mes=?, monto=? WHERE id_presupuesto=?",
        #         (presupuesto.id_usuario, presupuesto.id_categoria, presupuesto.mes, presupuesto.monto, presupuesto.id_presupuesto)
        #     )
        #     conexion.commit()

    @staticmethod
    def eliminar(id_presupuesto):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM presupuestos WHERE id_presupuesto=?", (id_presupuesto,))
            conexion.commit()