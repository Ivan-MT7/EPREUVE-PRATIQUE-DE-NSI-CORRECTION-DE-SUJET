# ///////////////////////////////////////////////////////////////////////////
# FONCTIONS DONNEES
# ///////////////////////////////////////////////////////////////////////////

def recupere_donnees_fichier_csv(nom_fichier):
    """ Fonction qui récupère les données relevées du ballon sonde sans les en-têtes de la 1ère ligne """
    altitudes = []                                  # Initialisation des listes de valeurs relevées
    temperatures = []
    longitudes = []
    latitudes = []
    # Ouverture du fichier csv au format npm.csv en mode "read"
    contenu_fichier = open(nom_fichier, 'r')
    # Supprime la 1ère ligne avec les en-têtes
    contenu_fichier.readline()
    # Parcours des lignes du fichier csv contenant les donnees relevées
    for ligne in contenu_fichier.readlines():
        # rstrip() supprime les \n et espaces en fin de ligne
        ligne = ligne.rstrip()
        # création d'une listeValeurs. split(";") sépare les valeurs grâce au ;
        listeValeurs = ligne.split(";")
        # conversion string en int de l'altitude et insertion dans la liste correspondante
        altitudes.append(int(listeValeurs[0]))
        # conversion string en float de l'altitude et insertion dans la liste correspondante
        temperatures.append(float(listeValeurs[1]))
        # conversion string en float de l'altitude et insertion dans la liste correspondante
        longitudes.append(float(listeValeurs[2]))
        # conversion string en float de l'altitude et insertion dans la liste correspondante
        latitudes.append(float(listeValeurs[3]))
    return altitudes, temperatures, longitudes, latitudes


def genere_kml(liste_longitudes, liste_latitudes):
    """ Fonction qui génère un fichier de données géographiques au format standard international KML
        Ce fichier est visionnable ensuite dans différents logiciels
    """
    assert len(liste_longitudes) == len(liste_latitudes) #Question 4
    fichier_kml = open(
        'ballon sonde.kml', 'w')    # Création et ouverture du fichier kml en mode "write"
    entete_fichier = '<?xml version="1.0" encoding="UTF-8"?>\n'
    entete_fichier += '<kml xmlns="http://www.opengis.net/kml/2.2">\n'
    entete_fichier += '<Document>\n'
    entete_fichier += '<name>Trajectoire ballon sonde</name>\n'
    # Ecriture du contenu de la variable entete_fichier dans le fichier kml
    fichier_kml.write(entete_fichier)
    for i in range(len(liste_longitudes)):
        corps_fichier = '<Placemark>\n'
        corps_fichier += f'<name>Point {i}</name>\n'
        corps_fichier += '<Point>\n'
        corps_fichier += f'<coordinates>{liste_longitudes[i]},{liste_latitudes[i]}</coordinates>\n'
        corps_fichier += '</Point>\n'
        corps_fichier += '</Placemark>\n'
        fichier_kml.write(corps_fichier)
    bas_fichier = '</Document>\n'
    fichier_kml.write(bas_fichier)
    #Question 6
    bas_fichier = '</kml>\n'
    fichier_kml.write(bas_fichier)
    fichier_kml.close()                         # Fermeture du fichier kml


# ///////////////////////////////////////////////////////////////////////////
# TRAVAIL DEMANDE
# ///////////////////////////////////////////////////////////////////////////

# QUESTION 1
# Compléter ici
# On appelle la fonction pour récupérer les 4 listes de données du fichier CSV
altitudes, temperature, longitude, latitudes = recupere_donnees_fichier_csv("releves_ballon_sonde.csv")

# QUESTION 2
def conversion_K_en_C(liste_temperatures):
    liste_k = []
    for valeur in liste_temperatures :
        # Formule de conversion : °C = K - 273.15
        valeur = round(valeur - 273.15, 1)
        # On ajoute la valeur convertie dans la nouvelle liste
        liste_k.append(valeur)
    return liste_k
def test_conversion_K_en_C() :
    assert conversion_K_en_C([273.15]) == [0.0]
    assert conversion_K_en_C([273.15, 500]) == [0, 226.9]
    

# QUESTION 3
def altitude_la_plus_froide(liste_altitudes, liste_temperatures):
    temperature_basse = liste_temperatures[0]
    liste_index = []
    resultat = []
    for i in range(len(liste_temperatures)) :
        if liste_temperatures[i] < temperature_basse :
            temperature_basse = liste_temperatures[i]
            liste_index = [i]
        elif liste_temperatures[i] == temperature_basse :
            liste_index.append(i)
    for truc in liste_index :
        resultat.append(liste_altitudes[truc])
    return (temperature_basse, resultat)
altitudes = [7000, 10125, 13896, 14211]
temperatures = [-35.2, -52.1, -57.4, -57.4]
# AUTRES ELEMENTS DE CODE
def test_altitude_la_plus_froide() :
    altitudes = [7000, 10125, 13896, 14211]
    temperatures = [-35.2, -52.1, -57.4, -57.4]
    assert altitude_la_plus_froide(altitudes, temperatures) == (-57.4, [13896, 14211])
    altitudes = [6000, 7250, 11542, 15214, 17300]
    temperatures = [-33.7, -45, -53, -58.5, -60.1]
    assert altitude_la_plus_froide(altitudes,temperatures) == (-60.1, [17300])
    print("Test réussi")
#Question 5, une fichier apparaît dans le même répertoire
variable = genere_kml(longitude, latitudes)