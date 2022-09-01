from packageF1.StatsEcurie import *

class Ecurie:
    
    # INITIALISATION

    def __init__(self, nom) -> None:

        liste = ["Mercedes", "RedBull", "Ferrari", "McLaren", "Alpine", "AlphaTauri", "AstonMartin", "Williams", "AlfaRomeo", "Haas"]
        if nom not in liste:
            print("Ecurie.Erreur : écurie invalide.")
        else:
            self.__nom = nom
            self.__donnees = StatsEcurie()
            self.__resultat = []

    # GETTERS & SETTERS

    def getNom(self) -> str:
        return self.__nom

    def getDonnees(self) -> StatsEcurie:
        return self.__donnees

    def getResultat(self) -> list:
        return self.__resultat

    def setNom(self, nom) -> None:
        self.__nom = nom

    def setResultat(self, resultat) -> None:
        self.__resultat = resultat
