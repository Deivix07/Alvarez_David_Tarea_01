import tkinter as tk      #Importar la biblioteca tkinter para la interfaz gráfica

#Solicita tres números y determina cuál es el mayor
def mayor_num():
    def verificar_num_mayor():    #Función verificar qué número es mayor
        try:
            num_1 = float(num1.get())  #Obtener num del campo de entrada
            num_2 = float(num2.get())
            num_3 = float(num3.get())
            if num_1 >= num_2 and num_1 >= num_3:
                mensaje = (f"El número mayor es: {num_1}")
            elif num_2 >= num_1 and num_2 >= num_3:
                mensaje = (f"El número mayor es: {num_2}")
            else:
                mensaje = (f"El número mayor es: {num_3}")
        except ValueError:
            mensaje = "Por favor, ingrese un número válido."
        
        #Mostrar mensaje de resultado en la ventana
        resultado.config(text=mensaje)

    #Ventana número mayor
    ventana_num_mayor = tk.Toplevel()
    ventana_num_mayor.title("Actividad 7")
    ventana_num_mayor.geometry("501x300")

    #Intrucciones
    actividad = tk.Label(ventana_num_mayor, text="Determine cúal es el número mayor", font=("Arial", 12 ,"bold"))
    actividad.pack(pady=10)
    
    etiqueta_instrucciones = tk.Label(ventana_num_mayor, text="Ingrese tres números: ", font=("Arial", 12))
    etiqueta_instrucciones.pack(pady=10)

    #Frame para contener las entradas
    nums = tk.Frame(ventana_num_mayor)
    nums.pack(pady=10)

    #Crear las entradas para los númeors
    num1 = tk.Entry(nums, font=("Times", 12), width=7)
    num1.pack(side="left", padx=5)

    num2 = tk.Entry(nums, font=("Times", 12), width=7)
    num2.pack(side="left", padx=5)

    num3 = tk.Entry(nums, font=("Times", 12), width=7)
    num3.pack(side="left", padx=5)

    #Botón verificar cual es mayor
    boton_verificar = tk.Button(ventana_num_mayor, text="Verificar", command=verificar_num_mayor)
    boton_verificar.pack(pady=10)

    #Mostrar el resultado
    resultado = tk.Label(ventana_num_mayor, text="", font=("Arial", 12))
    resultado.pack(pady=20)

    #Botón cerrar la ventana
    boton_cerrar = tk.Button(ventana_num_mayor, text="Cerrar", command=ventana_num_mayor.destroy)
    boton_cerrar.pack(pady=10)