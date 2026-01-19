devise = input("Ma devise : ")
montant = int (input("Montant : "))

# 1 € = 1,17 $
taux_euro_dollar = 1.17
# 1€ = 0,91 £
taux_euro_livre = 0.91
# 1$ = 0,77 £
taux_dollar_livre = 0.77

if devise == 'E':
    print(montant,"€ est égal à:", montant * taux_euro_dollar, "$")
    print(montant,"€ est égal à:", montant * taux_euro_livre, "£")
elif devise == 'D':
    print(montant,"$ est égal à:", montant / taux_euro_dollar, "€")
    print(montant,"$ est égal à:", montant * taux_dollar_livre, "£")
else:
    print(montant,"£ est égal à:", montant / taux_euro_livre, "€")
    print(montant,"£ est égal à:", montant / taux_dollar_livre, "$")
