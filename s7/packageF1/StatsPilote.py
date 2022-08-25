
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
        - __str__() -> str : renvoie les résultats des qualifications, sprints et des courses.
        - stats() -> str : renvoie les statistiques du pilote.
        - __calculeDeltaSprint() -> int : calcule la moyenne des positions gagnées en sprint.
        - __calculDeltaCourse() -> int : calcule la moyenne des positions gagnées en course.
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
        return "Historique des qualifications : " + str(self.__qualif) + "\n" + "Historique des sprints : " + str(self.__sprint) + "\n" + "Historique des courses : " + str(self.__course)

    def stats(self) -> None:

        # Qualifications
        toReturn = "Nombre de qualifications : " + str(len(self.__qualif)-self.__qualif.count(None)) + "\n"
        if len(self.__qualif)-self.__qualif.count(None) > 0:
            toReturn += "Meilleur resultat (Q) : P" + str(min(self.__qualif)) + "\n"
            toReturn += "Position moyenne (Q) : " + str(sum(self.__qualif)/len(self.__qualif)) + "\n"
        else:
            toReturn += "Meilleure resultat (Q) : N/A\n"

        # Sprints
        toReturn += "\nNombre de sprints : " + str(len(self.__sprint)-self.__sprint.count(None)) + "\n"
        if len(self.__sprint)-self.__sprint.count(None) > 0:
            ignoreNone = [x for x in self.__sprint if x is not None]
            toReturn += "Meilleur resultat (S) : P" + str(min(ignoreNone)) + "\n"
            toReturn += "Position moyenne (S) : " + str(sum(ignoreNone)/len(ignoreNone)) + "\n"
        else:
            toReturn += "Meilleur resultat (S) : N/A\n"
        toReturn += "Moyenne positions gagnees (S) : " + str(self.__calculeDeltaSprint()) + "\n"

        # Courses
        toReturn += "\nNombre de courses : " + str(len(self.__course)-self.__course.count(None)) + "\n"
        if len(self.__course)-self.__course.count(None) > 0:
            toReturn += "Meilleure resultat (C) : P" + str(min(self.__course)) + "\n"
            toReturn += "Position moyenne (C) : " + str(sum(self.__course)/len(self.__course)) + "\n"
        else:
            toReturn += "Meilleure resultat (C) : N/A\n"
        toReturn += "Moyenne positions gagnees (C) : " + str(self.__calculDeltaCourse()) + "\n"

        return toReturn

    def __calculeDeltaSprint(self) -> int:
        tab = []
        for i in range (len(self.__sprint)):
            if self.__sprint[i] != None:
                if self.__qualif[i] != None:
                    tab.append(self.__qualif[i] - self.__sprint[i])
                else:
                    print("Stats.__calculeDeltaSprint.Erreur : Position de départ manquante.")
        return sum(tab)/len(tab)

    def __calculDeltaCourse(self) -> int:
        tab = []
        for i in range (len(self.__course)):
            if self.__sprint[i] == None:
                reference = self.__qualif[i]
            else:
                reference = self.__sprint[i]
            tab.append(reference - self.__course[i])
        return sum(tab)/len(tab)