# ------------------------------------
# gestion_eau.py
# Programme de contrôle des réservoirs
# ------------------------------------
from donnees import reservoirs

# Question 1 : écrire la fonction est_en_penurie


def est_en_penurie(reservoirs, nom_reservoir):
    # On parcourt chaque réservoir de la liste
    for reservoir in reservoirs :
        # Si on trouve le réservoir avec le bon nom
        if nom_reservoir == reservoir["nom"] :
            volume_actuel = reservoir["volume"]
            capacite_total = reservoir["capacite"]
            # On calcule son taux de remplissage (en pourcentage)
            pourcentage = (volume_actuel / capacite_total)*100
            # On renvoie True si le taux est strictement inférieur à 20, sinon False
            return pourcentage < 20
            

# Question 2 : écrire la fonction volume_par_district


def volume_par_district(reservoirs):
    resultat = {}
    # On parcourt tous les réservoirs
    for reservoir in reservoirs :
        # Si le district n'existe pas encore dans le dictionnaire, on assigne le district avec le volume
        if reservoir["district"] not in resultat :
            resultat[reservoir["district"]] = reservoir["volume"]
        # On ajoute le volume du réservoir au total du district s'il existe
        else :
            resultat[reservoir["district"]] += reservoir["volume"]
    return resultat
# Question 3


def volume_moyen(reservoirs):
    """
    Renvoie le volume moyen d'eau disponible dans les réservoirs.
    """
    # 1. Test : vérifier que la liste contient au moins un réservoir
    assert len(reservoirs) > 0, "La liste des réservoirs ne doit pas être vide"
    somme_totale = 0
    capacite_max = 0

    for r in reservoirs:
        somme_totale += r["volume"]
        # On mémorise la plus grande capacité pour le second test
        if r["capacite"] > capacite_max:
            capacite_max = r["capacite"]
    # La correction de l'erreur est ici : 
    # on divise par len(reservoirs) au lieu de (len(reservoirs)-1)
    moyenne = somme_totale / (len(reservoirs))
    # 2. Test : vérifier qu'une moyenne doit être strictement inférieure 
    # ou égale à la plus grande capacité parmi les réservoirs de la liste
    return moyenne
def test_volume_moyen() :
    # 3. Test : vérifier que la fonction renvoie le bon résultat dans un cas simple
    # On crée une petite liste de deux réservoirs identiques
    liste_1 = [
        {"nom": "Smooth", "capacite": 100000, "volume": 55000, "district": "Tepua"},
        {"nom": "Thriller", "capacite": 20000, "volume": 10000, "district": "Tepua"}

        
        ]
    assert len(liste_1) >= 1
    assert volume_moyen(liste_1) <= max(r["capacite"] for r in liste_1)
    assert volume_moyen(liste_1) == 32500, "La moyenne de 55000 et 10000 est 32500"
    print("Test réussi")
    
    

        
# Question 4


def liste_districts(reservoirs):
    """
    Renvoie la liste des districts présents dans les données.
    """
    liste = []
    for r in reservoirs:
        if (r["district"] not in liste):
            liste.append(r["district"])
    return liste


def reservoirs_par_district(reservoirs):
    """
    Renvoie un dictionnaire associant chaque district à la liste
    des réservoirs qui s’y trouvent.
    """
    liste_rpd = {}
    for r in reservoirs:
        district = r["district"]
        if district not in liste_rpd:
            liste_rpd[district] = []
        liste_rpd[district].append(r)
    return liste_rpd


def districts_vulnerables(reservoirs):
    """
    Identifie les districts dont le volume moyen par réservoir est
    inférieur à seuil * volume moyen global (ex: 80% = 0.8).
    Utilise les fonctions fournies précédemment.
    """
    districts = liste_districts(reservoirs)
    # On rassemble les réservoirs par district (la clé est le district, la valeur sa liste de réservoirs)
    rpd = reservoirs_par_district(reservoirs)
    # On calcule le volume moyen global de tous les réservoirs

    moyenne_global = volume_moyen(reservoirs)
    resultat = []
    
    # On va calculer la moyenne de chaque district pour voir s'il est vulnérable
    for district in districts:
        moyenne_district = volume_moyen(rpd[district])
        # Si la moyenne locale est sous le seuil global, on garde le district
        if moyenne_district < 0.8 * moyenne_global:
            resultat.append(district)

    return resultat
#Exemple d'execution :
#districts donne toutes les noms de districtes donc ['Tepua', 'Fare', 'Hiva Oro', 'Avera']
#rpd(reservoire par district) associe une clé districts à ces reservoires
#On calcule la moyenne global de tous les réservoirs
#On calcule la moyenne de tous les districtes
#Si la moyenne de cette district spécifique est inférieure à la 80% de moyennne global on l'ajoute dans le resultat.

