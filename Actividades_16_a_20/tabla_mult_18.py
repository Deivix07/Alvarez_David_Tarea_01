import tkinter as tk      #Importar la biblioteca tkinter para la interfaz gráfica

#Solicita un número al usuario y muestra su tabla de multiplicar del 1 al 10
def tabla_mult():
    def mult():    #Función verificar número si es positivo, negativo o cero
        try:
            num = int(entrada_numero.get())  #Obtener el número del campo de entrada
            encabezado.config(text=f"Tabla de multiplicar del {num}:", font=("Arial", 12, "bold"))
            mensaje = ""
            for i in range(1,11):     #usar bucle for con rango de 1 a 10
                result = num * i      #realizar la operación para cada numero
                mensaje += (f"{num} x {i} = {result}\n")  #imprimir resultado
                
        except ValueError:
            mensaje = "Por favor, ingrese un número válido."
        
        #Mostrar mensaje de resultado en la ventana
        resultado.config(text=mensaje)

    #Ventana par o impar
    ventana_multi = tk.Toplevel()
    ventana_multi.title("Actividad 18")
    ventana_multi.geometry("501x500")

    #Intrucciones
    actividad = tk.Label(ventana_multi, text="Tabla de Multiplicar", font=("Arial", 12 ,"bold"))
    actividad.pack(pady=10)
    
    etiqueta_instrucciones = tk.Label(ventana_multi, text="Ingrese el número del que quiere su tabla de multiplicar:", font=("Arial", 12))
    etiqueta_instrucciones.pack(pady=10)

    #Entrada para el número
    entrada_numero = tk.Entry(ventana_multi, font=("Arial", 12),width=5)
    entrada_numero.pack(pady=10)

    #Botón tabla multiplicar
    boton_tabla = tk.Button(ventana_multi, text="Tabla Multiplicar", command=mult)
    boton_tabla.pack(pady=10)

    encabezado = tk.Label(ventana_multi, text="", font=("Arial", 12, "bold"))
    encabezado.pack(pady=5)
    
    #Mostrar el resultado
    resultado = tk.Label(ventana_multi, text="", font=("Arial", 12))
    resultado.pack(pady=5)

    #Botón cerrar la ventana
    boton_cerrar = tk.Button(ventana_multi, text="Cerrar", command=ventana_multi.destroy)
    boton_cerrar.pack(pady=10)