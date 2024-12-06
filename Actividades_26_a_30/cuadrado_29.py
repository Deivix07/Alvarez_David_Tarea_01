#Escribe una función que reciba un número y retorne su cuadrado

def cuadrado(num):          #definimos la función que tome como parámetro un número
    return num * num        #retornamos el cuadrado de un numero

num=float(input("Ingresa un número: "))          #solicitamos un número

print(f"El cuadrado de {num} es: {(cuadrado(num))}")  #llamar a la funcion cuadrado e imprimir el resultado