import tkinter as tk          #Importar la biblioteca tkinter para la interfaz gráfica

from Actividades_26_a_30.saludo_26 import saludo           #Importar la función 'saludo' desde la carpeta 'Actividades_26_a_30'
from Actividades_26_a_30.def_suma_27 import suma_num       #Importar la función 'suma_num' desde la carpeta 'Actividades_26_a_30'
from Actividades_26_a_30.def_par_impar_28 import par_imp   #Importar la función 'par_imp' desde la carpeta 'Actividades_26_a_30'
from Actividades_26_a_30.cuadrado_29 import cuadrado_num   #Importar la función 'cuadrado_num' desde la carpeta 'Actividades_26_a_30'
from Actividades_26_a_30.area_30 import area_circulo       #Importar la función 'area_circulo' desde la carpeta 'Actividades_26_a_30'

#Crea la ventana para las actividades
def ventana_26_30():
    global ventana_26_30
    ventana_26_30 = tk.Toplevel()
    ventana_26_30.title("Actividades 26 a 30")
    ventana_26_30.geometry("501x300")  

    #Agregar el título
    tk.Label(ventana_26_30, text="Actividades 26 a 30", font=("Times", 14, "bold"), bg="orange").pack(pady=10)

    #Botones para las actividades
    tk.Button(ventana_26_30, text="Actividad 26 : Saludo personalizado", command=saludo, font=("Times", 12, "bold"), bg="pale green").pack(pady=5)
    tk.Button(ventana_26_30, text="Actividad 27 : Suma de dos números", command=suma_num, font=("Times", 12, "bold"), bg="pale green").pack(pady=5)
    tk.Button(ventana_26_30, text="Actividad 28 : Número par o impar", command=par_imp, font=("Times", 12, "bold"), bg="pale green").pack(pady=5)
    tk.Button(ventana_26_30, text="Actividad 29 : Calcular el cuadrado", command=cuadrado_num, font=("Times", 12, "bold"), bg="pale green").pack(pady=5)
    tk.Button(ventana_26_30, text="Actividad 30 : Calcular el área de un círculo", command=area_circulo, font=("Times", 12, "bold"), bg="pale green").pack(pady=5)  