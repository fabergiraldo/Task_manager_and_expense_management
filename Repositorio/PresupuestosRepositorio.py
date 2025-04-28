import pyodbc
from Entidades.Presupuestos import Presupuestos
from Utilidades.Configuracion import Configuracion

class PresupuestosRepositorio:
    def listar(self):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            consulta = "SELECT id_presupuesto, id_usuario, id_categoria, mes, monto FROM presupuestos"
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista = []
            for e in cursor:
                p = Presupuestos(
                    id_presupuesto=e[0],
                    id_usuario=e[1],
                    id_categoria=e[2],
                    mes=e[3],
                    monto=e[4]
                )
                lista.append(p)

            cursor.close()
            conexion.close()
            return lista
        except Exception as ex:
            print("Error al listar presupuestos:", str(ex))
            return []

    def guardar(self, id_usuario, id_categoria, mes, monto):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = "INSERT INTO presupuestos (id_usuario, id_categoria, mes, monto) VALUES (?, ?, ?, ?)"
            cursor.execute(consulta, (id_usuario, id_categoria, mes, monto))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Presupuesto guardado correctamente")
        except Exception as ex:
            print("Error al guardar presupuesto:", str(ex))

    def actualizar(self, id_presupuesto, id_usuario, id_categoria, mes, monto):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = ("UPDATE presupuestos SET id_usuario = ?, id_categoria = ?, mes = ?, monto = ? "
                        "WHERE id_presupuesto = ?")
            cursor.execute(consulta, (id_usuario, id_categoria, mes, monto, id_presupuesto))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Presupuesto actualizado correctamente")
        except Exception as ex:
            print("Error al actualizar presupuesto:", str(ex))

    def eliminar(self, id_presupuesto):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = "DELETE FROM presupuestos WHERE id_presupuesto = ?"
            cursor.execute(consulta, (id_presupuesto,))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Presupuesto eliminado correctamente")
        except Exception as ex:
            print("Error al eliminar presupuesto:", str(ex))
