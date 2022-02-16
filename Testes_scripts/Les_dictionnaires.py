# personne: dict[str | int | float] = {"nom": "Claire", "age": 25, "taille": 1.60, "poste": "Développeur"}

# print(personne)
#
# print(personne["nom"])
# print(personne["age"])

# achat: tuple[str, str, str] = ("chocolat", "beurre", "fromage")
# personne["achat"] = achat
# print(personne)

# On itère sur le dictionnaire pour récupérer les clefs et valeurs

# for i in personne:
#     print(f"clef: {i} - valeur: {personne[i]}")

# --------- Listes vs Dictionnaires ----------- #
# personnes = [
#     ("Mélanie", 25, 1.6),
#     ("Paul", 29, 1.8),
#     ("Jacques", 35, 1.75),
#     ("Martin", 16, 1.65),
# ]
#
#
# def obtinir_informations(nom, liste):
#     for i in liste:
#         if i[0] == nom:
#             return i
#     return None
#
#
# infos = obtinir_informations("Jacques", personnes)
# print(infos)

# --------- Dictionnaires ----------- #
"""
Beaucoup plus puissant, car pas besoin de bouclier un nombre de fois par clés
"""
personnes_dict = {
    "Mélanie": (25, 1.6),
    "Paul": (29, 1.8),
    "Jacques": (35, 1.75),
    "Martin": (16, 1.65)
}

infos = personnes_dict.get("Jacques")  # En ajoutant .get permet de vérifier l'existance et si n'existe pas renvoie None

if not infos:
    print("La clef n'existe pas")
else:
    print(infos)
