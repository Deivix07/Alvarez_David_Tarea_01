import tkinter as tk      #Importar la biblioteca tkinter para la interfaz gráfica

#Encuentra e imprime todos los números primos
def primos():
    def prim():    #Función primos
        try:
            num_1 = int(num1.get())  #Obtener num del campo de entrada
            num_2 = int(num2.get())
            encabezado.config(text=f"Números primos entre {num_1} y {num_2}:", font=("Arial", 12, "bold"))
            mensaje = ""
            
            #Verificar números primos entre num_1 y num_2
            for num in range(num_1, num_2 + 1):
                if num > 1:  # Los números menores o iguales a 1 no son primos
                    for i in range(2, num):
                        if num % i == 0:  # Si num es divisible por i, no es primo
                            break
                    else:
                        #Si no se encontró ningún divisor, es primo
                        mensaje += f"{num}, "  # oncatenar número primo a mensaje
            
            if not mensaje:      #Si no se hay números primos
                mensaje = "No se encontraron números primos en ese rango."
                
        except ValueError:
            mensaje = "Por favor, ingrese un número válido."
        
        #Mostrar mensaje de resultado en la ventana
        resultado.config(text=mensaje)

    #Ventana primos
    ventana_primos = tk.Toplevel()
    ventana_primos.title("Actividad 22")
    ventana_primos.geometry("550x350")

    #Intrucciones
    actividad = tk.Label(ventana_primos, text="Números primos", font=("Arial", 12 ,"bold"))
    actividad.pack(pady=10)
    
    #Frame para intrucciones
    instrucciones = tk.Frame(ventana_primos)
    instrucciones.pack(pady=10)
    
    isnt_1 = tk.Label(instrucciones, text="Ingrese primer número", font=("Arial", 12))
    isnt_1.pack(side="left", padx=10)
    
    isnt_2= tk.Label(instrucciones, text="Ingrese segundo número", font=("Arial", 12))
    isnt_2.pack(side="left", padx=10)

    #Frame para contener las entradas
    nums = tk.Frame(ventana_primos)
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
    boton_imp = tk.Button(ventana_primos, text="Imprimir Números Primos", command=prim)
    boton_imp.pack(pady=10)
    
    encabezado = tk.Label(ventana_primos, text="", font=("Arial", 12, "bold"))
    encabezado.pack(pady=5)

    #Mostrar el resultado
    resultado = tk.Label(ventana_primos, text="", font=("Arial", 12))
    resultado.pack(pady=20)

    #Botón cerrar la ventana
    boton_cerrar = tk.Button(ventana_primos, text="Cerrar", command=ventana_primos.destroy)
    boton_cerrar.pack(pady=10)