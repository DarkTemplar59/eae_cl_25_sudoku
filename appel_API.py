import requests
import random
from fonction_calcul import chaine_vers_grille
from VariableSudoku import variable

def obtenir_grille():
    # URL de l'API YouDoSudoku pour récupérer une grille
    url_api = "https://youdosudoku.com/api/"

    # Corps de la requête : difficulté souhaitée et options
    corps_requete = {
        "difficulty": variable.difficulte,  # "easy", "medium" ou "hard"
        "solution": False,          # True ou False
        "array": False              # True ou False
    }

    try:
        # Envoi de la requête POST avec un délai d'attente de 10 secondes
        reponse_api = requests.post(url_api, json=corps_requete, timeout=10)
        # Vérification du code de statut HTTP -> lève une exception si différent de 200
        reponse_api.raise_for_status()
        # Extraction de la grille et conversion des 0 en points
        return chaine_vers_grille(reponse_api.json()["puzzle"].replace("0", "."))

    # Capture toutes les exceptions liées à requests
    except requests.exceptions.RequestException as erreur_reseau:
        print("⛔ Une erreur réseau est survenue :", erreur_reseau)
        return chaine_vers_grille(obtenir_grille_offline())


# # Exemple d’appel
# data = get_puzzle("hard")
# if data:
#     print("Succès 🟢 :", data)
# else:
#     print("⚠️ Impossible d’obtenir une grille.")


def obtenir_grille_offline():
    # Correspondance entre les difficultés de l'API et les fichiers locaux
    correspondance = {
        "easy": "easy",
        "medium": "intermediate",
        "hard": "expert",
    }

    # Construction du chemin du fichier correspondant à la difficulté
    nom_fichier = "grille/" + correspondance.get(variable.difficulte)
    # Ouverture du fichier correspondant à la difficulté (encodage UTF-16)
    with open(nom_fichier, "r",encoding="utf-16") as fichier_grille:
        # Ignorer les X premières lignes du fichier
        for _ in range(random.randint(1, 10000)):
            fichier_grille.readline()

        # Lecture de la ligne contenant la grille brute
        ligne_grille = fichier_grille.readline().strip()

    # Retourne la ligne de la grille
    return ligne_grille