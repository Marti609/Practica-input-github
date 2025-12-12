#14. Realiza un programa que a partir de introducir el diámetro de un círculo calcule el área y perímetro. Importa la librería match y utiliza el valor PI para hacer el cálculo. Redondea el resultado a un decimal.
import math

#solicitamos al usuario el valor numerico del diametro
diametro=float(input("introduce el valor del diametro del circulo: "))

#hacemos los calculos
radio=diametro/2
perimetro=2*math.pi*radio
area=math.pi*radio**2
arearedondeada=round(area,2)
perimetroredondeado=round(perimetro,2)

#mostramos el resultado de las operaciones por pantalla
print("el perimetro del circulo es:",perimetroredondeado)
print("el area del circulo es:",arearedondeada)
        

