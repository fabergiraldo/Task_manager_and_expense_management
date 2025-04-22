from Repositorio.UsuariosRepositorio import UsuariosRepositorio

# Crear instancia del repositorio
repositorio = UsuariosRepositorio()

# Guardar un usuario nuevo
#repositorio.guardar("Faber Giraldo", "faber@example.com", "14235")

# Listar usuarios
usuarios = repositorio.listar()
for u in usuarios:
    print(u)

# Actualizar usuario
#repositorio.actualizar(1, "Juan P. Gómez", "juanp@example.com")

# Eliminar usuario
#repositorio.eliminar(2)