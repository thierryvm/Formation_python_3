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

def mult_callback(a, b):
    return a * b


def addition_callback(a, b):
    return a + b


def sustraction_callback(a, b):
    return a - b


def division_callback(a, b):
    return a / b


def power_callback(a, b):  # pow est la méthode pour calculer la puissance ici de a ^ b
    return pow(a, b)


def afficher_table(n, operateur_str, operation_cbk):
    for i in range(1, 10):
        print(i, operateur_str, n, "=", operation_cbk(i, n))


afficher_table(2, "x", mult_callback)
print()
afficher_table(2, "+", addition_callback)
print()
afficher_table(2, "-", sustraction_callback)
print()
afficher_table(2, "/", division_callback)
print()
afficher_table(2, "^", power_callback)

# Fonction LAMBDA, on écrit la fonction après le mot-clés lambda

afficher_table(2, "x", lambda a, b: a * b)
print()
afficher_table(2, "+", lambda a, b: a + b)
print()
afficher_table(2, "/", lambda a, b: a / b)
print()
afficher_table(2, "^", lambda a, b: pow(a, b))
