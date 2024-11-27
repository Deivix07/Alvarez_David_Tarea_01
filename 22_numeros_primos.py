#Encuentra e imprime todos los números primos entre 1 y 50

print("Números primos entre 1 y 50:")

for num in range(2, 51):      #usar bucle for del 2 al 50
    #si el número es divisible por 1 y por sí mismo, es primo
    for i in range(2, num):   
        if num % i == 0:      #si hay divisores el número no es primo
            break  
    else:
        print(num)            #si no hay divisores, es primo
