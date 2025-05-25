import pyodbc
from Entidades.Presupuestos import Presupuestos
from Utilidades.Configuracion import Configuracion
from Utilidades.Encriptar import EncriptarAES 

class PresupuestosRepositorio:
    def __init__(self):
        self.encriptarAES = EncriptarAES() 

    def listar(self):
        respuesta: dict = {}
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            consulta = "SELECT id_presupuesto, id_usuario, id_categoria, mes, monto FROM presupuestos"
            cursor = conexion.cursor()
            cursor.execute(consulta)

            contador = 0
            for elemento in cursor:
                lista: dict = {}                
                lista["id_presupuesto"] = elemento[0]
                lista["id_usuario"] = elemento[1]
                lista["id_categoria"] = elemento[2]
                lista["mes"] = self.encriptarAES.decifrar(elemento[3])
                lista["monto"] = float(elemento[4]) 
                respuesta[str(contador)] = lista
                contador += 1  

            cursor.close()
            conexion.close()
            return respuesta

        except Exception as ex:
            print("Error al listar presupuestos:", str(ex))
            return respuesta

    def guardar(self, id_usuario, id_categoria, mes, monto):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            encriptador = EncriptarAES()
            cifrado = encriptador.cifrar(mes)

            consulta = "INSERT INTO presupuestos (id_usuario, id_categoria, mes, monto) VALUES (?, ?, ?, ?)"
            cursor.execute(consulta, (id_usuario, id_categoria, cifrado, monto))
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

            consulta = "UPDATE presupuestos SET id_usuario = ?, id_categoria = ?, mes = ?, monto = ? WHERE id_presupuesto = ?"
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
