#26. Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición.
# Pedimos al usuario que escriba una letra
var1=input("Introduce una letra: ")

# Comprobamos si es minuscula o mayuscula
if var1.isupper()==True:
    print("La letra es mayuscula")
elif var1.islower()==True:
    print("La letra es minuscula")
else: 
    print("Error")