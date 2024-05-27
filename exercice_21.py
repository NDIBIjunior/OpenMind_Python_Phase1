nombre = int(0)
chaine = input("Veuillez entrer votre chaine:  ")
for i in range(len(chaine)):
    if(chaine[i] =='a' or chaine[i] =='e' or chaine[i] =='u' or chaine[i] =='o' or chaine[i] =='i' or chaine[i] =='y' ):
        nombre = nombre+1

print("le mot ", chaine, "comporte", nombre," voyelles")
