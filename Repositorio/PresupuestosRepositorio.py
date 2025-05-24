import pyodbc
from Utilidades.Configuracion import strConnection
from Entidades.Presupuestos import Presupuestos

class PresupuestosRepositorio:

    @staticmethod
    def listar():
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "SELECT id_presupuesto, id_usuario, id_categoria, mes, monto FROM presupuestos"
            )
            return [Presupuestos(*fila) for fila in cursor.fetchall()]

    @staticmethod
    def crear(presupuesto: Presupuestos):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO presupuestos (id_usuario, id_categoria, mes, monto) VALUES (?, ?, ?, ?)",
                (presupuesto.id_usuario, presupuesto.id_categoria, presupuesto.mes, presupuesto.monto)
            )
            conexion.commit()

    @staticmethod
    def actualizar(presupuesto: Presupuestos):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "UPDATE presupuestos SET id_usuario=?, id_categoria=?, mes=?, monto=? WHERE id_presupuesto=?",
                (presupuesto.id_usuario, presupuesto.id_categoria, presupuesto.mes, presupuesto.monto, presupuesto.id_presupuesto)
            )
            conexion.commit()

    @staticmethod
    def eliminar(id_presupuesto):
        with pyodbc.connect(strConnection) as conexion:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM presupuestos WHERE id_presupuesto=?", (id_presupuesto,))
            conexion.commit()