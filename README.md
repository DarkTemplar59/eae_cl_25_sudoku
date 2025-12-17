## 🧩 Projet Sudoku – Algorithmique et Structures Fondamentales.

L’application développée est un jeu de Sudoku graphique, intégrant :
- Une interface utilisateur (Tkinter),
- Une récupération dynamique de données (API),
- Une gestion algorithmique des structures de données,
- Des interactions utilisateur contrôlées.


## 📂 Organisation du projet

Le projet est structuré de manière modulaire afin de séparer :
- la logique métier,
- l’interface graphique,
- la gestion des données.

```text
├── main.py                 # Lancement de l’application
├── appel_API.py            # Accès aux grilles Sudoku
├── fonction_affichage.py   # Gestion de l’interface graphique
├── fonction_calcul.py      # Calculs et conversions
├── VariableSudoku.py       # État global du jeu
├── constantes.py           # Paramètres fixes
└── grille/                 # Données locales
    ├── easy
    ├── intermediate
    └── expert

