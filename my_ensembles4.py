ens1 = {1,2,3, ('a', 'b')}

k = ens1.pop() # Supprime un élément au hasard de l'ensemble ens1 et l'assigne à la variable k
print(k)  # Affiche l'élément supprimé au hasard --- IGNORE ---
print(ens1)  # Affiche l'ensemble après la suppression --- IGNORE ---

ens1.clear() # Supprime tous les éléments de l'ensemble ens1
print(ens1)  # Affiche l'ensemble après la suppression de tous les éléments --- IGNORE ---
print(len(ens1))  # Affiche la taille de l'ensemble ens1 après la suppression de tous les éléments --- IGNORE ---