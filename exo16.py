prenoms = ["Amine", "Lina", "Antoine","Teresa", "Clara", "Fatima", "Lionel", "Adam", "Augustin", "Saida"]
prenoms.append("Julie")
print(prenoms)

for p in prenoms:
    if p[0] == "A":
        prenoms.remove(p)
print(prenoms)