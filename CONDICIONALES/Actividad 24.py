# 24. Corrige los errores del siguiente código y comprueba que se ejecuta correctamente
var1 = float(input("Introduce el peso: "))
var2 = float(input("Introduce la altura: "))
varimc = var1 / var2**2

# Mostramos el IMC por pantalla
print("Si pesas",var1,"kilos y mides",var2,"tu IMC es:",varimc)

# Comprobamos si tiene sobrepeso o no
if varimc>25:
    print("tienes sobrepeso")
else:
    print("Estás dentro de los parámetros normales")