note_maths = { "Lionel":13.5, "Youssef":14, "Karine":17, "Pierre":20, "Amine":15}

# len renvoie le nombre d'éléments dans une liste ou un dictionnaire

s = len(note_maths)
print(s)

print("Youssef" in note_maths)
print("Sophie" in note_maths)

# Copy d'un dictionnaire

note2 = note_maths.copy()
# Modification du dictionnaire copié n'affecte pas l'original
note2["Lionel"] = 20
print(note_maths)
print(note2)

# Effacement d'un ou plusieurs éléments du dictionnaire
note_maths.clear()
print(note_maths)