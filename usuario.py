from firebase_config import db

class Usuario:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def eliminar_usuarios(self):#elimina todos los usuarios
        db.reference("usuarios").delete()
        print("Todos los usuarios han sido eliminados.")

    def leer_usuarios(self):
        usuarios = db.reference("usuarios").get() or {}#manda el comando para obtener la informacion
        for key, usuario in usuarios.items():#recorre toda la lista obteniendo toda la info
            print(f"Nombre: {usuario['nombre']}, Cédula: {usuario['cedula']}")# imprime la informacion

def actualizar_usuario(self):
    usuarios = db.reference("usuarios").get() or {}

    if not usuarios:
        print("No hay usuarios registrados.")
        return

    print("\nUsuarios actuales:")#basicamente hace lo mismo que la funcion leer
    for key, usuario in usuarios.items():
        print(f"{key}: {usuario['nombre']} - {usuario['cedula']}")

    id_usuario = input("\nIngrese el ID del usuario que desea actualizar: ")# pide la ID que se crea automaticamente en firebase

    if id_usuario not in usuarios:# si no se encuentra la ID, printea el mensaje
        print("No se encontró el ID especificado.")
        return

    nuevo_nombre = input("Ingrese el nuevo nombre (deje vacío si no quiere cambiarlo): ")# Se pide el dato que se quiere actualizar
    nueva_cedula = input("Ingrese la nueva cédula (deje vacío si no quiere cambiarla): ")

    if nuevo_nombre:# condicionales que no cambian nada si se deja vacio
        usuarios[id_usuario]['nombre'] = nuevo_nombre
    if nueva_cedula:
        usuarios[id_usuario]['cedula'] = nueva_cedula

    db.reference(f"usuarios/{id_usuario}").update(usuarios[id_usuario])# se actualiza el usuario y se imprime
    print("Usuario actualizado correctamente.")
