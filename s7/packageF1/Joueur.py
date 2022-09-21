
class Joueur():
    '''
    Cette classe simule les choix d'un joueur et calcule ses points.

    Attributs :
        - __equipe (dict<str : int>) : l'équipe du joueur et points associés.
        - __discord (str) : le discord du joueur.

    Méthodes :
        - __init__(discord : str) -> None : construit les objets <Joueur>.
        - getEquipe() -> str : récupère l'équipe du joueur.
        - getDiscord() -> str : récupère le discord du joueur.
        - addEquipe(listePilotes : list<str>) -> None : ajoute l'équipe de pilotes représentés par leur gamertag.
        - updatePoints(generalPoints : dict<str : int>) -> None : actualise les points de l'équipe du joueur.
        - calcScore() -> int : calcule et renvoie le score du joueur.
    '''

    def __init__(self, discord : str) -> None:
        self.__equipe = {}
        self.__discord = discord
                         
    def getEquipe(self) -> str:
        return self.__equipe

    def getDiscord(self) -> str:
        return self.__discord

    def addEquipe(self, listePilotes : list) -> None:
        for i in listePilotes:
            self.__equipe[i] = 0

    def updatePoints(self, generalPoints : dict) -> None:
        for i in self.__equipe:
            self.__equipe[i] = generalPoints[i]

    def calcScore(self) -> int:
        return sum([i for i in self.__equipe.values()])