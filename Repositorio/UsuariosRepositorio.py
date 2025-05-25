import pyodbc
from Entidades.Usuarios import Usuarios
from Utilidades.Configuracion import Configuracion
from Utilidades.Encriptar import EncriptarAES 

class UsuariosRepositorio:
    def __init__(self):
        self.encriptarAES = EncriptarAES() 

    def Listar(self, datos: dict) -> dict:
        respuesta: dict = {};
        try:
            conexion = pyodbc.connect(Configuracion.strConnection);
            consulta = "SELECT id_usuario, nombre, correo, contrasena, fecha_registro FROM usuarios";
            cursor = conexion.cursor();
            cursor.execute(consulta);

            contador = 0;
            for elemento in cursor:
                lista: dict = {};                
                lista["id_usuario"]=elemento[0];
                lista["nombre"]=elemento[1];
                lista["correo"]=self.encriptarAES.decifrar(elemento[2]);
                lista["contrasena"]=self.encriptarAES.decifrar(elemento[3]);
                lista["fecha_registro"]=elemento[4];
                respuesta[str(contador)] = lista;
                contador = contador + 1;
                   
            cursor.close();
            conexion.close();
            return respuesta;

        except Exception as ex:
            respuesta["Error"] = str(ex);
            return respuesta;


    def guardar(self, nombre, correo, contrasena):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            encriptador = EncriptarAES()
            cifradoE = encriptador.cifrar(correo)
            cifrado = encriptador.cifrar(contrasena)

            consulta = "INSERT INTO usuarios (nombre, correo, contrasena, fecha_registro) VALUES (?, ?, ?, ?)"
            cursor.execute(consulta, (nombre, cifradoE, cifrado,"2025-05-23"))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("✅ Usuario guardado correctamente con contraseña cifrada.")

        except Exception as ex:
            print("❌ Error al guardar usuario:", str(ex))


    def actualizar(self, id_usuario, nombre, correo):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = "UPDATE usuarios SET nombre = ?, correo = ? WHERE id_usuario = ?"
            cursor.execute(consulta, (nombre, correo, id_usuario))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("✅ Usuario actualizado correctamente.")

        except Exception as ex:
            print("❌ Error al actualizar usuario:", str(ex))

    def eliminar(self, id_usuario):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = "DELETE FROM usuarios WHERE id_usuario = ?"
            cursor.execute(consulta, (id_usuario,))
            conexion.commit()

            cursor.close()
            conexion.close()
            print("✅ Usuario eliminado correctamente.")

        except Exception as ex:
            print("❌ Error al eliminar usuario:", str(ex))

    def obtener_por_correo(self, correo):
        try:
            conexion = pyodbc.connect(Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = "SELECT id_usuario, nombre, correo, contrasena, fecha_registro FROM usuarios WHERE correo = ?"
            cursor.execute(consulta, (correo,))
            resultado = cursor.fetchone()

            if resultado:
                id_usuario, nombre, correo, contrasena, fecha_registro = resultado

                contrasena = resultado[3]

                # 🛠 Convertir a bytes si son strings
                if isinstance(contrasena, str): contrasena = bytes.fromhex(contrasena)

                print("✅ Datos correctos para descifrado:", contrasena)

                encriptador = EncriptarAES()
                contrasena_descifrada = encriptador.descifrar((contrasena))

                usuario = Usuarios(id_usuario, nombre, correo, contrasena_descifrada, fecha_registro)
                cursor.close()
                conexion.close()
                return usuario

            cursor.close()
            conexion.close()
            return None

        except Exception as ex:
            print("❌ Error al obtener usuario:", str(ex))
            return None

