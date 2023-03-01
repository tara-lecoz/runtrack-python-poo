class Voiture:
    def __init__(self, marque, modele, annee, km):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.km = km
        self.en_marche = False
        self.__reservoir = 50

    def demarrer(self):
        if self.__verifier_plein() > 5:
            self.en_marche = True
            print("La voiture démarre")
        else:
            print("Le réservoir est vide")

    def arreter(self):
        self.en_marche = False

    def __verifier_plein(self):
        return self.__reservoir
    
voiture1 = Voiture("Audi", "RsQ8", 2020, 10000)
voiture1.demarrer()