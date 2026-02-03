def occurrence_caracteres(chaine):
    dictionnaire = {}
    for caractere in chaine:
        if caractere in dictionnaire:
            dictionnaire[caractere] += 1
        else:
            dictionnaire[caractere] = 1
    return dictionnaire

chaine = "bonjour"
print(occurrence_caracteres(chaine))
