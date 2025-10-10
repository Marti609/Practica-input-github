# 21. Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz cuadrada no de un valor negativo
# Pedimos al usuario los coeficientes de la ecuación
import math
a=float(input("Introduce el coeficiente a: "))
b=float(input("Introduce el coeficiente b: "))
c=float(input("Introduce el coeficiente c: "))

# Verificamos que sea una ecuación de segundo grado
if a==0:
    print("No es una ecuación de segundo grado.")
else:
    # Calculamos el discriminante
    discriminante=b**2-4*a*c
    if discriminante<0:
        print("la raiz no puede ser un numero negativo")
    else:
        # Calculamos las raíces
        r1=(-b + math.sqrt(discriminante)) / (2*a)
        r2=(-b - math.sqrt(discriminante)) / (2*a)
        
        # Mostramos las raíces por pantalla
        if r1==r2:
            print("Raíz doble:", r1)
        else:
            print("Raíces:",r1,"y",r2)