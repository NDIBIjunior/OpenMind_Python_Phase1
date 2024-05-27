
def somme(Liste):

    som = float()
    for i in Liste:
        som = som + float(i)
    return som


def multiplication(liste):

    mul = float(1)
    for i in liste:
        mul = mul * float(i)
    return mul

liste = input("Veuillez entrer les nombres de votre liste séparés d'un espace: ")
liste = liste.split(" ")

somme = somme(liste)
produit = multiplication(liste)


print("La somme des éléments de votre liste est ", somme)
print("Le produit de votre liste est ", produit)
