# Sudoku (Tkinter) — EAE CL 25

Application Sudoku en **Python + Tkinter** avec :
- choix de la difficulté (**easy / medium / hard**) ;
- récupération d’une grille via l’API **YouDoSudoku** ;
- **fallback hors-ligne** (fichiers locaux) si l’API est indisponible.

## Aperçu rapide

- Les chiffres **bleus** sont les chiffres initiaux (non modifiables).
- Les chiffres **noirs** sont les chiffres saisis par l’utilisateur.
- Un clic sur une case permet de **saisir** un chiffre (1–9).
- Le bouton **Vider la case** active/désactive un mode de suppression (la case cliquée est effacée).
- Le bouton **Stop** ferme l’application.
- Le bouton **Autoresolve** est présent mais la logique n’est pas encore implémentée.

## Prérequis

- Python 3.x
- Dépendance : `requests`

## Installation

```bash
pip install requests
```

## Lancement

Depuis la racine du projet :

```bash
python main.py
```

## Organisation du code

- `main.py` : point d’entrée, lance l’interface.  
- `VariableSudoku.py` : instance globale `variable` (fenêtre, canvas, grille, difficulté, état de vidage).  
- `constantes.py` : constantes d’affichage (TAILLE, CASE, OFFSET).  
- `fonction_affichage.py` : interface (fenêtre de difficulté, dessin du canvas, gestion clic/saisie, boutons).  
- `fonction_calcul.py` : conversions (chaine -> grille 9x9, index <-> coordonnées pixels).  
- `appel_API.py` : appel YouDoSudoku + fallback vers les grilles locales.

## Grilles hors-ligne

En cas de problème réseau, le jeu lit une grille dans le dossier `grille/` :
- `easy`
- `intermediate`
- `expert`

Les fichiers sont lus en **UTF-16** et une ligne aléatoire est sélectionnée.

## Détails de fonctionnement

### API YouDoSudoku
L’appel se fait via un `POST` sur :
- `https://youdosudoku.com/api/`

Paramètres utilisés :
- `difficulty`: `easy`, `medium`, `hard`
- `solution`: `False`
- `array`: `False`

La grille récupérée est une chaîne : les `0` sont convertis en `.` puis transformés en grille 9x9.

### Interaction
- Clic sur une case vide : saisie d’un chiffre (1–9).
- Clic sur une case bleue : ignoré (case initiale).
- Mode vidage activé : clic sur une case noire => suppression du chiffre.

## Idées d’amélioration
- Implémenter **Autoresolve** (solveur + affichage).
- Vérifier la validité des coups (lignes/colonnes/blocs).
- Ajouter un message “victoire” quand la grille est complète et correcte.
