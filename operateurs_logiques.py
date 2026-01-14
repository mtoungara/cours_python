a,b,c = -5,8,0
if(a<c and b<c):
    print("Vrai")
else:
    print("Faux")

# 
a,b,c = -5,8,0
if(a<c or b<c):
    print("Vrai")
else:
    print("Faux")

#
a,b = 3,10
if(not(a<b)):
    a,b = b,a
    print("Les valeurs de a et b seront inversées")
    print("a = ", a)
    print("b = ", b)
else:
    print("Les valeurs de a et b restent les memes!")
    print("a = ",a)
    print("b = ",b)

