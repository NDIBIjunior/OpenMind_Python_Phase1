mot = str()

chaine = input("Entrer le mot svp: ")
taille = len(chaine)

while taille >= 0:
    mot = mot + chaine[taille-1:taille]  
    taille = taille - 1

if( mot == chaine):
    print("Le mot '", chaine, "' est un palindrome")
else:
    print("Le mot '", chaine, "' n'est pas un palindrome")