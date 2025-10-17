import firebase_admin
from firebase_admin import credentials, db

# Cambia la ruta a donde tengas tu archivo JSON
RUTA_CREDENCIALES = 'C:/Users/HP/OneDrive/Documentos/POO/proyecto/llave base de datos/clubes_unal.json'

# Inicializar Firebase solo una vez
if not firebase_admin._apps:
    cred = credentials.Certificate(RUTA_CREDENCIALES)
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://clubes-unal-default-rtdb.firebaseio.com/'
    })

# Exportamos db para ser usado en otros módulos