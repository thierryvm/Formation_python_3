# Listes - Exercice : Demander nom de personnes


noms = []


while True:
    nom = input("Veuillez entrer votre nom: ").upper()
    if nom == "":
        print("Veuillez entrer un nom correct! ")
        break
    noms.append(nom)

print()
print("Nom de la personne: ")
noms.sort()
for nom in noms:
    print(" " + nom)
