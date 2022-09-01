
class StatsPilote:
    """
    Cette classe mémorise les statistiques d'un pilote.

    Attributs :
        - __qualif (list) : résultats des qualifications.
        - __sprint (list) : résultats des sprints.
        - __course (list) : résultats des courses.

    Méthodes :
        - getQualif() -> list : retourne les résultats des qualifications.
        - getSprint() -> list : retourne les résultats des sprints.
        - getCourse() -> list : retourne les résultats des courses.
        - addQualif(qualif : int) : ajoute une qualification.
        - addSprint(sprint : int) : ajoute un sprint.
        - addCourse(course : int) : ajoute une course.
    """

    # INITIALISATION

    def __init__(self) -> None:

        self.__qualif = []
        self.__coeqBattuQ = 0
        self.__sprint = []
        self.__coeqBattuS = 0
        self.__course = []
        self.__coeqBattuC = 0
    
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
        return str(self.__qualif) + "\n" + str(self.__sprint) + "\n" + str(self.__course) + "\n" + str(self.__coeqBattuQ) + "\n" + str(self.__coeqBattuS) + "\n" + str(self.__coeqBattuC)

    def vsCoequipier(self, battu, session) -> None:
        bonus = 1
        if not battu:
            bonus = -1

        if session == "q":
            self.__coeqBattuQ += bonus

        elif session == "s":
            self.__coeqBattuS += bonus

        elif session == "c":
            self.__coeqBattuC += bonus

        else:
            print("StatsPilote.vsCoequipier.Erreur : session inconnue.")

    def stats(self) -> str:
        pass