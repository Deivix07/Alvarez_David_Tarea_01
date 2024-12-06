import tkinter as tk      #Importar la biblioteca tkinter para la interfaz gráfica

#Usa un bucle para mostrar los números del 1 al 10 en la consola.
def imprimir_nums():
    def imp():    #Función imprimir números
        try:
            num_1 = int(num1.get())  #Obtener num del campo de entrada
            num_2 = int(num2.get())
            
            numeros = [i for i in range(num_1, num_2 + 1)]
            mensaje = ", ".join(map(str, numeros))
                
        except ValueError:
            mensaje = "Por favor, ingrese un número válido."
        
        #Mostrar mensaje de resultado en la ventana
        resultado.config(text=mensaje)

    #Ventana imprimir números
    ventana_imp = tk.Toplevel()
    ventana_imp.title("Actividad 16")
    ventana_imp.geometry("550x350")

    #Intrucciones
    actividad = tk.Label(ventana_imp, text="Imprimir números", font=("Arial", 12 ,"bold"))
    actividad.pack(pady=10)
    
    #Frame para intrucciones
    instrucciones = tk.Frame(ventana_imp)
    instrucciones.pack(pady=10)
    
    isnt_1 = tk.Label(instrucciones, text="Ingrese primer número", font=("Arial", 12))
    isnt_1.pack(side="left", padx=10)
    
    isnt_2= tk.Label(instrucciones, text="Ingrese segundo número", font=("Arial", 12))
    isnt_2.pack(side="left", padx=10)

    #Frame para contener las entradas
    nums = tk.Frame(ventana_imp)
    nums.pack(pady=10)

    #Crear las entradas para los números
    num1 = tk.Entry(nums, font=("Times", 12), width=7)
    num1.pack(side="left", padx=60)
    
    isnt_3 = tk.Label(nums, text="al", font=("Arial", 12, "bold"))
    isnt_3.pack(side="left", padx=10)
  
    num2 = tk.Entry(nums, font=("Times", 12), width=7)
    num2.pack(side="left", padx=60)

    #Botón Imprimir
    boton_imp = tk.Button(ventana_imp, text="Imprimir", command=imp)
    boton_imp.pack(pady=10)

    #Mostrar el resultado
    resultado = tk.Label(ventana_imp, text="", font=("Arial", 12))
    resultado.pack(pady=20)

    #Botón cerrar la ventana
    boton_cerrar = tk.Button(ventana_imp, text="Cerrar", command=ventana_imp.destroy)
    boton_cerrar.pack(pady=10)