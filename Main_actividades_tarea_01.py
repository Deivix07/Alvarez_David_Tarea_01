import tkinter as tk        #Importar la biblioteca tkinter para la interfaz gráfica

from Actividades_1_5 import ventana_1_5        #Importar la función 'ventana_1_5' desde el archivo 'Actividades_1_5'
from Actividades_6_10 import ventana_6_10      #Importar la función 'ventana_6_10' desde el archivo 'Actividades_6_10
from Actividades_11_15 import ventana_11_15    #Importar la función 'ventana_11_15' desde el archivo 'Actividades_11_15'
from Actividades_16_20 import ventana_16_20    #Importar la función 'ventana_16_20' desde el archivo 'Actividades_16_20'
from Actividades_21_25 import ventana_21_25    #Importar la función 'ventana_21_25' desde el archivo 'Actividades_21_25'
from Actividades_26_30 import ventana_26_30    #Importar la función 'ventana_26_30' desde el archivo 'Actividades_26_30'

#Crea la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Actividades Tarea 01")
ventana_principal.geometry("550x400")  

#Agregar el título
tk.Label(ventana_principal, text="Actividades Programación Estructurada", font=("Times", 20, "bold"), bg="light blue").pack(pady=15)

#Botones para las actividades
tk.Button(ventana_principal, text="Actividad 1 - 5", command=ventana_1_5, font=("Arial", 16, "bold"), bg="cornsilk2").pack(pady=5)
tk.Button(ventana_principal, text="Actividad 6 - 10", command=ventana_6_10, font=("Arial", 16, "bold"), bg="cornsilk2").pack(pady=5)
tk.Button(ventana_principal, text="Actividad 11 - 15", command=ventana_11_15, font=("Arial", 16, "bold"), bg="cornsilk2").pack(pady=5)
tk.Button(ventana_principal, text="Actividad 16 - 20", command=ventana_16_20, font=("Arial", 16, "bold"), bg="cornsilk2").pack(pady=5)
tk.Button(ventana_principal, text="Actividad 21 - 25", command=ventana_21_25, font=("Arial", 16, "bold"), bg="cornsilk2").pack(pady=5)
tk.Button(ventana_principal, text="Actividad 26 - 30", command=ventana_26_30, font=("Arial", 16, "bold"), bg="cornsilk2").pack(pady=5)

#Ejecutar el bucle de la interfaz gráfica
ventana_principal.mainloop()