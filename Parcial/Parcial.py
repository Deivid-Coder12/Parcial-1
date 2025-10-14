class Biblioteca:
    def __init__(self):
        #Inicializa listas para cada categoría de libros
        self.libros_accion = []
        self.libros_romance = []
        self.libros_terror = []

    # Funcion para agregar libros a una categoría específica
    def agregar_libro(self, nombre, categoria):
        if categoria == "accion":
            self.libros_accion.append(nombre)
        elif categoria == "romance":
            self.libros_romance.append(nombre)
        elif categoria == "terror":
            self.libros_terror.append(nombre)
        else:
            print("Categoría no válida. Debe ser 'accion', 'romance' o 'terror'.")
    #Funcion que se usa para mostrar los libros agregados
    def mostrar_libros(self):
        print("Libros de Acción:", self.libros_accion)
        print("Libros de Romance:", self.libros_romance)
        print("Libros de Terror:", self.libros_terror)


class Usuario:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
    #Muestra la informacion agregada
    def mostrar_info(self):
        print("Nombre:", self.nombre)
        print("Cédula:", self.cedula)

def main():
    biblioteca = Biblioteca()
    #Menu para agregar libros
    print("Ingrese el número según el libro que quiera agregar:")
    print("1 para acción, 2 para romance, 3 para terror")
    opcion = int(input())

    if opcion == 1:
        libro = input("Ingrese el nombre del libro de Acción: ")
        biblioteca.agregar_libro(libro, "accion")
    elif opcion == 2:
        libro = input("Ingrese el nombre del libro de Romance: ")
        biblioteca.agregar_libro(libro, "romance")
    elif opcion == 3:
        libro = input("Ingrese el nombre del libro de Terror: ")
        biblioteca.agregar_libro(libro, "terror")
    else:
        print("Opción no válida.")
    #Pide los datos
    nombre = input("Ingrese su nombre: ")
    cedula = input("Ingrese su cédula: ")
    usuario = Usuario(nombre, cedula)
    usuario.mostrar_info()

   #Muestra  liberos agregados
    biblioteca.mostrar_libros()




#ejecuta el menu 
if __name__ == "__main__":
    main()

    if a==2:
        a=(input("ingrese el nombre del libro"))
        print(a)   

    
