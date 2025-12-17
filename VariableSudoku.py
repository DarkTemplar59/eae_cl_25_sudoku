import tkinter
from constantes import *

class VariableSudoku:
    def __init__(self):
        self.grille = None              # Grille de Sudoku (liste 2D)
        self.difficulte = None          # Difficulté sélectionnée
        self.fenetre = tkinter.Tk()     # Fenêtre principale
        self.fenetre.title("Sudoku")
        self.canvas = None              # Zone de dessin
        self.vidage = False             # Indicateur de vidage activé ou non

    def initialiser_canvas(self):
        """Crée et affiche le canvas de la grille Sudoku"""
        self.canvas = tkinter.Canvas(
            self.fenetre,
            width=TAILLE * CASE + 2 * OFFSET,
            height=TAILLE * CASE + 2 * OFFSET
        )
        self.canvas.pack()

# Instance globale partagée
variable = VariableSudoku()