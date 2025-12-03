# 57. Realiza un programa que permita adivinar un número comprendido entre 1 y 5. El programa debe controlar si el usuario introduce un número no comprendido entre 1 y 5
import random
numero_aleatorio = random.randint(1, 5)

for i in range(2):
    numero=int(input("Introduce el numero que crees que es: "))
    if numero==numero_aleatorio:
        print("numero acertado")
        break
    else:
        print("numero no acertado")