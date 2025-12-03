inicio=int(input("Introduce un numero que sea el inicio: "))
fin=int(input("Introduce un numero que sea el fin: "))
incremento=int(input("Introduce un incremento: "))
concatenar=""

for x in range(inicio,fin,incremento):
    if not x%4==0:
        if x%6==0:
            concatenar=concatenar+"*"+str(x)+ "*" ","
        else:
            concatenar=concatenar+str(x)+","
concatenar=concatenar[:-1]
print(concatenar)