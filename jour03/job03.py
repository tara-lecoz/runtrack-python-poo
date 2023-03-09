class Tache:
    def __init__(self, titre, description, statut):
        self.titre = titre
        self.description = description
        self.statut = statut

class ListeDeTaches:
    def __init__(self, taches):
        self.listetaches = taches

    def ajouterTache(self, tache):
        self.listetaches.append(tache)
    
    def supprimerTache(self, tache):
        self.listetaches.remove(tache)

    def marquerCommeFinie(self, tache):
        if tache.statut == "à réaliser":
            tache.statut = "terminée"
        else:
            print("Cette tâche est déjà terminée")

    def afficherListe(self):
        for tache in self.listetaches:
            print(f'Liste tâches : {tache.titre}, {tache.description}, {tache.statut}')

    def filtrerListe(self,statut):
        for tache in self.listetaches:
            if tache.statut == statut:
                print(f'{tache.titre}')

tache1 = Tache("Tâche 1", "Description tâche 1", "à réaliser")
tache2 = Tache("Tâche 2", "Description tâche 2", "à réaliser")
tache3 = Tache("Tâche 3", "Description tâche 3", "terminée")

listetaches = ListeDeTaches([tache2, tache3])

listetaches.ajouterTache(tache1)
listetaches.afficherListe()

listetaches.marquerCommeFinie(tache1)
listetaches.supprimerTache(tache1)

listetaches.afficherListe()
listetaches.filtrerListe("terminée")