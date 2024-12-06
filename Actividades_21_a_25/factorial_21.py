import tkinter as tk      #Importar la biblioteca tkinter para la interfaz gráfica

#Calcula el factorial de un número ingresado por el usuario (n!).
def factorial():
    def fact():    #Función para factorial
        try:
            num_1 = int(num1.get())  #Obtener num del campo de entrada
            
            factorial = 1        #inicializar la variable factorial en 1
            
            for i in range(1,num_1+1):        #usar bucle for con rango de 1 hasta el numero ingresado
                factorial *= i                #realizar la operacion para factorial

            mensaje = (f"El factorial de {num_1}! es: {factorial}")
                
        except ValueError:
            mensaje = "Por favor, ingrese un número válido."
        
        #Mostrar mensaje de resultado en la ventana
        resultado.config(text=mensaje)

    #Ventana factorial
    ventana_factorial = tk.Toplevel()
    ventana_factorial.title("Actividad 21")
    ventana_factorial.geometry("550x350")

    #Intrucciones
    actividad = tk.Label(ventana_factorial, text="Factorial de un número", font=("Arial", 12 ,"bold"))
    actividad.pack(pady=10)
    
    #Frame para intrucciones
    instrucciones = tk.Frame(ventana_factorial)
    instrucciones.pack(pady=10)
    
    isnt_1 = tk.Label(instrucciones, text="Introduzca el número del cual quiere el factorial:", font=("Arial", 12))
    isnt_1.pack(side="left", padx=10)

    #Frame para contener las entradas
    nums = tk.Frame(ventana_factorial)
    nums.pack(pady=10)

    #Crear entradas para el número
    num1 = tk.Entry(nums, font=("Times", 12), width=7)
    num1.pack(side="left", padx=60)
  
    #Botón Imprimir suma
    boton_imp = tk.Button(ventana_factorial, text="Imprimir Factorial", command=fact)
    boton_imp.pack(pady=10)

    #Mostrar el resultado
    resultado = tk.Label(ventana_factorial, text="", font=("Arial", 12))
    resultado.pack(pady=20)

    #Botón cerrar la ventana
    boton_cerrar = tk.Button(ventana_factorial, text="Cerrar", command=ventana_factorial.destroy)
    boton_cerrar.pack(pady=10)