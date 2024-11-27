#Calcula y muestra la suma de los números del 1 al 10

suma=0   #inicializar la variable suma en 0

for i in range(1,11):     #usar bucle for con rango de 1 a 10
    suma += i             #sumar el numero a la variable suma

print(f"La suma de los números del 1 al 10 es: {suma}")  #imprimir el resultado final