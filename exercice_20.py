chaine = input("Veuillez entrer votre chaine:  ")

taille = len(chaine)
mot = chaine[taille - 1:taille]  + chaine[1:taille - 1] + chaine[0:1]

print("\n\nLa chaine a été modifiéé en '", mot, "'\n")