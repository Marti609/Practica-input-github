#5. Programa que pida cinco palabras y muestre una frase con las cinco. Modifica el código para que entre palabra y palabra haya una coma
#solicitar 5 palabras
texto1 = input("introduce primera palabra")
texto2 = input("introduce segunda palabra")
texto3 = input("introduce tercera palabra")
texto4 = input("introduce cuarta palabra")
texto5 = input("introduce quinta palabra")

#determinamos las variables frase1 y frase2
frase1 = f"Las palabras que has introducido son: {texto1} {texto2} {texto3} {texto4} {texto5}."

frase2 = f"Las palabras que has introducido son: {texto1}, {texto2}, {texto3}, {texto4}, {texto5}."

#mostramos por pantalla las palabras introducidas
print(frase1)
print(frase2)