#Solicita tres números y determina cuál es el mayor

#solicitar tres números
num1=float(input("Ingresa el primer número: "))
num2=float(input("Ingresa el segundo número: "))
num3=float(input("Ingresa el tercer número: "))

#determinar que número es mayor
if num1 >= num2 and num1 >= num3:
    print(f"El número mayor es: {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"El número mayor es: {num2}")
else:
    print(f"El número mayor es: {num3}")