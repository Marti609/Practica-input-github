# 39. Programa que pida n números y que, tras introducir el último número, debe aparecer por pantalla el número total de positivos, negativos y número de 0.
cantidad_de_numeros=int(input("Introduce la cantidad de numeros que deseas introducir: "))

numeros_positivos=0
numeros_negativos=0
cantidad_de_0=0

for i in range(cantidad_de_numeros):
    numero=float(input("Introduce un numero: "))
    if numero>0:
        numeros_positivos += 1
    elif numero<0:
        numeros_negativos += 1
    elif numero==0:
        cantidad_de_0 += 1
print(f"La cantidad de números positivos es: {numeros_positivos}")
print(f"La cantidad de números negativos es: {numeros_negativos}")
print(f"La cantidad de 0 es: {cantidad_de_0}")
