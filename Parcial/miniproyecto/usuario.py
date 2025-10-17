from firebase_config import db

class Usuario:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def mostrar_info(self):
        print("Nombre:", self.nombre)
        print("Cédula:", self.cedula)

    def eliminar_usuarios(self):
        db.reference("usuarios").delete()
        print("Todos los usuarios han sido eliminados.")

    def leer_usuarios(self):
        usuarios = db.reference("usuarios").get() or {}
        for key, usuario in usuarios.items():
            print(f"Nombre: {usuario['nombre']}, Cédula: {usuario['cedula']}")