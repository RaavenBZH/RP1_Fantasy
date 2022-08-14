
class Stats:
    """
    Cette classe mémorise les statistiques d'un pilote.

    Attributs :
        - __courses (int) : nombre de courses disputées.
        - __qualifs (int) : nombre de qualifications disputées.
        - __victoires (int) : nombre de victoires.
        - __podiums (int) : nombre de podiums.
        - __poles (int) : nombre de poles.
        - __points (int) : nombre de points.

    Méthodes :
        - getCourses() : retourne le nombre de courses disputées.
        - getQualifs() : retourne le nombre de qualifications disputées.
        - getVictoires() : retourne le nombre de victoires.
        - getPodiums() : retourne le nombre de podiums.
        - getPoles() : retourne le nombre de poles.
        - getPoints() : retourne le nombre de points.
        - setCourses(courses : int) : modifie le nombre de courses disputées.
        - setQualifs(qualifs : int) : modifie le nombre de qualifications disputées.
        - setVictoires(victoires : int) : modifie le nombre de victoires.
        - setPodiums(podiums : int) : modifie le nombre de podiums.
        - setPoles(poles : int) : modifie le nombre de poles.
        - setPoints(points : int) : modifie le nombre de points.
        - __check(value : int) : vérifie si value est un entier positif.
    """

    # INITIALISATION

    def __init__(self, courses : int = 0, qualifs : int = 0, victoires : int = 0, podiums : int = 0, poles : int = 0, points : int = 0) -> None:

        self.__courses = None
        self.__qualifs = None
        self.__victoires = None
        self.__podiums = None
        self.__poles = None
        self.__points = None  

        if self.__check(courses) and self.__check(qualifs) and self.__check(victoires) and self.__check(podiums) and self.__check(poles) and self.__check(points):
            self.__courses = courses
            self.__qualifs = qualifs
            self.__victoires = victoires
            self.__podiums = podiums
            self.__poles = poles
            self.__points = points
        else:
            print("Stats.Erreur : paramètre invalide.")
    
    # GETTERS & SETTERS

    def getCourses(self) -> int:
        return self.__courses

    def getQualifs(self) -> int:
        return self.__qualifs

    def getVictoires(self) -> int:
        return self.__victoires

    def getPodiums(self) -> int:
        return self.__podiums

    def getPoles(self) -> int:
        return self.__poles

    def getPoints(self) -> int:
        return self.__points

    def setCourses(self, courses : int) -> None:
        if self.__check(courses):
            self.__courses = courses
        else:
            print("Stats.setCourses.Erreur : paramètre invalide.")

    def setQualifs(self, qualifs : int) -> None:
        if self.__check(qualifs):
            self.__qualifs = qualifs
        else:
            print("Stats.setQualifs.Erreur : paramètre invalide.")

    def setVictoires(self, victoires : int) -> None:
        if self.__check(victoires):
            self.__victoires = victoires
        else:
            print("Stats.setVictoires.Erreur : paramètre invalide.")

    def setPodiums(self, podiums : int) -> None:
        if self.__check(podiums):
            self.__podiums = podiums
        else:
            print("Stats.setPodiums.Erreur : paramètre invalide.")

    def setPoles(self, poles : int) -> None:
        if self.__check(poles):
            self.__poles = poles
        else:
            print("Stats.setPoles.Erreur : paramètre invalide.")

    def setPoints(self, points : int) -> None:
        if self.__check(points):
            self.__points = points
        else:
            print("Stats.setPoints.Erreur : paramètre invalide.")

    # METHODES

    def __str__(self) -> str:
        return "Courses : " + str(self.__courses) + "\n" + "Qualifs : " + str(self.__qualifs) + "\n" + "Victoires : " + str(self.__victoires) + "\n" + "Podiums : " + str(self.__podiums) + "\n" + "Poles : " + str(self.__poles) + "\n" + "Points : " + str(self.__points)

    def __check(self, value):
        if value < 0:
            return False
        else:
            return True

    