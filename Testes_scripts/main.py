"""Premier programme
Formation Python
apprendre la programmation"""

# nom = input("Quel est votre nom ? ")
#
# age = 0
# while age == 0:
#     age_str = input("Quel est votre age ? ")
#     try:
#         age = int(age_str)
#     except ValueError:
#         print("ERREUR: Vous devez rentrer un nombre pour l'age")
#
# print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")
# print("L'an prochain vous aurez " + str(age+1) + " ans")

# La version avec des chaînes de caractères formatés

# Création de fonction pour demander l'age

# def demander_age(nom_personne):
#     age_int = 0
#     while age_int == 0:
#         try:
#             age_int = int(input(nom_personne + " Quel est votre age ? "))
#         except ValueError:
#             print("ERREUR: Vous devez rentrer un nombre pour l'age")
#     return age_int
#
#
# def demander_nom():
#     reponse_nom = ""
#     while reponse_nom == "":
#         reponse_nom = input("Quel est votre nom ? ")
#     return reponse_nom

""" 
Je récupère les inforations en passant les paramètres de la fonction 
recuperer_et_afficher_infos_personne(numero_personne) 
Ajout de la fonction est_majeur() pour comparer si l'age est majeur ou mineur
"""


def est_majeur(age: int):
    if age <= 0:
        return False

    if age >= 18:
        return True
    return False


def recuperer_infos_personne(numero_personne):
    nom_personne = input(f"Nom de la personne {numero_personne} :")
    age_personne = int(input(f"Age de la personne {numero_personne} :"))
    return nom_personne, int(age_personne)


def afficher_infos_personnes(numero_personne, nom, age: int):
    print(f"La personne {numero_personne} est {nom}, son age est {age} ans")
    print(f"Le nom possède {len(nom)} caractères")
    if est_majeur(age):
        print("Il est majeur")
    else:
        print("Il est mineur")


# taille ici est un paramètre optionnel on lui assigne la valeur de 0
def recuperer_et_afficher_infos_personne(numero_personne):
    nom, age = recuperer_infos_personne(numero_personne)
    afficher_infos_personnes(numero_personne, nom, age)


nb_personnes = 2

for i in range(nb_personnes):
    recuperer_et_afficher_infos_personne(i + 1)

afficher_infos_personnes("007", "James", "40")

# recuperer_et_afficher_infos_personne()


# def afficher_information_personne(nom, age, taille=0):
#     print()
#     print(f"Vous vous appelez {nom} et vous avez {age} ans.")
#     print(f"L'an prochain vous aurez {age + 1} ans.")
#
#     if age == 1 or age == 2:
#         print("Vous êtes un bébé")
#     elif age < 10:
#         print("Vous êtes enfants")
#     elif age == 17:
#         print("Vous êtes presque majeur !")
#     elif 12 <= age < 18:
#         print("Vous êtes adolescent")
#     elif age == 18:
#         print("Tout juste majeur : Félicitation")
#     elif age > 60:
#         print("Vous êtes sénior")
#     elif age >= 18:
#         print("Vous êtes majeur")
#     else:
#         print("Vous êtes mineur")
#
#     if not taille == 0:
#         print(f"Votre taille : {taille} m")
#
#
# nom1 = demander_nom()
# nom2 = demander_nom()
#
# age1 = demander_age(nom1)
# age2 = demander_age(nom2)
#
# afficher_information_personne(nom1, age1)
# afficher_information_personne(nom2, age2)
#
# NB_PERSONNES = 1  # Ajout d'une constante par convention, elle sont en majuscule et on ne les modifie jamais
#
# for i in range(0, NB_PERSONNES):
#     nom = "personne" + str(i + 1)
#     age = demander_age(nom)
#     afficher_information_personne(nom, age, 1.80)
#
# print("""
# Un print
#     sur plusieurs
#                 lignes
#
# """)
