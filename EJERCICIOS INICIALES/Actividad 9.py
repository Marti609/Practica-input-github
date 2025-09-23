#pedimos al usuario que introduzca un numero
Segundos=float(input("introduce un numero de segundos para pasarlo a minutos y a horas"))
#realizamos los calculos
Minutos=Segundos/60
Hora=Segundos/3600
#mostramos por pantalla el resultado
print("el numero de minutos son:", Minutos)
print("el numero de horas son:", Hora)
