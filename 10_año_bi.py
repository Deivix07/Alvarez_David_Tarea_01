#Solicita un año y determina si es bisiesto
#(divisible entre 4 pero no entre 100, excepto si es divisible entre 400)

año=int(input("Ingresa un año: "))     #solicitar el año

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):    #verificar si el año es bisiesto
    print(f"El año {año} es bisiesto.")
else:                  #de lo contrario no es bisiesto
    print(f"El año {año} no es bisiesto.")