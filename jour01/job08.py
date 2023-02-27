from math import *

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon
    
    def changerRayon(self):
        self.rayon = int(input("Entrez le nouveau rayon du cercle: "))
        print("Le nouveau rayon du cercle est: ", self.rayon)
        
    def circonférence(self):
        return 2 * pi * self.rayon
    
    def aire(self):
        return pi * self.rayon ** 2

    def diametre(self):
        return self.rayon * 2

    def afficherInfos(self):
        print("-----Cercle-----")
        print("Rayon: ", self.rayon)
        print("Circonférence: ", self.circonférence())
        print("Aire: ", self.aire())
        print("Diamètre: ", self.diametre())


cercle1 = Cercle(4)
cercle1.afficherInfos()
cercle2 = Cercle(7)
cercle2.afficherInfos()

