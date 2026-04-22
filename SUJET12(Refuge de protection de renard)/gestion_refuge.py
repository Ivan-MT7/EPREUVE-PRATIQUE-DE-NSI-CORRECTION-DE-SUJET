import csv

class Renard:
    """
    Classe représentant un renard dans le refuge.
    Attributs : identifiant, nom, poids, date_arrivee.
    """
    def __init__(self, identifiant, nom, poids, date_arrivee):
        self.identifiant = identifiant
        self.nom = nom
        self.poids = poids
        self.date_arrivee = date_arrivee

    def __str__(self):
        return f"Renard ID {[self.identifiant]} - {[self.nom]} (Arrivé le {[self.date_arrivee]})"
renard1 = Renard(200, "Oscard", 5.1, "2026-01-01")
print(renard1)# Affiche : Renard ID 200 - Oscar (Arrivé le 2026-01-01)
class Refuge:
    """
    Classe représentant le refuge contenant la liste des renards.
    """
    def __init__(self, nom, adresse):
        self.nom = nom
        self.adresse = adresse
        self.liste_renards = []
        
    def recueillir(self, un_renard):
        """
        Méthode d'ajout d'un renard au refuge.
        """
        self.liste_renards.append(un_renard)

    def lister_peu_corpulents(self):
        """
        Méthode qui renvoie une liste des Renards dont le poids est < 6.0 kg.
        """
        return [renard for renard in self.liste_renards if renard.poids < 6.0]

    def pourcentage_peu_corpulents(self):
        """
        Méthode qui renvoie le pourcentage des renards peu corpulents.
        """
        if len(self.liste_renards) == 0:
            return 0.0
        return len(self.lister_peu_corpulents()) / len(self.liste_renards) * 100

    def importer_donnees(self, nom_fichier):
        """
        Fonction qui importe les données des renards à partir d'un fichier CSV.
        """
        print(f"Tentative d'importation depuis {nom_fichier}...")
        with open(nom_fichier, 'r', encoding='utf-8') as f:
            lignes = csv.DictReader(f, delimiter=';')
            for ligne in lignes:
                # CORRECTION : les valeurs lues depuis le CSV sont toutes des chaînes (str).
                # Il faut convertir 'id' en int et 'poids' en float,
                # sinon les comparaisons comme renard.poids < 6.0 ne fonctionneront pas correctement.
                print(ligne)
                renard = Renard(int(ligne['id']), ligne['nom'], float(ligne['poids']), ligne['date_arrivee'])
                self.recueillir(renard)
        print(f"Exemple de poids {self.liste_renards[0].poids} -> {type(self.liste_renards[0].poids)})") 
# Test de la correction (Question 3 — instanciation du refuge et import CSV)
refuge = Refuge("SOS Goupil", "12 rue des Bois, 01000 Bourg-en-Bresse")
refuge.importer_donnees("donnees_renards.csv")
# ===========================================================================
# QUESTION 4 — Utilisation des méthodes d'analyse de corpulence
# ===========================================================================

# Listage des renards peu corpulents (poids < 6.0 kg)
peu_corpulents = refuge.lister_peu_corpulents()
print(peu_corpulents)
# Pourcentage de renards peu corpulents dans le refuge
print(refuge.pourcentage_peu_corpulents())
# Justification du pourcentage :
# On isole le nombre de renards peu corpulents et le nombre total
nb_peu_corpulents = len(refuge.lister_peu_corpulents())
nb_total = len(refuge.liste_renards)
print(nb_peu_corpulents)  # nombre de renards peu corpulents
print(nb_total)           # nombre total de renards hébergés