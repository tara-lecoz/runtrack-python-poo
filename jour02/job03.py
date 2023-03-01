class Livre:
    def __init__(self, titre, auteur, nbpages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nbpages = nbpages
        self.__disponible = True

    def getTitre(self):
        print(f"Le titre du livre est : {self.__titre}")
        return self.__titre
    
    def getAuteur(self):
        print(f"L'auteur du livre est : {self.__auteur}")
        return self.__auteur
    
    def getNbpages(self):
        print(f"Le nombre de pages du livre est : {self.__nbpages}")
        return self.__nbpages
    
    def setTitre(self, titre):
        self.__titre = titre

    def setAuteur(self, auteur):
        self.__auteur = auteur

    def setNbpages(self, nbpages):
        self.__nbpages = nbpages
        if self.__nbpages < 0:
            return "Le nombre de pages doit être supérieur à 0"
        
    def verification(self):
        if self.__disponible == True:
            print(f"le livre est disponible")
        else:
            print (f"le livre n'est pas disponible")

    def emprunter(self):
        if self.__disponible == True:
            self.__disponible = False
            print(f"le livre est emprunté")
        else:
            print (f"le livre n'est pas disponible")

    def rendre(self):
        if self.__disponible == False:
            self.__disponible = True
            print(f"le livre est rendu")
        else:
            print (f"le livre est disponible")

livre1 = Livre("The jungle book", "Rudyard Kipling", 102)
livre1.getTitre()
livre1.getAuteur()
livre1.getNbpages()
livre1.verification()
livre1.emprunter()
livre1.rendre()