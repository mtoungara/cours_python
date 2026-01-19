m = float(input("Veuillez saisir votre note en mathématique"))
i = float(input("Veuillez saisir votre note en informatique"))
if m > 15 and i < 12 :
    print('Vous ne bénéficiez pas de vos compétences en mathématiques en informatique')
elif m > 15 and i > 18 :
    print("Bravo, c’est super")
