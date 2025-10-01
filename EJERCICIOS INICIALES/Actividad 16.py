#16. Utiliza el método sqrt de la librería math para calcular la raíz cuadrada de un número. El resultado de la raíz cuadrada divídelo entre 2 de manera que se obtenga siempre un resultado entero. Haz que se muestre por pantalla los dos resultados de todo el proceso (raíz y división).
import math #importar libreria de mates

#solicitamos al usuario que introduzca un numero
numero=float(input("Introduce un numero: ")) 
raiz=math.sqrt(numero)
divison_entera=int(raiz//2)

#mostramos el resultado por pantalla
print("La raiz cuadrada dividida entre 2:",(divison_entera))
print("La raiz cuadrada es:",raiz)
