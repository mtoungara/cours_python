votre_age = float(input("Veuillez saisir votre age:"))
age_partenaire = float(input("Veuillez saisir l'age de votre partenaire:"))
if votre_age <= 30 :
    if age_partenaire < votre_age:
        print("Vous avez moins de 30 ans et votre partenaire est moins agé que vous!")
    else:
        print("Vous avez moins de 30 ans, mais votre partenaire est plus agé que vous!")
else:
    print("Votre age est superieur à 30")
