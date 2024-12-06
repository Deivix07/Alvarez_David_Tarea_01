import tkinter as tk      #Importar la biblioteca tkinter para la interfaz gráfica

#user y password por defecto
user="admin"
passw="admin"

intentos = 3 #número de intentos

#Solicita un nombre de usuario y contraseña, y valida si ambos son correctos.
#Permite tres intentos antes de bloquear el acceso.

def control_acceso():
    def acceso():  # Función validar acceso
        global intentos  #Usar la variable global para controlar los intentos
        usuario = entrada_user.get()  #Obtener el nombre de usuario
        password = entrada_passw.get()  #Obtener la contraseña

        if intentos > 0:
            if usuario == user and password == passw:
                mensaje = (f"Bienvenido, {usuario}")
                intentos = 3  # Restablecer intentos
                boton_validar.config(state=tk.NORMAL)  # Habilitar el botón
            else:
                intentos -= 1
                if intentos > 0:
                    mensaje = (f"Credenciales incorrectas. Te quedan {intentos} intentos.")
                else:
                    mensaje = ("Acceso bloqueado. Has superado el número de intentos.")
                    boton_validar.config(state=tk.DISABLED)  # Deshabilitar el botón
                    
        #Mostrar mensaje de resultado en la ventana
        resultado.config(text=mensaje)

    #Ventana acceso
    ventana_acceso = tk.Toplevel()
    ventana_acceso.title("Actividad 15")
    ventana_acceso.geometry("501x400")

    #Intrucciones
    actividad = tk.Label(ventana_acceso, text="Control de Acceso", font=("Arial", 12 ,"bold"))
    actividad.pack(pady=10)
    
    etiqueta_instrucciones = tk.Label(ventana_acceso, text="Ingrese el usuario:", font=("Arial", 12))
    etiqueta_instrucciones.pack(pady=10)

    #Entrada para el usuario
    entrada_user = tk.Entry(ventana_acceso, font=("Arial", 12))
    entrada_user.pack(pady=10)

    #Intrucciones 
    etiqueta_instrucciones = tk.Label(ventana_acceso, text="Ingrese la contraseña:", font=("Arial", 12))
    etiqueta_instrucciones.pack(pady=10)

    #Entrada para la contraseña
    entrada_passw = tk.Entry(ventana_acceso, font=("Arial", 12))
    entrada_passw.pack(pady=10)

    #Botón validar contraseña
    boton_validar= tk.Button(ventana_acceso, text="Validar", command=acceso)
    boton_validar.pack(pady=10)

    #Mostrar el resultado
    resultado = tk.Label(ventana_acceso, text="", font=("Arial", 12))
    resultado.pack(pady=20)

    #Botón cerrar la ventana
    boton_cerrar = tk.Button(ventana_acceso, text="Cerrar", command=ventana_acceso.destroy)
    boton_cerrar.pack(pady=10)