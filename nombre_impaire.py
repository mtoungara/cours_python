def nombre_impair():
    n = int(input("Entrez un nombre entier positif: "))
    for i in range(n + 1):
        if i % 2 != 0:
            print(i)
            
nombre_impair()