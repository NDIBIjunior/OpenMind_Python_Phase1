chaine = input("veuillez saisir votre chaine de caractère...\n")

liste = chaine.split(" ")
taille = int(0)
mot_le_plus_long = str()

for mot in liste:
    if(taille < len(mot)):
        mot_le_plus_long = mot[:]
        taille = len(mot)

print("Le mot le plus long de votre phrase est: ", mot_le_plus_long)
