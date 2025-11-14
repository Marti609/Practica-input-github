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
