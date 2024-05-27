chaine = input("Veuillez entrer votre chaine:  ")
trouvee = int(0)

for i in range(len(chaine)):

    if(chaine[i] == 'a'):
        trouvee = 1
        print("La lettre 'a' se trouve la position", i+1,"dans la chaine",chaine)

if(trouvee == 0):
    print("La lettre 'a' ne se trouve pas dans cette chaine de carectère: ", chaine )
