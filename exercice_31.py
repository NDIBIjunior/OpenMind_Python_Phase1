liste = input("Entrer les nombres de la liste: ")
liste = liste.split(" ")

pairs = []
impairs = []

for element in liste:
    if(int(element)%2 == 0):
        pairs.append(element)
    else:
        impairs.append(element)

print("La liste des nombres pairs est: ", pairs)
print("La liste des nombres impairs est: ", impairs)
