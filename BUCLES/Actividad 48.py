# 48. Realiza un programa que introduzcas por teclado una palabra ‘secreta’, consigue la longitud de esa palabra para que sea ese el criterio que establezca el rango del bucle de manera que el usuariotenga x oportunidades para ver si letra introducida está en esa palabra.
palabra_secreta = input("Introduce la palabra secreta: ").strip().lower()

# Obtener longitud de la palabra
longitud = len(palabra_secreta)
print(f"La palabra tiene {longitud} letras.")

# Crear lista para guardar el estado de adivinanza
estado_actual = ["_"] * longitud

# Número de intentos permitidos
intentos = 6

# Conjunto de letras ya adivinadas
letras_adivinadas = set()

while intentos > 0 and "_" in estado_actual:
    print("
Palabra: " + " ".join(estado_actual))
    print(f"Te quedan {intentos} intentos.")
    letra = input("Introduce una letra: ").strip().lower()

    if len(letra) != 1 or not letra.isalpha():
        print("Por favor, introduce solo una letra válida.")
        continue

    if letra in letras_adivinadas:
        print("Ya has intentado esa letra.")
        continue

    letras_adivinadas.add(letra)

    if letra in palabra_secreta:
        print(f"¡Bien! La letra '{letra}' está en la palabra.")
        # Actualizar estado actual
        for i, c in enumerate(palabra_secreta):
            if c == letra:
                estado_actual[i] = letra
    else:
        print(f"La letra '{letra}' no está en la palabra.")
        intentos -= 1

# Resultado final
if "_" not in estado_actual:
    print(f"
¡Felicidades! Has adivinado la palabra: {palabra_secreta}")
else:
    print(f"
Se acabaron los intentos. La palabra era: {palabra_secreta}")
