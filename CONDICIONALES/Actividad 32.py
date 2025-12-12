#32. Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para no distinguir entre mayúsculas y minúsculas
# Asignamos la frase a una variable
frase="A quién madruga Dios ayuda"

# Convertimos la frase a minúsculas 
frase_minuscula=frase.lower()

# Palabras a buscar
palabras_a_buscar=["quién", "dios", "ayuda", "noexiste"]

# Recorremos la lista de palabras y mostramos su índice
for palabra in palabras_a_buscar:
    # Convertimos la palabra a minúsculas para la búsqueda
    indice = frase_minuscula.find(palabra.lower())  
    if indice!=-1:
        print(f"La palabra '{palabra}' se encuentra en el índice {indice}.")
    else:
        print(f"La palabra '{palabra}' no se encuentra en la frase.")