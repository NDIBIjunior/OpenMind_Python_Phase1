nombre = int(input("Veuillez entrer un nombre entier positif:"))
somme = int(1)
i = int(1)
if nombre == 0:
    print("Factorielle de 0 est 1")

if ( 0 > nombre ):
    print("La factorielle d'un nombre négatif n'existe pas !!!")

if(nombre > 0):

    while( i != nombre + 1):
        somme = somme*i
        i = i+1

    print("La factorielle de ", nombre, "est egale à ", somme)