from classes import Database
import json

#Leer el archivo json
try:
    with open('config.json') as f:
        config=json.load(f)
except FileNotFoundError:
    print("Saliendo, No se entro al archivo de configuración")
    exit()
except PermissionError:
    print("Saliendo, faltan permisos de lectura en la carpeta")
    exit()
except json.JSONDecodeError:
    print("Saliendo, el formato del archivo de configuración es incorrecto")
    exit()
    
# Crear la connection string
connection_string = (
    f"DRIVER={config['database']['DRIVER']};"
    f"SERVER={config['database']['SERVER']};"
    f"DATABASE={config['database']['DATABASE']};"
    f"Trusted_Connection={config['database']['Trusted_Connection']};"
)

def obtener_database() -> Database:
    return Database(connection_string)
