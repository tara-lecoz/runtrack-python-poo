class Joueur:
    def __init__(self, nom, numero, position, nbbuts, pd, cj, cr):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.nbbuts = nbbuts
        self.pd = pd
        self.cj = cj
        self.cr = cr

    def marquerUnBut(self):
        self.nbbuts += 1
    
    def effectuerUnePasseDecisive(self):
        self.pd += 1

    def recevoirUneCartonJaune(self):
        self.cj += 1

    def recevoirUneCartonRouge(self):
        self.cr += 1

    def afficherStatistiques(self):
        print(f'Nom : {self.nom}, Numéro : {self.numero}, Position : {self.position}, Nombre de buts : {self.nbbuts}, Passe décisive : {self.pd}, Carton jaune : {self.cj}, Carton rouge : {self.cr}')

class Equipe:
    def __init__(self, nom, joueurs):
        self.nom = nom
        self.joueurs = joueurs

    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)

    def AfficherStatistiquesJoueurs(self):
        for joueur in self.joueurs:
            joueur.afficherStatistiques()

joueur1 = Joueur("Mbappé", 7, "attaquant", 0, 0, 0, 0)
joueur2 = Joueur("Pogba", 6, "milieu", 0, 0, 0, 0)
joueur3 = Joueur("Varane", 4, "défenseur", 0, 0, 0, 0)
joueur4 = Joueur("Lloris", 1, "gardien", 0, 0, 0, 0)

joueur5 = Joueur("Griezmann", 7, "attaquant", 0, 0, 0, 0)
joueur6 = Joueur("Kante", 6, "milieu", 0, 0, 0, 0)
joueur7 = Joueur("Laporte", 14, "défenseur", 0, 0, 0, 0)
joueur8 = Joueur("Lloris", 1, "gardien", 0, 0, 0, 0)

equipe1 = Equipe("France", [joueur1, joueur3, joueur4])
equipe2 = Equipe("Francebis", [joueur5, joueur7, joueur8])

equipe1.AfficherStatistiquesJoueurs()
equipe2.AfficherStatistiquesJoueurs()

equipe1.ajouterJoueur(joueur2)
equipe2.ajouterJoueur(joueur6)

joueur2.effectuerUnePasseDecisive()
joueur1.marquerUnBut()

joueur5.recevoirUneCartonJaune()
joueur7.recevoirUneCartonRouge()

equipe2.AfficherStatistiquesJoueurs()