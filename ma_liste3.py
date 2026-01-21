ma_liste = [1,2, "john", "martin", -5, False]
ma_liste.append(100)
ma_liste.append("Paris")
print(ma_liste)
ma_liste[3] = "monaco"
print(ma_liste[3])
print(ma_liste)

ma_liste[1:3] = [20, 30, "dublin", "Madrid", True]
print(ma_liste)
del ma_liste[0]
print(ma_liste)
del ma_liste[1:4]
print(ma_liste)
