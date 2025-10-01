#19. Programa que introduzca dos números y devuelva cuál de los dos es mayor, menor o son iguales
#solicitamos los dos numeros
var1=float(input("introduce un numero: "))
var2=float(input("introduce otro numero: "))

if  var1>var2:
    print("el numero", var1,"es mas grande que", var2)
elif var1==var2:
    print("el numero", var1,"es igual a", var2)
elif var1<var2:
    print("el numero", var2,"es mas grande que", var1)


