a=7
mayores_de_100=0
suma_negativos=0
suma_positivos=0
for i in range(a):
    var=int(input("Introduce un numero: "))
    if var>0 or var==0:
        suma_positivos=suma_positivos+var
    else:
        suma_negativos=suma_negativos-var
    if var>100 or var==100:
        mayores_de_100+=1
print(mayores_de_100)
print(-suma_negativos)
print(suma_positivos)