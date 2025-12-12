#33. Programa un código que permita contar el número de vocales de la siguiente frase: No hay mal que dure cien años
def contar_vocales(frase):
    # Definimos las vocales
    vocales="aeiouáéíóúAEIOUÁÉÍÓÚ"
    #Inicializamos el contador
    contador=0
    # Recorremos cada caracter de la frase
    for caracter in frase:
        if caracter in vocales:
            contador += 1
    return contador

#Frase de ejemplo
frase = "No hay mal que por bien no venga"

#Contar vocales
total_vocales = contar_vocales(frase)

#Mostrar resultado
print(f"La frase '{frase}' tiene {total_vocales} vocales.")