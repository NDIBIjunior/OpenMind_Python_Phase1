table = int(input("Entrer le numéro de la table: "))

for i in range(11):
    print(table," fois ", i ,"=", table*i)

# deuxième partie de l'exercice
nombre = int(1)
while(nombre != 10):
    for i in range(11):
        print(nombre, "*", i, "=", nombre*i)
    nombre = nombre+1
    print("\t\t\t")
