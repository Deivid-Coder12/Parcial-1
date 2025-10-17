from menu import Menu

def main():# ejecuta el menu en un bucle while para que podamos seguir usando el programa sin necesidad de reproducirlo una y otra vez
    menu = Menu()
    while True:
        menu.mostrar_menu()
        continuar = input("\n¿Desea realizar otra acción? (s/n): ")
        if continuar.lower() != 's':
            print("Saliendo del programa...")
            break

if __name__ == "__main__":# se inicia todo
    main()
