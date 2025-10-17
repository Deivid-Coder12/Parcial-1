from biblioteca import Biblioteca
from usuario import Usuario
from firebase_config import db

class Menu:
    def __init__(self):
        self.biblioteca = Biblioteca()

    def mostrar_menu(self):
        print("Ingrese el número según la opción:")
        print("1. Agregar libro de acción")
        print("2. Agregar libro de romance")
        print("3. Agregar libro de terror")
        print("4. Mostrar libros")
        print("5. Registrar usuario")
        print("6. Eliminar libros")
        print("7. Eliminar usuarios")
        print("8. Leer todos los usuarios")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            libro = input("Ingrese el nombre del libro de Acción: ")
            self.biblioteca.agregar_libro(libro, "accion")

        elif opcion == 2:
            libro = input("Ingrese el nombre del libro de Romance: ")
            self.biblioteca.agregar_libro(libro, "romance")

        elif opcion == 3:
            libro = input("Ingrese el nombre del libro de Terror: ")
            self.biblioteca.agregar_libro(libro, "terror")

        elif opcion == 4:
            self.biblioteca.leer_libros()
            print("Libros de Acción:", self.biblioteca.libros_accion)
            print("Libros de Romance:", self.biblioteca.libros_romance)
            print("Libros de Terror:", self.biblioteca.libros_terror)

        elif opcion == 5:
            nombre = input("Ingrese su nombre: ")
            cedula = input("Ingrese su cédula: ")
            usuario = Usuario(nombre, cedula)
            usuario.mostrar_info()
            db.reference("usuarios").push({"nombre": nombre, "cedula": cedula})

        elif opcion == 6:
            self.biblioteca.eliminar_libros()

        elif opcion == 7:
            usuario = Usuario("", "")
            usuario.eliminar_usuarios()

        elif opcion == 8:
            usuario = Usuario("", "")
            usuario.leer_usuarios()

        else:
            print("Opción no válida.")