class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def getlongeurlargeurinit(self):
        print(f'La longueur du rectangle est de {self.longueur}')
        print(f'La largeur du rectangle est de {self.largeur}')

    def __setmodiflongeur(self):
        longueur = int(input("Entrez la nouvelle longueur du rectangle: "))
        return longueur

    def __setmodiflargeur(self):
        largeur = int(input("Entrez la nouvelle largeur du rectangle: "))
        return largeur
    
    def getlongueurmodif(self):
        self.longueur = self.__setmodiflongeur()
        print(f'La longueur du rectangle est de {self.longueur}')
    
    def getlargeurmodif(self):
        self.largeur = self.__setmodiflargeur()
        print(f'La largeur du rectangle est de {self.largeur}')

rectangle1 = Rectangle(10,5)
rectangle1.getlongeurlargeurinit()
rectangle1.getlongueurmodif()
rectangle1.getlargeurmodif()