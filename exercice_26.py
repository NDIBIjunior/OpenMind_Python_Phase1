chaine = input("Veuillez entrer votre texte:  ")
liste = chaine.split(" ")

print("Recherche des mots ayant la lettre 'a' dans votre texte...")
for elt in liste:
    if(elt[0] == 'a' or elt[0] == 'A'):
        print(elt)