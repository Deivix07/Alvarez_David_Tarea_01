#Solicita un número entero y muestra su versión invertida

num=input("Ingresa un número entero: ")   #solicitar un número entero

num_invert=""     #inicializar la variable con una cadena vacia

for i in num:                       #recorrer cada dígito del número
    num_invert = i + num_invert     #concatenar el dígito al principio

print(f"El número invertido es: {num_invert}")  #mostrar el numero invertido