import pyodbc
from Entidades.Categorias import Categorias
from Utilidades.Configuracion import Configuracion
from Utilidades.Encriptar import EncriptarAES 

class CategoriasRepositorio:
    def __init__(self):
        self.encriptarAES = EncriptarAES() 
    def listar(self):
        respuesta: dict = {};
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            consulta = "SELECT id_categoria, nombre, descripcion FROM categorias"
            cursor = conexion.cursor()
            cursor.execute(consulta)

            contador = 0;
            for elemento in cursor:
                lista: dict = {};                
                lista["id_categoria"]=elemento[0];
                lista["nombre"]=elemento[1];
                lista["descripcion"]=self.encriptarAES.decifrar(elemento[2]);
                respuesta[str(contador)] = lista;
                contador = contador + 1;  

            cursor.close()
            conexion.close()

            return respuesta;

        except Exception as ex:
            print("Error al listar categorías:", str(ex))
            return respuesta;

    def guardar(self, nombre, descripcion):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            encriptador = EncriptarAES()
            cifrado = encriptador.cifrar(descripcion)

            consulta = "INSERT INTO categorias (nombre, descripcion) VALUES (?, ?)"
            cursor.execute(consulta, (nombre, cifrado))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Categoría guardada correctamente")

        except Exception as ex:
            print("Error al guardar categoría:", str(ex))

    def actualizar(self, id_categoria, nombre, descripcion):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = "UPDATE categorias SET nombre = ?, descripcion = ? WHERE id_categoria = ?"
            cursor.execute(consulta, (nombre, descripcion, id_categoria))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Categoría actualizada correctamente")

        except Exception as ex:
            print("Error al actualizar categoría:", str(ex))

    def eliminar(self, id_categoria):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = "DELETE FROM categorias WHERE id_categoria = ?"
            cursor.execute(consulta, (id_categoria,))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Categoría eliminada correctamente")

        except Exception as ex:
            print("Error al eliminar categoría:", str(ex)) 