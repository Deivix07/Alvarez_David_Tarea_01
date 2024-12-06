import tkinter as tk      #Importar la biblioteca tkinter para la interfaz gráfica

#Solicita la edad del usuario y determina si es elegible para votar (mayor o igual a 18 años)
def edad_votar():
    def verificar_edad():    #Función verificar si es elegible para votar
        try:
            age = int(entrada_numero.get())  #Obtener el edad del campo de entrada
            if age < 0:  # Validar que la edad sea mayor a 0
                mensaje = "Por favor, ingrese una edad válida (mayor a 0)."
            elif age >= 18:
                mensaje = "Mayor de edad, puedes votar"
            else:
                mensaje = "Menor de edad, no puedes votar"
        except ValueError:
            mensaje = "Por favor, ingrese una edad válido."
        
        #Mostrar mensaje de resultado en la ventana
        resultado.config(text=mensaje)

    #Ventana edad para votar
    ventana_edad_votar = tk.Toplevel()
    ventana_edad_votar.title("Actividad 6")
    ventana_edad_votar.geometry("501x300")

    #Intrucciones
    actividad = tk.Label(ventana_edad_votar, text="Determine si es elegible para votar", font=("Arial", 12 ,"bold"))
    actividad.pack(pady=10)
    
    etiqueta_instrucciones = tk.Label(ventana_edad_votar, text="Ingrese su edad: ", font=("Arial", 12))
    etiqueta_instrucciones.pack(pady=10)

    #Entrada para la edad
    entrada_numero = tk.Entry(ventana_edad_votar, font=("Arial", 12))
    entrada_numero.pack(pady=10)

    #Botón verificar edad
    boton_verificar = tk.Button(ventana_edad_votar, text="Verificar", command=verificar_edad)
    boton_verificar.pack(pady=10)

    #Mostrar el resultado
    resultado = tk.Label(ventana_edad_votar, text="", font=("Arial", 12))
    resultado.pack(pady=20)

    #Botón cerrar la ventana
    boton_cerrar = tk.Button(ventana_edad_votar, text="Cerrar", command=ventana_edad_votar.destroy)
    boton_cerrar.pack(pady=10)