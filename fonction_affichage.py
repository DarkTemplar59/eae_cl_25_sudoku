# ----------------- Import des bibliothèques standard -----------------
import tkinter                                  # Interface graphique
from tkinter import ttk,simpledialog,messagebox            # Widgets avancés (Combobox)

# ----------------- Import des modules du projet -----------------
from constantes import *            # Constantes de taille et d'affichage
from VariableSudoku import variable # Variables globales du jeu
from appel_API import obtenir_grille
from fonction_calcul import index_vers_coordonnees
from fonction_calcul import coordonnees_vers_index


# ----------------- Dessin de la grille Sudoku -----------------
def dessiner_grille():
    # Calcul de la taille totale de la grille :
    # - OFFSET à gauche
    # - TAILLE * CASE pour les 9 cases
    taille_totale = OFFSET + TAILLE * CASE

    # Parcours des lignes internes de la grille
    # On commence à 1 car la bordure extérieure sera dessinée séparément
    for i in range(1, TAILLE):

        # Position exacte de la ligne dans le canvas
        position = OFFSET + i * CASE

        # Toutes les 3 cases, on trace une ligne plus épaisse
        # pour séparer les blocs 3x3
        epaisseur = 3 if i % 3 == 0 else 1

        # Création de la ligne horizontale
        variable.canvas.create_line(
            OFFSET,                 # x début
            position,               # y début
            taille_totale,           # x fin
            position,               # y fin
            width=epaisseur
        )

        # Création de la ligne verticale
        variable.canvas.create_line(
            position,               # x début
            OFFSET,                 # y début
            position,               # x fin
            taille_totale,           # y fin
            width=epaisseur
        )

    # Dessin de la bordure extérieure de la grille
    # Elle est toujours plus épaisse pour bien délimiter la zone de jeu
    variable.canvas.create_rectangle(
        OFFSET,
        OFFSET,
        taille_totale,
        taille_totale,
        width=3
    )


# ----------------- Initialisation des chiffres de la grille -----------------
def initialiser_chiffres_grille():
    # Parcours ligne par ligne de la grille Sudoku
    for y, ligne in enumerate(variable.grille):

        # Parcours colonne par colonne
        for x, valeur in enumerate(ligne):

            # Les cases vides sont représentées par "."
            # Seuls les chiffres initiaux sont affichés ici
            if valeur != ".":
                remplir_case(
                    x,              # colonne
                    y,              # ligne
                    valeur,         # chiffre initial
                    "blue"          # couleur des chiffres initiaux
                )


# ----------------- Fonction pour remplir une case -----------------
def remplir_case(x: int, y: int, valeur: str, couleur: str):
    # Conversion des indices de grille (x, y)
    # en coordonnées pixels exploitables par le canvas
    x_pixel, y_pixel = index_vers_coordonnees(x, y)

    # Affichage du chiffre au centre de la case sélectionnée
    variable.canvas.create_text(
        x_pixel,                   # position horizontale
        y_pixel,                   # position verticale
        text=valeur,               # valeur à afficher
        font=("Arial", 18),
        fill=couleur,
        tags=f"case_{x}_{y}"      # tag unique pour chaque case
    )


# ----------------- Fonction pour vider les cases -----------------
def vider_case(btn_vider):
    variable.vidage = not variable.vidage
    if variable.vidage:
        btn_vider.config(bg="#ff6b6b")
    else:
        btn_vider.config(bg="#f0f0f0")
    return

# ----------------- Fenêtre de sélection de la difficulté -----------------
def fenetreNiveau():
    # Définition d'une taille minimale pour éviter
    # que les éléments se chevauchent
    variable.fenetre.minsize(270, 155)

    # Création du texte expliquant l'action à l'utilisateur
    label = tkinter.Label(
        variable.fenetre,
        text="Choisir la difficulté",
        font=("Arial", 14)
    )
    label.pack(pady=10)

    # Création de la liste déroulante des difficultés disponibles
    combo = ttk.Combobox(
        variable.fenetre,
        values=["easy", "medium", "hard"],
        width=20,
    )

    # Sélection par défaut : easy
    combo.current(0)
    combo.configure(font=("Arial", 14))
    combo.pack(pady=10)

    # Frame servant à aligner les boutons horizontalement
    frame_boutons = tkinter.Frame(variable.fenetre)
    frame_boutons.pack(pady=10)

    # Bouton permettant de valider la difficulté choisie
    btn_validation = tkinter.Button(
        frame_boutons,
        text="Valider",
        command=lambda: valider_difficulte(combo),
        font=("Arial", 14)
    )
    btn_validation.pack(side="left", padx=5)

    # Bouton permettant de quitter le programme
    btn_quitter = tkinter.Button(
        frame_boutons,
        text="Quitter",
        command=variable.fenetre.quit,
        font=("Arial", 14)
    )
    btn_quitter.pack(side="left", padx=5)


def valider_difficulte(combo):
    # Récupération de la difficulté sélectionnée dans la combobox
    variable.difficulte = combo.get()

    # Suppression de tous les widgets actuels
    # pour préparer l'affichage du jeu
    vider_fenetre()

    # Récupération de la grille Sudoku
    # (API en ligne ou version locale en cas d'erreur)
    variable.grille = obtenir_grille()

    # Affichage de la difficulté choisie en haut de la fenêtre
    label = tkinter.Label(
        variable.fenetre,
        text="Difficulté : " + variable.difficulte,
        font=("Arial", 14)
    )
    label.pack(pady=5)

    # Création du canvas qui accueillera la grille
    variable.initialiser_canvas()

    # Dessin de la grille et affichage des chiffres
    dessiner_grille()
    initialiser_chiffres_grille()

    
    # Frame pour aligner les boutons horizontalement
    frame_boutons = tkinter.Frame(variable.fenetre)
    frame_boutons.pack(pady=10)

    # Bouton Vider la case
    btn_vider = tkinter.Button(
        frame_boutons,
        text="Vider la case",
        font=("Arial", 14),    # fonction à définir,
        command= lambda: vider_case(btn_vider)
    )
    btn_vider.pack(side="left", padx=5)

        # Bouton auto resolve
    btn_resolve = tkinter.Button(
        frame_boutons,
        text="Autoresolve",
        font=("Arial", 14)    # fonction à définir
    )
    btn_resolve.pack(side="left", padx=5)

    # Bouton Stop
    btn_stop = tkinter.Button(
        frame_boutons,
        text="Stop",
        font=("Arial", 14),
        command=variable.fenetre.quit
    )
    btn_stop.pack(side="left", padx=5)

    variable.canvas.bind('<Button-1>', lambda event: on_click(event,btn_vider))



# ----------------- Nettoyage de la fenêtre -----------------
def vider_fenetre():
    # Parcours de tous les widgets présents dans la fenêtre
    # et destruction un par un
    for widget in variable.fenetre.winfo_children():
        widget.destroy()


def on_click(event, bouton_vider):
    # Conversion des coordonnées du clic (pixels) en indices de la grille
    indice_x, indice_y = coordonnees_vers_index(event.x, event.y)

    # Recherche des éléments graphiques correspondant à la case cliquée
    elements_case = variable.canvas.find_withtag(f"case_{indice_x}_{indice_y}")

    # Vérification : clic en dehors de la grille
    if indice_x < 0 or indice_x >= TAILLE or indice_y < 0 or indice_y >= TAILLE:
        return

    # Cas 1 : aucun élément graphique dans la case (case vide)
    if not elements_case:
        # Si le mode vidage est actif, on ne fait rien
        if variable.vidage:
            return
        else:
            # Sinon, on saisit un chiffre dans une case vide
            saisir_chiffre(indice_x, indice_y, False)
            return

    # Cas 2 : la case contient un chiffre initial (couleur bleue → non modifiable)
    elif variable.canvas.itemcget(elements_case[0], "fill") == "blue":
        return

    # Cas 3 : la case contient un chiffre modifiable
    else:
        if variable.vidage:
            # Suppression du chiffre présent dans la case
            variable.canvas.delete(f"case_{indice_x}_{indice_y}")
            # Mise à jour de l'état du bouton de vidage
            vider_case(bouton_vider)
            return
        else:
            # Remplacement du chiffre existant par un nouveau
            saisir_chiffre(indice_x, indice_y, True)
            return


def saisir_chiffre(indice_x: int, indice_y: int, case_existe: bool):
    # Demande à l'utilisateur un chiffre à placer dans la case sélectionnée
    # Les indices sont affichés à partir de 1 pour être compréhensibles par l'utilisateur
    valeur_saisie = simpledialog.askstring(
        "Saisie",
        f"Entrez un chiffre (1-9) pour {indice_x + 1},{indice_y + 1}"
    )

    # Vérification : la valeur existe, est numérique et comprise entre 1 et 9
    if valeur_saisie and valeur_saisie.isdigit() and 1 <= int(valeur_saisie) <= 9:
        # Si un chiffre est déjà présent dans la case, on le supprime avant remplacement
        if case_existe:
            variable.canvas.delete(f"case_{indice_x}_{indice_y}")

        # Remplit graphiquement la case avec le chiffre saisi
        remplir_case(indice_x, indice_y, valeur_saisie, "black")

    elif valeur_saisie is None or valeur_saisie == "":
        return
    else:
        # Message d'erreur si la saisie est invalide
        messagebox.showwarning("Erreur", "Valeur invalide !")