# coding: utf-8

numero = 112
text = "des urgences"

print(f"Le numéro d'appel {text} est le {numero}")

liste = [1, 2, 3, 4, 5, 6]

i = 0

while i < len(liste):
    print(liste)
    i += 1

for i in liste:
    print(i)


def next_year():
    global year
    print("Fin de l'année", year)
    year += 1
    print("Début de l'année", year)
    print("Bonne année", year)


year = 2018
next_year()
