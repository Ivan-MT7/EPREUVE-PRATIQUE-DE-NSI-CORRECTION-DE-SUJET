class Boutique_smoothie:
    def __init__(self, liste_fruits_disponibles):
        self.liste_fruits_disponibles = liste_fruits_disponibles
        self.db_smoothies = {
            "Tropical": ["Mangue", "Ananas", "Banane"],
            "Rouge": ["Fraise", "Framboise", "Cerise"],
            "Vert": ["Kiwi", "Pomme verte", "Menthe"],
            "Agrume": ["Orange", "Citron", "Pamplemousse"],
            "Exotique": ["Papaye", "Fruit de la passion", "Noix de coco"],
            "Tropical citron": ["Mangue", "Ananas", "Citron"],
            "Rouge kiwi": ["Fraise", "Framboise", "Kiwi"],
            "Exotique rouge": ["Papaye", "Fraise", "Fruit de la passion"],
            "Vert citron": ["Kiwi", "Pomme verte", "Citron"],
            "Soleil couchant": ["Mangue", "Fraise", "Pamplemousse"]
        }

    ##### QUESTION 1 #####
    def smoothie_possible(self, nom_smoothie):
        """Retourne True si le smoothie peut être préparé avec les fruits disponibles, False sinon."""
        return all(fruit in self.liste_fruits_disponibles for fruit in self.db_smoothies[nom_smoothie])
#for fruit in self.db_smoothies[nom_smoothie] :
#             if fruit not in self.liste_fruits_disponibles :
#                 return False
#         return True
    #all s'arrête quand il n'y a une False.

    ##### QUESTION 2 #####
    def liste_smoothies_possibles(self):
        """Retourne la liste des smoothies pouvant être préparés avec les fruits disponibles."""
        return [nom for nom in self.db_smoothies
                if self.smoothie_possible(nom)
                ]
#         lst = []
#         for nom in self.db_smoothies :
#             if self.smoothie_possible(nom) :
#                 lst.append(nom)
#         return lst
    #On accède au nom de  toutes les smoothies puis on teste si c'est possible. Une boucle de compréhension est utilisé. 
    ##### QUESTION 3 #####
    def score_proximité(self, nom1, nom2):
        """Retourne le nombre de fruits communs entre deux smoothies."""
        nb = 0
        fruits1 = self.db_smoothies[nom1]
        fruits2 = self.db_smoothies[nom2]
        for fruit in fruits1:
            if fruit in fruits2:
                nb += 1
        return nb

    def plus_proche_possible(self, nom_smoothie_ref):
        """Retourne le nom du smoothie le plus proche de nom_smoothie_ref en termes de fruits communs parmi les smoothies possibles.
        En cas d'égalité, retourne le premier trouvé.
        """
        max_communs = 0
        smoothie_proche = None
        nb_communs = 0
        for nom_smoothie in self.db_smoothies:
            if nom_smoothie != nom_smoothie_ref : #On ajoute cette condition pour que la sortie ne soit pas la même que l'entrée 
                nb_communs = self.score_proximité(nom_smoothie_ref, nom_smoothie)
            if nb_communs > max_communs:
                max_communs = nb_communs
                smoothie_proche = nom_smoothie

        return smoothie_proche

    def affichage_possibles(self):
        """Affiche les smoothies possibles."""
        smoothies = self.liste_smoothies_possibles()
        print("Smoothies possibles avec les fruits disponibles :")
        for smoothie in smoothies:
            print(smoothie)
        print("Alternative aux autres smoothies :")
        for nom_smoothie in self.db_smoothies :
            if nom_smoothie != smoothies:
                proche = self.plus_proche_possible(nom_smoothie)
            if proche != None:
                print(f"Pour le smoothie {nom_smoothie}, essayez {proche}.")
            else:
                print(f"Pour le smoothie {nom_smoothie}, aucun smoothie proche disponible.")
#         for smoothie in self.db_smoothies :
#             if smoothie not in smoothies
#Remplacer cela dans les lignes 73 à 74 pour avoir un affichage de possibles sur tout

# ========= Fonctions de test ==================


def test_smoothie_possible():
    boutique = Boutique_smoothie(
        ["Mangue", "Ananas", "Banane", "Fraise", "Citron"])
    assert boutique.smoothie_possible("Tropical") == True
    assert boutique.smoothie_possible("Rouge") == False


def test_liste_smoothies_possibles():
    boutique1 = Boutique_smoothie(
        ["Mangue", "Ananas", "Banane", "Fraise", "Citron"])
    boutique2 = Boutique_smoothie(
        ["Fraise", "Framboise", "Cerise", "Kiwi", "Orange", "Citron", "Pamplemousse"])
    boutique3 = Boutique_smoothie(["Orange", "Mangue", "Papaye"])
    assert boutique1.liste_smoothies_possibles() == [
        "Tropical", "Tropical citron"]
    assert boutique2.liste_smoothies_possibles() == [
        "Rouge", "Agrume", "Rouge kiwi"] #Rouge Kiwi au lieu de Berry Mix
    assert boutique3.liste_smoothies_possibles() == []


def test_score_proximité():
    # À compléter
    boutique1 = Boutique_smoothie(
        ["Mangue", "Ananas", "Banane", "Fraise", "Citron"])
    assert boutique1.score_proximité("Tropical", "Tropical citron") == 2
    assert boutique1.score_proximité("Rouge", "Exotique") == 0


def test_plus_proche_possible():
    boutique = Boutique_smoothie(
        ["Mangue", "Ananas", "Banane", "Fraise", "Citron", "Kiwi", "Pomme verte"])
    smoothie_proche = boutique.plus_proche_possible("Tropical")
    assert smoothie_proche == "Tropical citron"

    smoothie_proche2 = boutique.plus_proche_possible("Exotique")
    assert smoothie_proche2 == "Exotique rouge"


# ======== Lancement des tests ========

test_smoothie_possible()
test_liste_smoothies_possibles()
test_plus_proche_possible()

boutique = Boutique_smoothie(
    ["Mangue", "Ananas", "Banane", "Fraise", "Citron", "Kiwi", "Pomme verte"])
boutique.affichage_possibles()