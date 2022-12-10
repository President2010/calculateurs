print("Bienvenue !")
print("c : Carré")
print("r : Rectangle")
print("t : Triangle")

operation = input("Entrez la lettre qui correspond à la figure que vous souhaitez mesurer: ")

if operation == "c" :
    c = input("Entrez la valeur d'un coté du carré : ")
    aire = int(c)*int(c)
if operation == "r":
    l=input("Entrez la valeur de la largeur du rectangle:")
    L=input("Entrez la valeur de la longueur du rectangle:")
    aire = int(l) * int(L)
if operation == "t":
    h=input("Entrez la valeur de la hauteur du triangle:")
    b=input("Entrez la valeur de la base du triangle: ")
    aire = int(h) * int(b)/2

print("Aire:",aire)