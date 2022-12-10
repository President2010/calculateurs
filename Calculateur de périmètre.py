print("Bienvenue !")
x = input("Entrez le nombre de cotés que comporte ta figure: ")
unite=input("Quelle est l'unité de mesure:")
x = int(x)
i = 0
perimetre=0

while i < x:
    i = i + 1

    # Recuperer la mesure de l'utilisateur
    c = input("Entrer la valeur du coté "+str(i)+":")
    c = int(c)

    # Incrémenter la mesure dans le perimetre
    perimetre = perimetre + c

# Afficher le résultat du périmetre
print("Le perimètre est de",perimetre,unite)



