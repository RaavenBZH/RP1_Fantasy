from packageF1.StatsPilote import *
from packageF1.Ecurie import *

class Pilote:
    '''
    Cette classe simule un pilote.

    Attributs :
        - __gamertag (str) : le gamertag du pilote.
        - __ecurie (Ecurie) : l'écurie du pilote.
        - __donnees (StatsPilote) : les statistiques du pilote.
        - __historique (list) : l'historique des résultats du pilote.

    Méthodes :
        - getGamertag() -> str : récupère le gamertag.
        - getEcurie() -> Ecurie : récupère l'écurie.
        - getDonnees() -> StatsPilote : récupère les statistiques.
        - getHistorique() -> list : récupère l'historique des résultats.    
        - getGamertagRempalcant() -> str : récupère le gamertag du remplacant.    
        - setGamertag(gamertag : str) -> None : modifie le gamertag.
        - setEcurie(ecurie : Ecurie) -> None : modifie l'écurie.
        - setHistorique(historique : list) -> None : modifie l'historique des résultats.
        - setGamertagRemplacant(gamertag : str) -> None : modifie le gamertag du remplacant.
        - __str__() -> str : renvoie le gamertag, l'écurie et les statistiques du pilote.
        - ajoutHistorique(desc : tuple) -> None : ajoute un résultat à l'historique.
        - retireHistorique(desc : tuple) -> None : retire un résultat de l'historique.
        - resetHistorique() -> None : réinitialise l'historique.
    ''' 

    # INITIALISATION

    def __init__(self, gamertag : str, ecurie : Ecurie) -> None:

        self.__gamertag = gamertag
        self.__ecurie = ecurie
        self.__donnees = StatsPilote(gamertag)
        self.__historique = []
        self.__gamertagRemplacant = gamertag

    # GETTERS & SETTERS

    def getGamertag(self) -> str:
        return self.__gamertag

    def getEcurie(self) -> Ecurie: 
        return self.__ecurie

    def getDonnees(self) -> StatsPilote:
        return self.__donnees

    def getHistorique(self) -> list:
        return self.__historique

    def getGamertagRemplacant(self) -> str:
        return self.__gamertagRemplacant

    def setGamertag(self, gamertag : str) -> None:
        self.__gamertag = gamertag

    def setDonnees(self, donnees : StatsPilote) -> StatsPilote:
        self.__donnees =donnees

    def setEcurie(self, ecurie : Ecurie) -> None:
        self.__ecurie = ecurie

    def setHistorique(self, historique : list) -> None:
        self.__historique = historique

    def setGamertagRemplacant(self, gamertag : str) -> None:
        self.__gamertagRemplacant = gamertag

    # METHODES

    def __str__(self) -> str:
        return self.__gamertag

    def ajoutHistorique(self, desc : tuple) -> None:
        self.__historique.append(desc)

    def retireHistorique(self, desc : tuple) -> None:
        for i in self.__historique:
            if i == desc:
                self.__historique.remove(i)
                break

    def resetHistorique(self) -> None:
        self.__historique = []