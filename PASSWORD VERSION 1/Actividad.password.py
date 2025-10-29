print("INSTRUCCIONS")
print("1.La longitud del password ha de tenir entre 6 i 8 caràcters")
print("Forçar els següents valors segons la posició indicada:")
print("Posició 0: un numero major o igual que 1 i menor o igual que 5") 
print("Posició 1: una lletra minúscula")
print("Posició 2: una lletra majúscula ")
print("Posició 3: un dels següents símbols *, _, @")
print("Posició 4: una lletra minúscula")
print("Posició 5: un numero major o igual que 6 i menor o igual que 9")
print("Posició 6: un dels següents símbols &, /, #")
print("Posició 7: un numero menor o igual que 5 ")  
password = input("Introdueix la paraula clau: ")

errors = []

#comprobem si la password te entre 6-8 carácters
if not len(password)>8 or not len(password)<6:
    if password[0].isdigit:
        if int(password[0]) >=1 and int(password[0])<=5:
            print("hola")
        else:
            print("Error")

else:
    print(f"Error, el password te una longitud de {len(password)} i no cumpleix els requisits")