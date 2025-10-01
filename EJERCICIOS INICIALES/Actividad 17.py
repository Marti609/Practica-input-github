#17. Calcula el índice de masa corporal IMC de una persona, introduciendo por teclado el peso (en kg) y dividiendo por la estatura (en metros y elevado al cuadrado). Si el resultado es igual o superior a 25, debe aparecer un mensaje informando de sobrepeso.
#solicitamos al usuario que introduzca su peso y su altura
peso=float(input("introduzca su peso: "))
altura=float(input("introduzca su altura: "))

#calculamos el IMC
IMC=peso/(altura*altura)
round(IMC,2)

#mostramos el resultado por pantalla
print("si pesas:",peso,"y mides :",altura, "tu IMC es:", IMC)
if IMC>=25:
    print("tienes sobrepeso")
