📚 Proyecto Biblioteca con Firebase 

Un sistema de gestión de libros y usuarios que se conecta a Firebase Realtime Database, desarrollado en Python utilizando Programación Orientada a Objetos (POO).

Permite registrar libros por categoría, eliminar o leer registros y manejar usuarios de forma dinámica, todo desde consola.

✨ Características principales

Conexión directa con Firebase Realtime Database

Estructura modular con clases separadas (Biblioteca, Usuario, Menu)

Funciones CRUD básicas (crear, leer, eliminar)

Interfaz de texto interactiva para el usuario

Diseño limpio y escalable, ideal para aprendizaje en POO

Estructura del proyecto
proyecto_biblioteca/
│
├── main.py                # Archivo principal que ejecuta el programa
├── menu.py                # Contiene la clase Menu con la lógica del menú principal
├── biblioteca.py          # Contiene la clase Biblioteca (gestión de libros)
├── usuario.py             # Contiene la clase Usuario (gestión de usuarios)
├── firebase_config.py     # Inicializa y conecta el proyecto con Firebase
└── README.md              # Este archivo 😊

Clases principales
📘 Biblioteca

Maneja la colección de libros divididos en tres categorías:

Acción 

Romance 

Terror 

Funciones principales:

agregar_libro(nombre, categoria) → Agrega un libro a la base de datos

eliminar_libros() → Elimina libros por categoría o todos

leer_libros() → Carga los libros desde Firebase

actualizar_libros -> actualiza un libro especifico
👤 Usuario

Administra los usuarios registrados en la biblioteca.

Funciones principales:

mostrar_info() → Muestra los datos del usuario actual

eliminar_usuarios() → Elimina todos los usuarios de Firebase

leer_usuarios() → Lista todos los usuarios registrados

actualizar_usuario _> actualiza un usuario en especifico

🧾 Menu

Clase encargada de interactuar con el usuario mediante consola.

Opciones disponibles:

Agregar libro de acción

Agregar libro de romance

Agregar libro de terror

Mostrar todos los libros

Registrar usuario

Eliminar libros

Eliminar usuarios

Leer todos los usuarios

🔥 Configuración de Firebase

Crea un proyecto en Firebase Console
.

Agrega una Realtime Database y selecciona modo de prueba.

Descarga el archivo .json de tu clave privada (credenciales).

Coloca el archivo en una ruta segura y actualiza su ubicación en firebase_config.py:

RUTA_CREDENCIALES = 'C:/ruta/a/tu/archivo/.json'


Verifica que la URL de la base de datos sea la correcta:

'databaseURL': 'https://tu-proyecto-default-rtdb.firebaseio.com/'

⚙️ Ejecución del proyecto

Abre la terminal en la carpeta del proyecto.

Asegúrate de tener instaladas las dependencias:

pip install firebase-admin


Ejecuta el programa:

python main.py


Interactúa con el menú desde la consola 

💡 Ejemplo de uso
Ingrese el número según la opción:
1. Agregar libro de acción
2. Agregar libro de romance
3. Agregar libro de terror
4. Mostrar libros
5. Registrar usuario
6. Eliminar libros
7. Eliminar usuarios
8. Leer todos los usuarios

Seleccione una opción: 1
Ingrese el nombre del libro de Acción: Misión Imposible
✅ Libro agregado correctamente.
