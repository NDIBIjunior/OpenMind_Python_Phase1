from math import *

nombre = int(input("entrer un nombre entier: "))
racine = sqrt(nombre)

i = int(1)
nombre_impaire = int(1)
somme = int(0)
while(i < racine+1):

    somme = somme + nombre_impaire
    nombre_impaire = nombre_impaire + 2
    i = i+1

if(somme == nombre):
    print(nombre, "est un carré parfait !!!")
else:
    print(nombre, "n'est pas un carré parfait !!!")
