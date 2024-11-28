#Escribe una función que reciba dos números como parámetros y retorne su suma

def suma(num1,num2):          #definimos la función que tome como parámetro los números
    return num1 + num2        #retornamos la suma de los dos números

#solicitamos dos números
num1=float(input("Ingresa el primer número: "))
num2=float(input("Ingresa el segundo número: "))

print(suma(num1,num2))        #llamar a la funcion suma e imprimir el resultado