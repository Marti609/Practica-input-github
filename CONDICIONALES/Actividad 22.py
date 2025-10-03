# 22.Programa que al introducir una nota por teclado te diga si has aprobado o suspendido. Si la nota es menos de un 5 es suspenso y si la nota es 5 o mayor estás aprobado.
# Pedimos que introduzca sus notas

var1= float(input("introduce tu nota: "))

# Calculamos si la nota es aprobado o suspenso

if var1==5:
    print("has sacado un:",var1, "y has aprobado")
elif var1>5:
    print("has sacado un:",var1, "y has aprobado")
elif var1<5:
    print("has sacado un:",var1, "y has suspendido")




