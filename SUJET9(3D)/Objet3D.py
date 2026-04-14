from Sommet import Sommet
from Face import Face
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


class Objet3D:

    """
    Représente un objet 3D composé de sommets, de faces et d'un nom.
    """

    def __init__(self):
        """
        Initialise un objet 3D vide.
        """
        self.sommets = []
        self.faces = []
        self.nom = ""

    def ajouter_sommet(self, x, y, z):
        """
        Ajoute un sommet à l'objet 3D.
        """
        self.sommets.append(Sommet(x, y, z))

    def ajouter_face(self, liste_sommets):
        """
        Ajoute une face à l'objet 3D.
        """
        self.faces.append(Face(liste_sommets))

    def __str__(self):
        """
        Renvoie une représentation textuelle de l'objet 3D.
        """
        return str({'nom': self.nom, 'sommets': len(self.sommets), 'faces': len(self.faces)})

    def afficher(self):
        #La fonction afficher était modifié par moi pour que ça soit plus correcte si on transforme
        """
        Affiche l'objet 3D à l'aide de matplotlib.
        """
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        f = []
        for face in self.faces:
            x = [(self.sommets[s-1].x, self.sommets[s-1].y, self.sommets[s-1].z)
                 for s in face.sommets]
            f.append(x)
        mesh = Poly3DCollection(f, alpha=0.4, edgecolor='black')
        ax.add_collection3d(mesh)

        xs = [sommet.x for sommet in self.sommets]
        ys = [sommet.y for sommet in self.sommets]
        zs = [sommet.z for sommet in self.sommets]

        ax.set_xlim(min(xs), max(xs))
        ax.set_ylim(min(ys), max(ys))
        ax.set_zlim(min(zs), max(zs))
    
        plt.show()

#############################################################################
# Méthode à modifier de la question 5                                       #
#############################################################################
    def transformer(self, rapport):
        """
        Applique une transformation d'échelle à l'objet 3D en modifiant directement ses sommets, ne modifie pas l'instance originelle.
        """
        nouvel_objet = Objet3D() #On remplace le tableau dynamique par le nouvel objet
        nouvel_objet.nom = self.nom #On prend le même nom pour le nouvelle 
        for sommet in self.sommets:
            nouvel_objet.ajouter_sommet(
                sommet.x*rapport,
                sommet.y*rapport,
                sommet.z*rapport)
        for face in self.faces :
            nouvel_objet.ajouter_face(face.sommets)
        return nouvel_objet


#############################################################################
# Écrire le code de la méthode trouver_sommets_adjacents de la question 2   #
#############################################################################
    def trouver_sommets_adjacents(self) :
        for i in range(len(self.sommets)) :
            for j in range(i+1, len(self.sommets)) :
                if self.sommets[i].est_adjacent(self.sommets[j]) :
                    return (self.sommets[i], self.sommets[j])
        return None
#La méthode self.sommets est une liste donc on compare un sommet i de la liste avec i+1ème sommet de la liste avec la méthode est_adjacent déjà écrit.
#On renvoie None s'il n'y a plus rien à comparer


#############################################################################
# Programme pour tester votre méthode de la question 2                                  #
#############################################################################
objet = Objet3D()
objet.ajouter_sommet(0, 0, 0)  # s1
objet.ajouter_sommet(1, 0, 0)  # s2
objet.ajouter_sommet(0, 1, 0)  # s3
def test_trouver_sommets_adjacents() :
    cord, cord2 = objet.trouver_sommets_adjacents() #Comme ça retourne une adresse mémoire, on regarde si les coordonées sont la même
    assert cord.x == 0
    assert cord.y == 0
    assert cord.z == 0
    assert cord2.x == 1
    assert cord2.y == 0
    assert cord2.z == 0
    print("Les test sont vérifiés")


