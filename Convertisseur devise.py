print("Bienvenue !")
print("1 : Euro -> Dirham")
print("2 : Dirham -> Euro ") 
operation=input("Entrez le numéro de l'opération que vous souhaitez :  ") 
operation= int(operation) 
if operation == 1:
    Euro=input("Entrez le nombre d'Euros que vous voulez changer : ")
    Euro=float(Euro)
    calcul= Euro * 11.13
    print(Euro,"€ =",calcul,"Dirhams")
if operation == 2:
    Dirhams=input("Entrez le nombre de Dirhams que vous voulez changer: " )
    Dirhams=float(Dirhams)
    calcul= Dirhams * 0.09
    print(Dirhams,"Dirhams =",calcul,"€")
