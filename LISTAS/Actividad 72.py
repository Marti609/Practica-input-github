# Función que cambia las letras con acento a normal
def normalizar(letra):
    letra = letra.lower()  # pasa a minúscula
    reemplazos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
    return reemplazos.get(letra, letra)  # si la letra es acentuada la cambia, si no, la deja igual

letras_nuevas = []
letras_repetidas = []

while True:
    letra = input("Escribe una letra: ").strip()
    if len(letra) != 1:
        print("Pon solo UNA letra, por favor.")
        continue
    
    letra_norm = normalizar(letra)
    
    if letra_norm in letras_nuevas:
        print(f"La letra '{letra}' ya estaba.")
        if letra_norm not in letras_repetidas:
            letras_repetidas.append(letra_norm)
    else:
        letras_nuevas.append(letra_norm)
    
    seguir = input("¿Quieres poner otra letra? (si/no): ").lower()
    if seguir != 'si':
        break

print("Letras que escribiste:", letras_nuevas)
print("Letras que se repitieron:", letras_repetidas)