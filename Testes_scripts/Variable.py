# Demande à l'utilisateur d'entrer son nom et l'affiche à l'écran ensuite

username = input("Entrer votre prénom ")  # retourne toujours un "str"

print(f'Bonjour {username}')

# Demande à l'utilisateur d'introduire les 3 notes et en fait la moyenne /3 pour l'afficher ensuite.

note1 = int(input("Entrer la premiere note "))
note2 = int(input("Entrer la seconde note "))
note3 = int(input("Entrer la derniere note "))
result = (note1 + note2 + note3) / 3

print("La moyenne de l'élève est {0}".format(result))

# Récupère le résultat et si celui-ci est supérieur à 15 alors il affichera la seconde condition sinon la première

if result < 15:
    print("Tu peux mieux faire !")
else:
    print("Bravo, tu as bien travaillé.")
