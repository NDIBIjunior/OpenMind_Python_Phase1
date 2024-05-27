premier_nombre = int(input("Entrer le premier nombre: "))
second_nombre = int(input("Entrer le second: "))

reste = premier_nombre%second_nombre
quotient = int((premier_nombre - reste)/second_nombre)
print("Le reste de la division de", premier_nombre,"par", second_nombre ,"est", reste)
print("et le quotient est: ", quotient)

