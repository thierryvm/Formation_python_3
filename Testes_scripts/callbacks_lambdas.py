"""
Python fonction avancée
callback → c'est le fait de stocker une fonction dans une variable ou passer cette fonction dans un paramètre
Lambdas →
"""


# def ma_fonction():
#     print("toto")
#     return 1
#
#
# a = 5
#
# b = ma_fonction  # sans les () ça équivaut à dire qu'on stocke cette fonction dans une variable
# print("a", a, "b", b())


def afficher_table_multiplication(n):
    """

    :type n: vaut 2 ici et calculer la table de multiplication de 2
    """
    for i in range(1, 10):
        print(f"{i} x {n} = ", i*n)


afficher_table_multiplication(2)
print()
