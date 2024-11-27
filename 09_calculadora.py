#Solicita dos números y una operación (+, -, *, /)
#y realiza el cálculo correspondiente

#solicitar  dos números y la operación
num1=float(input("Ingresa el primer número: "))
num2=float(input("Ingresa el segundo número: "))
op=input("Ingresa la operación (+, -, *, /): ")

#realizar el cálculo según la operación
if op == "+":
    result = num1 + num2
    print(f"La suma de {num1} + {num2} es: {result}")
elif op == "-":
    result = num1 - num2
    print(f"La resta de {num1} - {num2} es: {result}")
elif op == "*":
    result = num1 * num2
    print(f"La multiplicación {num1} * {num2} es: {result}")
elif op == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"La división de {num1} / {num2} es: {result}")
    else:
        print("No se puede dividir entre 0")
else:
    print("Operación no válida")