#13.Realiza un programa que, a partir introducir el lado de un cubo, presente por pantalla el área y para calcular el volumen utiliza el operador de exponente.
# Solicitar al usuario el lado del cubo
lado=float(input("Introduce el lado del cubo: "))

# Calcular el área del cubo (6 * lado^2)
area=6*lado**2

# Calcular el volumen del cubo (lado^3)
volumen=lado**3

# Mostrar los resultados de las operaciones por pantalla
print("El área del cubo es:", area)
print("El volumen del cubo es:", volumen)

