import tkinter as tk      #Importar la biblioteca tkinter para la interfaz gráfica

#Solicita dos números y una operación (+, -, *, /) y realiza el cálculo correspondiente
def calculadora():
    def calc():    #Función realizar el cálculo según la operación
        try:
            num_1 = float(num1.get())  #Obtener num del campo de entrada
            num_2 = float(num2.get())
            operacion = (op.get())
            if operacion == "+":
                result = num_1 + num_2
                mensaje = (f"La suma de {num_1} + {num_2} es: {result}")
            elif operacion == "-":
                result = num_1 - num_2
                mensaje = (f"La resta de {num_1} - {num_2} es: {result}")
            elif operacion == "*":
                result = num_1 * num_2
                mensaje = (f"La multiplicación {num_1} * {num_2} es: {result}")
            elif operacion == "/":
                if num_2 != 0:
                    result = num_1 / num_2
                    mensaje = (f"La división de {num_1} / {num_2} es: {result}")
                else:
                    mensaje = "No se puede dividir entre 0"
            else:
                mensaje = "Operación no válida"
        except ValueError:
            mensaje = "Por favor, ingrese un número válido."
        
        #Mostrar mensaje de resultado en la ventana
        resultado.config(text=mensaje)

    #Ventana calculadora
    ventana_calc = tk.Toplevel()
    ventana_calc.title("Actividad 9")
    ventana_calc.geometry("550x350")

    #Intrucciones
    actividad = tk.Label(ventana_calc, text="Calculadora básica", font=("Arial", 12 ,"bold"))
    actividad.pack(pady=10)
    
    #Frame para intrucciones
    instrucciones = tk.Frame(ventana_calc)
    instrucciones.pack(pady=10)
    
    isnt_1 = tk.Label(instrucciones, text="Ingrese primer número", font=("Arial", 12))
    isnt_1.pack(side="left", padx=5)
    
    isnt_2 = tk.Label(instrucciones, text="Ingrese la operación\n ( + , - , * , / )", font=("Arial", 12))
    isnt_2.pack(side="left", padx=20)
    
    isnt_3= tk.Label(instrucciones, text="Ingrese segundo número", font=("Arial", 12))
    isnt_3.pack(side="left", padx=5)

    #Frame para contener las entradas
    nums = tk.Frame(ventana_calc)
    nums.pack(pady=10)

    #Crear las entradas para los números y la operación
    num1 = tk.Entry(nums, font=("Times", 12), width=7)
    num1.pack(side="left", padx=20)
    
    op = tk.Entry(nums, font=("Times", 12), width=7)
    op.pack(side="left", padx=100)

    num2 = tk.Entry(nums, font=("Times", 12), width=7)
    num2.pack(side="left", padx=20)

    #Botón calcular
    boton_verificar = tk.Button(ventana_calc, text="Calcular", command=calc)
    boton_verificar.pack(pady=10)

    #Mostrar el resultado
    resultado = tk.Label(ventana_calc, text="", font=("Arial", 12))
    resultado.pack(pady=20)

    #Botón cerrar la ventana
    boton_cerrar = tk.Button(ventana_calc, text="Cerrar", command=ventana_calc.destroy)
    boton_cerrar.pack(pady=10)