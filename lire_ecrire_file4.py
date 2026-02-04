notre_poeme = open('lire_ecrire_file.txt', 'r', encoding='utf-8')
for ligne in notre_poeme:
    print(ligne)
    
with open('lire_ecrire_file.txt', 'r', encoding='utf-8') as notre_poeme:
    for ligne in notre_poeme:
        print(ligne)