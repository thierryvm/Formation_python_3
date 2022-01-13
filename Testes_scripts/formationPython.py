# coding: utf-8

numero = 112
text = "des urgences"

print(f'le numero d\'appel {text} est le {numero}')

print(f'le numéro d\'appel {text} est le {numero}')

print(f'le numéro d\'appel {text} est le {numero}')

list = [1, 2, 3, 4, 5, 6]

i = 0

while i < len(list):
    print(list)
    i += 1

for i in list:
    print(i)


def next_year():
    global year
    print("Fin de l'année", year)
    year += 1
    print("Début de l'année", year)
    print("Bonne année", year)


year = 2018
next_year()
