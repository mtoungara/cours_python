from math import pi

def volume_cylindre(rayon, hauteur):
    """Calcule le volume d'un cylindre de rayon r et de hauteur h."""
    return pi * rayon**2 * hauteur

volume1 = volume_cylindre(2,7)
volume2 = round(volume1,2)
print(volume2)
