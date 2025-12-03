var_min=int(input("Introduce el numero minimo: "))
var_max=int(input("Introduce el numero maximo: "))
var_intervalo=int(input("Introduce el intervalo: "))
valores=""

for i in range(var_min, var_max+1, var_intervalo):
    valores=valores+str(i)+","
print(valores[:-1])