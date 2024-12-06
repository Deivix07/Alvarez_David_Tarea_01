import tkinter as tk      #Importar la biblioteca tkinter para la interfaz gráfica

#Programa que solicite un número y determine si es mayor o menor que 10
def mayor_menor():
    def verificar_numero():    #Función verificar número
        try:
            num = float(entrada_numero.get())  #Obtener el número del campo de entrada
            if num == 10:
                mensaje = "El número ingresado es igual a 10"
            elif num> 10:
                mensaje = "El número ingresado es mayor que 10"
            else:
                mensaje = "El número ingresado es menor que 10"
        except ValueError:
            mensaje = "Por favor, ingrese un número válido."
        
        #Mostrar mensaje de resultado en la ventana
        resultado.config(text=mensaje)

    #Ventana mayor o menor
    ventana_mayor_menor = tk.Toplevel()
    ventana_mayor_menor.title("Actividad 1")
    ventana_mayor_menor.geometry("501x300")

    #Intrucciones
    actividad = tk.Label(ventana_mayor_menor, text="Determine si el número es mayor o menor que 10", font=("Arial", 12 ,"bold"))
    actividad.pack(pady=10)
    
    etiqueta_instrucciones = tk.Label(ventana_mayor_menor, text="Ingrese un número:", font=("Arial", 12))
    etiqueta_instrucciones.pack(pady=10)

    #Entrada para el número
    entrada_numero = tk.Entry(ventana_mayor_menor, font=("Arial", 12))
    entrada_numero.pack(pady=10)

    #Botón verificar el número
    boton_verificar = tk.Button(ventana_mayor_menor, text="Verificar", command=verificar_numero)
    boton_verificar.pack(pady=10)

    #Mostrar el resultado
    resultado = tk.Label(ventana_mayor_menor, text="", font=("Arial", 12))
    resultado.pack(pady=20)

    #Botón cerrar la ventana
    boton_cerrar = tk.Button(ventana_mayor_menor, text="Cerrar", command=ventana_mayor_menor.destroy)
    boton_cerrar.pack(pady=10)