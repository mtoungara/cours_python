ens1 = {1,2,3, ('a', 'b')}
ens2 = {10, 100}

ens1 |= ens2
print(ens1)  # Affiche l'ensemble après la fusion --- IGNORE ---

ens1.discard(1) # Supprime l'élément 1 de l'ensemble ens1 s'il est présent
print(ens1)  # Affiche l'ensemble après la suppression de 1 --- IGNORE ---  

ens1.remove(2) # Supprime l'élément 2 de l'ensemble ens1, génère une erreur s'il n'est pas présent
print(ens1)  # Affiche l'ensemble après la suppression de 2 --- IGNORE ---
