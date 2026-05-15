# =================================================================================#
# Données de test
donnees_test = [
    # Société - Données sur 2010 et 2020
    {'date': '2010-01-15', 'zone': 'Societe', 'temperature': 27.0},
    {'date': '2010-06-20', 'zone': 'Societe', 'temperature': 26.5},
    {'date': '2011-03-10', 'zone': 'Societe', 'temperature': 27.5},
    {'date': '2020-02-14', 'zone': 'Societe', 'temperature': 28.0},
    {'date': '2020-08-22', 'zone': 'Societe', 'temperature': 28.5},
    {'date': '2021-05-30', 'zone': 'Societe', 'temperature': 29.0},

    # Tuamotu - Données sur 2010 et 2020
    {'date': '2015-04-10', 'zone': 'Tuamotu', 'temperature': 26.8},
    {'date': '2020-07-15', 'zone': 'Tuamotu', 'temperature': 27.5},
    {'date': '2021-09-20', 'zone': 'Tuamotu', 'temperature': 28.0},

    # Marquises - Données uniquement sur 2020
    {'date': '2020-03-15', 'zone': 'Marquises', 'temperature': 25.5},
    {'date': '2021-07-10', 'zone': 'Marquises', 'temperature': 26.0},
    {'date': '2022-11-25', 'zone': 'Marquises', 'temperature': 26.5},
]

# =================================================================================#
#  Question 1 : Ecrire le code de votre fonction température_moyenne
def temperature_moyenne(zone, donnees) :
    total_temperature = 0
    compteur = 0
    # On parcourt chaque relevé dans la grande liste de dictionnaires
    for enregistrement in donnees :
        # Si la zone du relevé actuel est celle que l'on cherche
        if enregistrement["zone"] == zone :
            # On cumule la température associée
            total_temperature += enregistrement["temperature"]
            # On compte un relevé en plus pour pouvoir faire la moyenne ensuite
            compteur += 1
    # Si la zone n'existe pas ou n'a aucun relevé, on renvoie None

    if compteur == 0:
        return None
    # Si on a trouvé au moins un relevé (pour ne pas diviser par zéro)

    return total_temperature / compteur


# =================================================================================#
#  Question 2 : Ecrire le code de votre fonction detection_anomalies
def detecter_anomalies(zone, seuil, donnees) :
    # On commence par récupérer la température moyenne grâce à la fonction codée juste au dessus
    variable_moyenne = temperature_moyenne(zone, donnees)
    resultat = []
    # On parcourt à nouveau les relevés

    for enregistrement in donnees :
            if enregistrement["zone"] == zone :
                # On calcule l'écart en valeur absolue avec la moyenne afin d'évaluer la différence peu importe si c'est plus chaud ou plus froid
                ecart = abs(enregistrement['temperature'] - variable_moyenne)
                # Si cet écart est strictement supérieur au seuil toléré, c'est une anomalie
                if ecart > seuil:
                    # On ajoute la date à la liste des anomalies
                    resultat.append(enregistrement["date"])
    return resultat
                    

# =================================================================================#
# code de la fonction evolution_par_decennie à corriger dans la question 4:


def evolution_par_decennie(zone, donnees):
    """
    Calcule l'évolution des températures moyennes par décennie pour une zone.

    ATTENTION: Cette fonction contient un bug volontaire à détecter et corriger.

    Arguments:
        zone (str): Nom de l'archipel (ex: 'Societe', 'Tuamotu')
        donnees (list): Liste de dictionnaires de relevés

    Renvoie:
        dict: Dictionnaire {décennie : température_moyenne}
              ex: {2010: 27.5, 2020: 28.3}
              Renvoie un dictionnaire vide si la zone n'existe pas
    """
    # Filtrage des relevés pour la zone
    releves_zone = [r for r in donnees if r['zone'] == zone]

    if len(releves_zone) == 0:
        return {}

    # Regroupement par décennie
    temperatures_par_decennie = {}

    for releve in releves_zone:
        # Extraction de l'année de la date (format: 'YYYY-MM-DD')
        annee = int(releve['date'].split('-')[0])
        # Calcul de la décennie
        decennie = (annee // 10) * 10
        if decennie not in temperatures_par_decennie:
            temperatures_par_decennie[decennie] = []

        temperatures_par_decennie[decennie].append(releve['temperature'])

    # Calcul des moyennes
    moyennes = {}
    for decennie, temperatures in temperatures_par_decennie.items():
        moyennes[decennie] = round(sum(temperatures) / len(temperatures), 2)

    return moyennes


# =================================================================================#
#  Exercice 2.1 :
"""
Tests
À compléter par le candidat dans le cadre de la question 3
"""


def test_zone_inexistante():
    """
    Test 1 : Tester une zone qui n'existe pas

    À compléter:
    1. Appeler evolution_par_decennie avec une zone inexistante
    2. Vérifier que le résultat est un dictionnaire vide
    """
    # 1. On appelle avec une zone inventée et on le tesre 
    resultat =  evolution_par_decennie("France", donnees_test) 
    # 2. On vérifie que le résultat est un dictionnaire vide avec un test tout simple
    assert resultat == {}
    print("Test réussi")

def test_une_seule_decennie():
    """
    Test 2: Tester une zone avec données sur une seule décennie

    À compléter:
    1. Appeler evolution_par_decennie avec la zone appropriée
    2. Vérifier que le résultat ne contient qu'une seule décennie (2020)
    3. Vérifier la température moyenne
    """
    # 1. Dans 'donnees_test', seule la zone 'Marquises' possède uniquement des données sur 2020, on l'appelle
    resultat = evolution_par_decennie("Marquises", donnees_test)
    # 2 et 3. On vérifie qu'il n'y a que 2020 et la moyenne attendue (25.5 + 26.0 + 26.5)/3 = 26.0
    # AVANT LA CORRECTION DU BUG : ce test obtenait {202: 26.0} ce qui mettait la puce à l'oreille pour trouver le problème.
    print("Test d'une unique décennie (doit afficher True) :", resultat == {2020: 26.0})


def test_plusieurs_decennies():
    """
    Test 3 : Tester une zone avec données sur plusieurs décennies

    À compléter:
    1. Appeler evolution_par_decennie avec la zone appropriée
    2. Vérifier que le résultat contient bien les clés 2010 et 2020
    3. Vérifier que les températures moyennes sont cohérentes
    """
    # 1. On utilise une zone avec des relevés sur plusieurs décennies comme Societe
    resultat = evolution_par_decennie("Societe", donnees_test)
    # 2 et 3. On vérifie les moyennes avec un simple affichage et que 2010 et 2020 sont présentes : 
    # Moyenne de 2010 (une seule donnée) : 27
    # Moyenne de 2020 : (27.5 + 28.0)/2 = 28.5
    assert  len(resultat) == 2
    assert resultat[2010] == 27
    assert resultat[2020] == 28.5
    print("Test de multiples décennies (doit afficher True) :", resultat == {2010: 26.8, 2020: 27.75})