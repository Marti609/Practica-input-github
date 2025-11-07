# 37. Programa que pregunte cuantas notas quiero introducir y para cada nota diga si estoy aprobado o suspendido.
numerodenotas=int(input("Introduce el numero de notas que deseas introducir: "))

for i in range(numerodenotas):
    nota=float(input(f"Introduce tu nota:"))   
    if nota>=5:
     print("Asignatura aprobada")
    elif nota<5:
        print("Asignatura suspendida")
