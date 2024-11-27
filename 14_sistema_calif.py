#Solicita una calificación numérica y devuelve la letra correspondiente:
	#90-100: A.
	#80-89: B.
	#70-79: C.
	#60-69: D.
	#Menor a 60: F.

calif=float(input("Ingresa la calificación: "))

if 90 <= calif <=100:
    print("Tu calificación es: A")
elif 80 <= calif < 90:
    print("Tu calificación es: B")
elif 70 <= calif < 80:
    print("Tu calificación es: C")
elif 60 <= calif < 70:
    print("Tu calificación es: D")
else:
    print("Tu calificación es: F")