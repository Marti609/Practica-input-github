import math #importar libreria de mates

#solicitamos al usuario que introduzca un numero
numero=float(input("Introduce un numero: ")) 
raiz=math.sqrt(numero)
divison_entera=int(raiz//2)

#mostramos el resultado por pantalla
print("La raiz cuadrada dividida entre 2:",(divison_entera))
print("La raiz cuadrada es:",raiz)
