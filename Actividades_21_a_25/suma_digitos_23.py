import tkinter as tk      #Importar la biblioteca tkinter para la interfaz gráfica

#Solicita un número entero y calcula la suma de sus dígitos
def sum_dig():
    def dig():    #Función para sumar digitos
        try:
            num_1 = int(num1.get())  #Obtener num del campo de entrada
            
            num = str(num_1)  #convertir a string
            
            sumdigit=0      #inicializar la variable de suma en 0
            
            for i in num:         #recorrer cada dígito del número
                sumdigit += int(i)                #sumamos el valor del dígito

            mensaje = (f"La suma de los dígitos es: {sumdigit}")
                
        except ValueError:
            mensaje = "Por favor, ingrese un número válido."
        
        #Mostrar mensaje de resultado en la ventana
        resultado.config(text=mensaje)

    #Ventana sumar dígitos
    ventana_dig = tk.Toplevel()
    ventana_dig.title("Actividad 23")
    ventana_dig.geometry("550x350")

    #Intrucciones
    actividad = tk.Label(ventana_dig, text="Suma de sus Dígitos", font=("Arial", 12 ,"bold"))
    actividad.pack(pady=10)
    
    #Frame para intrucciones
    instrucciones = tk.Frame(ventana_dig)
    instrucciones.pack(pady=10)
    
    isnt_1 = tk.Label(instrucciones, text="Ingresa un número entero:", font=("Arial", 12))
    isnt_1.pack(side="left", padx=10)

    #Frame para contener las entradas
    nums = tk.Frame(ventana_dig)
    nums.pack(pady=10)

    #Crear entradas para el número
    num1 = tk.Entry(nums, font=("Times", 12), width=15)
    num1.pack(side="left", padx=60)
  
    #Botón Imprimir suma
    boton_imp = tk.Button(ventana_dig, text="Imprimir Suma Dígitos", command=dig)
    boton_imp.pack(pady=10)

    #Mostrar el resultado
    resultado = tk.Label(ventana_dig, text="", font=("Arial", 12))
    resultado.pack(pady=20)

    #Botón cerrar la ventana
    boton_cerrar = tk.Button(ventana_dig, text="Cerrar", command=ventana_dig.destroy)
    boton_cerrar.pack(pady=10)
