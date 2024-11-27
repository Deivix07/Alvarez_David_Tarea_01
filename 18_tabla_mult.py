#Solicita un número al usuario y muestra su tabla de multiplicar del 1 al 10

num=int(input("Ingrese el número del que quiere su tabla de multiplicar: ")) #solicitar un número

print(f"Tabla de multiplicar del {num}")
for i in range(1,11):     #usar bucle for con rango de 1 a 10
    result = num * i      #realizar la operación para cada numero
    print(f"{num} x {i} = {result}")  #imprimir resultado