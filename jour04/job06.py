class Vehicule:
    def __init__(self, marque, annee, prix, modele):
        self.marque = marque
        self.annee = annee
        self.prix = prix
        self.modele = modele

    def informationsVehicule(self):
        print(f"\nInformations véhicule: \nMarque: {self.marque}\nModèle: {self.modele}\nAnnée: {self.annee}\nPrix: {self.prix} euros")
        
    def demarrer(self):
        print("Attention, je roule.")


class Voiture(Vehicule):
    def __init__(self, marque, annee, prix, modele):
        Vehicule.__init__(self, marque, annee, prix, modele)
        self.nb_portes = 4

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes: {self.nb_portes}")

    def demarrer(self):
        print("Attention je roule en Voiture")

class Moto(Vehicule):
    def __init__(self, marque, annee, prix, modele):
        Vehicule.__init__(self, marque, annee, prix, modele)
        self.nb_roues = 2

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues: {self.nb_roues}")

    def demarrer(self):
        print("Attention je roule en Moto")

voiture1 = Voiture("Peugeot", 2015, 15000, "308")
moto1 = Moto("Yamaha", 2018, 10000, "MT-07")

voiture1.informationsVehicule()
voiture1.demarrer()

moto1.informationsVehicule()
moto1.demarrer()