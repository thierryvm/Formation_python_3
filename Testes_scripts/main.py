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

def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        try:
            age_int = int(input(nom_personne + " Quel est votre age ? "))
        except ValueError:
            print("ERREUR: Vous devez rentrer un nombre pour l'age")
    return age_int


def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est votre nom ? ")
    return reponse_nom


def afficher_information_personne(nom, age):
    print()
    print(f"Vous vous appelez {nom} et vous avez {age} ans.")
    print(f"L'an prochain vous aurez {age + 1} ans.")

    if age >= 18:
        print("Vous êtes majeur")
    else:
        print("Vous êtes mineur")


nom1 = demander_nom()
nom2 = demander_nom()

age1 = demander_age(nom1)
age2 = demander_age(nom2)

afficher_information_personne(nom1, age1)
afficher_information_personne(nom2, age2)
