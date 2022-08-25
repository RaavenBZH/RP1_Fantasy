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

    # GETTERS & SETTERS

    def getNom(self) -> str:
        return self.__nom

    def getDonnees(self) -> StatsEcurie:
        return self.__donnees