liste = input("Entrer les éléments de votre liste en les séparants d'un espace: ")
liste = liste.split(" ")
i = int(0)
j = int(0)

for elt in liste:
    j = j+1
    while i < (len(liste) - 1):
        if liste[i+1] == elt:
            liste.remove(elt) 

        i = i +1 
    i = j

print("Les éléments dupliqués ont été supprimés ! \nVoici la nouvelle liste: ", liste)