import turtle


def escalier(taille, nb):
    for _ in range(nb):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
    t.forward(taille)


t = turtle.Turtle()


# escalier(60, 5)

def carre(taille):
    for _ in range(4):
        t.forward(taille)
        t.left(90)


# On créer une nouvelle fonction qui fait appel à la précédente pour créer plusieurs carres
def carres(taille_de_depart, nb):
    for i in range(nb):
        taille = (i + 1) * taille_de_depart
        carre(taille)


carres(10, 10)
# carre(100)

turtle.done()
