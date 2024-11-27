#Solicita una edad y clasifica al usuario como 
#niño (0-12), adolescente (13-17) o adulto (18+)

edad=int(input("Ingresa la edad: "))   #solicitar la edad

#determinar a que grupo corresponde
if 0 <= edad <= 12:
    print("Eres un niño")
elif 13 <= edad <= 17:
    print("Eres un adolescente")
else:
    print("Eres un adulto")