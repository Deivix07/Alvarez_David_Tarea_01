#Una tienda ofrece un 20% de descuento si el cliente 
#gasta más de $100. Escribe un programa que calcule el monto final

monto=float(input("Ingrese el monto a pagar: $ ")) #solicitar ingresar el monto a pagar

if monto > 100.00 :            #verificar se gasta más de $100
    desc = monto * 0.20        #calcular el 20% de descuento
    montodesc = monto - desc   #calcular el monto final
    print("Aplica descuento del 20 %")
    print(f"Monto final: $ {montodesc}")
else:                          #de lo contrario no aplica descuento
    print("No aplica descuento")
    print(f"Monto final: $ {monto}")