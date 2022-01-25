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
    N = int(input("Veuillez saisir un nombre : "))
    if N > 0:
        break

table_de_multiplication(N, 10, 1)
