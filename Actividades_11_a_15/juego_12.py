import tkinter as tk      #Importar la biblioteca tkinter para la interfaz gráfica
import random             #Importar random para generar números aleatorios

#Genera un número aleatorio entre 1 y 10 y solicita al usuario
#que adivine el número. Usa if para verificar si acertó o no.
def num_aleat():
    def verificar_num():    #Función verificar numero
        try:
            num_aleatorio = random.randint(1, 10)   #Generar un número aleatorio cada vez que se verifica
            num = int(entrada_num.get())  #Obtener la num del campo de entrada
            if num == num_aleatorio:
                mensaje = (f"¡Felicidades, acertaste! El número era {num_aleatorio}.")
            else:
                mensaje = (f"Intenta de nuevo. El número era {num_aleatorio}.")
        except ValueError:
            mensaje = "Por favor, ingrese un número válido."
        
        #Mostrar mensaje de resultado en la ventana
        resultado.config(text=mensaje)

    #Ventana numero aleatorio
    ventana_num = tk.Toplevel()
    ventana_num.title("Actividad 12")
    ventana_num.geometry("501x300")

    #Intrucciones
    actividad = tk.Label(ventana_num, text="Adivina el número entre 1 y 10", font=("Arial", 12 ,"bold"))
    actividad.pack(pady=10)
    
    etiqueta_instrucciones = tk.Label(ventana_num, text="Ingrese un número:", font=("Arial", 12))
    etiqueta_instrucciones.pack(pady=10)

    #Entrada para el número
    entrada_num = tk.Entry(ventana_num, font=("Arial", 12))
    entrada_num.pack(pady=10)

    #Botón verificar numero
    boton_validar= tk.Button(ventana_num, text="Verificar", command=verificar_num)
    boton_validar.pack(pady=10)

    #Mostrar el resultado
    resultado = tk.Label(ventana_num, text="", font=("Arial", 12))
    resultado.pack(pady=20)

    #Botón cerrar la ventana
    boton_cerrar = tk.Button(ventana_num, text="Cerrar", command=ventana_num.destroy)
    boton_cerrar.pack(pady=10)