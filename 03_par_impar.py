#Solicita un número al usuario y determina si es par o impar

num=int(input("Ingrese un número entero: ")) #solicitar ingresar un número

if num % 2 == 0 :       #verificar si es par (si el residuo de dividir entre 2 es 0)
    print("El número es par") 
else:                   #verificar si es impar
    print("El número es impar")