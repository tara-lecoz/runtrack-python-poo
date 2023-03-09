class Personne:
    def __init__(self):
        self.age = 14
    
    def afficherAge(self):
        print(self.age)
    
    def bonjour(self):
        print("Hello")
    
    def modifierAge(self, age):
        self.age = age
        return self.age

class Eleve(Personne):
    def __init__(self):
        Personne.__init__(self)
    
    def allerEnCours(self):
        print("Je vais en cours")
    
    def affichageAge(self):
        print(f"J'ai {self.age} ans.")

class Professeur(Personne):
    def __init__(self, matiere_enseignee):
        self.__matiere_enseignee = matiere_enseignee

    def enseigner(self):
        print("Le cours va commencer.")

personne1 = Personne()
personne1.afficherAge()

tara = Eleve()
tara.modifierAge(21)
tara.affichageAge()

test = Professeur("Maths")
test.modifierAge(26)
test.afficherAge()
test.bonjour()
test.enseigner()