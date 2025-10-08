#27. Mejora el programa anterior para controlar que el valor introducido es una letra y en caso de introducir un número, aparezca un aviso por pantalla.
# Pedimos al usuario que escriba una letra
var1=input("Introduce una letra: ")

# Comprobamos si es minuscula o mayuscula
if var1.isupper()==True:
    print("La letra es mayuscula")
if var1.islower()==True:
    print("La letra es minuscula")
if var1.isnumeric()==True: 
    print("El valor introducido es un numero")
else:
    print("La letra es mayuscula ¿?")