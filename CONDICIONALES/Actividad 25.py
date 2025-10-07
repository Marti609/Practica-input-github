#25. Repite el programa número 23 pero en esta ocasión utilizando operadores lógicos.
# Pedimos que introduzca su nota

var1=float(input("introduce tu nota: "))

# Calculamos si la nota es satisfactorio, excelente, notable o insatisfacotio
if var1>10 or var1<0:
    print("la nota no es valida")
elif var1>5 and var1<6.5 or var1==5:
    print(f"tu nota es {var1}, y has sacado un satisfactorio")
elif var1>6.5 and var1<8.5 or var1==6.5:
    print(f"tu nota es {var1}, y has sacado un notable")
elif var1<5:
    print(f"tu nota es {var1}, y has suspendido")
elif var1>8.5 or var1==8.5:
    print(f"tu nota es {var1}, y has sacado un excelente")
