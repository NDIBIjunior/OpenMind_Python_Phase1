chaine = input("Saisissez votre chaine de caaractère: ")

i = int(0)
mot = str()

while i <= len(chaine):
    
    mot = mot+chaine[i:i+1]   # Mr j'ai utilisé la sélection pour me placer toujours sur un idice pairs
    i = i+2                 #et ici j'incrémente pour me replacer sur le  chiffre pair suivant

print("les lettre d'indices pairs sont:'",mot,"'")

