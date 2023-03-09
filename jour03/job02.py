class CompteBancaire:
    def __init__(self, nmcompte, nom, prenom, solde):
        self.__nmcompte = nmcompte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.decouvert = True

    def afficher(self):
        print(f'N° de compte : {self.__nmcompte} | Nom : {self.__nom} | Prénom : {self.__prenom} | Solde : {self.__solde} euros')

    def afficherSolde(self):
        print(f'Le solde du compte n°{self.__nmcompte} est de {self.__solde}')

    def versement(self, versement):
        self.__solde += versement
        print(f'Le nouveau solde du compte n°{self.__nmcompte} est de {self.__solde}')

    def retrait(self, retrait):
        self.__solde -= retrait
        print(f'Le nouveau solde du compte n°{self.__nmcompte} est de {self.__solde}')

    def agios(self):
        if self.__solde < 0:
            self.__solde *= 1.5

    def virement(self, comptevers, montant):
        if self.__solde >= montant:
            comptevers.__solde += montant
            self.__solde -= montant
            print(f'Le virement du compte n°{self.__nmcompte} vers le compte n°{comptevers.__nmcompte} a été effectué avec succès !')
            print(f'Le nouveau solde du compte n°{self.__nmcompte} est de {self.__solde}')
            print(f'Le nouveau solde du compte n°{comptevers.__nmcompte} est de {comptevers.__solde}')
        else:
            print('Le solde du compte n°{self.__nmcompte} est insuffisant pour effectuer le virement')


test = CompteBancaire(123456, 'Doe', 'John', 1000)
test.afficher()
test.afficherSolde()
test.versement(100)
test.retrait(50)

test1 = CompteBancaire(654321, 'Doe', 'Jane', 500)
test1.afficher()
test1.afficherSolde()
test1.versement(100)
test1.retrait(50)

test.virement(test1, 100)