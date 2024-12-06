import tkinter as tk      #Importar la biblioteca tkinter para la interfaz gráfica

#Solicita un año y determina si es bisiesto
#(divisible entre 4 pero no entre 100, excepto si es divisible entre 400)
def anio_bi():
    def anio_bisiesto():    #Función verificar si el año es bisiesto
        try:
            anio = int(entrada_anio.get())  #Obtener el año del campo de entrada
            if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
                mensaje = (f"El año {anio} es bisiesto.")
            else:
                mensaje = (f"El año {anio} no es bisiesto.")
        except ValueError:
            mensaje = "Por favor, ingrese un año válido"
        
        #Mostrar mensaje de resultado en la ventana
        resultado.config(text=mensaje)

    #Ventana año bisiesto
    ventana_anio_bi = tk.Toplevel()
    ventana_anio_bi.title("Actividad 10")
    ventana_anio_bi.geometry("501x300")

    #Intrucciones
    actividad = tk.Label(ventana_anio_bi, text="Determine si el año es bisiesto", font=("Arial", 12 ,"bold"))
    actividad.pack(pady=10)
    
    etiqueta_instrucciones = tk.Label(ventana_anio_bi, text="Ingrese un año", font=("Arial", 12))
    etiqueta_instrucciones.pack(pady=10)

    #Entrada para el año
    entrada_anio = tk.Entry(ventana_anio_bi, font=("Arial", 12))
    entrada_anio.pack(pady=10)

    #Botón verificar el año
    boton_verificar = tk.Button(ventana_anio_bi, text="Verificar", command=anio_bisiesto)
    boton_verificar.pack(pady=10)

    #Mostrar el resultado
    resultado = tk.Label(ventana_anio_bi, text="", font=("Arial", 12))
    resultado.pack(pady=20)

    #Botón cerrar la ventana
    boton_cerrar = tk.Button(ventana_anio_bi, text="Cerrar", command=ventana_anio_bi.destroy)
    boton_cerrar.pack(pady=10)