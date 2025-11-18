# 45. Realiza un programa que permita introducir una palabra por teclado y puedas recorrer el stringdistinguiendo vocales y las consonantes:
palabra=input("Introduce una palabra: ")
vocales="aeiouáéíóú"

lista_consonantes=[]
lista_vocales=[]

for letra in palabra:
    if letra in vocales:
        lista_vocales.append(letra)
    else:
        lista_consonantes.append(letra)

print(f"las consonantes de la palabra {palabra} son: {lista_consonantes}")
print(f"las vocales de la palabra {palabra} son: {lista_vocales}")