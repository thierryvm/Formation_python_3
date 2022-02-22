

def tri_personnalise(e):
    return len(e)


def afficher(collection, n_premiers_elements=-1):
    c = collection
    if n_premiers_elements != -1:   # Simplification de la condition if not n_premiers_elements == 1
        c = collection[:n_premiers_elements]

    c.sort(key=tri_personnalise)
    nb_pizzas = len(c)
    if nb_pizzas == 0:
        print("AUCUNE PIZZA")
        return

    print(f"---- LISTE DES PIZZAS{nb_pizzas} ---")
    for i in c:
        print(i)
    print()
    print("Première pizza: ", c[0])
    print("Dernière pizza: ", c[-1])


def ajouter_pizza_utilisateur(collection):
    p: str = input("Pizza à ajouter: ").upper()
    if p in collection:
        print("ERREUR : Cette pizza existe déjà")
    else:
        collection.append(p)

    print(afficher)


# def pizza_existe(e, collection):
#     for i in collection:
#         if i == e:
#             return True
#     return False


pizzas: list[str] = ["4 fromages", "végétarienne", "hawai", "calzone"]


# vide = ()

ajouter_pizza_utilisateur(pizzas)
afficher(pizzas, 5)
