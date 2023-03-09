class Ville:
    def __init__(self, nom, nbhabitants):
        self.__nom = nom
        self.__nbhabitants = nbhabitants

    def afficherville(self):
        print(f"Populaition de la ville de {self.__nom} : {self.__nbhabitants} habitants")

class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def ajouterPopulation(self):
        self.__ville._Ville__nbhabitants += 1
        print('Mise a jour de la population de la ville de', self.__ville._Ville__nom, self.__ville._Ville__nbhabitants, 'habitants')

ville1 = Ville("Paris", 1000000)
ville1.afficherville()
ville2 = Ville("Marseille", 861635)
ville2.afficherville()

personne1 = Personne("John", 45, ville1)
personne1.ajouterPopulation()
personne2 = Personne("Myrtille", 4, ville1)
personne2.ajouterPopulation()
personne3 = Personne("Chloé", 18, ville2)
personne3.ajouterPopulation()