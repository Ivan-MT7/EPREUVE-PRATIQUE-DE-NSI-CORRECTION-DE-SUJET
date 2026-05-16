import ascii

#############################################################################
# Question 1 et 2 : Écrire les codes des fonctions bin2dec et qrcode2dec
#              Proposer un test de qrcode2dec
#############################################################################
    
# implémentation du QR Code de la figure 1:
qrcode_fig1 = ascii.figure1
def bin2dec(nombre_binaire) :
    # On initialise la valeur décimale à 0
    resultat = 0
    # On parcourt chaque bit du tuple de gauche à droite
    for i in range(len(nombre_binaire)) :
        # Si le bit est à 1, on ajoute la puissance de 2 correspondante.
        # (len(t_bin) - 1 - i) permet d'avoir la bonne puissance de 2 selon la position.
        resultat += nombre_binaire[i] * 2**(len(nombre_binaire) - 1 - i)
    return resultat
def qrcode2dec(qrcode) :
    """
    Entrée : Une liste de tuples (le QR code complet)
    Sortie : Une liste d'entiers décimaux (chaque ligne convertie)
    """
    entiers = []
    # On parcourt chaque tuple binaire (chaque ligne) du qrcode
    for ligne in qrcode:
        # On convertit cette ligne binaire en entier décimal grâce à bin2dec
        # Puis on l'ajoute à la liste des entiers
        entiers.append(bin2dec(ligne))
    return entiers
#nom de créateur de qrcode demandé dans la question 1
liste_decimale = qrcode2dec(qrcode_fig1)
ch = ""
for nombre in liste_decimale :
    ch += ascii.dict_ascii[nombre]
print(ch) #M.Hara
def test_qrcode2dec() :
    assert qrcode2dec(qrcode_fig1) == [77, 46, 72, 97, 114, 97]
    print("Test réussi")
#############################################################################
# Question 3 : Fonctions dec2str et test_dec2str
#############################################################################

# PROBLÈME IDENTIFIÉ : Le test3 de test_dec2str inclut le nombre 233. 
# Or, la table ascii du dictionnaire s'arrête à 127. Cela déclenche une erreur KeyError.
# MODIFICATION APPORTÉE : On vérifie si l'entier est présent dans la table avant de l'ajouter.

def dec2str(liste_dec):
    """ entrée: liste d'entiers décimaux
        sortie: chaine de caractère formée des caractères correspondant
        de la table ascii """
    table_ascii = ascii.dict_ascii
    chaine = ""
    for entier in liste_dec:
        # On vérifie que l'entier est bien dans le dictionnaire pour éviter le plantage
        if entier in table_ascii :
            chaine += table_ascii[entier]
    return chaine


def test_dec2str():
    """ Teste la fonction dec2str avec des données issues du module fourni """
    tests = [ascii.test1, ascii.test2, ascii.test3]
    for test in tests:
        print(dec2str(test))


def qrcode2str(qrcode):
    return dec2str(qrcode2dec(qrcode))

#############################################################################
# Question 4 : Fonction str2qrcode déficiente
#############################################################################

# PROBLÈME IDENTIFIÉ : La fonction bin(entier) enlève les zéros non significatifs à gauche.
# Par exemple pour 97 ("a"), on obtiendra "1100001" (7 bits) au lieu de "01100001" (8 bits).
# Cela décale les tuples et les rangées qui doivent strictement contenir 8 bits.
# MODIFICATION APPORTÉE : On rajoute des "0" au début de la chaîne binaire jusqu'à ce qu'elle fasse 8 de long.
def str2qrcode(message):
    """
    Convertit une chaine de caractères en liste de tuples binaires.
    """
    qrcode = []
    table_inverse = {valeur: cle for cle, valeur in ascii.dict_ascii.items()}
    for caractere in message:
        entier = table_inverse.get(caractere, 63)
        binaire_str = bin(entier)[2:] #bin(entier) ne garde pas les zéros à gauche.
        # On complète avec des zéros à gauche pour avoir exactement 8 bits.
        while len(binaire_str) < 8:
            binaire_str = "0" + binaire_str

        ligne = tuple(int(bit) for bit in binaire_str)
        qrcode.append(ligne)

    return qrcode
