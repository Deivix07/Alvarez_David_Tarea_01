import tkinter as tk      #Importar la biblioteca tkinter para la interfaz gráfica

key="Rx4832"           #inicializar la variable key con una contraseá fija

#Escribe un programa que solicite una contraseña
#y valide si es correcta (ejemplo: contraseña fija es 12345).
def passw():
    def password():    #Función validar contraseña
        try:
            password = (entrada_passw.get())  #Obtener la contraseña del campo de entrada
            if password == key:
                mensaje = "Contraseña correcta"
            else:
                mensaje = "Contraseña incorrecta"
        except ValueError:
            mensaje = "Por favor, ingrese un número válido."
        
        #Mostrar mensaje de resultado en la ventana
        resultado.config(text=mensaje)

    #Ventana contraseña
    ventana_passw = tk.Toplevel()
    ventana_passw.title("Actividad 11")
    ventana_passw.geometry("501x300")

    #Intrucciones
    actividad = tk.Label(ventana_passw, text="Validar contraseña", font=("Arial", 12 ,"bold"))
    actividad.pack(pady=10)
    
    etiqueta_instrucciones = tk.Label(ventana_passw, text="Ingrese la contraseña:", font=("Arial", 12))
    etiqueta_instrucciones.pack(pady=10)

    #Entrada para la contraseña
    entrada_passw = tk.Entry(ventana_passw, font=("Arial", 12))
    entrada_passw.pack(pady=10)

    #Botón validar contraseña
    boton_validar= tk.Button(ventana_passw, text="Validar", command=password)
    boton_validar.pack(pady=10)

    #Mostrar el resultado
    resultado = tk.Label(ventana_passw, text="", font=("Arial", 12))
    resultado.pack(pady=20)

    #Botón cerrar la ventana
    boton_cerrar = tk.Button(ventana_passw, text="Cerrar", command=ventana_passw.destroy)
    boton_cerrar.pack(pady=10)