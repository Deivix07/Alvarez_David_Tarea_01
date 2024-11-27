#Solicita la calificación de un estudiante y determina 
#si está aprobado (mayor o igual a 7) o reprobado

calif=float(input("Ingrese la calificación: ")) #solicitar ingresar una calificación

if calif >= 7 :       #verificar si es mayor o igual a 7
    print("Aprobado") 
else:                 #de lo contrario es menor a 7
    print("Reprobado")