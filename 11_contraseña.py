#Escribe un programa que solicite una contraseña
#y valide si es correcta (ejemplo: contraseña fija es 12345).

key="Rx4832"

contraseña=input("Ingrese una contraseña: ") #solicitar ingresar la contraseña

if contraseña == key:   #verificar si las contraseñas coinciden
    print("Contraseña correcta") 
else:                   #de lo contrario es incorrecta
    print("Contraseña incorrecta")