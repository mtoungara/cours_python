def inter_set(set1,set2):
    if set1.isdisjoint(set2):
        print("L'intersection de ", set1, " et ", set2, " est vide")
    else:
        print("L'intersection de ", set1, " et ", set2, " n'est pas vide")

#Exemple
set1 = {1,2,4,5}
set2 = {3,6,9}
inter_set(set1,set2)