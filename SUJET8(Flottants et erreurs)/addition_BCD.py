#############################################################################
# Question 1 : Mise en évidence du problème des flottants                   #
#############################################################################
# Écrire ci-dessous la fonction calcul_recettes() et son appel
def calcul_recettes(nombre) :
    resultat = 0
    for i in range(nombre) :
        resultat = resultat + (2.27 + 5.19 + 1.81)
    return resultat
#On obtient une résultat de 4635.000000000018 au lieu de 4635 car lorsqu'on additionne les nombres le résultat n'est pas 9.27 à cause de float
#qui ne peut pas convertir correctement les nombres flottantes.

#############################################################################
# Question 2 : Conversion BCD vers Décimal                                  #
#############################################################################
# Écrire ci-dessous la fonction convertir_BCD_vers_decimal(liste_quartets)
# et l'assertion de test demandée
def convertir_BCD_vers_decimal(liste_quartets) :
    resultat = ""
    for i in range(len(liste_quartets)) :
        nombre = 0 #On génére un nombre pour donner le résultat d'une chaine de caractères 
        nb = 1 #On génére un nombre pour modifier le nombre si le bit est égale à 1

        for j in range(len(liste_quartets[i])-1, -1, -1) : #On parcours, le boucle de manière inverse pour le chaîne de caractère car on sait pas combien d'éléments il peut contenir
            if liste_quartets[i][j] == "1" : #Si le nombre est 1, on ajoute nb
                nombre += nb
            nb*=2 #On multiplie par 2 pour que les additions soient 
        if i == len(liste_quartets)-2 : #On vérifie qu'on est pas à 2 dernière élément 
            resultat += "."
        resultat += str(nombre)
    return float(resultat)

                
            
            
def test_convertir_BCD_vers_decimal() :
    assert convertir_BCD_vers_decimal(['0001', '0011', '0101', '0110']) == 13.56


#############################################################################
# Code fourni pour les questions 3 et 4                                     #
#############################################################################

def convertir_dec_vers_BCD(decimal):
    """
    Convertit une chaîne représentant un décimal vers une liste de quartets BCD.
    Convention : virgule implicite avant les deux derniers quartets.
    """
    ajouter_zero = False
    liste_quartets = []

    if '.' not in decimal:
        decimal = decimal + '.00'

    for i in range(len(decimal)):
        if decimal[i] != '.':
            quartet = bin(int(decimal[i]))[2:].zfill(4)
            liste_quartets.append(quartet)

        # Si le nombre n'a qu'un seul chiffre après la virgule
        if decimal[i] == '.' and i == len(decimal) - 2:
            ajouter_zero = True

    if ajouter_zero:
        liste_quartets.append('0000')

    return liste_quartets


def additionner_binaire_quartets(quartet1, quartet2, retenue):
    """
    Additionne bit à bit deux quartets binaire purs.
    Renvoie un tuple (somme_binaire_str, nouvelle_retenue_int).
    """
    somme = ""
    for i in range(4):
        # Lecture de la droite vers la gauche
        bit1 = int(quartet1[3 - i])
        bit2 = int(quartet2[3 - i])
        total = bit1 + bit2 + retenue

        if total == 0:
            somme = '0' + somme
            retenue = 0
        elif total == 1:
            somme = '1' + somme
            retenue = 0
        elif total == 2:
            somme = '0' + somme
            retenue = 1
        elif total == 3:
            somme = '1' + somme
            retenue = 1

    return somme, retenue


def corriger_BCD(somme, retenue):
    """
    Applique la correction BCD si le quartet dépasse 9 ou génère une retenue.
    Ajoute '0110' (6) au quartet invalide.
    """
    # Si somme >= 10 ('1010' ou '1011' ou '1100' etc.)
    if somme[0] == '1' and (somme[1] == '1' or somme[2] == '1'):
        somme, retenue = additionner_binaire_quartets(somme, '0110', 0)
        return somme, retenue

    # S'il y a eu dépassement naturel lors de l'addition binaire
    if retenue == 1:
        somme, _ = additionner_binaire_quartets(somme, '0110', 0)
        return somme, retenue
        
    return somme, retenue


def aligner_quartets(q1: list, q2: list) -> tuple:
    """
    Doit équilibrer les deux listes en ajoutant des '0000' à gauche 
    de la liste la plus courte.
    """
    #On ajoute à gauche donc on utilise insert(0, "0000") ou ["0000"] + q1. Je préfère utiliser cela car le prof de nsi dit que les fonctions natives peuvent être interditsK
    while len(q1) < len(q2) :
        q1 = ["0000"] + q1
    while len(q2) < len(q1) :
        q2 = ["0000"] + q2
    return q1, q2


def additionner_nombres_format_BCD(a, b):
    """
    Additionne deux nombres au format BCD, quartet par quartet.
    """
    liste_quartets1 = convertir_dec_vers_BCD(a)
    liste_quartets2 = convertir_dec_vers_BCD(b)
    

    # Ajustement de la longueur
    liste_quartets1, liste_quartets2 = aligner_quartets(liste_quartets1, liste_quartets2)

    retenue = 0
    resultat = []
    longueur_max = max(len(liste_quartets1), len(liste_quartets2)) 

    for i in range(longueur_max):
        index = longueur_max - i - 1
        
        # Addition binaire simple des quartets
        somme, retenue = additionner_binaire_quartets(liste_quartets1[index], liste_quartets2[index], retenue)
        print("avant correction :", somme, retenue)
        somme, retenue = corriger_BCD(somme, retenue)
        print("après correction :", somme, retenue)

        resultat.insert(0, somme) 

    # Gestion de la dernière retenue éventuelle
    if retenue == 1:
        resultat.insert(0, '0001')
        
    return resultat