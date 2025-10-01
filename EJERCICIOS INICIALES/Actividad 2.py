#2.Programa que introduzca por teclado tres tipos de variables y se muestren por pantalla en el siguiente orden: número entero, texto y número decimal.
#solicitar un entero
entero = int(input("introduce un numero entero"))
             
#solicitar un numero decimal
decimal =float(input("introduce un numero decimal."))

#solicitar una cadena de texto
texto = input("introduce una cadena de texto")

#mostrat por pantalla los valores ingresados
print("los valores introducidos son:")
print(f"entero:", entero)
print(f"cadena de texto:", texto)
print(f"decimal:", decimal)