#############################################################################
# Jeux de données fournis                                                   #
#############################################################################
from plantes import plantes
from plantes import plantes_1
from plantes import plantes_2
from mesures import mesures

#############################################################################
# Écrire le code de la fonction croissance_moyenne de la question 1         #
#############################################################################

#1) Pour cette exercice, il faut additioner le croissance de tous les plantes
#et ensuite diviser par le nombre total des plantes ce qui fait la croissance moyenne de tous les plantes
def croissance_moyenne(plantes) :
    if len(plantes) == 0 :
        return None
    croissance_ensemble = 0
    for i in range(len(plantes)) :
        croissance_ensemble += plantes[i].croissance
    return croissance_ensemble / len(plantes)

def test_croissance_moyenne() :
    assert croissance_moyenne([]) == None
    assert croissance_moyenne(plantes) == 79.0
#############################################################################
# Écrire le code de la fonction dictionnaire_mesure de la question 2      #
#############################################################################


#1) on crée d’abord toutes les clés avec des listes vides ;
#2) puis on range chaque mesure dans la bonne liste ;
#3) si une mesure concerne une plante absente de plantes, elle est ignorée.
def dictionnaire_mesure(plantes, mesures) :
    dico = {}
    for plante in plantes :
        dico[plante.nom] = []
    for mesure in mesures :
        if mesure["plante"] in dico :
            dico[mesure["plante"]].append(mesure)
    return dico

def test_dictionnaire_mesure() :
    assert  dictionnaire_mesure(plantes_1, mesures) == {"Vegetum" : []}
    assert dictionnaire_mesure(plantes, []) == {'Basilic': [], 'Tomate': [], 'Menthe': [], 'Tournesol': [], 'Fougère': []}
    resultat = dictionnaire_mesure(plantes_2, mesures)
    assert "Basilic" in resultat
    assert len(resultat["Basilic"]) == 60
    assert resultat["Basilic"][0]["jour"] == 1
    assert resultat["Basilic"][59]["jour"] == 60
#Si les assertions sont égales à True alors le test est réussi

#############################################################################
# Fonction défaillante à analyser et corriger pour les questions 3 et 4     #
#############################################################################

def purger_mesures_extremes(liste_mesures):
    """
    Supprime de la liste toutes les mesures dont la température 
    n'est pas comprise entre 20 et 25°C inclus.
    """
    return [element for element in liste_mesures if element["temperature"] >= 20 and element["temperature"] <= 25] 
#Il y avait une erreur pour le programme en dessous car cela modifie la boucle en place. Pn doit utiliser une tableau de compréhension plûtot que de parcourir le boucle et de modifier les variables
#     for mesure in liste_mesures:
#         if mesure['temperature'] < 20 or mesure['temperature'] > 25: 
#             liste_mesures.remove(mesure)
#     return liste_mesures

def test_purger():
    mesures_test = [
         {'jour': 1, 'plante': 'Basilic', 'temperature': 18.0},
         {'jour': 2, 'plante': 'Basilic', 'temperature': 19.0},
         {'jour': 3, 'plante': 'Basilic', 'temperature': 22.0},
         {'jour': 4, 'plante': 'Basilic', 'temperature': 28.0},
         {'jour': 5, 'plante': 'Basilic', 'temperature': 29.0}
    ]

    mesures_test = purger_mesures_extremes(mesures_test) #Il y avait une erreur, on devait assigner mesures_test à cette fonction

    print("Résultat après la purge :")
    for m in mesures_test:
        print(f"Jour {m['jour']} : {m['temperature']}°C")