notre_poeme = open("lire_ecrire_file.txt", "r")

lignes = notre_poeme.readlines()

print(lignes)

for ligne in lignes:
    print(ligne)
notre_poeme.close()
