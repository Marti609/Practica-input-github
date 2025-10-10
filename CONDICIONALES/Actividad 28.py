#28. Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza elif
# Pedimos al usuario que escriba una letra
var1=input("Introduce una letra: ")

# Comprobamos si es minuscula o mayuscula
if var1.isupper()==True:
    print("La letra es mayuscula")
elif var1.islower()==True:
    print("La letra es minuscula")
elif var1.isnumeric()==True: 
    print("El valor introducido es un numero")
else:
    print("El valor introducido es un simbolo")