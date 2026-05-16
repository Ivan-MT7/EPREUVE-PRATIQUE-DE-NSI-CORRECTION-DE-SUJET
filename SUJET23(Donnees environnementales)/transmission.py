class Transmission:

    def __init__(self, trame):
        self._id = None
        self._temperature = None
        self._humidite = None
        self._trame = trame

        self.decoder()

    def __repr__(self):
        """ Méthode permettant l'affichage """
        return f"ID : {self._id} / Temp. : {self._temperature}°C / Hum. : {self._humidite}%"

    def decoder(self):
        # Question 4 : Rendre la classe Transmission plus robuste pour l'analyse.
        # On ajoute une vérification de la longueur de la trame. En effet, certaines
        # lignes dans 'data.txt' ne font pas 40 caractères, ce qui générait une erreur bloquante
        if len(self._trame) == 40 :
            self.decoder_id()
            self.decoder_temperature()
            self.decoder_humidite()

    def decoder_id(self):
        # int(s, 2) : conversion binaire -> décimal
        self._id = int(self._trame[0:8], 2)

    def decoder_temperature(self):
        # Question 1 : on récupère les 12 bits de la température
        self._temperature = int(self._trame[16:28], 2)
        # On applique la formule de conversion en °C
        self._temperature = (self._temperature - 900) / 10 
        
    
    def decoder_humidite(self):
        resultat = ""
        # Question 1 : on récupère les 8 bits de l'humidité
        self._humidite = self._trame[28:36]
        # Gestion de l'exception explicite du sujet pour les 100%
        if self._humidite == "10100000":
            self._humidite = 100
        else :
            #Sinon, c'est du Décimal Codé Binaire (BCD)
            # On sépare en 2 blocs de 4 bits pour obtenir la dizaine et l'unite en binaire
            première_nombre = int(self._trame[28:32], 2) #"0110" --> 6
            deuxième_nombre = int(self._trame[32:36], 2) # "0010" --> 2
            resultat = resultat + str(première_nombre) + str(deuxième_nombre) # On convertit ces 2 blocs binaires en décimal (pour avoir la dizaine et l'unite en décimal)

            self._humidite = int(resultat)
     
            

    def get_id(self):
        return self._id

    def get_temperature(self):
        return self._temperature

    def get_humidite(self):
        return self._humidite

    def est_valide(self):
        # Question 4 : On sécurise la méthode face aux éventuelles trames de tailles invalides
        if len(self._trame) != 40:
            return False

        #On recoupere chaque section
        id_v = self._trame[0:8]
        cle_securite = self._trame[8:16]
        temperature = self._trame[16:28]
        humidite = self._trame[28:36]
        controle = self._trame[36:40]
        #On crée une liste pour vérifier des choses plus facilement 
        liste = [id_v, cle_securite, temperature, humidite]
        compteur = 0 # Pour compter le nombre de "1"
        for i in range(len(liste)) : # on parcourt chaque section
            for j in range(len(liste[i])) : # on parcourt chaque caractère de chaque section
                if liste[i][j] == '1': # Si c'est bien un "1", on augmente le compteur.
                    compteur += 1
            # Le bit de parité attendu est 0 si le décompte de '1' est pair sinon 1
            # Cela correspond exactement au résultat du modulo 2
            if compteur % 2 != int(controle[i]):
                return False
            compteur = 0
        # Si tous les blocs ont une parité valide
        return True
# --- Tests de vérification demandés à la Question 1 ---
print("--- Tests sur la trame d'exemple ---")
trame_exemple = "0010101011001000010010001100011000101101"
transmission_test = Transmission(trame_exemple)

print("Température obtenue :", transmission_test.get_temperature(), "°C (attendu : 26.4)")
print("Humidité obtenue :", transmission_test.get_humidite(), "% (attendu : 62)")
# QUESTION 3 : data.txt contient des trames de longueurs différentes