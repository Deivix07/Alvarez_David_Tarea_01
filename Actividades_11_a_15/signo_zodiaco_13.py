import tkinter as tk

def determinar_signo_zodiacal():            # Función para determinar el signo zodiacal
    def calcular_signo():
        try:
            #Obtener el día y el mes de nacimiento desde las entradas
            dia = int(dia_nacimiento.get())  #Día de nacimiento
            mes = mes_nacimiento.get().lower()  #Mes de nacimiento, convertir a minúsculas
            
            meses_validos = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
            if mes not in meses_validos:
                raise ValueError("Mes incorrecto. Ingresa un mes válido (enero, febrero, etc.)")

            #determinar el signo zodiacal según el día y mes
            if (mes == "enero" and dia >= 20) or (mes == "febrero" and dia <= 18):
                signo = "Acuario"
            elif (mes == "febrero" and dia >= 19) or (mes == "marzo" and dia <= 20):
                signo = "Piscis"
            elif (mes == "marzo" and dia >= 21) or (mes == "abril" and dia <= 19):
                signo = "Aries"
            elif (mes == "abril" and dia >= 20) or (mes == "mayo" and dia <= 20):
                signo = "Tauro"
            elif (mes == "mayo" and dia >= 21) or (mes == "junio" and dia <= 20):
                signo = "Géminis"
            elif (mes == "junio" and dia >= 21) or (mes == "julio" and dia <= 22):
                signo = "Cáncer"
            elif (mes == "julio" and dia >= 23) or (mes == "agosto" and dia <= 22):
                signo = "Leo"
            elif (mes == "agosto" and dia >= 23) or (mes == "septiembre" and dia <= 22):
                signo = "Virgo"
            elif (mes == "septiembre" and dia >= 23) or (mes == "octubre" and dia <= 22):
                signo = "Libra"
            elif (mes == "octubre" and dia >= 23) or (mes == "noviembre" and dia <= 21):
                signo = "Escorpio"
            elif (mes == "noviembre" and dia >= 22) or (mes == "diciembre" and dia <= 21):
                signo = "Sagitario"
            elif (mes == "diciembre" and dia >= 22) or (mes == "enero" and dia <= 19):
                signo = "Capricornio"

            # Mostrar el signo zodiacal
            resultado.config(text=f"Tu signo zodiacal es: {signo}")
        
        except ValueError:
            resultado.config(text="Por favor, ingrese un día o mes (enero, febrero, ...) válidos")

    #Ventana signo
    ventana = tk.Toplevel()
    ventana.title("Actividad 13")
    ventana.geometry("400x300")

    #Instrucciones
    instrucciones = tk.Label(ventana, text="Introduce tu día y mes de nacimiento", font=("Arial", 14))
    instrucciones.pack(pady=10)

    #Frame para las entradas
    entradas = tk.Frame(ventana)
    entradas.pack(pady=10)

    #Entrada para el día
    dia_label = tk.Label(entradas, text="Día:", font=("Arial", 12))
    dia_label.pack(side="left", padx=5)
    dia_nacimiento = tk.Entry(entradas, font=("Arial", 12), width=5)
    dia_nacimiento.pack(side="left")

    #Entrada para el mes
    mes_label = tk.Label(entradas, text="Mes:", font=("Arial", 12))
    mes_label.pack(side="left", padx=5)
    mes_nacimiento = tk.Entry(entradas, font=("Arial", 12), width=10)
    mes_nacimiento.pack(side="left")

    #Botón para el signo
    boton_calcular = tk.Button(ventana, text="Determinar Signo", command=calcular_signo)
    boton_calcular.pack(pady=10)

    #Mostrar el resultado
    resultado = tk.Label(ventana, text="", font=("Arial", 12))
    resultado.pack(pady=20)

    #Botón para cerrar la ventana
    boton_cerrar = tk.Button(ventana, text="Cerrar", command=ventana.destroy)
    boton_cerrar.pack(pady=10)