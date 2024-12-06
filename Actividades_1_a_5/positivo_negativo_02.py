import tkinter as tk      #Importar la biblioteca tkinter para la interfaz gráfica

#Programa que solicite un número y determine si es positivo, negativo o cero
def positivo_negativo():
    def verificar_numero():    #Función verificar número si es positivo, negativo o cero
        try:
            num = float(entrada_numero.get())  #Obtener el número del campo de entrada
            if num == 0:
                mensaje = "El número ingresado es cero"
            elif num > 0:
                mensaje = "El número ingresado es positivo"
            else:
                mensaje = "El número ingresado es negativo"
        except ValueError:
            mensaje = "Por favor, ingrese un número válido."
        
        #Mostrar mensaje de resultado en la ventana
        resultado.config(text=mensaje)

    #Ventana mayor o menor
    ventana_positivo_negativo = tk.Toplevel()
    ventana_positivo_negativo.title("Actividad 2")
    ventana_positivo_negativo.geometry("501x300")

    #Intrucciones
    actividad = tk.Label(ventana_positivo_negativo, text="Determine si el número es positivo, negativo o cero", font=("Arial", 12 ,"bold"))
    actividad.pack(pady=10)
    
    etiqueta_instrucciones = tk.Label(ventana_positivo_negativo, text="Ingrese un número:", font=("Arial", 12))
    etiqueta_instrucciones.pack(pady=10)

    #Entrada para el número
    entrada_numero = tk.Entry(ventana_positivo_negativo, font=("Arial", 12))
    entrada_numero.pack(pady=10)

    #Botón verificar el número
    boton_verificar = tk.Button(ventana_positivo_negativo, text="Verificar", command=verificar_numero)
    boton_verificar.pack(pady=10)

    #Mostrar el resultado
    resultado = tk.Label(ventana_positivo_negativo, text="", font=("Arial", 12))
    resultado.pack(pady=20)

    #Botón cerrar la ventana
    boton_cerrar = tk.Button(ventana_positivo_negativo, text="Cerrar", command=ventana_positivo_negativo.destroy)
    boton_cerrar.pack(pady=10)