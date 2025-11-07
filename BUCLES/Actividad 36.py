# 36. Programa que sume los n primeros números naturales. n Lo introduce el usuario.
# Pedimos al usuario que introduzca un numero entero
numerodeveces=int(input("Introduce un numero entero positivo: "))

# Hacemos la suma
suma=numerodeveces* (numerodeveces + 1) // 2

# Mostramos la suma por pantalla
print(f"la suma total de numeros naturales es: {suma}")
