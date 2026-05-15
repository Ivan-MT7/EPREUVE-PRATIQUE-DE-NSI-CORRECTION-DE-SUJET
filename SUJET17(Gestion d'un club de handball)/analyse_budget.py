import csv


def lire_mouvements_depuis_csv(nom_fichier_csv):
    """
    Lit les données d'un fichier CSV et les retourne en liste de dictionnaires.
    Les colonnes 'montant' et 'mois' sont converties respectivement en flottant et en entier.
    """
    mouvements_csv = []
    try:
        with open(nom_fichier_csv, mode='r', newline='', encoding='utf-8') as fichier_csv:
            lecteur_csv = csv.DictReader(fichier_csv)
            for ligne in lecteur_csv:
                ligne['montant'] = float(ligne['montant'])
                ligne['mois'] = int(ligne['mois'])
                mouvements_csv.append(ligne)
        return mouvements_csv
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{nom_fichier_csv}' est introuvable.")
        return []


mouvements_test = [
    {'type': 'recette', 'catégorie': 'cotisations', 'montant': 1200.0, 'mois': 1},
    {'type': 'recette', 'catégorie': 'billetterie', 'montant': 300.0, 'mois': 6},
    {'type': 'dépense', 'catégorie': 'fonctionnement', 'montant': 450.0, 'mois': 6},
    {'type': 'dépense', 'catégorie': 'déplacements', 'montant': 200.0, 'mois': 12},
    {'type': 'dépense', 'catégorie': 'salaires', 'montant': 1500.0, 'mois': 12},
    {'type': 'recette', 'catégorie': 'subventions', 'montant': 800.0, 'mois': 12}
]

#############################################################################
# Écrire ci-dessous la fonction total_par_type et ses tests (Question 1)    #
#############################################################################
def total_par_type(mouvements, type_mouvement) :
    # Initialisation du total à 0
    resultat = 0
    # On parcourt chaque mouvement (qui est un dictionnaire) de la liste
    for enregistrement in mouvements :
        # On vérifie si le type du mouvement correspond à celui qu'on cherche
        if enregistrement["type"] == type_mouvement :
            resultat += enregistrement["montant"] # Si oui, on ajoute le montant au total
    return resultat
def test_total() :
    # Le total des recettes (cotisations + billetterie + subventions) : 1200 + 300 + 800 = 2300.0
    assert total_par_type(mouvements_test, "recette") == 2300.0
    # Le total des dépenses (fonctionnement + déplacements + salaires) : 450 + 200 + 1500 = 2150.0
    assert total_par_type(mouvements_test, "dépense") == 2150.0
    #Si le type de mouvement n'est pas dans la liste, nous avons 0.
    assert total_par_type(mouvements_test, "nidépensenirecette") == 0
    print("Test réussi")
test_total()

#############################################################################
# Fonctions de calcul du solde (Questions 2 et 3)                           #
#############################################################################

def solde_mensuel(mouvements, mois):
    """
    Calcule le solde pour un mois donné (recettes - dépenses).
    """
    total_recettes = 0
    total_depenses = 0

    for m in mouvements:
        if m['mois'] == mois:
            if m['type'] == 'recette':
                total_recettes += m['montant']
            else:
                total_depenses += m['montant']

    return total_recettes - total_depenses


def solde_annuel(mouvements):
    """
    Calcule le solde annuel en additionnant les soldes de chaque mois.
    """
    total = 0
    # Parcourt les mois de l'année pour cumuler le bilan
    #Correction : Le boucle parcourt jusqu'à 11ième mois, il faut que l'argument à la fin soit 13
    for m in range(1, 13):
        total = total + solde_mensuel(mouvements, m)

    return total
#############################################################################
# Écrire ci-dessous la fonction test_solde_annuel (Question 2)              #
#############################################################################
def test_solde_annuel() :
    # Avec mouvements_test : total recettes (2300) - total dépenses (2150) = 150.0
    # L'assertion vérifiera si le résultat théorique (150.0) est bien retourné
    assert solde_annuel(mouvements_test) == 150.0
    print("Test reussi")
test_solde_annuel()

#############################################################################
# Programme principal pour analyser le fichier complet                      #
#############################################################################
# Application sur le fichier complet (comme demandé à la question 3)
mouvements_complets = lire_mouvements_depuis_csv("budget_complet.csv")
print("Le solde annuel sur le fichier complet est de :", solde_annuel(mouvements_complets))
