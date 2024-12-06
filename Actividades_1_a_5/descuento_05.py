import tkinter as tk          #Importar la biblioteca tkinter para la interfaz gráfica

#Una tienda ofrece un 20% de descuento si el cliente gasta más de $100. 
#Escribe un programa que calcule el monto final
def monto_final():
    def descuento():    #Función verificar si aplica descuento
        try:
            monto = float(entrada_calif.get())  #Obtener el monto del campo entrada
            if monto > 100.00:
                desc = monto * 0.20        #calcular el 20% de descuento
                montodesc = monto - desc   #calcular el monto final
                mensaje = "Aplica descuento del 20%\n"
                mensaje += (f"Monto final: $ {montodesc}")
            else:
                mensaje = "No aplica descuento\n"
                mensaje += (f"Monto final: $ {monto}")
        except ValueError:
            mensaje = "Por favor, ingrese un monto válido"
        
        #Mostrar mensaje de resultado en la ventana
        resultado.config(text=mensaje)

    #Ventana descuento
    ventana_descuento = tk.Toplevel()
    ventana_descuento.title("Actividad 5")
    ventana_descuento.geometry("501x350")

    #Intrucciones
    actividad = tk.Label(ventana_descuento, text="Obtén 20% de descuento si gasta más de $100", font=("Arial", 12 ,"bold"))
    actividad.pack(pady=10)
    
    etiqueta_instrucciones = tk.Label(ventana_descuento, text="Ingrese el monto gastado: ", font=("Arial", 12))
    etiqueta_instrucciones.pack(pady=10)

    #Entrada para el monto
    entrada_calif = tk.Entry(ventana_descuento, font=("Arial", 12))
    entrada_calif.pack(pady=10)

    #Botón verificar si aplica descuento
    boton_verificar = tk.Button(ventana_descuento, text="Verificar", command=descuento)
    boton_verificar.pack(pady=10)

    #Mostrar el resultado
    resultado = tk.Label(ventana_descuento, text="", font=("Arial", 12))
    resultado.pack(pady=20)

    #Botón cerrar la ventana
    boton_cerrar = tk.Button(ventana_descuento, text="Cerrar", command=ventana_descuento.destroy)
    boton_cerrar.pack(pady=10)