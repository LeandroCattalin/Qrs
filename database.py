import pyodbc   
import json

#Leer el archivo json
with open('config.json') as f:
    config=json.load(f)

# Crear la connection string
connection_string = (
    f"DRIVER={config['database']['DRIVER']};"
    f"SERVER={config['database']['SERVER']};"
    f"DATABASE={config['database']['DATABASE']};"
    f"Trusted_Connection={config['database']['Trusted_Connection']};"
)

def insertar_dato_en_db(dato):
    qr=config['numeroQr']
    #Abro conexion
    conn=pyodbc.connect(connection_string)
    cursor=conn.cursor()
    #Defino el query
    query="INSERT INTO Qrs (numeroQr, charlaN, apellidoNombre, legajo, asistencia, fechaInscripcion) VALUES (?,?,?,?,?,?);"
    cursor.execute(query, (qr, dato["charlaN"], dato["apellidoNombre"], dato["legajo"], 0, dato["fecha"]))
    conn.commit()
    cursor.close()
    conn.close()
    config["numeroQr"]=qr+1
    with open('config.json', 'w') as archivo:
        json.dump(config, archivo, indent=4)