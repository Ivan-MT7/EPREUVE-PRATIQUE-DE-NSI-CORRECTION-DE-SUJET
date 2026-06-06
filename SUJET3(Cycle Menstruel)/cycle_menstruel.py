import calendar

#############################################################################
# Écrire le code de la fonction est_bissextile de la question 1             #
#############################################################################
def est_bissextile(annee) :
    if annee % 4 == 0 and annee % 100 != 0:
        return True
    elif annee % 4 == 0 and annee % 100 == 0 and annee % 400 == 0 :
        return True
    else :
        return False 
#############################################################################
# Écrire le code de la fonction determiner_phase de la question 2           #
#############################################################################
def determiner_phase(jour) :
    assert jour > 0 and jour <= 28
    if 1 <= jour <= 5 :
        return 1
    if 6 <= jour <= 13 :
        return 2
    if jour == 14 :
        return 3
    else :
        return 4
#############################################################################
# Fonctions fournies pour la question 3                                     #
#############################################################################
def jours_dans_mois(annee, mois):
    """Renvoie le nombre de jours dans un mois donné d'une année donnée.
       Utilise le module calendar pour gérer les années bissextiles."""
    if mois == 2:  # février
        return 29 if calendar.isleap(annee) else 28
    elif mois in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    else:
        return 30


def ajouter_jours(date, nb_jours):
    """Ajoute nb_jours à une date donnée et renvoie la nouvelle date.
       La date est représentée par un tuple (jour, mois, année)."""
    jour, mois, annee = date
    jour = jour + nb_jours

    # Ajustement du jour et du mois si dépassement
    while jour > jours_dans_mois(annee, mois):
        jour = jour - jours_dans_mois(annee, mois)
        mois = mois + 1
        if mois > 12:  # passage à l'année suivante
            mois = 1
            annee = annee + 1

    return (jour, mois, annee)


def test_ajouter_jours():
    assert ajouter_jours((7, 9, 2025), 3) == (10, 9, 2025)
    #On doit passer à la mois suivante lorsque le jour_donnee + jour_actuelle dépasse 31
    assert ajouter_jours((31, 3, 2025), 3) == (3, 4, 2025)
    #On vérifie que l'année peut être passée
    assert ajouter_jours((31, 3, 2025), 366) == (1, 4, 2026)
    #On vérifie que la date est 28 février si on avance une journée pour les années bissextiles
    assert ajouter_jours((28, 2, 2024), 1) == (29, 2, 2024)
    #On vérifie que la date est 1 mars pour les années non bissextiles
    assert ajouter_jours((28, 2, 2023), 1) == (1, 3, 2023)
    print("Test réussi")
#############################################################################
# Fonction fournie pour la question 4                                       #
#############################################################################


def calendrier_cycles(date_regles):
    """Renvoie une chaîne de caractère contenant au format iCalendar, l'ensemble
    des dates de début de règles qui se présentent dans les 100 jours suivants 
    `date_regles`, date incluse.

    Hypothèse : cycle régulier de 28 jours. """
    # Problème identifié : dans la ligne qui construit la date DTSTART,
    # les nombres inférieurs à 10 ne sont pas complétés avec un 0.
    # Exemple : le 3 juillet 2026 donnait "202673" au lieu de "20260703".
    # Il faut utiliser zfill(2) pour s'assurer que jour et mois font 2 chiffres.
    cal_lignes = ['BEGIN:VCALENDAR', 'VERSION:2.0', 'PRODID:']

    date_courante = date_regles
    jours_ecoules = 0

    # On ajoute les dates tant que l'on ne dépasse pas 100 jours écoulés
    while jours_ecoules + 28 <= 100 and date_courante[1] <= 12:
        jour, mois, annee = date_courante
        
        cal_lignes.append('BEGIN:VEVENT')
        cal_lignes.append('SUMMARY: Règles')
        #Correction on sépare le mois et le jour pour ajouter un zero derrière eux
        if len(str(mois)) == 1 :
            mois = "0" + str(mois)
        if len(str(jour)) == 1 :
            jour = "0" + str(jour)
        date = str(annee)+ str(mois) + str(jour)

        cal_lignes.append('DTSTART:'+date)
        cal_lignes.append('END:VEVENT')
        date_courante = ajouter_jours(date_courante, 28)
        jours_ecoules += 28
    
    cal_lignes.append('END:VCALENDAR')

    # La méthode join va renvoyer ici une unique chaîne contenant toutes les
    # chaînes de la liste séparées par des sauts de lignes.
    return '\n'.join(cal_lignes)


def test_calendrier_cycles():
    '''Crée un calendrier et le charge avec le module ics pour vérifier sa
    validité.

    Nécessite que le module ics soit présent sur la machine (pip install ics).
    '''
    from ics import Calendar
    c = calendrier_cycles((12, 3, 2026))
    print(c)
    cal = Calendar(c)
    print(cal.events)
    print("Test réussi")