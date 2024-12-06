import tkinter as tk      #Importar la biblioteca tkinter para la interfaz gráfica

#Imprime los números del 10 al 1 en orden descendente
def descendente():
    def orden_descendente():    #Función imprimir números orden descendente
        try:
            num_1 = int(num1.get())  #Obtener nums del campo de entrada
            num_2 = int(num2.get())
            
            #Ajustar el rango según el orden de los números
            if num_1 >= num_2:
                orden_desc = [i for i in range(num_1, num_2 - 1, -1)]  #Paso negativo
            else:
                orden_desc = [i for i in range(num_2, num_1 - 1, -1)]  #Paso negativo

            mensaje = ", ".join(map(str, orden_desc))
                
        except ValueError:
            mensaje = "Por favor, ingrese un número válido."
        
        #Mostrar mensaje de resultado en la ventana
        resultado.config(text=mensaje)

    #Ventana orden descendente
    ventana_descendente = tk.Toplevel()
    ventana_descendente.title("Actividad 20")
    ventana_descendente.geometry("550x350")

    #Intrucciones
    actividad = tk.Label(ventana_descendente, text="Imprimir números en orden descendente", font=("Arial", 12 ,"bold"))
    actividad.pack(pady=10)
    
    #Frame para intrucciones
    instrucciones = tk.Frame(ventana_descendente)
    instrucciones.pack(pady=10)
    
    isnt_1 = tk.Label(instrucciones, text="Ingrese primer número", font=("Arial", 12))
    isnt_1.pack(side="left", padx=10)
    
    isnt_2= tk.Label(instrucciones, text="Ingrese segundo número", font=("Arial", 12))
    isnt_2.pack(side="left", padx=10)

    #Frame para contener las entradas
    nums = tk.Frame(ventana_descendente)
    nums.pack(pady=10)

    #Crear las entradas para los números
    num1 = tk.Entry(nums, font=("Times", 12), width=7)
    num1.pack(side="left", padx=60)
  
    isnt_3 = tk.Label(nums, text="al", font=("Arial", 12, "bold"))
    isnt_3.pack(side="left", padx=10)
    
    #Crear las entradas para los números
    num2 = tk.Entry(nums, font=("Times", 12), width=7)
    num2.pack(side="left", padx=60)

    #Botón Imprimir orden descendente
    boton_imp = tk.Button(ventana_descendente, text="Imprimir Orden Descendente", command=orden_descendente)
    boton_imp.pack(pady=10)

    #Mostrar el resultado
    resultado = tk.Label(ventana_descendente, text="", font=("Arial", 12))
    resultado.pack(pady=20)

    #Botón cerrar la ventana
    boton_cerrar = tk.Button(ventana_descendente, text="Cerrar", command=ventana_descendente.destroy)
    boton_cerrar.pack(pady=10)