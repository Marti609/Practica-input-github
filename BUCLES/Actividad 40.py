# 40. Crea un programa que cuente todos los números pares hasta el número 50
pares=0
impares=0
for numero in range(0, 50):
    if numero%2==0:
        pares+=1
    else:
        impares+=1
print(f"El total de pares es: {pares}")
print(f"El total de impares es: {impares}")