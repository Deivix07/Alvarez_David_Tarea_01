import tkinter as tk          #Importar la biblioteca tkinter para la interfaz gráfica

from Actividades_1_a_5.mayor_menor_01 import mayor_menor                #Importar la función 'mayor_menor' desde la carpeta 'Actividades_1_a_5'
from Actividades_1_a_5.positivo_negativo_02 import positivo_negativo    #Importar la función 'positivo_negativo' desde la carpeta 'Actividades_1_a_5'
from Actividades_1_a_5.par_impar_03 import par_impar                    #Importar la función 'par_impar' desde la carpeta 'Actividades_1_a_5'
from Actividades_1_a_5.aprobado_reprobado_04 import aprobado_reprobado  #Importar la función 'aprobado_reprobado' desde la carpeta 'Actividades_1_a_5'
from Actividades_1_a_5.descuento_05 import monto_final                  #Importar la función 'monto_final' desde la carpeta 'Actividades_1_a_5'

#Crea la ventana para las actividades de 1-5
def ventana_1_5():
    global ventana_1_5
    ventana_1_5 = tk.Toplevel()
    ventana_1_5.title("Actividades 1 a 5")
    ventana_1_5.geometry("501x300")  

    #Agregar el título
    tk.Label(ventana_1_5, text="Actividades 1 a 5", font=("Times", 14, "bold"), bg="orange").pack(pady=10)

    #Botones para las actividades
    tk.Button(ventana_1_5, text="Actividad 1 : Mayor o menor", command=mayor_menor, font=("Times", 12, "bold"), bg="pale green").pack(pady=5)
    tk.Button(ventana_1_5, text="Actividad 2 : Positivo o negativo", command=positivo_negativo, font=("Times", 12, "bold"), bg="pale green").pack(pady=5)
    tk.Button(ventana_1_5, text="Actividad 3 : Par o impar", command=par_impar, font=("Times", 12, "bold"), bg="pale green").pack(pady=5)
    tk.Button(ventana_1_5, text="Actividad 4 : Aprobado o reprobrado", command=aprobado_reprobado, font=("Times", 12, "bold"), bg="pale green").pack(pady=5)
    tk.Button(ventana_1_5, text="Actividad 5 : Descuento", command=monto_final, font=("Times", 12, "bold"), bg="pale green").pack(pady=5)  