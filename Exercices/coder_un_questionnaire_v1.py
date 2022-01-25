# Les FONCTIONS : PROJET QUESTIONNAIRE
#
# Question : Quelle est la capitale de la France ?
# (a)Marseille
# (b)Nice
# (c)Paris
# (d)Nantes
#
# Votre réponse :
# Bonne réponse / Mauvaise réponse
#
# ...
#
# Question : Quel est la capitale de l'italie' ?

# ------------------------------------- Solution ----------------------------------------- #

def poser_question(question, r1, r2, r3, r4, choix_bonne_reponse):
    global score
    print("Question")
    print(" ", question)
    print(" (a)", r1)
    print(" (b)", r2)
    print(" (c)", r3)
    print(" (d)", r4)

    reponse = input("Entré votre réponse: ")
    if reponse == choix_bonne_reponse:
        print("Bonne réponse")
        score += 1
    else:
        print("Mauvaise réponse")

    print()


score = 0

poser_question("Quel est la capitale de la France ?", "Marseille", "Nice", "Paris", "Nantes", "c")
print(f"Votre score est de {score}")