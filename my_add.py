participants = {"Amine", "Lionel", "Karine", "Valérie", 17, 19, "Christopher"}

femmes = {"Karine", "Lina", "Valérie", "Sarah"}

participants.add("Dupond")
print(participants)  # Affiche l'ensemble après l'ajout de "Dupond" --- IGNORE ---

participants.add("101")
print(participants)  # Affiche l'ensemble après l'ajout de 101 --- IGNORE ---

participants.update(femmes)
print(participants)  # Affiche l'ensemble après l'ajout des éléments de femmes --- IGNORE ---