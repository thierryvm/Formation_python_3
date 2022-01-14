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
nom = input("Quel est votre nom ? ")

age = 0
while age == 0:
    try:
        age = int(input("Quel est votre age ? "))
    except ValueError:
        print("ERREUR: Vous devez rentrer un nombre pour l'age")

print(f"Vous vous appelez {nom} et vous avez {age} ans.")
print(f"L'an prochain vous aurez {age + 1} ans.")
