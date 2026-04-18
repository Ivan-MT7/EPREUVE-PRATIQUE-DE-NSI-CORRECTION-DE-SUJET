donnees = [
    {"jour": "2025-02-04", "heure": "00:00", "chaude": 2, "froide": 3},
    {"jour": "2025-02-04", "heure": "01:00", "chaude": 1, "froide": 2},
    {"jour": "2025-02-04", "heure": "02:00", "chaude": 0, "froide": 0},
    {"jour": "2025-02-04", "heure": "03:00", "chaude": 0, "froide": 0},
    {"jour": "2025-02-04", "heure": "04:00", "chaude": 0, "froide": 1},
    {"jour": "2025-02-04", "heure": "05:00", "chaude": 0, "froide": 0},
    {"jour": "2025-02-04", "heure": "06:00", "chaude": 4, "froide": 6},
    {"jour": "2025-02-04", "heure": "07:00", "chaude": 6, "froide": 8},
    {"jour": "2025-02-05", "heure": "00:00", "chaude": 0, "froide": 0},
    {"jour": "2025-02-05", "heure": "01:00", "chaude": 1, "froide": 1},
    {"jour": "2025-02-05", "heure": "02:00", "chaude": 1, "froide": 1},
    {"jour": "2025-02-05", "heure": "03:00", "chaude": 1, "froide": 1},
    {"jour": "2025-02-05", "heure": "04:00", "chaude": 0, "froide": 0},
    {"jour": "2025-02-05", "heure": "05:00", "chaude": 0, "froide": 0},
]


# -----------------------------
# Fonctions à compléter
# -----------------------------

def total_conso(donnees, jour):
    # À compléter
    #On initialise une variable total pour avoir un résultat
    total = 0
    trouve = None
    for mesure in donnees :
        if jour == mesure["jour"] :
            #On additionne le volume d'eau chaude et le volume d'eau froide si le jour est la même
            total += mesure["chaude"] + mesure["froide"]
            #On modifie trouve = True puisque le jour existe
            trouve = True  
    if trouve : #Si le variable était modifié, on le renvoie sinon None.
        return total
    return None
        
            
        
   
def test_total_conso() :
    assert  total_conso(donnees, "2025-02-04") == 33
    assert  total_conso(donnees, "2025-06-02") == None
    print("test réussis")


def fuite_possible(donnees, jour):
    # À compléter
    mesure_filtre = []
    for mesure in donnees :
        if mesure["jour"] == jour and mesure["heure"] <= "05:00" :
            mesure_filtre.append(mesure)
    consecutive = 0
    for mesure_heure in mesure_filtre :
        if mesure_heure["chaude"] + mesure_heure["froide"] > 0 :
            consecutive += 1
        else :
            consecutive = 0
        if consecutive == 3 :
            return True
    return False
        
        
    
    
            
def test_fuite_possible() :
    assert fuite_possible(donnees, "2025-02-04") == False 
    assert fuite_possible(donnees, "2025-02-05") == True
    print("Test réussi")


# -----------------------------
# Fonction fournie (erronée)
# -----------------------------




# -----------------------------
# QUESTION 3 : correction de lissage_conso
# -----------------------------

# EXPLICATION DE L'ERREUR :
# Pour les éléments intermédiaires (ni le premier, ni le dernier), on calcule
# la moyenne de TROIS valeurs : la valeur précédente, la valeur actuelle et la valeur suivante.
# Or le code initial divisait par 2 au lieu de 3, ce qui ne donne pas la vraie moyenne.
# Exemple avec [10, 20, 30, 40, 50] pour l'élément d'indice 1 (valeur 20) :
#   Résultat incorrect : (10 + 20 + 30) / 2 = 30.0   (faux)
#   Résultat correct   : (10 + 20 + 30) / 3 = 20.0   (juste

def lissage_conso(valeurs):
    """
    Calcule une moyenne glissante sur les valeurs.
    Pour chaque valeur, on calcule la moyenne avec ses voisins.
    """
    # Si la liste est vide, il n'y a rien à lisser → on renvoie une liste vide
    if len(valeurs) == 0 :
        return []
    # Si la liste contient un seul élément, la moyenne = l'élément lui-même
    if len(valeurs) == 1 :
        return valeurs
    lisse = []
    for i in range(len(valeurs)):
        if i == 0:
            m = (valeurs[i] + valeurs[i+1]) / 2
        elif i == len(valeurs)-1:
            m = (valeurs[i-1] + valeurs[i]) / 2
        else:
            #Il faut diviser par 3 au lieu de 2
            m = (valeurs[i-1] + valeurs[i] + valeurs[i+1]) / 3
        lisse.append(m)
    
    return lisse


# -----------------------------
# Espace pour les tests
# -----------------------------

def test_lissage():
    # À compléter : produire au moins 3 tests révélant les erreurs
    assert lissage_conso([10, 20, 30, 40, 50]) == [15.0, 20.0, 30.0, 40.0, 45.0]
    assert lissage_conso([10]) == [10]
    assert lissage_conso([]) == []
    assert lissage_conso([10, 20]) == [15, 15]
    print("Les tests sont réussis")