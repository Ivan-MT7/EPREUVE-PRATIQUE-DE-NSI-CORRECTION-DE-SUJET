from math import sqrt
from donnees_habitats import zones_connues

nouveau = {'vegetation': 5, 'proximite_eau': 2, 'densite_urbaine': 4, 'disponibilite_proies': 6}

def distance(habitat_1, habitat_2):
    '''
    Calcule la distance euclidienne entre deux habitats.
    entrée : 
        - habitat_1 : dictionnaire représentant un habitat.
        - habitat_2 : dictionnaire représentant un autre habitat.
    sortie : 
        - float : distance euclidienne entre habitat_1 et habitat_2.
    '''
    d = sqrt(
        (habitat_1["vegetation"] - habitat_2["vegetation"])**2 +
        (habitat_1["proximite_eau"] - habitat_2["proximite_eau"])**2 +
        (habitat_1["densite_urbaine"] - habitat_2["densite_urbaine"])**2 +
        (habitat_1["disponibilite_proies"] - habitat_2["disponibilite_proies"])**2 
        )
    return d


def distance_d_un_habitat(habitat, habitats):
    '''
    Calcule la distance entre un habitat et chaque habitat de la liste.
    entrée : 
        - habitat : dictionnaire représentant un habitat.
        - habitats : liste de dictionnaires représentant des habitats.
    sortie : 
        - list[tuple] : liste de tuples (distance, habitat) où distance est la distance entre habitat et chaque habitat de la liste.
    '''
    array = []
    for element in habitats :
        array.append((distance(element, habitat), element))
    return array

def test_distance_d_un_habitat() :
    array = distance_d_un_habitat(nouveau, zones_connues)
    assert array[0] == (7.211102550927978, {'vegetation': 9, 'proximite_eau': 6, 'densite_urbaine': 0,
                                            'disponibilite_proies': 4, 'presence_renard': 1})
    assert array[1] == (8.660254037844387, {'vegetation': 10, 'proximite_eau': 5,
                                            'densite_urbaine': 9, 'disponibilite_proies': 10, 'presence_renard': 0})
    assert array[2] == (5.196152422706632, {'vegetation': 8, 'proximite_eau': 5,
                                            'densite_urbaine': 1,
                                            'disponibilite_proies': 6, 'presence_renard': 0})
    print("Test réussi")


def k_plus_proches(k, habitat, habitats):
    '''
    Calcule les k habitats les plus proches de l'habitat donné.
    entrée : 
        - k : entier représentant le nombre d'habitats à retourner.
        - habitat : dictionnaire représentant un habitat.
        - habitats : liste de dictionnaires représentant des habitats.
    sortie : 
        - list[tuple] : liste de tuples (distance, habitat) l'élément à l'indice 0 est la distance euclidienne entre habitat 
                        et chaque habitat de la liste et l'élément à l'indice 1 est le dictionnaire correspondant à l'habitat correspondant.
    '''
    # On calcule les distances
    distances = distance_d_un_habitat(habitat, habitats)
    # On cherche à trier les distances en fonction de la distance euclidienne.
    distances.sort(key = lambda x: x[0])
    return distances[:k] # renvoie les distances jusque la borne k non comprise

def presence_renard(k, habitat, habitats):
    '''
    Vérifie si l'habitat donné a plus de k/2 voisins avec des renards.
    entrée : 
        - k : entier représentant le nombre d'habitats à considérer.
        - habitat : dictionnaire représentant un habitat.
        - habitats : liste de dictionnaires représentant des habitats.
    sortie : 
        - bool : True si l'habitat a plus de k/2 voisins avec des renards, False sinon.
    '''
    habitats = k_plus_proches(k, habitat, habitats)
    n_renards = 0
    for habitat in habitats :
        distance = habitat[0]
        caracteristiques = habitat[1]
        if caracteristiques['presence_renard'] == 1:
            n_renards += 1
    return n_renards > k/2
#Question 4 : On change dans la condition la distance["presence_renard"] == 1
#vers caracteristiques["presence_rendard"]

#Question 5

# On teste la fonction presence_renard avec différentes valeurs de k
# pour déterminer si la zone "nouveau" est susceptible d'accueillir des renards

print(presence_renard(3, nouveau, zones_connues))  # k = 3
print(presence_renard(5, nouveau, zones_connues))  # k = 5
print(presence_renard(7, nouveau, zones_connues))  # k = 7

# Si la majorité des résultats est True, alors la zone est susceptible
# d'accueillir des renards.