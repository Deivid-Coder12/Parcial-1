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

def actualizar_usuario(self):
    usuarios = db.reference("usuarios").get() or {}

    if not usuarios:
        print("No hay usuarios registrados.")
        return

    print("\nUsuarios actuales:")
    for key, usuario in usuarios.items():
        print(f"{key}: {usuario['nombre']} - {usuario['cedula']}")

    id_usuario = input("\nIngrese el ID del usuario que desea actualizar: ")

    if id_usuario not in usuarios:
        print("No se encontró el ID especificado.")
        return

    nuevo_nombre = input("Ingrese el nuevo nombre (deje vacío si no quiere cambiarlo): ")
    nueva_cedula = input("Ingrese la nueva cédula (deje vacío si no quiere cambiarla): ")

    if nuevo_nombre:
        usuarios[id_usuario]['nombre'] = nuevo_nombre
    if nueva_cedula:
        usuarios[id_usuario]['cedula'] = nueva_cedula

    db.reference(f"usuarios/{id_usuario}").update(usuarios[id_usuario])
    print("Usuario actualizado correctamente.")