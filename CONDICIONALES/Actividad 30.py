#30. Realiza un programa que controle si la longitud de una frase introducida por teclado es igual, menor o mayor de 11 caracteres. Utiliza elif
#Pedimos al usuario que introudzca una frase
frase=input("introduce una frase: ")

#Calculamos la longitud de la frase
longitud_frase=len(frase)

#Calculamos si la longitud es menor. mayor o igual a 11
if longitud_frase==11:
    print("la longitud es igual a 11")
elif longitud_frase>11:
    print("la longitud es mayor que 11")
else:
    print("la longitud es menor que 11")
