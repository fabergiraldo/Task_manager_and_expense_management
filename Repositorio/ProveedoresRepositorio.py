import pyodbc
from Entidades.Proveedores import Proveedores
from Utilidades.Configuracion import Configuracion
from Utilidades.Encriptar import EncriptarAES 

class ProveedoresRepositorio:
    def __init__(self):
        self.encriptarAES = EncriptarAES()
    def listar(self):
        respuesta: dict = {};
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            consulta = "SELECT id_proveedor, nombre, contacto, telefono, correo FROM proveedores"
            cursor = conexion.cursor()
            cursor.execute(consulta)

            contador = 0;
            for elemento in cursor:
                lista: dict = {};                
                lista["id_proveedor"]=elemento[0];
                lista["nombre"]=elemento[1];
                lista["contacto"]=self.encriptarAES.decifrar(elemento[2]);
                lista["telefono"]=self.encriptarAES.decifrar(elemento[3]);
                lista["correo"]=self.encriptarAES.decifrar(elemento[4]);
                respuesta[str(contador)] = lista;
                contador = contador + 1; 
            
            cursor.close()
            conexion.close()
            return respuesta;
        except Exception as ex:
            print("Error al listar proveedores:", ex)
            return respuesta;

    def guardar(self, nombre, contacto, telefono, correo):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            encriptador = EncriptarAES()
            cifradoC = encriptador.cifrar(contacto)
            cifradoT = encriptador.cifrar(telefono)  
            cifradoE = encriptador.cifrar(correo)      
            consulta = "INSERT INTO proveedores (nombre, contacto, telefono, correo) VALUES (?, ?, ?, ?)"
            cursor.execute(consulta, (nombre, cifradoC, cifradoT, cifradoE))
            conexion.commit()
                      
            cursor.close()
            conexion.close()
            print("Proveedor guardado correctamente")
        except Exception as ex:
            print("Error al guardar proveedor:", ex)

    def actualizar(self, id_proveedor, nombre, contacto, telefono, correo):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            cursor.execute(
                "UPDATE proveedores SET nombre = ?, contacto = ?, telefono = ?, correo = ? WHERE id_proveedor = ?",
                (nombre, contacto, telefono, correo, id_proveedor)
            )
            conexion.commit()
            cursor.close()
            conexion.close()
            print("Proveedor actualizado correctamente")
        except Exception as ex:
            print("Error al actualizar proveedor:", ex)

    def eliminar(self, id_proveedor):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM proveedores WHERE id_proveedor = ?", (id_proveedor,))
            conexion.commit()
            cursor.close()
            conexion.close()
            print("Proveedor eliminado correctamente")
        except Exception as ex:
            print("Error al eliminar proveedor:", ex)