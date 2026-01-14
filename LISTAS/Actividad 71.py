#71. Haz un programa que permita al usuario introducir letras en una lista (cantidad indefinida), en esta lista no deben almacenarse las letras que se han introducido repetidas.

milista=[]
letra=input("Introduce una letra: ")
respuesta=input("deseas repetir si/no: ")
while respuesta=="si":
    letra=input("Introduce una letra: ")
    respuesta=input("deseas repetir si/no: ")
    if respuesta=="no":
        break


