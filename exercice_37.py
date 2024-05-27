chaine1 = input("Entrer la premiere chaine de caractère: ")
chaine2 = input("entrer la seconde: ")

liste1 = chaine1.split(" ")
liste2 = chaine2.split(" ")

liste = []

for mot_1 in liste1:
    for mot_2 in liste2:
        if(mot_1 == mot_2):
            liste.append(mot_1)


print("la liste des mots communs est: ", liste)