class StatsEcurie():
    """
    Cette classe mémorise les statistiques d'une écurie.
    """

    # INITIALISATION

    def __init__(self) -> None:

        self.__qualif = []
        self.__sprint = []
        self.__course = []
        
    # GETTERS & SETTERS

    def getQualif(self) -> list:
        return self.__qualif

    def getSprint(self) -> list:
        return self.__sprint

    def getCourse(self) -> list:
        return self.__course

    def addQualif(self, qualif) -> None:
        self.__qualif.append(qualif)

    def addSprint(self, sprint) -> None:
        self.__sprint.append(sprint)

    def addCourse(self, course) -> None:
        self.__course.append(course)

    # METHODES

    def __str__(self) -> str:
        return "Qualif : " + str(self.__qualif) + "\nSprint : " + str(self.__sprint) + "\nCourse : " + str(self.__course)