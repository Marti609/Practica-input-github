#31. Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda. Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su índice.
# Asignamos la frase a una variable
frase = "A quién madruga Dios ayuda"

# Palabras a buscar en la frase
palabras_a_buscar = ["quién", "Dios", "ayuda", "noexiste"]

# Recorremos la lista de palabras y mostramos su índice
for palabra in palabras_a_buscar:
    indice = frase.find(palabra)  
    if indice != -1:
        print(f"La palabra '{palabra}' se encuentra en el índice {indice}.")
    else:
        print(f"La palabra '{palabra}' no se encuentra en la frase.")