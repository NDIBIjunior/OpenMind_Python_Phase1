chaine = input("veuillez saisir votre chaine de caractère...\n")

liste = chaine.split(" ")

taille = len(liste)
nouvelle_chaine = list()
premier_mot = liste[:1]
dernier_mot = liste[taille - 1:taille]
autre_mots = liste[1:taille - 1]
nouvelle_chaine = dernier_mot + autre_mots + premier_mot
chaine_inversee = " ".join(nouvelle_chaine)
print("La chaine inversée est: ", chaine_inversee)