# 35. Programa que al introducir un número por teclado permita mostrar ese número de veces tu nombre
# Le pedimos al usuario que introduzca su nombre y un numero
nombre=input("Introduce tu nombre: ")
numerodeveces=int(input("Introduce un numero: "))

# Ahora muestro el nombre las veces que me ha dicho el usuario
for i in range(numerodeveces):
    print(nombre)