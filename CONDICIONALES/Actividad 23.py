#23. Modifica el programa anterior para establecer si la nota es un excelente (8.5 a 10), un notable (>=6.5 -<8.5), satisfactorio (<6.5 -5) o insuficiente (<5). Controla que la nota introducida esté entre 0 y 10. Utilizar elif sin operadores lógicos.
# Pedimos que introduzca sus notas

var1=float(input("introduce tu nota: "))

# Calculamos si la nota es satisfactorio, excelente, notable o insatisfacotio

if var1<5:
    print("has sacado un:",var1, "y has sacado un insuficiente")
elif var1>8.5:
    print("has sacado un:",var1," y has sacado un excelente")
elif var1>=6.5:
    print("has sacado un:",var1," y has sacado un notable")
elif var1<6.5:
    print("has sacado un:",var1," y has sacado un satisfactorio")
elif var1==5:
    print("has sacado un:",var1," y has sacado un satisfactorio")
