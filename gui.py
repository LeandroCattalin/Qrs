import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox

#Crear la ventana principal
def iniciar_interfaz(callback_guardar):
    ventana = tk.Tk()
    ventana.title("Aplicación")
    ventana.geometry("1280x768")

    #Label título
    labelTitulo= tk.Label(ventana, text="INGRESE LOS DATOS DE LA PERSONA PARA GENERAR QR", font=("Arial", 24))
    labelTitulo.pack(padx=10, pady=10)

    #Label apellidoNombre
    entry1= tk.Entry(ventana, fg="grey", width=70)
    entry1.insert(0, "Ingrese apellido y nombre: ")
    entry1.pack(padx=10, pady=10, anchor="w")

    #Label legajo
    entry2= tk.Entry(ventana, fg="grey", width=70)
    entry2.insert(0, "Ingrese numero de legajo: ")
    entry2.pack(padx=10,pady=10,anchor="w")

    # Etiqueta para el error o mensaje
    mensaje = tk.Label(ventana, text="", fg="red")  # Texto en rojo para mostrar el error
    mensaje.pack(padx=10, pady=10, anchor="w")

    #Listbox para elegir charla
    labelListbox = tk.Label(ventana, text="Ingrese la charla a la que se desea inscribir")
    labelListbox.pack(padx=10, pady=10, anchor="w")

    opciones = ['19:30 Ciberseguridad', '18:00 Metodologias Agiles', '21:00 YPF']
    combobox1 = ttk.Combobox(ventana, values=opciones, width=70)
    combobox1.pack(padx=10,pady=10, anchor="w")


    #Funciones para manejar el placeholder del entry1
    def on_entry_click(event):
        if entry1.get() == "Ingrese apellido y nombre: ": #Si el usuario hizo click en el label y esta el texto por defecto
            entry1.delete(0,"end") #Eliminar el texto
            entry1.config(fg="black") #Cambiar el color del texto a negro

    def on_focusout(event):
        if entry1.get() == '': #Si el usuario saco de foco el entry y sigue vacio
            entry1.insert(0, 'Ingrese apellido y nombre: ') #Ingresa texto en el entry
            entry1.config(fg="grey") #Cambia el color a gris
    
    entry1.bind('<FocusIn>', on_entry_click)
    entry1.bind('<FocusOut>', on_focusout)

    #Funciones para manejar el placeholder del entry2
    def on_entry2_click(event):
        if entry2.get() == "Ingrese numero de legajo: ": #Si el usuario hizo click en el label y esta el texto por defecto
            entry2.delete(0,"end") #Eliminar el texto
            entry2.config(fg="black") #Cambiar el color del texto a negro

    def on_entry2_focusout(event):
        if entry2.get() == '': #Si el usuario saco de foco el entry y sigue vacio
            entry2.insert(0, 'Ingrese numero de legajo: ') #Ingresa texto en el entry
            entry2.config(fg="grey") #Cambia el color a gris

    entry2.bind('<FocusIn>', on_entry2_click)
    entry2.bind('<FocusOut>', on_entry2_focusout)

    #Función para obtener valores de los controles
    def guardar_valores():
        if combobox1.get() == '19:30 Ciberseguridad':
            charla = 1
        if combobox1.get() == '18:00 Metodologias Agiles':
            charla = 2
        if combobox1.get() == '21:00 YPF':
            charla = 3
        

        datos = {
            "apellidoNombre" : entry1.get(),
            "legajo" : entry2.get(),
            "charlaN" : charla,
            "fecha" : datetime.now()
        }
        callback_guardar(datos)
        messagebox.showinfo("Exito", "Se inscribió a la charla correctamente")

    boton= tk.Button(ventana, text="Guardar", command=guardar_valores)
    boton.pack(padx=10,pady=10, anchor="w")

    #Mantener la ventana abierta
    ventana.mainloop()