nom = "dragon"
prenom = "Serge"
age = 43

phrase = "{} {} a pour age {} ans".format(nom, prenom, age)
print(phrase)
phrase2 = "{} est un prénom, {} est un nom et {} désigne l'age".format(prenom, nom, age)
print(phrase2)
phrase3 = "L'age {2} est celui de {1} {0}".format(nom,prenom,age)
print(phrase3)
phrase4 = "{prenom} {nom} a pour age {age}".format(prenom = prenom, nom=nom, age=age)
print(phrase4)
