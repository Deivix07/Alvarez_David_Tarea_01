#Genera un número aleatorio entre 1 y 10 y solicita al usuario
#que adivine el número. Usa if para verificar si acertó o no.

import random  #importar random para generar números aleatorios

num_aleatorio = random.randint(1, 10)   #generar un número aleatorio

num=int(input("Adivina el número entre 1 y 10: "))   #solicitar al usuario que adivine el número

#verificar si el número adivinado es correcto
if num == num_aleatorio:
    print("¡Felicidades, acertaste!")
else:
    print("Intenta de nuevo")