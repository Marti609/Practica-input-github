# Pedimos al usuario los coeficientes de la ecuación
import math
a = float(input("Introduce el coeficiente a: "))
b = float(input("Introduce el coeficiente b: "))
c = float(input("Introduce el coeficiente c: "))

# Verificamos que sea una ecuación de segundo grado
if a == 0:
    print("No es una ecuación de segundo grado.")
else:
    # Calculamos el discriminante
    discriminante = b**2 - 4*a*c
    
    # Revisamos si hay raíces reales
    if discriminante < 0:
        print("No hay raíces reales.")
    else:
        # Calculamos las raíces
        r1 = (-b + math.sqrt(discriminante)) / (2*a)
        r2 = (-b - math.sqrt(discriminante)) / (2*a)
        
        # Mostramos las raíces
        if r1 == r2:
            print("Raíz doble:", r1)
        else:
            print("Raíces:",r1,"y", r2)