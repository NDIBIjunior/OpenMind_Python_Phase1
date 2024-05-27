chaine = input("Veuillez entrer votre chaine:  ")
print("\n\n")
nombre = int(0)

for i in range(len(chaine)):
    
    for j in range(len(chaine)):

        if(chaine[i] == chaine[j]):
            nombre = nombre +1
    
    print("Le caractère", chaine[i], "figure", nombre, "fois dans ", chaine)
    nombre = 0