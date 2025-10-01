#15. Utiliza el valor Pi de la librería math para calcular el área y volumen de un cilindro, introduciendo por teclado el valor de radio y altura. Resultado con 2 decimales.
import math

#solicitamos al usuario que introduzca el valor de radio y el de la altura
radio=float(input("introduce el valor del radio del circulo"))
altura=float(input("introduce el valor de la altura del cilindro"))

#hacemos los calculos
volumen=math.pi*radio**2*altura
area=2*math.pi*radio*altura+2*math.pi*radio**2
volumenredondeado=round(volumen,2)
arearedondeada=round(area,2)

#mostramos el resultado por pantalla
print("el volumen del cilindro es:",volumenredondeado)
print("el area del cilindro es:",arearedondeada)
