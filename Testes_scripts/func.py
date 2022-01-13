def parler(personnage, message):
    print(f"{personnage} : {message}")


def au_revoir():
    print("Au revoir :) !")


if __name__ == "__main__":
    parler("Jason", "Bonjour tous le monde !")
    au_revoir()

# grille OX <-> XO

for loop in range(20):
    for loop in range(20):
        print("OX", end="")
    print("")
    for loop in range(20):
        print("XO", end="")
    print("")
