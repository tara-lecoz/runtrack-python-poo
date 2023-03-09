class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    def perimetre(self):
        return (self.__largeur + self.__longueur) * 2
    
    def surface(self):
        return self.__largeur * self.__longueur
    
    def setLongueur(self, longueur):
        self.__longueur = longueur
    
    def setLargeur(self, largeur):
        self.__largeur = largeur
    
    def getLongueur(self):
        return self.__longueur

    def getLargeur(self):
        return self.__largeur
    
class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        Rectangle.__init__(self, longueur, largeur)
        self.hauteur = hauteur
    
    def volume(self):
        return self.hauteur * self.surface()
    
rectangle1 = Rectangle(10, 25)
parallelepipede1 = Parallelepipede(10, 25, 15)

print(f"Premier rectangle : \n perimetre : {rectangle1.perimetre()} \n surface : {rectangle1.surface()}")

print(f"Premier parallelepipede : \n perimetre : {parallelepipede1.perimetre()} \n surface : {parallelepipede1.surface()} \n surface : {parallelepipede1.volume()}")