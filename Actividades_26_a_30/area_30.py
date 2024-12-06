#Crea una función que reciba el radio de un círculo y retorne su área

def area(radio):          #definimos la función área que tome como parámetro el radio
    return 3.1416 * (radio * radio)       #retornamos el area del circulo

radio=float(input("Ingresa el radio del círculo : "))          #solicitamos el radio

print(f"El área del circulo con radio {radio} es: {(area(radio))}")  #llamar a la funcion area e imprimir el resultado