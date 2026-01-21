entiers = [-10, -3, -1, 0, 23, 56, 78]
carres_entiers = [i*i for i in entiers]
print(carres_entiers)

entiers2 = [-10, -3, -1, 0, 23, 56, 78]
carres_entiers2_negatifs = [i*i for i in entiers2 if i < 0]
print(carres_entiers2_negatifs)
