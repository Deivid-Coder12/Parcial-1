from firebase_config import db

class Biblioteca:
    def __init__(self):
        self.libros_accion = []
        self.libros_romance = []
        self.libros_terror = []

    def agregar_libro(self, nombre, categoria):
        if categoria == "accion":
            self.libros_accion.append(nombre)
            db.reference("libros/accion").push(nombre)
        elif categoria == "romance":
            self.libros_romance.append(nombre)
            db.reference("libros/romance").push(nombre)
        elif categoria == "terror":
            self.libros_terror.append(nombre)
            db.reference("libros/terror").push(nombre)
        else:
            print("Categoría no válida. Debe ser 'accion', 'romance' o 'terror'.")

    def eliminar_libros(self):
        print("Escoja la categoría de libros que desea eliminar: c = acción, r = romance, t = terror, a = todos")
        categoria = input()
        if categoria == "c":
            self.libros_accion.clear()
            db.reference("libros/accion").delete()
            print("Libros de acción eliminados.")
        elif categoria == "r":
            self.libros_romance.clear()
            db.reference("libros/romance").delete()
            print("Libros de romance eliminados.")
        elif categoria == "t":
            self.libros_terror.clear()
            db.reference("libros/terror").delete()
            print("Libros de terror eliminados.")
        elif categoria == "a":
            self.libros_accion.clear()
            self.libros_romance.clear()
            self.libros_terror.clear()
            db.reference("libros").delete()
            print("Todos los libros han sido eliminados.")

    def leer_libros(self):
        libros_accion = db.reference("libros/accion").get() or []
        libros_romance = db.reference("libros/romance").get() or []
        libros_terror = db.reference("libros/terror").get() or []

        self.libros_accion = list(libros_accion.values()) if isinstance(libros_accion, dict) else libros_accion
        self.libros_romance = list(libros_romance.values()) if isinstance(libros_romance, dict) else libros_romance
        self.libros_terror = list(libros_terror.values()) if isinstance(libros_terror, dict) else libros_terror