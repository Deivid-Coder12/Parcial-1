class Biblioteca:
    def __init__(self):#constructor
        self.librosAccion=[]
        self.librosRomance=[]
        self.librosTerror=[]

    @property#funcion para leer la lista de librosAccion
    def librosAccion(self):
        return self.librosAccion
    
    @property#funcion para leer la lista de librosAccion
    def librosRomance(self):
        return self.librosRomance
    
    @property#funcion para leer la lista de librosAccion
    def librosTerror(self):
        return self.librosTerror

    def agregar(self, x):#Metodo para agregar libros
        return self.librosAccion.append(x)

    
b=Biblioteca()

Biblioteca().add("pez")




class Usuario:
    def __init__(self, nombre, cedula ):#Constructor
        self.nombre=nombre
        self.cedula=cedula
        self.usuario=[]#Lista en la que se agregan a los usuarios


    def agregarUsuario(self):#Metodo para agregar al usuario a una lista
        pass

a=Usuario(input("ingrse su nombre"), input("ingrese su cedula"))

print(a.nombre)
print(a.cedula)


class main:
    print("ingrese el numero segun el libro que quiera agregar:")
    a=int(input("1 para accion, 2 para romance, 3 para terror"))
    if a==1:
        a=(input("ingrese el nombre del libro"))
        print(a)

    if a==2:
        a=(input("ingrese el nombre del libro"))
        print(a)   
    