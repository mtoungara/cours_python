import random

mise = int(input("Veuillez saisir le montant de votre mise:"))

pari = input("Veuillez saisir votre choix de pari:")

numero_sortant = random.randint(0,3)

print("Le nombre sortant est:",numero_sortant)

if int(pari) == numero_sortant:   # La valeur du pari est par défaut str, il faut la convertir en int

        print("Vous avez gagné", mise*5)

elif pari == "P" and numero_sortant % 2 == 0:

    print("Vous avez gagné", mise*3)

elif pari == "I" and numero_sortant % 2 != 0:

    print("Vous avez gagné", mise*3)

elif pari == "R" and (numero_sortant == 1 or numero_sortant == 2 or numero_sortant==4 or numero_sortant==6 or numero_sortant==7 or numero_sortant==9 or numero_sortant==12 or numero_sortant==13):

    print("Vous avez gagné", mise*2)

elif pari == "B" and (numero_sortant == 0 or numero_sortant == 3 or numero_sortant==5 or numero_sortant==8 or numero_sortant==10 or numero_sortant==11 or numero_sortant==14):

    print("Vous avez gagné", mise*2)

else:

    print("Vous avez gangné:", 0)
