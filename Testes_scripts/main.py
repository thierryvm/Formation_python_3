"""
Premier programme
formation python 3
Apprendre la programmation

"""
# On demande à l'utilisateur de rentrer des données qui seront équivalent à un "str" ( chaîne de caratères )

nom = input("Quel est votre nom ? ")
age = input("Quel est votre age ? ")

# On vérifie ce que l'utilisateur entre comme données et on gere un type d'erreur ici en occurence ValueError

try:
    age_prochain = int(age) + 1  # On fait une conversion  de al variable age en int
except ValueError:  # Gestion d'un type d'erreurs ici ValueError
    print("Erreur vous devez rentrer un nombre pour l'age")
else:
    # print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans.")
    print(f"Vous vous appelez {nom} et vous avez {age} ans.")  # J'utilise ici une chaîne de caractère formaté.
    print("L'an prochain vous aurez " + str(age_prochain) + " ans")
