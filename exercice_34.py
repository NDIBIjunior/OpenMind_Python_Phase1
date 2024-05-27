liste = ["12","04","11","18","13","07","10","05","09","15","08","14","16"]

moyenne = []

for elt in liste:
    if( 10 <= int(elt)   ):
        moyenne.append(elt)
    
print("La liste des notes données est: ", liste)
print("Les moyennes de cette liste sont: ", moyenne)