# Données d'émissions en gCO2e par unité
EMISSIONS = {
    'emails_simples': 4,       # par email
    'emails_pj': 19,           # par email avec pièce jointe
    'streaming_sd': 36,        # par heure
    'streaming_hd': 100,       # par heure
    'recherches': 7,           # par recherche
    'stockage_cloud': 10       # par Go par mois
}

# Exemples d'utilisateurs pour les tests
utilisateur1 = {
    'emails_simples': 150,
    'emails_pj': 20,
    'streaming_sd': 10,
    'streaming_hd': 25,
    'recherches': 500,
    'stockage_cloud': 15
}

utilisateur2 = {
    'streaming_hd': 15,
    'emails_simples': 100,
    'recherches': 10
}

utilisateur3 = {
    'emails_simples': 50,
    'emails_pj': 5,
    'streaming_sd': 30,
    'streaming_hd': 5,
    'recherches': 200,
    'stockage_cloud': 5
}

utilisateur4 = {
    'emails_simples': 100,
    'recherches': 50
}

utilisateur5 = {
    'emails_simples': 50,
    'recherches': 100
}

utilisateur6 = {}

#############################################################################
# Écrire le code de la fonction calculer_empreinte de la question 1         #
#############################################################################
def calculer_empreinte(utilisateur) :
    # Initialisation du total des émissions
    resultat = 0
    # On parcourt chaque activité 

    for activite in utilisateur :
        # L'émission de cette activité est la quantité multipliée par son coût unitaire
        # On ajoute ce résultat à l'empreinte totale
        resultat += utilisateur[activite] * EMISSIONS[activite]
    return resultat
#############################################################################
# Écrire le code de la fonction classer_par_impact de la question 2         #
#############################################################################
def classer_par_impact(utilisateur) :
    # Initialisation du dictionnaire de résultat avec les trois catégories (listes vides)

    dictionnaire = {
        "fort" : [],
        "moyen" : [],
        "faible" : [],
        }
    # On parcourt chaque activité de l'utilisateur
    for activite in utilisateur :
        # On calcule l'émission pour cette activité précise

        emissions = utilisateur[activite] * EMISSIONS[activite]
        # On classe l'activité dans la bonne liste selon la valeur des émissions (en gCO2e)

        if emissions >= 1000 :
            dictionnaire["fort"].append(activite)
        elif  200 <= emissions < 1000 :
            dictionnaire["moyen"].append(activite)
        else :
            dictionnaire["faible"].append(activite)
    return dictionnaire
#############################################################################
# Fonction fournie pour la question 3                                       #
#############################################################################

def comparer(u1, u2):
    """Compare les émissions de deux utilisateurs pour toutes les activités.
    Renvoie un dictionnaire avec, pour chaque activité, la différence des
    émissions (émissions de l’utilisateur 2 moins celles de l’utilisateur 1).
    Si une activité est absente chez un utilisateur, on considère que
    son émission vaut 0."""
    differences = {}
    for activite in EMISSIONS:
        quantite1 = 0
        quantite2 = 0
        if activite in u1:
            quantite1 = u1[activite]
        if activite in u2:
            quantite2 = u2[activite]
        emission1 = quantite1 * EMISSIONS[activite]
        emission2 = quantite2 * EMISSIONS[activite]
        differences[activite] = emission2 - emission1
    return differences


def test_comparer():
    diff = comparer(utilisateur4, utilisateur5)
    assert diff['emails_simples'] == -200  # (50-100) * 4
    assert diff['recherches'] == 350     # (100-50) * 7
    # Test 1 : On compare avec un dictionnaire qui n'a pas les mêmes activités
    # Justification : Cela permet de valider le comportement sur des activités qui apparaissent que chez l'utilisateur 1
    diff = comparer(utilisateur1, utilisateur5)
    assert diff['emails_pj'] == -380 #(0-20)*19
    # Test 2 : L'un des utilisateurs n'a aucune activité inscrite (dictionnaire vide)
    # Justification : Cela permet de vérifier le cas où toutes les activités sont absentes chez un utilisateur (elles valent 0)
    diff_vide = comparer(utilisateur4, utilisateur6)
    assert diff_vide['emails_simples'] == -400 # 0 - (100 * 4)
    assert diff_vide['recherches'] == -350 # 0 - (50 * 7)
    
    print("Test de comparaison réussi")

#############################################################################
# Fonction fournie pour la question 4                                       #
#############################################################################
def comparer_v2(u1, u2):
    """Compare les émissions de deux utilisateurs pour toutes les activités.
    Renvoie un dictionnaire avec, pour chaque activité, l'écart des émissions
    sous forme de pourcentage, en proportion de la première émission."""
    ecarts = {}
  
    for activite in EMISSIONS:
        quantite1 = 0
        quantite2 = 0
        if activite in u1:
            quantite1 = u1[activite]
        if activite in u2:
            quantite2 = u2[activite]
        # CORRECTION : l'erreur survient si l'émission de u1 est 0, 
        # car on va diviser par "emission1" qui vaut 0, ce qui lève une ZeroDivisionError.
        # On ajoute un test pour éviter de diviser par zéro :

        emission1 = quantite1 * EMISSIONS[activite]
        emission2 = quantite2 * EMISSIONS[activite]
        if emission1 != 0:
            ecarts[activite] = (emission2 - emission1)/emission1 * 100
        else:
            # S'il n'y a pas d'émission initialement (emission1 = 0)
            if emission2 == 0:
                ecarts[activite] = 0.0 # L'émission reste à 0, pas d'évolution
            else:
                ecarts[activite] = "infini" # L'évolution est de 0 vers une valeur positive
    return ecarts
