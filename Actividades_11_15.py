import tkinter as tk          #Importar la biblioteca tkinter para la interfaz gráfica

from Actividades_11_a_15.contraseña_11 import passw                        #Importar la función 'passw' desde la carpeta 'Actividades_11_a_15'
from Actividades_11_a_15.juego_12 import num_aleat                         #Importar la función 'num_aleat'Actividades_11_a_15'
from Actividades_11_a_15.signo_zodiaco_13 import determinar_signo_zodiacal #Importar la función 'determinar_signo_zodiacal' desde la carpeta 'Actividades_11_a_15'
from Actividades_11_a_15.sistema_calif_14 import calificacion              #Importar la función 'calificacion' desde la carpeta 'Actividades_11_a_15'
from Actividades_11_a_15.control_acceso_15 import control_acceso           #Importar la función 'control_acceso' desde la carpeta 'Actividades_11_a_15'

#Crea la ventana para las actividades
def ventana_11_15():
    global ventana_11_15
    ventana_11_15 = tk.Toplevel()
    ventana_11_15.title("Actividades 11 a 15")
    ventana_11_15.geometry("501x300")  

    #Agregar el título
    tk.Label(ventana_11_15, text="Actividades 11 a 15", font=("Times", 14, "bold"), bg="orange").pack(pady=10)

    #Botones para las actividades
    tk.Button(ventana_11_15, text="Actividad 11 : Validar contraseñas", command=passw, font=("Times", 12, "bold"), bg="pale green").pack(pady=5)
    tk.Button(ventana_11_15, text="Actividad 12 : Juego de números", command=num_aleat, font=("Times", 12, "bold"), bg="pale green").pack(pady=5)
    tk.Button(ventana_11_15, text="Actividad 13 : Calcular el signo zodiacal", command=determinar_signo_zodiacal, font=("Times", 12, "bold"), bg="pale green").pack(pady=5)
    tk.Button(ventana_11_15, text="Actividad 14 : Sistema de calificaciones", command=calificacion, font=("Times", 12, "bold"), bg="pale green").pack(pady=5)
    tk.Button(ventana_11_15, text="Actividad 15 : Control de acceso", command=control_acceso, font=("Times", 12, "bold"), bg="pale green").pack(pady=5)  