# 53. A partir del código anterior, haz que aparezca al finalizar el programa por pantalla el total las sumas y el número de repeticiones. Con While
repetir="s"
total=0
repeticiones=0

while repetir.lower=="s":
    numero1=int(input("Introduce un numero: "))
    numero2=int(input("Introduce otro numero: "))
    suma=numero1+numero2
    total+=suma
    rpeticiones+=1
    print(f"El resultado de la suma es: {suma}")
    repetir=input("Deseas repetir la operación s/n:")
 
    print(f"La repeticiones totales son: {repeticiones}")
    print(f"La suma total es: {total}")

