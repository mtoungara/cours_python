fichier = open("mots.txt","w")

liste_mots = ["acrobate", "arrêt", "arrière", "barre", "barreau", "bord", "bras", "cerceau",

"chaises", "cheville", "chute", "cœur", "corde", "corps", "côté", "cou",

"coude", "cuisse", "danger", "doigts", "dos"]

for mot in liste_mots:

    fichier.write (mot + "\n")

fichier.close()