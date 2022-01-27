"""
Les fonctions récursives permette de boucler sur elle même, comme par exemple demander un utilisateur d'entrer un choix
ou dans le premier cas calculer une puissance
"""


def a(n, limit):
    if n > limit:
        return
    print("n:", n)
    a(n * n, limit)


a(2, 100000)

"""
n: 2
n: 4
n: 16
n: 256
n: 65536
"""


# ----------------------------------- bouclier sur un choix que l'utilisateur dois faire ----------------------------

def demander_choix_utilisateur(min, max):
    reponse_str = input(f"Quel est votre choix entre {min} et {max} : ")
    try:
        reponse_int = int(reponse_str)
        if not min <= reponse_int <= max:
            print(f"ERREUR: Vous devez entrer un nombre entre {min} et {max}")
            return demander_choix_utilisateur(min, max)  # la recursivité ce fait à cette ligne
        return reponse_int
    except ValueError:
        print("ERREUR: Vous devez renter un nombre")
        return demander_choix_utilisateur(min, max)


choix = demander_choix_utilisateur(1, 4)
print("Choix de l'utilisateur", choix)
