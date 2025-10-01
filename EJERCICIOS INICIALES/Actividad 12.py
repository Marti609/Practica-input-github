#12.Realiza un programa que, introduciendo en los valores de lado, base menor, base mayor y altura de un trapecio isósceles, nos devuelva por pantalla en el área y el perímetro.
#pedimos que introduzca varios numeros
lados=float(input("introduce el valor de los lados: "))
basemenor=float(input("introduce el valor de la basemenor: "))
basemayor=float(input("introduce el valor de la basemayor: "))
altura=float(input("introduce el valor de la altura: "))
#hacemos los calculos
perimetro=basemenor+basemayor+2*lados
area=(basemenor+basemayor)+altura/2
#mostramos el resultado por pantalla
print("el perimetro del trapecio isosceles es:", perimetro)
print("el area del trapecio isosceles es:", area)

