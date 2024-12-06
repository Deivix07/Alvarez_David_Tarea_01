#Crea una función que reciba un número y retorne True si es par y False si es impar

def par_impar(num):         #definimos la función que tome como parámetro un número
    if num % 2 == 0 :       #verificar si es par y retornar True
        return True
    else:                   #caso contrario impar y retornar False
        return False
    
num=int(input("Ingrese un número entero: ")) #solicitar ingresar un número
print(par_impar(num))                        #llamar a la funcion par_impar e imprimir True o False