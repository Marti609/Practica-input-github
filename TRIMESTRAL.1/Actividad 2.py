suma_positivos=0
suma_negativos=0

for i in range(6):
    numero=int(input("Introduce 6 numeros: "))
    if numero>=0:
        suma_positivos=suma_positivos+numero
    else:
        suma_negativos=suma_negativos+numero
print(f"La suma de los numeros positivos es: {suma_positivos}")
print(f"La suma de los numeros negativos es: {suma_negativos}")