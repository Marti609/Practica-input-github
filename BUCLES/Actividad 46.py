#
palabra=input("Introduce una palabra: ")
vocales = 'AEIOUaeiouÁÉÍÓÚáéíóú'

lista_consonantes=[]
lista_vocales=[]

for letra in palabra:
    if letra in vocales:
        lista_vocales.append(letra)
    else:
        lista_consonantes.append(letra)

print(f"las consonantes de la palabra {palabra} son: {lista_consonantes}")
print(f"las vocales de la palabra {palabra} son: {lista_vocales}")