import random

NOMBRE_MIN = 1
NOMBRE_MAX = 100
NB_QUESTIONS = 10


def poser_question():
    a = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    o = random.randint(0, 3)
    # 0 -> +
    # 1 -> *
    # 2 -> -
    # 3 -> /
    operateur_str = "+"
    if o == 1:
        operateur_str = "*"
        calcul = a * b
    elif o == 2:
        operateur_str = "-"
        calcul = a - b
    elif o == 3:
        operateur_str = "/"
        calcul = a / b
    else:
        calcul = a + b

    reponse = int(input(f"Calculez : {a} {operateur_str} {b} = "))

    return reponse == calcul


nb_points = 0

for i in range(0, NB_QUESTIONS):
    print(f"Question n° {i + 1} sur {NB_QUESTIONS} : ")
    if poser_question():
        print("Réponse correcte")
        nb_points += 1
    else:
        print("Réponse incorrect")
    print()

print(f"Votre note est : {nb_points} / {NB_QUESTIONS} ")


moyenne = int(NB_QUESTIONS/2)

if nb_points == NB_QUESTIONS:
    print("Excellent")
elif nb_points == 0:
    print("Révisez vos math")
elif nb_points > moyenne:
    print("Pas mal")
else:
    print("Peut mieux faire")
