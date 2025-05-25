class Proveedores:
    def __init__(self, id_proveedor=None, nombre=None, contacto=None, telefono=None, correo=None):
        self.id_proveedor = id_proveedor
        self.nombre = nombre
        self.contacto = contacto
        self.telefono = telefono
        self.correo = correo

    def serialize(self):
        return {
            "id_proveedor": self.id_proveedor,
            "nombre": self.nombre,
            "contacto": self.contacto,
            "telefono": self.telefono,
            "correo": self.correo
        }