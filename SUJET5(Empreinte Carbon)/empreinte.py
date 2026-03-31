import os
import os.path
import json
########### Fonctions données ###########

def chargement_json(nom_fichier):
    """Charge le contenu d'un fichier JSON dans un dictionnaire Python renvoyé"""
    with open(nom_fichier, "r", encoding="utf8") as curseur:
        return json.load(curseur)


def sauvegarde_json(dictionnaire, nom_fichier):
    """Sauvegarde le contenu d'un dictionnaire dans un fichier JSON"""
    with open(nom_fichier, "w", encoding="utf8") as curseur:
        json.dump(dictionnaire, curseur)


def est_dictionnaire(objet):
    """Teste si un objet est de type dictionnaire"""
    return isinstance(objet, dict)


##########################################


### Première fonction à implémenter après avoir découvert le fichier JSON agrégé
### Cf fichier `empreinte_ada_agr.json`
def total_simple(empreinte) :
    """Fonction qui renvoie l'empreinte carbone totale d'un dictionnaire associant
    une empreinte carbone à des noms de catégories
    """
    total = 0
    for element in empreinte.values() :  #Pour les dictionnaires uniquement, values permet d'afficher uniquement les valeurs de dictionnaires
        total += element  
    return total

def test_total_simple() :
    variable = chargement_json("empreinte_ada_agr.json")
    assert total_simple(variable) == 7252

### Deuxième fonction : il faut la récursivité pour le cas des sous-catégories
### Cf fichier `empreinte_ada.json`
def total_rec(empreinte):
    """Fonction récursive qui renvoie l'empreinte carbone totale représentée
    par un dictionnaire dont les valeurs peuvent aussi être des dictionnaires"""
    if est_dictionnaire(empreinte) == False :
        return empreinte #Condition d'arrêt si la fonction n'est plus une dictionnaire mais une valeur
    total = 0 #On initialise une variable pour compter tout
    for valeur in empreinte.values() : #On accède au valeur de dico
        total += total_rec(valeur) #On parcours jusqu'à ce que le dictionnaire ne soit plus vrai et on additione avec total
    return total 
def test_total_rec():
    test_dico1 = {"a": 1, "d": 2}
    assert total_rec(test_dico1) == 3
    test_dico2 = {"a": {"b": 1, "c": 2}, "d": {"e": 3}}
    assert total_rec(test_dico2) == 6
    variable = "empreinte_ada.json"
    truc = chargement_json(variable)
    assert total_rec(truc) == 7252
# ==========================================
# Fonction à analyser et corriger (Question 3)
# ==========================================
def alerte_valeur_aberrante(empreinte, limite):
    """
    Fonction censée déterminer si au moins une valeur du dictionnaire
    dépasse strictement la limite donnée.
    """
    for categorie, valeur in empreinte.items():
        if est_dictionnaire(valeur):
            if alerte_valeur_aberrante(valeur, limite) : #On ne retourne pas immédiatement retourne parce qu'il va examiner qu'une seule partie de dictionnaire et on fait if pour examiner tout.
                return True
        else:
            if valeur > limite:
                return True
    return False

def test_alerte_valeur_aberrante() :
    variable = "empreinte_ada.json"
    truc = chargement_json(variable)
    assert alerte_valeur_aberrante(truc, 1000) == True
    assert alerte_valeur_aberrante(truc, 1600) == False 
    assert alerte_valeur_aberrante({}, 1000) == False 
    d1 = {"a" : 10, "b" : 20}
    assert alerte_valeur_aberrante(d1, 15) == True
    d2 = {"a" : {"b" : 5}, "c" : {"d": 8}}
    assert alerte_valeur_aberrante(d2, 10) == False 