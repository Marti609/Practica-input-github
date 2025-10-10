nombre= input("introduce tu nombre: ")
nombre_mayus=nombre.upper()
edad=int(input("introduce tu edad: "))
año_actual=2025
futuro=año_actual+(100-edad)
if edad>=0 or edad>100:
    print(f"hola {nombre_mayus} cumpliras 100 años en el año {futuro}")
else:
    print("edad no valida")