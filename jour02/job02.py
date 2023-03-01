class Livre:
    def __init__(self, titre, auteur, nbPages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nbPages = nbPages

    def getTitre(self, titre):
        self.__titre = titre

    def getAuteur(self, auteur):
        self.__auteur = auteur
    
    def getNbpages(self, nbpages):
        if self.nbPages > 0:
            self.__nbPages = nbpages
        else:
            return "Le nombre de pages doit être positif."
    
    def setTitre(self, titre):
        self.getTitre(titre)
        print(f'Le titre du livre est {self.titre}')

    def setAuteur(self, auteur):
        self.getAuteur(auteur)
        print(f"L'auteur du livre est {self.auteur}")

    def setNbpages(self, nbpages):
        self.getNbpages(nbpages)
        print(f'Le nombre de pages du livre est {self.nbPages}')

livre1 = Livre()
livre1.gettitremodif()
livre1.getauteurmodif()
livre1.getnbPagesmodif()
