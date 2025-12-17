from constantes import *


def chaine_vers_grille(chaine: str):
    """
    Transforme une chaîne de 81 caractères en grille 9x9.
    """
    # Initialisation d'une grille 9x9 remplie de '0'
    grille = [['0' for _ in range(TAILLE)] for _ in range(TAILLE)]

    # Parcours linéaire de la chaîne pour remplir la grille
    for index in range(TAILLE * TAILLE):
        # Calcul de la ligne via division entière
        ligne = index // TAILLE
        # Calcul de la colonne via le reste de la division
        colonne = index % TAILLE
        # Affectation du caractère correspondant dans la grille
        grille[ligne][colonne] = chaine[index]

    # Retourne la grille 9x9 construite
    return grille


def index_vers_coordonnees(x: int, y: int):
    """
    Convertit des indices de grille (x, y) en coordonnées pixels du canvas.
    """
    # Calcul de la coordonnée X en pixels
    x_pixel = OFFSET + x * CASE + CASE // 2
    # Calcul de la coordonnée Y en pixels
    y_pixel = OFFSET + y * CASE + CASE // 2

    # Retourne les coordonnées (x, y) en pixels
    return x_pixel, y_pixel


def coordonnees_vers_index(x: int, y: int):
    """
    Convertit des coordonnées pixels en index x et y .
    """
    # Calcul de la coordonnée X en pixels
    x_index = (x - OFFSET) // CASE
    # Calcul de la coordonnée Y en pixels
    y_index = (y - OFFSET) // CASE

    # Retourne les coordonnées (x, y) en pixels
    return x_index, y_index