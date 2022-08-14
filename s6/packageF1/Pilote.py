
class Pilote:
    '''
    Cette classe simule un pilote.

    Attributs :
        - __gamertag (str) : le gamertag du pilote.
        - __ecurie (str) : l'écurie du pilote.
        - __historique (list) : l'historique des actions d'un pilote

    Méthodes :
        - __init__(gamertag : str, ecurie : str) -> None : construit les objets <Pilote>.
        - getGamertag() -> str : récupère le gamertag.
        - getEcurie() -> str : récupère l'écurie.
        - setEcurie(ecurie : str) -> None : modifie l'écurie.
        - addAction(desc : str) -> None : ajoute la description des bonus à l'historique.
        - resetHistorique() -> None : efface l'historique.
        - getHistorique() -> list : permet de récupérer l'historique.
    ''' 

    def __init__(self, gamertag : str, ecurie : str) -> None:

        self.__gamertag = None
        self.__ecurie = None
        self.__historique = []
        
        listeEcuries = ["Mercedes", "RedBull", "Ferrari", "McLaren", "Alpine", "AlphaTauri", "AstonMartin", "Williams", "AlfaRomeo", "Haas", None]
        if ecurie in listeEcuries:
            self.__gamertag = gamertag
            self.__ecurie = ecurie
        else:
            print("Pilote.Erreur : écurie invalide.")

    def getGamertag(self) -> str:
        return self.__gamertag

    def getEcurie(self) -> str: 
        return self.__ecurie

    def setEcurie(self, ecurie : str) -> None:
        listeEcuries = ["Mercedes", "RedBull", "Ferrari", "McLaren", "Alpine", "AlphaTauri", "AstonMartin", "Williams", "AlfaRomeo", "Haas", None]
        if ecurie in listeEcuries:
            self.__ecurie = ecurie
        else:
            print("Pilote.setEcurie.Erreur : paramètre invalide.")

    def addAction(self, desc : tuple) -> None:
        self.__historique.append(desc)

    def removeAction(self, desc : tuple) -> None:
        for i in self.__historique:
            if i == desc:
                self.__historique.remove(i)
                break

    def resetHistorique(self) -> None:
        self.__historique = []

    def getHistorique(self) -> list:
        return self.__historique