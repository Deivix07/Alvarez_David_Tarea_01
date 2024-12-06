import tkinter as tk      #Importar la biblioteca tkinter para la interfaz gráfica

#Escribe una función que reciba dos números como parámetros y retorne su suma

def suma(num_1,num_2):          #definimos la función que tome como parámetro los números
    return num_1 + num_2        #retornamos la suma de los dos números


def suma_num():
    def sum():  #Función sumar
        try:
            num_1 = float(num1.get().strip()) #Obtener num del campo de entrada
            num_2 = float(num2.get().strip())
            
            mensaje = f"La suma de {num_1} + {num_2} es: {suma(num_1, num_2)}"
            
        except ValueError:
            # Si ocurre un error, mostrar un mensaje
            mensaje = "Por favor, ingresa números válidos."
            
        # Mostrar mensaje de resultado en la ventana
        resultado.config(text=mensaje)

    #Ventana sumar números
    ventana_sum = tk.Toplevel()
    ventana_sum.title("Actividad 27")
    ventana_sum.geometry("550x350")

    #Intrucciones
    actividad = tk.Label(ventana_sum, text="Suma", font=("Arial", 12 ,"bold"))
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
  
    isnt_3 = tk.Label(nums, text="+", font=("Arial", 12, "bold"))
    isnt_3.pack(side="left", padx=10)
    
    #Crear las entradas para los números
    num2 = tk.Entry(nums, font=("Times", 12), width=7)
    num2.pack(side="left", padx=60)

    #Botón Imprimir suma
    boton_imp = tk.Button(ventana_sum, text="Sumar", command=sum)
    boton_imp.pack(pady=10)

    #Mostrar el resultado
    resultado = tk.Label(ventana_sum, text="", font=("Arial", 12))
    resultado.pack(pady=20)

    #Botón cerrar la ventana
    boton_cerrar = tk.Button(ventana_sum, text="Cerrar", command=ventana_sum.destroy)
    boton_cerrar.pack(pady=10)