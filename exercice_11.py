nombre = int(input("Bonjour !\nVeuillez entrer un nombre entier: "))

for i in range(nombre +1):
    if(i != 0 and nombre%i == 0):
        print(i," est un diviseur de", nombre)
