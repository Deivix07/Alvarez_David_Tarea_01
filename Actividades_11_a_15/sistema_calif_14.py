import tkinter as tk      #Importar la biblioteca tkinter para la interfaz gráfica

#Solicita una calificación numérica y devuelve la letra correspondiente:
	#90-100: A.
	#80-89: B.
	#70-79: C.
	#60-69: D.
	#Menor a 60: F.
def calificacion():
    def calif_num():    #Función calificación para devolver letras
        try:
            calif = float(entrada_calif.get())  #Obtener la calificación del campo de entrada
            if 90 <= calif <=100:
                mensaje = "Tu calificación es: A"
            elif 80 <= calif < 90:
                mensaje = "Tu calificación es: B"
            elif 70 <= calif < 80:
                mensaje = "Tu calificación es: C"
            elif 60 <= calif < 70:
                mensaje = "Tu calificación es: D"
            else:
                mensaje = "Tu calificación es: F"
        except ValueError:
            mensaje = "Por favor, ingrese una calificación válida"
        
        #Mostrar mensaje de resultado en la ventana
        resultado.config(text=mensaje)

    #Ventana calificacion
    ventana_calif = tk.Toplevel()
    ventana_calif.title("Actividad 14")
    ventana_calif.geometry("501x400")

    #Intrucciones
    actividad = tk.Label(ventana_calif, text="Determine Calificación del Estudiante\n#90-100: A\n80-89: B\n70-79: C\n60-69: D\n< 60: F", font=("Arial", 12 ,"bold"))
    actividad.pack(pady=10)
    
    etiqueta_instrucciones = tk.Label(ventana_calif, text="Ingrese una calificación:", font=("Arial", 12))
    etiqueta_instrucciones.pack(pady=10)

    #Entrada para la calificación
    entrada_calif = tk.Entry(ventana_calif, font=("Arial", 12))
    entrada_calif.pack(pady=10)

    #Botón calificación
    boton_verificar = tk.Button(ventana_calif, text="Calificación", command=calif_num)
    boton_verificar.pack(pady=10)

    #Mostrar el resultado
    resultado = tk.Label(ventana_calif, text="", font=("Arial", 12))
    resultado.pack(pady=20)

    #Botón cerrar la ventana
    boton_cerrar = tk.Button(ventana_calif, text="Cerrar", command=ventana_calif.destroy)
    boton_cerrar.pack(pady=10)