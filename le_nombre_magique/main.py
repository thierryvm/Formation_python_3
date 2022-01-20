from random import randint


def demander_nombre():
    NOMBRE_ESSAIS = 10
    i = 0
    NOMBRE_A_DEVINER: int = randint(1, 100)
    essais = input(f'Entrez un nombre ({i + 1} essai): ')
    while i < NOMBRE_ESSAIS:
        try:
            essais = int(input(f'Entrez un nombre ({i + 1} essai): '))
        except ValueError:
            print("Désolé, tu dois entrer un nombre !")
        else:
            if essais < NOMBRE_A_DEVINER:
                print(f'Le nombre a deviner est plus grand que {essais}')
            elif essais > NOMBRE_A_DEVINER:
                print(f'Le nombre a deviner est plus petit que {essais}')
            else:
                print(f'Bravo vous avez gagne en {i} essai(s)')
                break

            i += 1

    if essais != NOMBRE_A_DEVINER:
        print('Vous avez perdu')
        print(f'Le nombre a deviner etait: {NOMBRE_A_DEVINER}')

    print('Fin du jeu.')


# ------------------------------ Appel de la fonction -------------------
demander_nombre()
