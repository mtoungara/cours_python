def supp_inter_set(set1,set2):
    return set1.intersection_update(set2)

#Exemple
set1 = {1,2,4,5,3,6}
set2 = {3,6,9}
supp_inter_set(set1,set2)
print(set1)