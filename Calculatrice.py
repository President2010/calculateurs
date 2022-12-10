print("Bienvenue !")
print("1 : Addition")
print("2 : Soustraction")
print("3 : Multiplication")
print("4 : Division")
operation = input("Entrez le numéro de l'opération que vous souhaitez : ")
operation = int(operation)

x = input("Entrez la valeur de x :")
y = input("Entrez la valeur de y: ")
if operation == 1:
    label = "+"
    z = int(x) + int(y)
if operation == 2:
    label = "-"
    z = int(x) - int(y)
if operation == 3:
    label= "x"
    z = int(x) * int(y)
if operation == 4:
    label= "/"
    z = int(x) / int(y)
print(x,label,y,"=",z)
