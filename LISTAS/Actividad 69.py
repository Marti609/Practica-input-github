#69. Realiza un programa que permita introducir una cantidad exacta de números, cada número se irá almacenando en una lista. El programa debe finalizar presentando por pantalla los números ordenados de menor a mayor
milista=[]
longitud=int(input("Introduce la cantidad de números que quieres ingresar: "))

for i in range(0,longitud):
    num=int(input("Introduce un numero: "))
    milista.append(num)

milista.sort()
print(milista)