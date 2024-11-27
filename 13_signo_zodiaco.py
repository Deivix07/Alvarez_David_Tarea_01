#Solicita el día y mes de nacimiento y determina
#el signo zodiacaldel usuario.

#solicitar el día y el mes de nacimiento
dia=int(input("Ingresa el día de tu nacimiento (1-31): "))
mes=input("Ingresa el mes de tu nacimiento (enero,febrero,...): ").lower()

#determinar el signo zodiacal según en el mes y día
if (mes == "enero" and dia >= 20) or (mes == "febrero" and dia <= 18):
    signo = "Acuario"
elif (mes == "febrero" and dia >= 19) or (mes == "marzo" and dia <= 20):
    signo = "Piscis"
elif (mes == "marzo" and dia >= 21) or (mes == "abril" and dia <= 19):
    signo = "Aries"
elif (mes == "abril" and dia >= 20) or (mes == "mayo" and dia <= 20):
    signo = "Tauro"
elif (mes == "mayo" and dia >= 21) or (mes == "junio" and dia <= 20):
    signo = "Géminis"
elif (mes == "junio" and dia >= 21) or (mes == "julio" and dia <= 22):
    signo = "Cáncer"
elif (mes == "julio" and dia >= 23) or (mes == "agosto" and dia <= 22):
    signo = "Leo"
elif (mes == "agosto" and dia >= 23) or (mes == "septiembre" and dia <= 22):
    signo = "Virgo"
elif (mes == "septiembre" and dia >= 23) or (mes == "octubre" and dia <= 22):
    signo = "Libra"
elif (mes == "octubre" and dia >= 23) or (mes == "noviembre" and dia <= 21):
    signo = "Escorpio"
elif (mes == "noviembre" and dia >= 22) or (mes == "diciembre" and dia <= 21):
    signo = "Sagitario"
elif (mes == "diciembre" and dia >= 22) or (mes == "enero" and dia <= 19):
    signo = "Capricornio"

print(f"Tu signo zodiacal es: {signo}")    #mostrar el signo zodiacal
