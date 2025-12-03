cifras=int(input("Introduce un numero de cifras: "))
numero=input("Introduce un nuemro con esa cantidad de cifras: ")
longitud_numero=len(numero)
suma=0

if longitud_numero==cifras:
    for i in (numero):
        suma+=int(i)
    print(f"El resaultado es: {suma}")
else:
    print("Error, no coincide el numero de cifras")

        