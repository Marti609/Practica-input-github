

import math

def calcular_area_circulo(diametro):
    radio = diametro / 2
    area = math.pi * (radio ** 2)
    return area

def calcular_perimetro_circulo(diametro):
    perimetro = math.pi * diametro
    return perimetro

def main():
    try:
        diametro = float(input("Introduce el diámetro del círculo: "))
        if diametro <= 0:
            print("El diámetro debe ser un número positivo.")
            return
        area = calcular_area_circulo(diametro)
        perimetro = calcular_perimetro_circulo(diametro)
        
        print("Área del círculo:", area:)
        print(f"Perímetro del círculo:", perimetro)
        
    except ValueError:
        print("Por favor, introduce un número válido.")

