#solicitamos al usuario que introduzca su peso y su altura
peso=float(input("introduzca su peso: "))
altura=float(input("introduzca su altura: "))

#calculamos el IMC
IMC=peso/(altura*altura)
round(IMC,2)

print("si pesas:",peso,"y mides :",altura, "tu IMC es:", IMC)
if IMC>=25:
print("sobrepeso")