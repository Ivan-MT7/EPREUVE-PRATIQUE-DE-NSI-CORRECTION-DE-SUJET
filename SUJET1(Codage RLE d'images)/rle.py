from PIL import Image

#1) La liste obtenue par codage RLE n'est pas forcement inférieure ou égale à la codage RLE.
#Exemple : Pour la liste, [1], on aura la liste RLE : [1, 1]
#4)Le problème est liée au fait qu'il est possible d'avoir 255 pixels de même couleur.
#On limite donc dans la fonction codage_rle pour que le maximum de pixel à ajouter dans une liste soit 255.
#Bug : [256, 255], solution : [255, 255, 1, 255]
def codage_rle(liste_octets):
    """Renvoie une liste d'octets obtenue par compression RLE"""
    liste_rle = []
    i = 0
    while i < len(liste_octets):
        valeur = liste_octets[i]
        occ = 1
        #Question 4 : On ajoute occ < 255.
        while i + occ < len(liste_octets) and liste_octets[i + occ] == valeur and occ < 255:
            occ += 1
        liste_rle.append(occ)
        liste_rle.append(valeur)
        i += occ
    return liste_rle

#On a [3, 4, 1, 0, 2, 5]
def decodage_rle(liste_rle):
    """Renvoie la liste d'octets obtenue à partir de la liste liste_rle obtenue
    par compression RLE"""
    #On initialise une variable pour décoder RLE
    resultat = []
    #On commence par initialiser une boucle bornée qui va de 0 à la fin de liste avec des pas de 2
    for i in range(0, len(liste_rle), 2) :
        #On initialise une variable repetition 
        repetition = liste_rle[i]
        while repetition != 0 :
            #On ajoute le resultat autant de fois jusqu'à ce que répétition ne soit pas égale à 0.
            resultat.append(liste_rle[i+1])
            repetition -= 1
    return resultat

def test_codage():
    assert codage_rle([255, 255, 0, 255, 255, 255]) == [2, 255, 1, 0, 3, 255]
    assert decodage_rle([2, 255, 1, 0, 3, 255]) == [255, 255, 0, 255, 255, 255]
    print("Test réussi")


def enregistrer_octets(nom_fichier, liste_octets):
    """Enregistre une liste de valeurs numériques entre 0 et 255 dans un
    le fichier nom_fichier. Si une valeur est plus grande que 255 on considère
    que c'est 255. De même pour les valeur plus petite que 0."""
    # Le fichier est ouvert en mode binaire pour pouvoir écrire sans restriction toute valeur
    # entre 0 et 255
    with open(nom_fichier, "wb") as fichier:
        # Pour convertir une liste de valeur entre 0 et 255 en une liste d'octets qui peuvent
        # être écrits dans le fichier, on utilise `bytes`
        fichier.write(bytes([max(0, min(255, b)) for b in liste_octets]))


def charger_octets(nom_fichier):
    """Renvoie la liste des octets présents dans le fichier nom_fichier"""
    with open(nom_fichier, "rb") as fichier:
        liste_octets = list(fichier.read())
        return liste_octets


def enregistrer_image(nom_image, largeur, liste_niveaux):
    """Enregistre un fichier image nom_image de la largeur donnée et dont les
    valeurs de niveaux de gris des pixels sont celles de la liste
    liste_niveaux"""
    hauteur = len(liste_niveaux) // largeur
    im = Image.frombytes("L", (largeur, hauteur), bytes(liste_niveaux))
    im.save(nom_image)


def charger_image(nom_image):
    """Étant donné une image nom_image, renvoie un couple (largeur, liste_niveaux) où
    largeur est la largeur de l'image et liste_niveaux est la liste des valeurs de niveaux
    de gris de l'image ligne par ligne"""

    image = Image.open(nom_image).convert("L")
    return (image.width, list(image.tobytes()))


#############################################################################
# Fonction nécessaire pour les tests de la question 3                       #
#############################################################################


def encoder_decoder_image(nom_image):
    """Fonction de test permettant d'encoder puis décoder une image avec un
    codage RLE. Le fichier rle est nommé nom_image.rle et le fichier decodé
    est nom_image.dec.png"""
    largeur, niveaux = charger_image(nom_image)
    enregistrer_octets(nom_image + ".rle", codage_rle(niveaux))
    niveaux_dec = charger_octets(nom_image + ".rle")
    enregistrer_image(nom_image + ".dec.png", largeur,
                      decodage_rle(niveaux_dec))
