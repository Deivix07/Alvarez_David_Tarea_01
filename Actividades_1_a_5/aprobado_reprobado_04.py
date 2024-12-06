import tkinter as tk      #Importar la biblioteca tkinter para la interfaz gráfica

#Solicita la calificación de un estudiante y determina 
#si está aprobado (mayor o igual a 7) o reprobado
def aprobado_reprobado():
    def verificar_calif():    #Función verificar si esta aprobado o reprobado
        try:
            calif = float(entrada_calif.get())  #Obtener la calificación del campo de entrada
            if calif >= 7:
                mensaje = "Aprobado"
            else:
                mensaje = "Reprobado"
        except ValueError:
            mensaje = "Por favor, ingrese una calificación válida"
        
        #Mostrar mensaje de resultado en la ventana
        resultado.config(text=mensaje)

    #Ventana aprobado o reprobado
    ventana_aprobado_reprobado = tk.Toplevel()
    ventana_aprobado_reprobado.title("Actividad 4")
    ventana_aprobado_reprobado.geometry("501x300")

    #Intrucciones
    actividad = tk.Label(ventana_aprobado_reprobado, text="Determine si estudiante está aprobado o repobrado", font=("Arial", 12 ,"bold"))
    actividad.pack(pady=10)
    
    etiqueta_instrucciones = tk.Label(ventana_aprobado_reprobado, text="Ingrese una calificación:", font=("Arial", 12))
    etiqueta_instrucciones.pack(pady=10)

    #Entrada para la calificación
    entrada_calif = tk.Entry(ventana_aprobado_reprobado, font=("Arial", 12))
    entrada_calif.pack(pady=10)

    #Botón verificar el número
    boton_verificar = tk.Button(ventana_aprobado_reprobado, text="Verificar", command=verificar_calif)
    boton_verificar.pack(pady=10)

    #Mostrar el resultado
    resultado = tk.Label(ventana_aprobado_reprobado, text="", font=("Arial", 12))
    resultado.pack(pady=20)

    #Botón cerrar la ventana
    boton_cerrar = tk.Button(ventana_aprobado_reprobado, text="Cerrar", command=ventana_aprobado_reprobado.destroy)
    boton_cerrar.pack(pady=10)