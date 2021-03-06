# Exercice fonction
# Table de multiplication
#
#
# 1 x 4 = 4
# 2 x 4 = 8
# 3 x 4 = 12
# ...
# 10 x 4 = 40
#
# Afficher_table_multiplication(n)
# min / max
# erreur : si min > max

def table_de_multiplication(n, min=1, max=10):
    if min > max:
        print("ERREUR: Le min est supérieur au max")
        return

    for i in range(min, max + 1):
        print(f'{i} x {n} = {i * n}')


while True:
    N = float(input("Veuillez saisir un nombre : "))
    if N > 0:
        break

table_de_multiplication(N, 1, 10)


# autre façon de faire avec les callback

def mult_callback(a, b):
    return a * b


def addition_callback(a, b):
    return a + b


def sustraction_callback(a, b):
    return a - b


def division_callback(a, b):
    return a / b


def afficher_table(operateur_str, operation_cbk):
    for i in range(1, 10):
        print(i, operateur_str, N, "=", operation_cbk(i, N))


# afficher_table("x", mult_callback)
print()
afficher_table("+", addition_callback)
print()
afficher_table("-", sustraction_callback)
print()
afficher_table(":", division_callback)
