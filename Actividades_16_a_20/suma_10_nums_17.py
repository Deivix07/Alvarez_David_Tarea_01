import tkinter as tk      #Importar la biblioteca tkinter para la interfaz gráfica

#Calcula y muestra la suma de los números del 1 al 10
def suma_nums():
    def sum():    #Función sumar números
        try:
            num_1 = int(num1.get())  #Obtener num del campo de entrada
            num_2 = int(num2.get())
            
            suma = 0        #inicializar la variable suma en 0
            
            for i in range(num_1,num_2+1):          #Calcular la suma del rango
                suma += i
                mensaje = (f"La suma de los números del {num_1} al {num_2} es: {suma}")
                
        except ValueError:
            mensaje = "Por favor, ingrese un número válido."
        
        #Mostrar mensaje de resultado en la ventana
        resultado.config(text=mensaje)

    #Ventana sumar números
    ventana_sum = tk.Toplevel()
    ventana_sum.title("Actividad 17")
    ventana_sum.geometry("550x350")

    #Intrucciones
    actividad = tk.Label(ventana_sum, text="Suma de Números Consecutivos", font=("Arial", 12 ,"bold"))
    actividad.pack(pady=10)
    
    #Frame para intrucciones
    instrucciones = tk.Frame(ventana_sum)
    instrucciones.pack(pady=10)
    
    isnt_1 = tk.Label(instrucciones, text="Ingrese primer número", font=("Arial", 12))
    isnt_1.pack(side="left", padx=10)
    
    isnt_2= tk.Label(instrucciones, text="Ingrese segundo número", font=("Arial", 12))
    isnt_2.pack(side="left", padx=10)

    #Frame para contener las entradas
    nums = tk.Frame(ventana_sum)
    nums.pack(pady=10)

    #Crear las entradas para los números
    num1 = tk.Entry(nums, font=("Times", 12), width=7)
    num1.pack(side="left", padx=60)
  
    isnt_3 = tk.Label(nums, text="al", font=("Arial", 12, "bold"))
    isnt_3.pack(side="left", padx=10)
    
    #Crear las entradas para los números
    num2 = tk.Entry(nums, font=("Times", 12), width=7)
    num2.pack(side="left", padx=60)

    #Botón Imprimir suma
    boton_imp = tk.Button(ventana_sum, text="Imprimir Suma", command=sum)
    boton_imp.pack(pady=10)

    #Mostrar el resultado
    resultado = tk.Label(ventana_sum, text="", font=("Arial", 12))
    resultado.pack(pady=20)

    #Botón cerrar la ventana
    boton_cerrar = tk.Button(ventana_sum, text="Cerrar", command=ventana_sum.destroy)
    boton_cerrar.pack(pady=10)