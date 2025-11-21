#52. Realiza un programa que sume dos números enteros por teclado y presente el resultado por pantalla. El programa preguntará si deseas o no repetir la operación. Con While
repetir="s"

while repetir=="s":
    numero1=int(input("Introduce un numero: "))
    numero2=int(input("Introduce otro numero: "))
    suma=numero1+numero2
    print(f"El resultado de la suma es: {suma}")
    repetir=input("Deseas repetir la operación s/n:")
    if repetir=="n":
        break
print("Programa finalizado")