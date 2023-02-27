class Produit:
    def __init__(self, nom, prixHT):
        self.nom = nom
        self.prix = prixHT
        self.TVA = 0

    def CalculerPrixTTC(self):
        TVA = int(input("Entrez la TVA: "))
        return self.prix * (1 + TVA / 100)
    
    def afficherInfos(self):
        return f"Produit : {self.nom} \nPrix : {self.prix} \nPrix TVA : {self.TVA} \nPrix TTC : {self.CalculerPrixTTC()}"
    
    def changerprix(self):
        self.prix = int(input("Entrez le nouveau prix du produit: "))
        return f"Le nouveau prix HT est de : {self.prix}, le prix TTC est de : {self.CalculerPrixTTC()}"
    
    def changernom(self):
        self.nom = input("Entrez le nouveau nom du produit: ")
        return f"Le nouveau nom est de : {self.nom}"

produit1 = Produit("Nissan GTR", 111000)
print(produit1.afficherInfos())
print(produit1.changerprix())
print(produit1.changernom())

produit2 = Produit("BMW M3", 80000)
print(produit2.afficherInfos())
print(produit2.changerprix())
print(produit2.changernom())

produit3 = Produit("Audi RS6", 100000)
print(produit3.afficherInfos())
print(produit3.changerprix())
print(produit3.changernom())