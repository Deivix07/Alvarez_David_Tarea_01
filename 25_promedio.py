#Solicita calificaciones al usuario (hasta que ingrese -1) y calcula el promedio.

#inicializar variables
calificaciones=0
cantidad_calif=0

while True:
    calificacion = float(input("Ingresa las calificaciones (-1 para finalizar): ")) #pedir calificaciones hasta que ingrese -1
    
    if calificacion == -1:   #si se ingresa -1, termina el ciclo
        break
    
    calificaciones += calificacion  # Sumar la calificación a la total
    cantidad_calif += 1  # Contar la cantidad de calificaciones

# Calcular y mostrar el promedio si se ingresaron calificaciones válidas
if cantidad_calif > 0:
    promedio = calificaciones / cantidad_calif
    print(f"Promedio final: {promedio}")
else:
    print("No hay calificaciones")