# 47. Realiza un programa donde el usuario introduzca por teclado 2 intervalos, por pantalla se debe mostrar el rango de números teniendo en cuenta que se a<b la secuencia será incremental y si a>b la secuencia en descenso. Respeta el formato de salida
a=int(input("Introduce el primer número: "))
b=int(input("Introduce el segundo número: "))

if a<b:
    for i in range(a, b+1):
        print(i, end="-")  
elif a>b:
    for i in range(a, b-1, -1):
        print(i, end="-")  
else:
    print("Los numeros son iguales")
