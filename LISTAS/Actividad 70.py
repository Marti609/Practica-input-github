#70. Crea un programa que permita introducir x palabras en una lista llamada lista1. Una vez introducidas, crea una nueva lista, llamada lista2, exactamente igual a lista1. Se deben mostrar por pantalla el contenidos de lista1 en orden ascendente y lista2 en orden descendente. Respeta el formato de entrada y salida tal y como se muestra en el testeo.
milista1=[]
milista2=[]
longitud=int(input("Introduce la cantidad de palabras que quieres ingresar: "))

for i in range(0,longitud):
    palabras=input("Introduce una palabra: ")
    milista1.append(palabras)
    milista2.append(palabras)

milista1.sort()
milista2.sort(reverse=True)

print(milista1)
print(milista2)