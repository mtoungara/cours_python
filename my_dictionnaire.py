note_maths = {"Lionel":13.5, "Amine":14, "Lina":17, "Pierre":20}
print(type(note_maths))

print(note_maths)

# ajout d'une entrée

note_maths["Sofia"] = 15.5
print(note_maths)

# accès à une valeur via sa clé

print(note_maths["Amine"])

# Si la clef n'existe pas, une erreur est levée

dic = {"prenom":"Amine", "liste":[1,2,3], "tp":(10,20,30,40), 1:"Python", "capitales":{"France":"Paris","Espagne":"Madrid"}}
print(dic["capitales"])
print(dict["liste"])
print(dic["prenom"])

# Mise à jour d'une valeur 

dic = {"prenom":"Amine", "notes":note_maths,"liste":[1,2,3], "tp":(10,20,30,40), 1:"Python", "capitales":{"France":"Paris","Espagne":"Madrid"}}

print(dic)
