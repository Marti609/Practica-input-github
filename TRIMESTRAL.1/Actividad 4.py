valor=50
numero=int(input("Introduce un numero: "))

if numero%2==0:
    valor=valor+numero
else:    
    valor=valor-numero
print(valor)

while (valor<=60) and (numero>0):
    numero=int(input("Introduce un numero: "))
    if numero%2==0:
        valor=valor+numero
    else:    
        valor=valor-numero
    print(valor)  
print("fin del programa")