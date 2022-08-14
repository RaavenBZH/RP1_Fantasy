from packageF1.Stats import *

class Pilote:
    '''
    Cette classe simule un pilote.

    Attributs :
        - __gamertag (str) : le gamertag du pilote.
        - __ecurie (str) : l'écurie du pilote.
        - __donnees (Stats) : les statistiques du pilote.
        - __historique (list) : l'historique des résultats du pilote.

    Méthodes :
        - getGamertag() -> str : récupère le gamertag.
        - getEcurie() -> str : récupère l'écurie.
        - getDonnees() -> Stats : récupère les statistiques.
        - getHistorique() -> list : récupère l'historique des résultats.        
        - setGamertag(gamertag : str) -> None : modifie le gamertag.
        - setEcurie(ecurie : str) -> None : modifie l'écurie.
        - setHistorique(historique : list) -> None : modifie l'historique des résultats.
        - __str__() -> str : renvoie le gamertag et l'écurie.
        - ajoutHistorique(desc : tuple) -> None : ajoute un résultat à l'historique.
        - retireHistorique(desc : tuple) -> None : retire un résultat de l'historique.
    ''' 

    # INITIALISATION

    def __init__(self, gamertag : str, ecurie : str) -> None:

        self.__gamertag = None
        self.__ecurie = None
        self.__donnees = Stats()
        self.__historique = []
        
        listeEcuries = ["Mercedes", "RedBull", "Ferrari", "McLaren", "Alpine", "AlphaTauri", "AstonMartin", "Williams", "AlfaRomeo", "Haas", None]
        if ecurie in listeEcuries:
            self.__gamertag = gamertag
            self.__ecurie = ecurie
        else:
            print("Pilote.Erreur : écurie invalide.")

    # GETTERS & SETTERS

    def getGamertag(self) -> str:
        return self.__gamertag

    def getEcurie(self) -> str: 
        return self.__ecurie

    def getDonnees(self) -> Stats:
        return self.__donnees

    def getHistorique(self) -> list:
        return self.__historique

    def setGamertag(self, gamertag : str) -> None:
        self.__gamertag = gamertag

    def setEcurie(self, ecurie : str) -> None:
        listeEcuries = ["Mercedes", "RedBull", "Ferrari", "McLaren", "Alpine", "AlphaTauri", "AstonMartin", "Williams", "AlfaRomeo", "Haas", None]
        if ecurie in listeEcuries:
            self.__ecurie = ecurie
        else:
            print("Pilote.setEcurie.Erreur : paramètre invalide.")

    def setHistorique(self, historique : list) -> None:
        self.__historique = historique

    # METHODES

    def __str__(self) -> str:
        return self.__gamertag + " (" + self.__ecurie + ")"

    def ajoutHistorique(self, desc : tuple) -> None:
        self.__historique.append(desc)

    def retireHistorique(self, desc : tuple) -> None:
        for i in self.__historique:
            if i == desc:
                self.__historique.remove(i)
                break