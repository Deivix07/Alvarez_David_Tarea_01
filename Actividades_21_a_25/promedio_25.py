import tkinter as tk  # Importar la biblioteca tkinter para la interfaz gráfica

# Solicita calificaciones al usuario y calcula el promedio.
def promedio_estudiante():
    
    calificaciones = []  #Lista para almacenar las calificaciones ingresadas

    def agregar_calificacion():
        try:
            calif = float(entrada_calif.get().strip())  #Obtener la calificación del campo de entrada

            if calif >= 0:  #Verificar que la calificación sea válida
                if calif <= 10:   #Verificar que la calificación sea menor que 10
                    calificaciones.append(calif)  #Agregar la calificación a la lista
                    mensaje = f"Calificación {calif} agregada"
                else:
                    mensaje = f"Por favor, ingrese una calificación menor a 10"
            else:
                mensaje = "Por favor, ingrese una calificación positiva"

        except ValueError:
            mensaje = "Por favor, ingrese una calificación válida"

        #Mostrar mensaje de resultado en la ventana
        resultado.config(text=mensaje)
        entrada_calif.delete(0, tk.END)  #Limpiar el campo de entrada

    def imprimir_promedio():
        if calificaciones:  #Verificar que haya calificaciones ingresadas
            promedio = sum(calificaciones) / len(calificaciones)  #Calcular el promedio
            mensaje = f"Promedio final: {promedio:.2f}"
        else:
            mensaje = "No se han ingresado calificaciones"

        #Mostrar mensaje de resultado en la ventana
        resultado.config(text=mensaje)

    #Ventana calificaciones
    ventana_calificaciones = tk.Toplevel()
    ventana_calificaciones.title("Actividad 4")
    ventana_calificaciones.geometry("501x350")

    #Instrucciones
    actividad = tk.Label(ventana_calificaciones, text="Promedio Calificaciones", font=("Arial", 12, "bold"))
    actividad.pack(pady=10)

    etiqueta_instrucciones = tk.Label(ventana_calificaciones, text="Ingrese una calificación:", font=("Arial", 12))
    etiqueta_instrucciones.pack(pady=10)

    #Entrada para la calificación
    entrada_calif = tk.Entry(ventana_calificaciones, font=("Arial", 12))
    entrada_calif.pack(pady=10)

    #Botón Agregar calificación
    boton_agregar = tk.Button(ventana_calificaciones, text="Agregar Calificación", command=agregar_calificacion)
    boton_agregar.pack(pady=10)

    #Botón Imprimir Promedio
    boton_promedio = tk.Button(ventana_calificaciones, text="Imprimir Promedio", command=imprimir_promedio)
    boton_promedio.pack(pady=10)

    #Mostrar el resultado
    resultado = tk.Label(ventana_calificaciones, text="", font=("Arial", 12))
    resultado.pack(pady=20)

    #Botón cerrar la ventana
    boton_cerrar = tk.Button(ventana_calificaciones, text="Cerrar", command=ventana_calificaciones.destroy)
    boton_cerrar.pack(pady=10)