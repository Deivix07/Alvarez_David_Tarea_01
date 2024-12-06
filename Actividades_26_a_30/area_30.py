import tkinter as tk      #Importar la biblioteca tkinter para la interfaz gráfica

#Crea una función que reciba el radio de un círculo y retorne su área

def area(radio):          #definimos la función área que tome como parámetro el radio
    return 3.1416 * (radio * radio)       #retornamos el area del circulo


def area_circulo():
    def impr_area():    #Función imprimir cuadrado
        try:
            radio = float(entrada_radio.get())  #Obtener el número del campo de entrada
            
            mensaje = (f"El área del circulo con radio {radio} es: {(area(radio))}")  #llamar a la funcion cuadrado e imprimir el resultado

        except ValueError:
            mensaje = "Por favor, ingrese un número válido."
        
        #Mostrar mensaje de resultado en la ventana
        resultado.config(text=mensaje)

    #Ventana radio
    ventana_radio = tk.Toplevel()
    ventana_radio.title("Actividad 30")
    ventana_radio.geometry("501x300")

    #Intrucciones
    actividad = tk.Label(ventana_radio, text="Área del circulo\n\nA = πr^2", font=("Arial", 12 ,"bold"))
    actividad.pack(pady=10)
    
    etiqueta_instrucciones = tk.Label(ventana_radio, text="Ingresa el radio del círculo:", font=("Arial", 12))
    etiqueta_instrucciones.pack(pady=10)

    #Entrada para el radio
    entrada_radio = tk.Entry(ventana_radio, font=("Arial", 12))
    entrada_radio.pack(pady=10)

    #Botón imprimir radio
    boton_verificar = tk.Button(ventana_radio, text="Radio del Círculo", command=impr_area)
    boton_verificar.pack(pady=10)

    #Mostrar el resultado
    resultado = tk.Label(ventana_radio, text="", font=("Arial", 12))
    resultado.pack(pady=20)

    #Botón cerrar la ventana
    boton_cerrar = tk.Button(ventana_radio, text="Cerrar", command=ventana_radio.destroy)
    boton_cerrar.pack(pady=10)