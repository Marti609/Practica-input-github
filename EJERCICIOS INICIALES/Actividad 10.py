# Solicitar al usuario los números
dividendo=int(input("Introduce el dividendo: "))
divisor=int(input("Introduce el divisor: "))

# Calcular cociente y resto
cociente=dividendo / divisor
resto=dividendo % divisor

# Determinar si el dividendo es par o impar
if dividendo % 2 == 0:
    paridad = "par"
else:
    paridad = "impar"

# Mostrar resultados por pantalla
print("El cociente es:",cociente)
print("El resto es:",resto)
print("El dividendo es:",paridad)