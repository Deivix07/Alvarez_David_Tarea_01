#Crea una función que reciba un nombre como parámetro y retorne un saludo

def saludar(nombre):  #definimos la función que tome como parámetro el nombre
    return (f"¡Hola!, {nombre}")  #retornamos el saludo que incluye el nombre

nombre=input("Ingrese su nombre: ")  #solicitamos el nombre
print(saludar(nombre))               #llamar a la funcion saludar e imprimir el saludo