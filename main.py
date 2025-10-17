from menu import Menu

def main():
    menu = Menu()
    while True:
        menu.mostrar_menu()
        continuar = input("\n¿Desea realizar otra acción? (s/n): ")
        if continuar.lower() != 's':
            print("Saliendo del programa...")
            break

if __name__ == "__main__":
    main()