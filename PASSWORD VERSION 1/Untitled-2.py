print("INSTRUCCIONS")
print("1. La longitud del password ha de tenir entre 6 i 8 caràcters")
print("Forçar els següents valors segons la posició indicada:")
print("Posició 0: un número major o igual que 1 i menor o igual que 5")
print("Posició 1: una lletra minúscula")
print("Posició 2: una lletra majúscula")
print("Posició 3: un dels següents símbols *, _, @")
print("Posició 4: una lletra minúscula")
print("Posició 5: un número major o igual que 6 i menor o igual que 9")
print("Posició 6: un dels següents símbols &, /, #")
print("Posició 7: un número menor o igual que 5")

# Demanem la contrasenya
password=input("Introdueix la contrasenya: ")

errors=[]  

# Comprovem si la longitud es entre 6 i 8 caràcters
if len(password)<6 or len(password)>8:
    print(f"Error, el password té una longitud de {len(password)} caràcters i no compleix els requisits")
else:
    # Comprovem cada posició

    # Comprovem si la posició 0 es correcte
    if not password[0].isdigit() or not (1<=int(password[0])<=5):
        errors.append("Error en el caràcter 1")

    # Comprovem si la posició 1 es correcte
    if not password[1].islower():
        errors.append("Error en el caràcter 2")

    # Comprovem si la posició 2 es correcte
    if not password[2].isupper():
        errors.append("Error en el caràcter 3")

    # Comprovem si la posició 3 es correcte
    if password[3] not in ["*", "_", "@"]:
        errors.append("Error en el caràcter 4")

    # Comprovem si la posició 4 es correcte
    if not password[4].islower():
        errors.append("Error en el caràcter 5")

    # Comprovem si la posició 5 es correcte
    if not password[5].isdigit() or not (6<=int(password[5])<=9):
        errors.append("Error en el caràcter 6")

    # Comprovem si la posició 6 es correcte
    if len(password)>=7:
        if password[6] not in ["&", "/", "#"]:
            errors.append("Error en el caràcter 7")

    # Comprovem si la posició 7 es correcte
    if len(password)==8:
        if not password[7].isdigit() or int(password[7])>5:
            errors.append("Error en el caràcter 8")

    # Resultat final
    if len(errors)==0:
        print("El format del PASSWORD és correcte ")
    else:

        print(e)
