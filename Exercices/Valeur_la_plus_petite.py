# Listes -Algo : Valeur la plus petite

nom_chauffeur = ["Patrick", "Paul", "Marc", "Jean", "Pierre", "Marie", "Maxime"]
distance_chauffeur_km = [1.5, 2.2, 0.4, 0.9, 7.1, 1.1, 0.6]

# V1
# distance_min = distance_chauffeur_km[0]
# index_min = 0
# for i in range(len(distance_chauffeur_km)):
#     distance = distance_chauffeur_km[i]
#     if distance < distance_min:
#         distance_min = distance
#         index_min = i
#
# print("Distance minimal: ", distance_min, "km")
# print("Index de la distance minimal: ", index_min)
# print("Nom du chauffeur", nom_chauffeur[index_min])


# V2


nom_et_distance = [("Patrick", 1.5), ("Paul", 2.2), ("Marc", 0.4), ("Jean", 0.9), ("Pierre", 7.1)]
nom_et_distance_min = nom_et_distance[0]
for nom_et_distance in nom_et_distance:
    if nom_et_distance[1] < nom_et_distance_min[1]:
        nom_et_distance_min = nom_et_distance

print(f"Distance minimal:{nom_et_distance_min[1]}, nom du chauffeur: {nom_et_distance_min[0]}")
