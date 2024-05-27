chaine = input("Veuillez entrer votre texte:  ")
liste = chaine.split(" ")

print("Recherche des mots ayant la lettre 'a' dans votre texte...")
for element in liste:
    if(element[0] == 'a' or element[0] == 'A'):
        print(element)