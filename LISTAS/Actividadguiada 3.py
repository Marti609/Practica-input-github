

entrada = input("Introduce los valores separados por un guion (-): ")

valores = entrada.split('-')

numeros = []  
no_numeros = []  

for valor in valores:
    valor = valor.strip() 
    if valor.replace('.', '', 1).isdigit():  
        numeros.append(float(valor)) 
    else:
        no_numeros.append(valor)  

total = sum(numeros)

# Mostrar resultados
print("Valores numéricos:", numeros)
print("Valores no numéricos:", no_numeros)
print("Suma de valores numéricos:", total)