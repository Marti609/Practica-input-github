import random
numero_aleatorio = random.randint(1, 5)
numero_de_intentos=0
while numero_aleatorio>=1 and numero_aleatorio<=5:
    numero=int(input("Introduce el numero que crees que es: "))
    if numero==numero_aleatorio:
        print("numero acertado")
        break
    elif not numero==numero_aleatorio:
        print("numero no acertado")
        numero_de_intentos=numero_de_intentos+1
    if numero_de_intentos==3:
        break
