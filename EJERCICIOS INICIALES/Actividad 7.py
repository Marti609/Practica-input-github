#solicitar dos numeros
var1=int(input("introduce un numero"))
var2=int(input("introduce otro numero"))

#realizamos las operaciones
total1=var1+var2
total2=var1-var2
total3=var1*var2
total4=var1/var2
total5=var1%var2
total6=var1//var2
total7=var1**var2

divisiondosdecimales=round(total4, 2)

#mostramos por pantalla los resultados
print("la suma de los dos numeros es:", total1)
print("la resta de los dos numeros es:", total2)
print("la multiplicación de los dos numeros es:", total3)
print("la división redondeada de los dos numeros es:", divisiondosdecimales)
print("el resto de los dos numeros es:", total5)
print("la división entera de los dos numeros es:", total6)
print("la pótencia de los dos numeros es:", total7)