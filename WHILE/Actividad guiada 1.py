import random

num_secreto=random.randir(1,20)
print(num_secreto)

numero=int(input("Introduce un numero del 1 al 20"))

while num_secreto!=numero:
    print(f"has introducido el numero {numero}, no has acertado")
    numero=int(input("vuelve a introducir un valor: "))

print ("acertaste")