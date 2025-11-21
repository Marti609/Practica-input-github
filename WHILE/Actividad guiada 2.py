edad=int(input("Introduce la edad: "))

while edad>99 or edad<=0:
    print("Edad incorrecta")
    edad=int(input("Introduce la edad: "))
    if edad==999:
        break