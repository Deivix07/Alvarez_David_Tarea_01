import tkinter as tk      #Importar la biblioteca tkinter para la interfaz gráfica

#Escribe una función que reciba un número y retorne su cuadrado

def cuadrado(num):          #definimos la función que tome como parámetro un número
    return num * num        #retornamos el cuadrado de un numero


def cuadrado_num():
    def cuadrad():    #Función imprimir cuadrado
        try:
            num = float(entrada_numero.get())  #Obtener el número del campo de entrada
            
            mensaje = (f"El cuadrado de {num} es: {(cuadrado(num))}")  #llamar a la funcion cuadrado e imprimir el resultado

        except ValueError:
            mensaje = "Por favor, ingrese un número válido."
        
        #Mostrar mensaje de resultado en la ventana
        resultado.config(text=mensaje)

    #Ventana cuadrado
    ventana_cuadrado = tk.Toplevel()
    ventana_cuadrado.title("Actividad 29")
    ventana_cuadrado.geometry("501x300")

    #Intrucciones
    actividad = tk.Label(ventana_cuadrado, text="Cuadrado de un número", font=("Arial", 12 ,"bold"))
    actividad.pack(pady=10)
    
    etiqueta_instrucciones = tk.Label(ventana_cuadrado, text="Ingrese un número:", font=("Arial", 12))
    etiqueta_instrucciones.pack(pady=10)

    #Entrada para el número
    entrada_numero = tk.Entry(ventana_cuadrado, font=("Arial", 12))
    entrada_numero.pack(pady=10)

    #Botón cuadrado del numero
    boton_verificar = tk.Button(ventana_cuadrado, text="Cuadrado", command=cuadrad)
    boton_verificar.pack(pady=10)

    #Mostrar el resultado
    resultado = tk.Label(ventana_cuadrado, text="", font=("Arial", 12))
    resultado.pack(pady=20)

    #Botón cerrar la ventana
    boton_cerrar = tk.Button(ventana_cuadrado, text="Cerrar", command=ventana_cuadrado.destroy)
    boton_cerrar.pack(pady=10)