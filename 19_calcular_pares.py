#Imprime todos los números pares entre 1 y 20

suma=0    #inicializar la variable suma en 0

for i in range(1,21):     #usar bucle for con rango de 1 a 20
    if i % 2 == 0:        #verificar si el numero es par
        print(f"{i}")     #imprimir los números