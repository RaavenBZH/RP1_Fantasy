from packageF1.Joueur import *

class EnsembleJoueur():
    '''
    Cette classe regroupe tous les participants au jeu.

    Attributs :
        - __listeJoueurs (list<Joueur>) : liste des participants.

    Méthodes :
        - __init__(str) -> None : construit les objets <EnsembleJoueur>.
        - __str__() -> str : affiche le score de chaque joueurs.
        - getListeJoueurs() -> list<Joueur> : récupère la liste des joueurs.
        - addJoueur(j : Joueur) -> None : ajoute un joueur dans la liste.
        - update(generalPoints : dict<str : int>) -> None : actualise les points de chaque joueur.
    '''

    def __init__(self) -> None:
        self.__listeJoueurs = []

    def __str__(self) -> str:
        affichage = "Classement : \n"
        for i in self.__listeJoueurs:
            affichage += i.getDiscord() + " : " + str(i.calcScore()) + "\n"
        return affichage[:-1]

    def getListeJoueurs(self):
        return self.__listeJoueurs

    def addJoueur(self, j : Joueur) -> None:
        self.__listeJoueurs.append(j)

    def update(self, generalPoints : dict) -> None:
        for i in self.__listeJoueurs:
            i.updatePoints(generalPoints)