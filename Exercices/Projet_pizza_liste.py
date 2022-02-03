def tri_personnalise(e):
    return len(e)


def afficher(collection):
    collection.sort(key=tri_personnalise)
    nb_pizzas = len(collection)
    if nb_pizzas == 0:
        print("AUCUNE PIZZA")
        return

    print(f"---- LISTE DES PIZZAS{nb_pizzas} ---")
    for i in collection:
        print(i)
    print()
    print("Première pizza: ", collection[0])
    print("Dernière pizza: ", collection[-1])


def ajouter_pizza_utilisateur(collection):
    p = input("Pizza à ajouter: ").lower()
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


pizzas = ["4 fromages", "végétarienne", "hawai", "calzone"]


# vide = ()

ajouter_pizza_utilisateur(pizzas)
afficher(pizzas)
