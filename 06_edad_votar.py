#Solicita la edad del usuario y determina 
#si es elegible para votar (mayor o igual a 18 años)

num=int(input("Ingrese la edad: ")) #solicitar ingresar la edad

if num >= 18:         #verificar si es mayor de 18 años
    print("Mayor de edad, puedes votar") 
else:                 #de lo contrario es menor de 18 años
    print("Menor de edad, no puedes votar")