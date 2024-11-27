#Solicita al usuario un número y
#determina si es positivo, negativo o cero

num=int(input("Ingrese un número entero: ")) #solicitar ingresar un número

if num == 0:                         #verificar si el número es cero
    print("El número ingresado es cero") 
elif num > 0:                        #verificar si el número es positivo
    print("El número ingresado es positivo")
else:                                 #condición si el número es negativo
    print("El número ingresado es negativo")