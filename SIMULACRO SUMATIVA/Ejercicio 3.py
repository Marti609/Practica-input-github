multiplicar=1
cifras=int(input("Introduce el numero de cifras: "))
numero=int(input("Introduce un numero: "))
longituddenumero=len(str(numero))
if longituddenumero==cifras:
    for x in str(cifras):
        multiplicar*int(x)
        if int(x)%2==0:
            
else: 
    print("Longitud no correcta")

print(multiplicar)
