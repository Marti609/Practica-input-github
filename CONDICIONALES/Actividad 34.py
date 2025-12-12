#34. Corrige los 4 errores o añade el código que necesites para que el siguiente programa se ejecute correctamente
#inicializo valores a cada variable
var_numero=6734
var_suma=0
#obtengo su longitud
var_longitud=len(var_numero)
#sumo cada digito a partir del índice de cada posición
var_suma = var_numero [0] + var_numero [1]+ var_numero[2] + var_numero [3]
#utilizo una condición y el operador aritmético // para saber si el resto da 0 y ver si es par
if var_suma // 2 == 0:
 print (f"el valor de {var_suma} es impar")