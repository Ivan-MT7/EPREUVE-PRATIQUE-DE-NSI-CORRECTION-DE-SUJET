# -----------------------------------------------------------------------------
# Numéros de téléphones
# Question 1 : nettoyage des numéros de téléphone

# Écrire la fonction normalisation_tel ici


import sqlite3

def normalisation_tel(numero) :
    # On initialise une chaîne de caractères vide pour construire le numéro nettoyé
    numero_normal = ""
     # On parcourt chaque caractère de la chaîne 'numero'
    for ch in numero :
        # On vérifie si le caractère est un chiffre
        if ch.isdigit():
            # Si c'est un chiffre, on l'ajoute à la suite de notre résultat
            numero_normal += ch
    return numero_normal
def test_normalisation_tel():
    """
    Tous les tests doivent passer...
    """
    assert normalisation_tel("06 12 99 90 12") == "0612999012"
    assert normalisation_tel("02 12 99 90 12") == "0212999012"
    assert normalisation_tel("02.12.99.90.12") == "0212999012"
    assert normalisation_tel("0.6.12.99.90.12") == "0612999012"
    assert normalisation_tel("06-12-99-90-12") == "0612999012"
    assert normalisation_tel("(0)6.12.99-90-12 gilbert") == "0612999012"
    assert normalisation_tel("061299901") == "061299901"
    assert normalisation_tel("06129990123") == "06129990123"
    print('Les tests de la fonction normalisation_tel sont passés')

test_normalisation_tel()
# -----------------------------------------------------------------------------
# Question 2 : validation des numéros de téléphone


def validation_tel(tel):
    """
    Validation des numéros de téléphone portable français
    selon les conditions spécifiées.
    :param tel: numéro de téléphone
    :return: True si le numéro est valide, False sinon
    """
    if len(tel) != 10:
        return False
    if tel[0] != "0":
        return False
    if tel[1] != "6" and tel[1] != "7":
        return False
    return True


# Ecrire votre jeu de tests permettant
# de vérifier le bon fonctionnement de la fonction.
def test_validation() :
    # Test d'un numéro de longueur incorrecte (10+ chiffres)

    assert validation_tel("0602020202020202") == False
    # Test d'un numéro qui ne commence pas par 0 (le 1er caractère)
    assert validation_tel("16273783839") == False
    # Test d'un numéro (ne commence ni par 06 ni par 07, mais par 03)
    assert validation_tel("0312999012") == False
    # Test d'un numéro valide commençant par 07
    assert validation_tel("0712999012") == True
    # Test d'un numéro valide commençant par 06

    assert validation_tel("0622333012") == True 
    print("Les tests de la fonction validation sont passés")
test_validation()

# -----------------------------------------------------------------------------
# Détermination de la liste des chats à vacciner
# Question 3 : interrogation de la base de données

DB_PATH = "cabinet.sqlite"


def proprietaires_animaux_nes_apres(date):
    """
    Renvoie les noms et prénoms des propriétaires d'animaux nés après la date `date`,
    triés par ordre alphabétique de noms puis prénoms

    :param: date: date de naissance minimale
    :return: liste [(nom_proprietaire, prenom_ proprietaire)]
    """
    conn = sqlite3.connect(DB_PATH) #On ouvre le fichier de bases de données
    cursor = conn.cursor() #Création d'un curseur pour executer les rêquetes ensuite
    resultat = cursor.execute(
        """
    SELECT proprietaire.nom, proprietaire.prenom
    FROM proprietaire
        JOIN  animal ON proprietaire.id = animal.id_proprietaire 
    WHERE animal.date_naissance > ?
    ORDER BY proprietaire.nom, proprietaire.prenom;
    """,
        (date,),
    )
    return list(resultat)


def consultation_vaccination_chat(date):
    """
    Renvoie les consultations de vaccination de chats dont la date
    est supérieure à la date `date`.

    :param: date: date minimale
    :return: liste [(id_animal, nom_animal, tel_proprietaire, date_consultation)]
    """
    # Étape 1 : Connexion à la base de données SQLite

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # Étape 2 : Exécution de la requête SQL demandée
    # On sélectionne les champs : id de l'animal, nom de l'animal, téléphone du propriétaire, date de consultation.
    # On fait des jointures entre 'consultation', 'animal' et 'proprietaire' pour relier toutes les données.
    # On filtre (WHERE) pour que l'espèce soit 'chat', que le motif soit 'vaccination' et que la date soit supérieure au paramètre 'date'.
    # On trie (ORDER BY) par id d'animal croissant, puis par date de consultation croissante.
    resultat = cursor.execute(
        """
        SELECT  animal.id, animal.nom, proprietaire.telephone, consultation.date
        FROM consultation
        JOIN animal on animal.id == consultation.id_animal 
        JOIN proprietaire on animal.id_proprietaire == proprietaire.id
        WHERE consultation.date > ? and animal.espece == "chat" and consultation.motif == "vaccination"
        ORDER BY animal.id, consultation.date;
        """,
            (date,),
        )
    # Étape 3 : Conversion du résultat ('resultat' est itérable) en liste Python et on le renvoie
    return list(resultat)


def test_consultation_vaccination_chat():
    vaccinations = consultation_vaccination_chat("20240923")
    assert len(vaccinations) == 118
    assert vaccinations[0] == (16, "Plume", "0.6.36.96.89.83", "20241024")
    assert vaccinations[1] == (16, "Plume", "0.6.36.96.89.83", "20251125")
    assert vaccinations[2] == (17, "Gollum", "0.6.36.96.89.83", "20250113")
    assert vaccinations[3] == (26, "Olympe", "(0)4 73 98 01 23", "20250109")
    assert vaccinations[4] == (32, "Chopin", "06.37.97.66.64", "20241201")
    assert vaccinations[5] == (32, "Chopin", "06.37.97.66.64", "20251119")
    assert vaccinations[6] == (34, "Jazz", "0.6.37.51.65.52", "20250801")
    assert vaccinations[7] == (35, "Tango", "0324182", "20250706")
    assert vaccinations[8] == (38, "Loulou", "05-35-95-87-54", "20250209")

    # Vérification stricte du tri (ORDER BY id_animal, date_consultation)
    assert vaccinations == sorted(vaccinations, key=lambda x: (x[0], x[3]))

    print('Les tests de la fonction consultation_vaccination_chat sont passés')

test_consultation_vaccination_chat()

# -----------------------------------------------------------------------------
# Question 4 : détermination de la date de dernière vaccination


def derniere_vaccination(consultations):
    """
    Renvoie un dictionnaire ayant pour clef l'identifiant de l'animal,
    et dont la valeur associée est la dernière consultation de cet animal.

    Chaque consultation est un tuple :

    (id_animal, nom_animal, tel_proprietaire, date_consultation)
    """
    derniere = {}
    for consult in consultations:
        #EXPLICATION DU DÉBOGAGE (Question 4) :
        #Le problème dans la fonction d'origine était sur la ligne 'elif date < derniere[id_animal][3]:'.
        #Cette condition conservait la date la moins récente (la plus ancienne), ce qui est le contraire 
        #d'une "dernière vaccination" (la plus récente).
        #Pour corriger le problème, il faut conserver la consultation si sa date est STRICTEMENT 
        # SUPÉRIEURE (>) à la date déjà enregistrée dans le dictionnaire, afin de garder la plus récente.
        id_animal = consult[0]
        date = consult[3]
        if id_animal not in derniere:
            derniere[id_animal] = consult
        elif date > derniere[id_animal][3]:
            derniere[id_animal] = consult
    
    return derniere


def test_derniere_vaccination():
    consultations_pour_test = [
        (16, "Plume", "0.6.36.96.89.83", "20241024"),
        (16, "Plume", "0.6.36.96.89.83", "20251125"),
        (17, "Gollum", "0.6.36.96.89.83", "20250113"),
        (26, "Olympe", "(0)4 73 98 01 23", "20250109"),
        (32, "Chopin", "06.37.97.66.64", "20241201"),
        (32, "Chopin", "06.37.97.66.64", "20251119"),
        (34, "Jazz", "0.6.37.51.65.52", "20250801"),
        (35, "Tango", "0324182", "20250706"),
        (38, "Loulou", "05-35-95-87-54", "20250209"),
        (39, "Tango", "07.45.48.02.42", "20250329"),
        (40, "Sésame", "07.45.48.02.42", "20250228"),
        (41, "Pixel", "0130709285", "20241204"),
        (41, "Pixel", "0130709285", "20251222"),
    ]

    resultat = derniere_vaccination(consultations_pour_test)
    # Affichage des résultats, décommenter si besoin
    # for a,r in resultat.items():
    #     print(a, ":", r)

    assert derniere_vaccination(consultations_pour_test) == {
        16: (16, "Plume", "0.6.36.96.89.83", "20251125"),
        17: (17, "Gollum", "0.6.36.96.89.83", "20250113"),
        26: (26, "Olympe", "(0)4 73 98 01 23", "20250109"),
        32: (32, "Chopin", "06.37.97.66.64", "20251119"),
        34: (34, "Jazz", "0.6.37.51.65.52", "20250801"),
        35: (35, "Tango", "0324182", "20250706"),
        38: (38, "Loulou", "05-35-95-87-54", "20250209"),
        39: (39, "Tango", "07.45.48.02.42", "20250329"),
        40: (40, "Sésame", "07.45.48.02.42", "20250228"),
        41: (41, "Pixel", "0130709285", "20251222"),
    }
    print('Les tests de la fonction derniere_vaccination sont passés')
test_derniere_vaccination()