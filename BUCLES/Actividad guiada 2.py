password="a1e4jk"
vocales="aeiouAEIOU"
total=0
#repeticiones int(input("numero de veces: "))
for i in password:
    if i.isnumeric: 
        total=total+int(i)
    if i in vocales:
        print(total)
