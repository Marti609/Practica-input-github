#9.programa que pida los segundos y muestre por pantalla y en la misma frase los minutos y las horas
#pedimos al usuario que introduzca un numero
Segundos=float(input("introduce un numero de segundos para pasarlo a minutos y a horas"))
#realizamos los calculos
Minutos=Segundos/60
Hora=Segundos/3600
#mostramos por pantalla el resultado de las operaciones
print("el numero de minutos son:", Minutos)
print("el numero de horas son:", Hora)
