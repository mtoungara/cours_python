participants = {"Amine", "Karine", "Christopher", "Amine", "Valerie", "Karine"}

nombre = len(participants)
print("Le nombre de participants uniques est de:", nombre)

# affichage le type de l'ensemble

ensemble = set()

print(type(ensemble))

print("Amine" in participants)
print("Sophie" in participants) 

for p in participants:
    print(p)