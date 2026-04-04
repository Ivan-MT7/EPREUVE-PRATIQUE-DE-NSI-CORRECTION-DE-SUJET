import random


class Coccinelle:
    def __init__(self, sexe, age, niv_nutrition):
        self.age = age
        self.esperance_de_vie = random.randint(200, 350)
        self.sexe = sexe
        self.niv_nutrition = niv_nutrition

    def chasser(self, nb_proies, nb_coccinelles):
        """
        Renvoie le nombre de proies restante en fonction de nombre de proies.
        Parametres :
        
        ----------
        nb_proies : int
        Nombre de proies qu'il faut chasser
        nb_coccinelles : int
        Nombre de coccinelles pour chasser
        ----------
        Sortie :
        nb_proies - consomme : int
        Le nb_proies qu'il reste.
        """
        if nb_coccinelles == 0:
            return nb_proies

        proies_par_cocci = nb_proies / nb_coccinelles #On divise le nombre de proies par le nombre de coccinelles(1000, 3)

        if proies_par_cocci > 20: 
            consomme = random.randint(12, 20) #On génére des nombres aléatoires
        elif proies_par_cocci > 10:
            consomme = random.randint(8, 15)
        else:
            consomme = random.randint(3, 8)

        consomme = min(consomme, nb_proies) #On prend le minimum entre consomme et nb_proies 

        if consomme >= 10:
            self.niv_nutrition += 1 #On ajoute un si le nombre de consommés est supérieur à 10 
        else:
            self.niv_nutrition = max(0, self.niv_nutrition - 1) #On prend le maximum si le nombre est inférieur à 10

        return nb_proies - consomme

    def reproduction(self):
        """
        Une femelle avec un niveau de nutrition >= 2 engendre exactement
        deux descendants : un mâle et une femelle.
        """
        descendants = []
        if self.sexe == "femelle" and self.niv_nutrition >= 2 and self.age >= 20:
            descendants.append(Coccinelle("male", 0, 0))
            descendants.append(Coccinelle("femelle", 0, 0))
            self.niv_nutrition = 0

        return descendants

    def a_survecu(self):
        """
        Met à jour l'âge de la coccinelle et indique si elle est encore en vie.
        """
        self.age = self.age + 1
        if self.niv_nutrition == 0 :
            if random.randint(0, 100) <= 67 :
                return self.age < self.esperance_de_vie 
            else :
                return False
        return self.age < self.esperance_de_vie 


    def __repr__(self):
        return f"Coccinelle {self.sexe}, âge: {self.age}/{self.esperance_de_vie}, niv_nutrition: {self.niv_nutrition}"


def evolution(population, nb_proies):
    """
    Simule une journée dans l'écosystème :
    - chasse des coccinelles
    - reproduction
    - vieillissement et mortalité
    - croissance des pucerons

    population est une liste d'instances de la classe Coccinelle
    nb_proies est un entier indiquant le nombre de proies

    Cette fonction renvoie un couple (population_suivante, nouveau_nb_proies) indiquant
    la nouvelle population à la fin de la journée et le nombre de proies.
    """
    population_suivante = []
    nouveau_nes = []
    nb_coccinelles = len(population)

    for coccinelle in population:
        nb_proies = coccinelle.chasser(nb_proies, nb_coccinelles)

        if coccinelle.a_survecu():
            population_suivante.append(coccinelle)

        nouveau_nes += coccinelle.reproduction()

    # Croissance naturelle des pucerons (augmentation de 20% par jour)
    nb_proies = int(nb_proies * 1.2)

    # Ajout des nouveau-nés en fin de journée
    population_suivante += nouveau_nes

    return population_suivante, nb_proies


#############################################################################
# Écrire ci-dessous le code pour les questions de l'énoncé                  #
#############################################################################

#Question 1

cocinelle_1 = Coccinelle("femelle", 10, 2) #Cocinelle de 10 jours, femelle, nutrition 2
cocinelle_2 = Coccinelle("femelle", 10, 2) #Cocinelle de 10 jours, femelle, nutrition 2
cocinelle_3 = Coccinelle("male", 10, 2) #Cocinelle de 10 jours, femelle, nutrition 2
population = [cocinelle_1, cocinelle_2, cocinelle_3]
nb_proies = 200
#Simulation sur 5 jours
for jour in range(5) :
    population, nb_proies = evolution(population, nb_proies)
    print("Jour", jour+1)
    print("Nombre de coccinelles : ", len(population))
    print("Nombre de pucerons : ", nb_proies)



#Question 2
def simulation_simple(population, nb_proies) :
    nb_jour_total = 0
    for jour in range(30) :
        if len(population) != 0 and nb_proies != 0 :
            population, nb_proies = evolution(population, nb_proies)
            print("Jour", jour+1)
            print("Nombre de coccinelles : ", len(population))
            print("Nombre de proies", nb_proies)
            nb_jour_total = nb_jour_total + 1
        else :
            break 
            
    var = (len(population), nb_proies, nb_jour_total)
    return var
simulation_simple(population, 1000) #La population et nombre de proies 1000
