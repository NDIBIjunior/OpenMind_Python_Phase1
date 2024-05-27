nombre = int(input("Veuillez entrer le nombre: "))
trouve = int(0)

for i in range(nombre + 1):
    if( (i != 0) and (i != 1) and (i != nombre) and (nombre%i == 0) ):
        trouve = 1

if(trouve == 1):
    print(nombre, "n'est pas un nombre premier !")
else:
    print(nombre, "est un nombre premier !") 

