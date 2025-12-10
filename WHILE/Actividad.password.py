print("INSTRUCCIONS")
print("1.La longitud del password ha de tenir entre 6 i 8 caràcters")
print("Forçar els següents valors segons la posició indicada:")
print("Posició 1: un numero major o igual que 1 i menor o igual que 5") 
print("Posició 2: una lletra minúscula")
print("Posició 3: una lletra majúscula ")
print("Posició 4: un dels següents símbols *, _, @")
print("Posició 5: una lletra minúscula")
print("Posició 6: un numero major o igual que 6 i menor o igual que 9")
print("Posició 7: un dels següents símbols &, /, #")
print("Posició 8: un numero menor o igual que 5 ")  

# Demano al usuari que posi contrasenya
password=input("Introdueix la contrasenya: ")

errors=[]  

# Ara comprovo si la contrasenya te una longitud de 6-8 caràcters
if len(password)<6 or len(password)>8:
    print(f"Error, el password té una longitud de {len(password)} caràcters i no compleix els requisits")
else:
    # Ara comrpovo posició per posició

    # Comprovo si la posició 0 es correcte es a dir si es un número major o igual que 1 i menor o igual que 5
    if not password[0].isdigit() and password[0]>=1 and password[0]<=5:
        errors.append("Error en el caràcter 1")

    # Comprovo si la posició 1 es correcte es a dir si es una lletra minúscula
    if not password[1].islower():
        errors.append("Error en el caràcter 2")

    # Comprovo si la posició 2 es correcte es a dir si es una lletra majúscula
    if not password[2].isupper():
        errors.append("Error en el caràcter 3")

    # Comprovo si la posició 3 es correcte es a dir si es un dels següents símbols *, _, @"
    if password[3] not in ["*", "_", "@"]:
        errors.append("Error en el caràcter 4")

    # Comprovo si la posició 4 es correcte es a dir si es una lletra minúscula
    if not password[4].islower():
        errors.append("Error en el caràcter 5")

    # Comprovo si la posició 5 es correcte es a dir si es un número major o igual que 6 i menor o igual que 9
    if not password[5].isdigit() and password[5]>=6 and password[5]<=9:
        errors.append("Error en el caràcter 6")

    # Comprovo si la posició 6 es correcte es a dir si es un dels següents símbols &, /, #"
    if len(password)>=7:
        if password[6] not in ["&", "/", "#"]:
            errors.append("Error en el caràcter 7")

    # Comprovo si la posició 7 es correcte es a dir si es un número menor o igual que 5
    if len(password)==8:
        if not password[7].isdigit() and password[7]<=5:
            errors.append("Error en el caràcter 8")

    # Mostro per pantalla si el password que ha introduit l'usuari es correcte o no, i també li mostro en quins caràcters ha comès errors
    if len(errors)==0:
        print("El format del PASSWORD és correcte")
    else:
        print(errors)


