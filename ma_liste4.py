ma_liste = [1,2, "john", "martin", -5, False]

ma_liste.remove(2)
print(ma_liste)
ma_liste.remove("john")
print(ma_liste)
ma_liste.pop(3)
print(ma_liste)
print(ma_liste.pop(0))
print(ma_liste)
ma_liste[1:3] = []
print(ma_liste)
