import random

num_cartes = ["1","2","3","4","5","6","7","8","9","10","V","D","R"]
symb_cartes = ["Coeur","Pique","Trefle","Carreau"]
possibilite_carte1 = []
possibilite_carte2 = []
tirage_carte1 = []
tirage_carte2 = []

# Création des possibilités de jeu de cartes
for symb in symb_cartes: # Boucle sur les symboles de la liste symb_cartes
    for num in num_cartes: # Boucle sur les valeurs de la liste num_cartes #
        possibilite = symb + "-" + num # cancatenation d'une symbole avec une valeur
        possibilite_carte1.append(possibilite) # Ajout de la possibilité à la liste possibilite_carte1
        possibilite_carte2.append (possibilite)

print (possibilite_carte1) # Affichage de la liste possibilite_carte1
print()
print (possibilite_carte2) # Affichage de la liste possibilite_carte1

# Choix aléatoire des cartes dans les deux jeux
for i in range (12) : # Boucle de 0 à 10 par pas de 1
    # Choix d'une carte aléatoirement dans la liste possibilite_carte1
    tirage_aleatoire1 = random.randint(0,len(possibilite_carte1)-1) 
    tirage_carte1.append(possibilite_carte1[tirage_aleatoire1]) # Ajout de cette carte à la liste tirage_carte1
    tirage_aleatoire2 = random.randint(0, len(possibilite_carte2) - 1)
    tirage_carte2.append(possibilite_carte1[tirage_aleatoire2])

print()
print(tirage_carte1)
print()
print(tirage_carte2)
print()
# Test et affichage si deux cartes sont identiques aux deux tirages
for carte1 in tirage_carte1 : # Boucle sur les cartes de la liste tirage_carte11
    for carte2 in tirage_carte2 : # Boucle sur les cartes de la liste tirage_carte2
        if carte1 == carte2 : # Comparaison entre les deux cartes
            print(carte1, " est identique au deux tirages")