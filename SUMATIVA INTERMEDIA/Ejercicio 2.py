frase=input("introduce una frase: ")
frase_minusculas=frase.lower()
var1=int(input("introduce un numero entero: "))
var2=int(input("introduce otro numero entero: "))
var3=int(input("introduce otro numero entero: "))
numeros=[var1,var2,var3]
suma=var1+var2+var3
media= suma/len(numeros)
producto=var1*var2*var3
print(f"{frase_minusculas}")
print(f"la suma es: {suma:.1f}")
print(f"la media es: {media:.2f}")
print(f"el producto es: {producto:.1f}")
if suma>producto:
    print("¿La suma es mayor que el producto?", True)
else:
    print("¿La suma es mayor que el producto?", False)

