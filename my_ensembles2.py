participants = {"Amine", "Lionel", "Karine", "Valérie", 17, 19, "Christopher"}

femmes = {"Karine", "Lina", "Valérie", "Sarah"}

ens_intersection = participants & femmes
print(ens_intersection)  # Affiche les éléments communs aux deux ensembles

participants.intersection_update(femmes)
print(participants)  # Affiche les éléments communs aux deux ensembles après mise à jour