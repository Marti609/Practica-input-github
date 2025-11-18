# 38. A partir del programa anterior, establece los rangos para que el usuario no pueda introducir notas inferiores a 0 y superiores a 10
# Pedimos al usuario que introduzca un numero
numerodenotas=int(input("Introduce el numero de notas que deseas introducir: "))

for i in range(numerodenotas):
    nota=float(input("Introduce tu nota:"))
    if nota<0  or nota>10:
        print("Has introducido una nota equivocada")
    else:
        if nota>=5:
            print("Asignatura aprobada")
        elif nota<5:
            print("Asignatura suspendida")
