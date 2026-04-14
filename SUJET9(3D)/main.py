from Objet3D import Objet3D

#############################################################################
# Variables et fonctions fournies pour la question 3                        #
#############################################################################
parametres_imprimante = {'remplissage': 20,
                         'vitesse_extrusion': 8}  # 8mm3 / seconde


def volume_cube(cube):
    a, b = cube.sommets_adjacents()
    taille_cote = a.distance(b)  # distance donnee en mm
    return taille_cote ** 3

#############################################################################
# Écrire le code de la fonction estimation_impression de la question 3      #
#############################################################################
def estimation_impression(volume, parametres_imprimante) :
    volume_impression_objet = volume * parametres_imprimante["remplissage"] / 100
    temps = volume_impression_objet / parametres_imprimante["vitesse_extrusion"]
    return float(temps)
def test_estimation_impression():
    parametres = {'remplissage': 20, 'vitesse_extrusion': 10}
    volume = 100
    
    resultat = estimation_impression(volume, parametres)
    
    if resultat == 2.0:
        print("Test réussi ✅")
    else:
        print("Test échoué ❌")


#############################################################################
# Programme à modifier de la question 4 et 5                                #
#############################################################################
objet = Objet3D()
#Sommet de la base
objet.ajouter_sommet(0, 0, 0) #1
objet.ajouter_sommet(0, 1, 0) #2
objet.ajouter_sommet(1, 1, 0) #3
objet.ajouter_sommet(1, 0, 0) #4
#Sommet de la pyramide
objet.ajouter_sommet(0.5, 0.5, 1) #5
#La face de la base
objet.ajouter_face([1, 2, 3, 4])
#Face latérale, on relie deux sommets avec la sommet de le sommet
objet.ajouter_face([1, 2, 5])
objet.ajouter_face([2, 3, 5])
objet.ajouter_face([3, 4, 5])
objet.ajouter_face([4, 1, 5])
objet.afficher()
pyramide2 = objet.transformer(2)
pyramide2.afficher()