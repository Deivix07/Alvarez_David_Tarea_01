import tkinter as tk      #Importar la biblioteca tkinter para la interfaz gráfica

#Crea una función que reciba un número y retorne True si es par y False si es impar

def par_impar(num):         #definimos la función que tome como parámetro un número
    if num % 2 == 0 :       #verificar si es par y retornar True
        return True
    else:                   #caso contrario impar y retornar False
        return False
    

def par_imp():
    def verificar_numero():    #Función verificar número si es par o impar
        try:
            num = int(entrada_numero.get())  #Obtener el número del campo de entrada
            
            mensaje = f"Número {num} = {(par_impar(num))}"    #llamar a la funcion par_impar e imprimir True o False

        except ValueError:
            mensaje = "Por favor, ingrese un número válido."
        
        #Mostrar mensaje de resultado en la ventana
        resultado.config(text=mensaje)

    #Ventana par o impar
    ventana_par_impar = tk.Toplevel()
    ventana_par_impar.title("Actividad 28")
    ventana_par_impar.geometry("501x350")

    #Intrucciones
    actividad = tk.Label(ventana_par_impar, text="Determine si el número es par o impar\n\nPar = True\nImpar = False", font=("Arial", 12 ,"bold"))
    actividad.pack(pady=10)
    
    etiqueta_instrucciones = tk.Label(ventana_par_impar, text="Ingrese un número entero:", font=("Arial", 12))
    etiqueta_instrucciones.pack(pady=10)

    #Entrada para el número
    entrada_numero = tk.Entry(ventana_par_impar, font=("Arial", 12))
    entrada_numero.pack(pady=10)

    #Botón par o impar
    boton_verificar = tk.Button(ventana_par_impar, text="Par o Impar", command=verificar_numero)
    boton_verificar.pack(pady=10)

    #Mostrar el resultado
    resultado = tk.Label(ventana_par_impar, text="", font=("Arial", 12))
    resultado.pack(pady=20)

    #Botón cerrar la ventana
    boton_cerrar = tk.Button(ventana_par_impar, text="Cerrar", command=ventana_par_impar.destroy)
    boton_cerrar.pack(pady=10)