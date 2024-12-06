import tkinter as tk      #Importar la biblioteca tkinter para la interfaz gráfica

#Imprime todos los números pares entre 1 y 20
def pares():
    def par():    #Función verificar e imprimir pares
        try:
            num_1 = int(num1.get())  #Obtener num del campo de entrada
            num_2 = int(num2.get())
            
            numeros_pares = [i for i in range(num_1, num_2 + 1) if i % 2 == 0]  #Verificar si el número es par
            mensaje = ", ".join(map(str, numeros_pares))

        except ValueError:
            mensaje = "Por favor, ingrese un número válido."
        
        #Mostrar mensaje de resultado en la ventana
        resultado.config(text=mensaje)

    #Ventana sumar números
    ventana_pares = tk.Toplevel()
    ventana_pares.title("Actividad 19")
    ventana_pares.geometry("550x350")

    #Intrucciones
    actividad = tk.Label(ventana_pares, text="Imprimir números pares", font=("Arial", 12 ,"bold"))
    actividad.pack(pady=10)
    
    #Frame para intrucciones
    instrucciones = tk.Frame(ventana_pares)
    instrucciones.pack(pady=10)
    
    isnt_1 = tk.Label(instrucciones, text="Ingrese primer número", font=("Arial", 12))
    isnt_1.pack(side="left", padx=10)
    
    isnt_2= tk.Label(instrucciones, text="Ingrese segundo número", font=("Arial", 12))
    isnt_2.pack(side="left", padx=10)

    #Frame para contener las entradas
    nums = tk.Frame(ventana_pares)
    nums.pack(pady=10)

    #Crear las entradas para los números
    num1 = tk.Entry(nums, font=("Times", 12), width=7)
    num1.pack(side="left", padx=60)
    
    isnt_3 = tk.Label(nums, text="al", font=("Arial", 12, "bold"))
    isnt_3.pack(side="left", padx=10)
  
    num2 = tk.Entry(nums, font=("Times", 12), width=7)
    num2.pack(side="left", padx=60)

    #Botón Imprimir pares
    boton_imp = tk.Button(ventana_pares, text="Imprimir Pares", command=par)
    boton_imp.pack(pady=10)

    #Mostrar el resultado
    resultado = tk.Label(ventana_pares, text="", font=("Arial", 12))
    resultado.pack(pady=20)

    #Botón cerrar la ventana
    boton_cerrar = tk.Button(ventana_pares, text="Cerrar", command=ventana_pares.destroy)
    boton_cerrar.pack(pady=10)