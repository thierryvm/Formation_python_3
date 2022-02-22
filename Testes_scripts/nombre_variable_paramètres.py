def somme(titre, **nombres):
    """

    :param titre: on indique un titre
    :param nombres: on récupère ici toutes les valeurs en mettant(*) ou (**) si on veut ajouter des clés
    :return: les paramètres titre et **nombres et on ajoute dans la boucle .value() pour pouvoir utiliser les clés
    """
    print("TITRE:", titre)
    return sum(nombres.values())


print(somme("La moyenne de vos notes est de :", math=5, geo=10, anglais=4))
