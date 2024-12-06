import tkinter as tk      #Importar la biblioteca tkinter para la interfaz gráfica

#Solicita un número entero y muestra su versión invertida
def num_invertido():
    def invert():    #Función invertir num
        try:
            num_1 = int(num1.get())  #Obtener num del campo de entrada
            
            num = str(num_1)  #convertir num_1 a string
            
            num_invert=""     #inicializar la variable con una cadena vacia
            
            for i in num:         #recorrer cada dígito del número
                num_invert = i + num_invert     #concatenar el dígito al principio

            mensaje = (f"El número invertido es: {num_invert}")        #mostrar el numero invertido
                
        except ValueError:
            mensaje = "Por favor, ingrese un número válido."          
        
        #Mostrar mensaje de resultado en la ventana
        resultado.config(text=mensaje)

    #Ventana invertir nums
    ventana_invert = tk.Toplevel()
    ventana_invert.title("Actividad 24")
    ventana_invert.geometry("550x350")

    #Intrucciones
    actividad = tk.Label(ventana_invert, text="Invertir Número", font=("Arial", 12 ,"bold"))
    actividad.pack(pady=10)
    
    #Frame para intrucciones
    instrucciones = tk.Frame(ventana_invert)
    instrucciones.pack(pady=10)
    
    isnt_1 = tk.Label(instrucciones, text="Ingresa un número entero de dos o más cifras:", font=("Arial", 12))
    isnt_1.pack(side="left", padx=10)

    #Frame para contener las entradas
    nums = tk.Frame(ventana_invert)
    nums.pack(pady=10)

    #Crear entradas para el número
    num1 = tk.Entry(nums, font=("Times", 12), width=15)
    num1.pack(side="left", padx=60)
  
    #Botón Imprimir suma
    boton_imp = tk.Button(ventana_invert, text="Invertir Número", command=invert)
    boton_imp.pack(pady=10)

    #Mostrar el resultado
    resultado = tk.Label(ventana_invert, text="", font=("Arial", 12))
    resultado.pack(pady=20)

    #Botón cerrar la ventana
    boton_cerrar = tk.Button(ventana_invert, text="Cerrar", command=ventana_invert.destroy)
    boton_cerrar.pack(pady=10)
