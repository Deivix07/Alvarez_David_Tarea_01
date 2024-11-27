#Escribe un programa que solicite una contraseña
#y valide si es correcta (ejemplo: contraseña fija es 12345).

#user y password por defecto
user="admin"
passw="admin"

intentos = 3 #número de intentos

while intentos > 0:
    
    usuario=input("Ingrese el usuario: ") #solicitar ingresar el usuario
    contraseña=input("Ingrese la contraseña: ") #solicitar ingresar la contraseña
    
    #validar si conciden
    if usuario == user and contraseña == passw:
        print(f"Bienvenido, {usuario}")
        break  #salir del bucle

    #credenciales son incorrectas restar 1 intento
    intentos -= 1
    if intentos > 0:
        print(f"Credenciales incorrectas. Te queda {intentos} intentos")
    else:
        print("Acceso bloqueado. Has superado el número de intentos")