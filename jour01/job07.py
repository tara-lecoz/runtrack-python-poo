class Personnage():
    def __init__(self):
        self.x = int(input("x = "))
        self.y = int(input("y = "))
        print(f"Le personnage est en position ({self.x}, {self.y}).")

    def gauche(self):
        self.x -= 1
    
    def droite(self):
        self.x += 1

    def haut(self):
        self.y += 1

    def bas(self):
        self.y -= 1

    def position(self):
        return (self.x, self.y)

personnage1 = Personnage()
personnage1.haut()
personnage1.droite()
print(personnage1.position())