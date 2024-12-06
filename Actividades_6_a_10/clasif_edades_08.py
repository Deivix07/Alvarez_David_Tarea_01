import tkinter as tk      #Importar la biblioteca tkinter para la interfaz gráfica

#Solicita una edad y clasifica al usuario como 
#niño (0-12), adolescente (13-17) o adulto (18+)
def clasi_edad():
    def clasif_edad():    #Función determinar a que grupo corresponde
        try:
            age = int(entrada_age.get())  #Obtener el edad del campo de entrada
            if age < 0:  # Validar que la edad sea mayor a 0
                mensaje = "Por favor, ingrese una edad válida (mayor a 0)."
            elif 0 <= age <= 12:
                mensaje = "Eres un niño"
            elif 13 <= age <= 17:
                mensaje = "Eres un adolescente"
            else:
                mensaje = "Eres un adulto"
        except ValueError:
            mensaje = "Por favor, ingrese una edad válida"
        
        #Mostrar mensaje de resultado en la ventana
        resultado.config(text=mensaje)

    #Ventana clasificación edades
    ventana_clasif_edades = tk.Toplevel()
    ventana_clasif_edades.title("Actividad 8")
    ventana_clasif_edades.geometry("501x300")

    #Intrucciones
    actividad = tk.Label(ventana_clasif_edades, text="Determine a que grupo de edad pertenece", font=("Arial", 12 ,"bold"))
    actividad.pack(pady=10)
    
    etiqueta_instrucciones = tk.Label(ventana_clasif_edades, text="Ingrese su edad: ", font=("Arial", 12))
    etiqueta_instrucciones.pack(pady=10)

    #Entrada para la edad
    entrada_age = tk.Entry(ventana_clasif_edades, font=("Arial", 12))
    entrada_age.pack(pady=10)

    #Botón verificar edad
    boton_verificar = tk.Button(ventana_clasif_edades, text="Verificar", command=clasif_edad)
    boton_verificar.pack(pady=10)

    #Mostrar el resultado
    resultado = tk.Label(ventana_clasif_edades, text="", font=("Arial", 12))
    resultado.pack(pady=20)

    #Botón cerrar la ventana
    boton_cerrar = tk.Button(ventana_clasif_edades, text="Cerrar", command=ventana_clasif_edades.destroy)
    boton_cerrar.pack(pady=10)