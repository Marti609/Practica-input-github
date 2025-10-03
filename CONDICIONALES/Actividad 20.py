#20. A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados números entre 0 y 10
#solicitamos los dos numeros
var1=float(input("introduce un numero entre el 1-10: "))
var2=float(input("introduce otro numero entre el 1-10: "))

#mostramos el resultado por pantalla
if var1>10:
    print("el numero o los numeros introducidos son mayor que 10 o menor que 0")
elif var1<0:
    print("el numero o los numeros introducidos son mayor que 10 o menor que 0")
elif var2>10:
    print("el numero o los numeros introducidos son mayor que 10 o menor que 0")
elif var2<0:
    print("el numero o los numeros introducidos son mayor que 10 o menor que 0")
elif var1>var2:
    print("el numero", var1,"es mas grande que", var2)
elif var1==var2:
    print("el numero", var1,"es igual a", var2)
elif var1<var2:
    print("el numero", var2,"es mas grande que", var1)

