#Escribe un programa que solicite un número y 
#determine si es mayor o menor que 10

num=int(input("Ingrese un número: ")) #solicitar ingresar un número

if num == 10:                         #verificar si el número es igual a 10
    print("El número ingresado es igual que 10") 
elif num > 10:                        #verificar si el número es mayor a 10
    print("El número ingresado es mayor que 10")
else:                                 #condición si el número es menor a 10
    print("El número ingresado es menor que 10")