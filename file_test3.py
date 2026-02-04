fichier = open("mots.txt","a+")

liste_ajout = ["bagarre", "balançoire", "ballon", "bande", "bicyclette", "bille",

               "cadenas", "château", "coup", "cour", "course", "échasse", "flaque"]

for mot in liste_ajout:

    fichier.write(mot + "\n")

fichier.close()