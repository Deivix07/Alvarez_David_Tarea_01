import tkinter as tk          #Importar la biblioteca tkinter para la interfaz gráfica

from Actividades_16_a_20.imprimir_numeros_16 import imprimir_nums             #Importar la función 'imprimir_nums' desde la carpeta 'Actividades_16_a_20'
from Actividades_16_a_20.suma_10_nums_17 import suma_nums                     #Importar la función 'suma_nums' desde la carpeta 'Actividades_16_a_20'
from Actividades_16_a_20.tabla_mult_18 import tabla_mult                      #Importar la función 'tabla_mult' desde la carpeta 'Actividades_16_a_20'
from Actividades_16_a_20.calcular_pares_19 import pares                       #Importar la función 'pares' desde la carpeta 'Actividades_16_a_20'
from Actividades_16_a_20.descendente_20 import descendente                    #Importar la función 'descendente' desde la carpeta 'Actividades_16_a_20'

#Crea la ventana para las actividades de 6-10
def ventana_16_20():
    global ventana_16_20
    ventana_16_20 = tk.Toplevel()
    ventana_16_20.title("Actividades 16 a 20")
    ventana_16_20.geometry("501x300")  

    #Agregar el título
    tk.Label(ventana_16_20, text="Actividades 16 a 20", font=("Times", 14, "bold"), bg="orange").pack(pady=10)

    #Botones para las actividades
    tk.Button(ventana_16_20, text="Actividad 16 : Imprimir números ", command=imprimir_nums, font=("Times", 12, "bold"), bg="pale green").pack(pady=5)
    tk.Button(ventana_16_20, text="Actividad 17 : Suma de números", command=suma_nums, font=("Times", 12, "bold"), bg="pale green").pack(pady=5)
    tk.Button(ventana_16_20, text="Actividad 18 : Tabla de multiplicar", command=tabla_mult, font=("Times", 12, "bold"), bg="pale green").pack(pady=5)
    tk.Button(ventana_16_20, text="Actividad 19 : Contar números pares", command=pares , font=("Times", 12, "bold"), bg="pale green").pack(pady=5)
    tk.Button(ventana_16_20, text="Actividad 20 : Contador regresivo", command=descendente, font=("Times", 12, "bold"), bg="pale green").pack(pady=5)  