#Calcula el factorial de un número ingresado por el usuario (n!).

num=int(input("Introduzca el número del cual quiere el factorial: "))

factorial = 1       #inicializar la variable en 1
       
for i in range(1,num+1):          #usar bucle for con rango de 1 hasta el numero ingresado
    factorial *= i                #realizar la operacion para factorial
        
print(f"El factorial de {num} es: {factorial}")     #imprimir resultado