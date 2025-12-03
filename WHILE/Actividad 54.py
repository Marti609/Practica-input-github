# 54. Modifica el programa anterior y haz que se repita el ciclo automáticamente hasta que el total de todas las sumas sea superior a 50, será entonces cuando el programa finalice. No hará falta preguntar si deseas repetir la operación. En cada operación aparece por pantalla la suma de la operación y su acumulado. Para aquellos de vosotros que os fijáis en los detalles, controlar que el mensaje del acumulado es singular o plural.. . Con While
repetir="s"
total=0
operaciones=0

while repetir.lower=="s":
    numero1=int(input("Introduce un numero: "))
    numero2=int(input("Introduce otro numero: "))
    suma=numero1+numero2
    total+=suma
    operaciones+=1
    print(f"El resultado de la suma es: {suma}")
    repetir=input("Deseas repetir la operación s/n:")
    if operaciones==1:
        print(f"La suma de todo es : {total} y llevas {operaciones} repeticiones")
    else:
        print(f"La suma total es: {total} y has hecho {operaciones} repeticiones")
        print("Fin del programa")