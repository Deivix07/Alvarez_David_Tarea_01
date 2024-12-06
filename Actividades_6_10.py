import tkinter as tk          #Importar la biblioteca tkinter para la interfaz gráfica

from Actividades_6_a_10.edad_votar_06 import edad_votar                   #Importar la función 'edad_votar' desde la carpeta 'Actividades_6_a_10'
from Actividades_6_a_10.mayor_tres_numeros_07 import mayor_num            #Importar la función 'mayor_num' desde la carpeta 'Actividades_6_a_10'
from Actividades_6_a_10.clasif_edades_08 import clasi_edad                #Importar la función 'clasi_edad' desde la carpeta 'Actividades_6_a_10'
from Actividades_6_a_10.calculadora_09 import calculadora                 #Importar la función 'calculadora' desde la carpeta 'Actividades_6_a_10'
from Actividades_6_a_10.año_bi_10 import anio_bi                          #Importar la función 'anio_bi ' desde la carpeta 'Actividades_6_a_10'

#Crea la ventana para las actividades
def ventana_6_10():
    global ventana_6_10
    ventana_6_10 = tk.Toplevel()
    ventana_6_10.title("Actividades 6 a 10")
    ventana_6_10.geometry("501x300")  

    #Agregar el título
    tk.Label(ventana_6_10, text="Actividades 6 a 10", font=("Times", 14, "bold"), bg="orange").pack(pady=10)

    #Botones para las actividades
    tk.Button(ventana_6_10, text="Actividad 6 : Edad para votar", command=edad_votar, font=("Times", 12, "bold"), bg="pale green").pack(pady=5)
    tk.Button(ventana_6_10, text="Actividad 7 : Mayor de tres números", command=mayor_num, font=("Times", 12, "bold"), bg="pale green").pack(pady=5)
    tk.Button(ventana_6_10, text="Actividad 8 : Clasificación de edades", command=clasi_edad, font=("Times", 12, "bold"), bg="pale green").pack(pady=5)
    tk.Button(ventana_6_10, text="Actividad 9 : Calculadora básica", command=calculadora, font=("Times", 12, "bold"), bg="pale green").pack(pady=5)
    tk.Button(ventana_6_10, text="Actividad 10 : Determinar un año bisiesto", command=anio_bi , font=("Times", 12, "bold"), bg="pale green").pack(pady=5)  