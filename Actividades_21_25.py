import tkinter as tk          #Importar la biblioteca tkinter para la interfaz gráfica

from Actividades_21_a_25.factorial_21 import factorial             #Importar la función 'factorial' desde la carpeta 'Actividades_21_a_25'
from Actividades_21_a_25.numeros_primos_22 import primos           #Importar la función 'primos' desde la carpeta 'Actividades_21_a_25'
from Actividades_21_a_25.suma_digitos_23 import sum_dig            #Importar la función 'sum_dig' desde la carpeta 'Actividades_21_a_25'
from Actividades_21_a_25.invetir_num_24 import num_invertido       #Importar la función 'num_invertido' desde la carpeta 'Actividades_21_a_25'
from Actividades_21_a_25.promedio_25 import promedio_estudiante    #Importar la función 'promedio_estudiante' desde la carpeta 'Actividades_21_a_25'

#Crea la ventana para las actividades
def ventana_21_25():
    global ventana_21_25
    ventana_21_25 = tk.Toplevel()
    ventana_21_25.title("Actividades 21 a 25")
    ventana_21_25.geometry("501x300")  

    #Agregar el título
    tk.Label(ventana_21_25, text="Actividades 21 a 25", font=("Times", 14, "bold"), bg="orange").pack(pady=10)

    #Botones para las actividades
    tk.Button(ventana_21_25, text="Actividad 21 : Factorial de un número", command=factorial , font=("Times", 12, "bold"), bg="pale green").pack(pady=5)
    tk.Button(ventana_21_25, text="Actividad 22 : Números primos", command=primos, font=("Times", 12, "bold"), bg="pale green").pack(pady=5)
    tk.Button(ventana_21_25, text="Actividad 23 : Sumar dígitos", command=sum_dig, font=("Times", 12, "bold"), bg="pale green").pack(pady=5)
    tk.Button(ventana_21_25, text="Actividad 24 : Invertir un número", command=num_invertido, font=("Times", 12, "bold"), bg="pale green").pack(pady=5)
    tk.Button(ventana_21_25, text="Actividad 25 : Promedio de calificaciones", command=promedio_estudiante, font=("Times", 12, "bold"), bg="pale green").pack(pady=5)  