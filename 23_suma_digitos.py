#Solicita un número entero y calcula la suma de sus dígitos

num=input("Ingresa un número entero: ")   #solicitar un número entero

sumdigit=0      #inicializar la variable de suma en 0

for i in num:           #recorrer cada dígito del número
    sumdigit += int(i)  #sumamos el valor del dígito

print(f"La suma de los dígitos es: {sumdigit}")  #mostrar el resultado
