# Collections : (Tableaux : Array), Listes, Tuples ....
# Contenir et gérer plusieurs éléments
# Tuple (): immutable -> Non modifiable
# Liste []: mutable -> modifiable : rajouter/supprimer des éléments ou les modifier


a = 5
b = "Toto"

# ------------------------------ Tuples ----------------------------------

# personnes = ("Mélanie", "Jean", "Martin", "Alice")
# print(len(personnes))
# print(personnes[-1])  # -1 pour le dernier élement

# for i in range(0, len(personnes)):
#     print(personnes[i])

# for i in personnes:
#     print(i)
#     print(len(i))
#     print(i[-1])


# ------------------------------ Listes ----------------------------------

# personnes = ["Mélanie", "Jean", "Martin", "Alice"]
# nouvelle_personne = "David"
#
# personnes.append(nouvelle_personne)
# del personnes[1]
#
# print(personnes)
#
#
# def afficher_personnes(c):
#     for i in c:
#         print(i)
#
#
# def modifier_valeur(a):
#     a[0] = 10
#
#
# test = [1, 2, 3, 4]
# print(test)
#
# modifier_valeur(test)
# print(test)


# ------------------------------ Fonction et tuples ----------------------------------


# def obtenir_information():
#     return "Mélanie", 37, 1.60
#
#
# def afficher_information(nom: str, age: int, taille: float):
#     print(f"information : Nom: {nom}, age: {age}, taille: {taille}")
#
#
# infos = obtenir_information()
# afficher_information(*infos)
#
# print(infos)
# print(*infos)  # ça revient à faire print(infos[0], info[1], infos[2]) ou on dit qu'on unpack
#
# # print("nom: ", infos[0])
# # print("age: ", str(infos[1]))
# # print("taille: ", str(infos[2]))
#
#
# nom, age, taille = obtenir_information()
# afficher_information(nom, age, taille)


# ------------------------------ Slices ----------------------------------


personnes = ["Mélanie", "Jean", "Martin", "Alice"]


for i in personnes[:2]:
    print(i)
