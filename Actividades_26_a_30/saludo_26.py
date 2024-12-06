import tkinter as tk      #Importar la biblioteca tkinter para la interfaz gráfica

#Crea una función que reciba un nombre como parámetro y retorne un saludo

def saludar(nombre):  #definimos la función que tome como parámetro el nombre
    return (f"¡Hola!, {nombre}")  #retornamos el saludo que incluye el nombre


def saludo():
    def impr_saludo():  #Función para imprimir saludo
        nombre = (entrada_nombre.get().strip())  #Obtener el nombre del campo de entrada
        if nombre:  #Verificar que no esté vacío
            mensaje = saludar(nombre)
        else:
            mensaje = "Por favor, ingresa un nombre"
        # Mostrar mensaje de resultado en la ventana
        resultado.config(text=mensaje)

    #Ventana saludo
    ventana_saludo = tk.Toplevel()
    ventana_saludo.title("Actividad 26")
    ventana_saludo.geometry("501x300")

    #Intrucciones
    actividad = tk.Label(ventana_saludo, text="Saludo personalizado", font=("Arial", 12 ,"bold"))
    actividad.pack(pady=10)
    
    etiqueta_instrucciones = tk.Label(ventana_saludo, text="Ingrese su nombre:", font=("Arial", 12))
    etiqueta_instrucciones.pack(pady=10)

    #Entrada para el número
    entrada_nombre = tk.Entry(ventana_saludo, font=("Arial", 12))
    entrada_nombre.pack(pady=10)

    #Botón saludar
    boton_verificar = tk.Button(ventana_saludo, text="Saludar", command=impr_saludo)
    boton_verificar.pack(pady=10)

    #Mostrar el saludo
    resultado = tk.Label(ventana_saludo, text="", font=("Arial", 12))
    resultado.pack(pady=20)

    #Botón cerrar la ventana
    boton_cerrar = tk.Button(ventana_saludo, text="Cerrar", command=ventana_saludo.destroy)
    boton_cerrar.pack(pady=10)