import pyodbc
from Entidades.Ingresos import Ingresos
from Utilidades.Configuracion import Configuracion

class IngresosRepositorio:

    def listar(self):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            consulta = """
                SELECT i.id_ingreso, i.id_usuario, i.monto, i.descripcion, 
                       i.fecha, i.id_metodo_pago, i.estado
                FROM ingresos i
            """
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista = []
            for elemento in cursor:
                ingreso = Ingresos(
                    id_ingreso=elemento[0],
                    id_usuario=elemento[1],
                    monto=elemento[2],
                    descripcion=elemento[3],
                    fecha=elemento[4],
                    id_metodo_pago=elemento[5],
                    estado=elemento[6]
                )
                lista.append(ingreso)

            cursor.close()
            conexion.close()

            return lista

        except Exception as ex:
            print("Error al listar ingresos:", str(ex))
            return []

    def guardar(self, id_usuario, monto, descripcion, fecha, id_metodo_pago, estado):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = """
                INSERT INTO ingresos (id_usuario, monto, descripcion, fecha, id_metodo_pago, estado)
                VALUES (?, ?, ?, ?, ?, ?)
            """
            cursor.execute(consulta, (id_usuario, monto, descripcion, fecha, id_metodo_pago, estado))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Ingreso guardado correctamente")

        except Exception as ex:
            print("Error al guardar ingreso:", str(ex))

    def actualizar(self, id_ingreso, id_usuario, monto, descripcion, fecha, id_metodo_pago, estado):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = """
                UPDATE ingresos 
                SET id_usuario = ?, monto = ?, descripcion = ?, fecha = ?, 
                    id_metodo_pago = ?, estado = ?
                WHERE id_ingreso = ?
            """
            cursor.execute(consulta, (id_usuario, monto, descripcion, fecha, 
                                    id_metodo_pago, estado, id_ingreso))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Ingreso actualizado correctamente")

        except Exception as ex:
            print("Error al actualizar ingreso:", str(ex))

    def eliminar(self, id_ingreso):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = "DELETE FROM ingresos WHERE id_ingreso = ?"
            cursor.execute(consulta, (id_ingreso,))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Ingreso eliminado correctamente")

        except Exception as ex:
            print("Error al eliminar ingreso:", str(ex)) 