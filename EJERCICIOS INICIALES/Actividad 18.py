#introducimos el valor de precio
precio=12

#pedimos al usuario que introduzca el numero de los mayores y menores de 18
menor=int(input("introduce el numero de los menores de 18 años:"))
mayor=int(input("intrtodcue el numero de los mayores de 18 años:"))

#hacemos los calculos
precio_menor=precio*0.5, 
round(precio_menor,3)
precio_mayor=precio*0.9
round(precio_mayor,3)
total_mayor=mayor*precio_mayor
total_menor=menor*precio_menor

#mostramos por pantalla el resultado
print("el precio total de cine de",mayor,"mayores de 18 años es:",total_mayor)
print("el precio total de cine de",menor,"menores de 18 años es:",total_menor)
