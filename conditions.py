#conditions
# if conditions:
#<-> code à executer
note = 12
if note > 10 :
    print("admis")

#
a,b = 10,6
if a <= b :
    a,b = b,a
    print("a= ", a)
    print("b= ", b)

# if conditions:
#   ensemble d'instruction
# else:
#   Un autre ensemble d'instructions
note = 11
if note >= 10 :
    print("Admis")
else:
    print("Redouble")

# elif
x,y = 13,10
if x > y :
    print("x est superieur strictment à y")
elif x==y :
    print("x est égale y")
else:
    print("x est inferieur strictement à y")
#
note = float(input("veuillez saisir votre note de mathematiques"))
if note >= 16 :
    print("Très bien")
elif note >= 14 :
    print("Bien")
elif note >= 12 :
    print("Assez bien")
elif note >= 10 :
    print("Votre travail est moyen")
else:
    print("Vous devez faire un effort")

