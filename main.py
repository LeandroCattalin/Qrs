from gui import iniciar_interfaz
from database import insertar_dato_en_db

#Funcion para manejar los datos desde el GUI hasta Database
def manejar_datos(datos):
    #Se ejecuta la funcion para insertar en la base de datos con lo que sale de GUI
    insertar_dato_en_db(datos)

if __name__=="__main__":
    #Se inicia la interfaz del programa y se pasa la funcion manejar datos para la interaccion posterior con database
    iniciar_interfaz(manejar_datos)
    