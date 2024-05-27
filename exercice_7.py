nombre_1 = float(input("Veuillez entrer le premier nombre:"))
nombre_2 = float(input("Entrer le second:"))
nombre_3 = float(input("entrer le dernier nombre: "))

if(nombre_1 > nombre_2 and nombre_1 > nombre_3):
    print("Le plus grand des trois nombres est: ", nombre_1 )
if(nombre_2 > nombre_1 and nombre_2 > nombre_3):
    print("Le plus grand des trois nombres est: ", nombre_2 )
if(nombre_3 > nombre_1 and nombre_3 > nombre_2):
    print("Le plus grand des trois nombres est: ", nombre_3)
print("Merci !!!")
