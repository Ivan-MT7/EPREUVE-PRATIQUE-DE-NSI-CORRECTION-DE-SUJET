import donnees
import donnees_completes
from math import sqrt


def salaire_moyen_condition(employes, champ, valeur):
    '''Renvoie le salaire moyen des employes ayant val comme valeur associée
    au champ donné en argument.
    Si le nombre d'employés considéré est nul, cette fonction renvoie None'''
    salaire_total = 0
    nombre_employe = 0
    for employe in employes :
        if employe[champ] == valeur :
            salaire_total += employe["salaire"]
            nombre_employe += 1
    if nombre_employe == 0 :
        return None
    return float(salaire_total // nombre_employe)
    

def test_salaire_moyen_condition():
    e = donnees.employes
    assert salaire_moyen_condition([], 'sexe', 'F') == None
    assert salaire_moyen_condition(e, 'sexe', 'F') == 2400.0
    assert salaire_moyen_condition(e, 'etudes', 3) == 2550.0
    assert salaire_moyen_condition(e, 'etudes', 12) == None
    print("Test réussi")


def effectif_par_sexe(employes):
    '''Renvoie un dictionnaire ayant deux clés 'F' et 'M'
    associée respectivement au nombre d'employées femmes et au
    nombre d'employés hommes dans les données en arguments.'''
    resultat = {"F" : 0, "M" : 0}
    for employe in employes :
        resultat[employe["sexe"]] += 1
    return resultat

def test_effectif_par_sexe():
    e = donnees.employes
    assert effectif_par_sexe(e) == {'F': 3, 'M': 3}
    print("Test réussi")


def calcul_ecart_sexe(employes):
    '''Renvoie l'écart de salaire en pourcentage pour les femmes 
    par rapport aux hommes'''
    truc = [employe["sexe"] for employe in employes]
    if "F" not in truc or "M" not in truc :
        return None
    moy_h = salaire_moyen_condition(employes, 'sexe', 'M')
    moy_f = salaire_moyen_condition(employes, 'sexe', 'F')
    return (moy_h - moy_f) / moy_h * 100 
#3) La fonction est incorrecte car dans moy_f, employes est considéré comme une chaîne de caractères.
#De plus la formule appliquée est incorrecte, il faut faire ecart = (moy_h - moy_f) / moy_h * 100
#L'écart de salaire moyen est 10.55 % arrondi au centième.
def test_calcul_ecart_sexe() :
    dico = [{'experience': 5, 'etudes': 3, 'sexe': 'F', 'salaire': 2400},
            {'experience': 3, 'etudes': 3, 'sexe': 'M', 'salaire': 2550},
            {'experience': 5, 'etudes': 5, 'sexe': 'F', 'salaire': 2500},
            {'experience': 3, 'etudes': 5, 'sexe': 'M', 'salaire': 2800}
            ]
    ecart = float(calcul_ecart_sexe(dico))
    assert round(ecart, 2) == 8.41
    print("Test réussi")
    




# Attribution d'un premier salaire après embauche par les k plus proches voisins


def sexe_vers_entier(e):
    if e['sexe'] == 'F':
        return 1
    else:
        return -1


def distance(e1, e2):
    '''Renvoie la mesure de distance entre deux personnes.'''
    s = 0
    #Q4)
    #On doit supprimer le s pour que ça ne compte pas le sexe.
    #s = s + (sexe_vers_entier(e1) - sexe_vers_entier(e2))**2
    s = s + (e1['experience'] - e2['experience'])**2
    s = s + (e1['etudes'] - e2['etudes'])**2
    return sqrt(s)


def k_plus_proches(k, employes, e):
    '''Renvoie les k employes les plus proches de e par la 
    distance définie au dessus.'''
    e_d = [(distance(e, employes[i]), i) for i in range(len(employes))]
    e_d.sort()  # va trier en premier sur la distance
    voisins = []
    for i in range(k):
        voisins.append(employes[e_d[i][1]])
    return voisins


def salaire_moyen(employes):
    '''Renvoie le salaire moyen pour une liste d'employes'''
    if len(employes) == 0:
        return None
    s = sum(e['salaire'] for e in employes)
    return s/len(employes)


def salaire_par_proximite(employes, e):
    '''Prend en entrée une liste d'employés et un dictionnaire comportant
    les champs experience, etudes et sexe et renvoie le salaire le plus
    proche en moyennant les 3 plus proches voisins'''
    voisins = k_plus_proches(3, employes, e)
    return salaire_moyen(voisins)





