def comparaison(liste1,liste2):

    trouve = int(0)
    for element1 in liste1:
        for element2 in liste2:
            if(element2 == element1):
                trouve = 1
            
    if(trouve == 1):
        print("Les deux listes ont une valeur en commun")
    else:
        print("Les deux listes n'ont pas de valeur en commun !")


Liste1 = input("Veuillez entrer les éléments de la première liste: ")
Liste1 = Liste1.split(" ")
liste2 = input("Entrer les éléments de la seconde liste: ")
liste2 = liste2.split(" ")

comparaison(Liste1,liste2)
