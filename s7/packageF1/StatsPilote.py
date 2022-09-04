
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

    def __init__(self, nom) -> None:

        self.__nom = nom
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
        return "Qualif : " + str(self.__qualif)

    def vsCoequipier(self, session) -> None:

        if session.lower() == "q":
            self.__coeqBattuQ += 1

        elif session.lower() == "s":
            self.__coeqBattuS += 1

        elif session.lower() == "c":
            self.__coeqBattuC += 1

        else:
            print("StatsPilote.vsCoequipier.Erreur : session inconnue.")

    def stats(self) -> str:
        return "\nStatistiques de " + self.__nom  + " :\n\n" + str(self.__statsQ()) + "\n" + str(self.__statsS()) + "\n" + str(self.__statsC())

    def __statsQ(self) -> str:

        resultat = ""

        # enregistrement des résultats des qualifications
        tab = []
        for manche in self.__qualif:
            if manche[0] != False:
                tab.append(manche[1])

        # calcul des statistiques
        resultat += "Participations en qualification : " + str(len(tab)) + "\n"
        if len(tab) > 0:
            resultat += "Passages en Q2 : " + str(len([x for x in tab if x < 16])) + "\n"
            resultat += "Passages en Q3 : " + str(len([x for x in tab if x < 11])) + "\n"
            resultat += "Meilleur resultat : P" + str(min(tab)) + "\n"
            resultat += "Poles : " + str(len([x for x in tab if x < 2])) + "\n"
            resultat += "Moyenne en qualification : " + str(sum(tab)/len(tab)) + "\n"
            resultat += "Coequipier battu en qualification : " + str(self.__coeqBattuQ) + "\n"
        return resultat

    def __statsS(self) -> str:

        resultat = ""

        # enregistrement des résultats des sprints
        tab = []
        for manche in self.__sprint:
            if manche[0] != False:
                tab.append(manche[1])

        # calcul des statistiques
        resultat += "Participations en sprint : " + str(len(tab)) + "\n"
        if len(tab) > 0:
            resultat += "Top 8 : " + str(len([x for x in tab if x < 9])) + "\n"
            resultat += "Podiums : " + str(len([x for x in tab if x < 4])) + "\n"
            resultat += "Victoires : " + str(len([x for x in tab if x < 2])) + "\n"
            resultat += "Meilleur resultat : P" + str(min(tab)) + "\n"
            resultat += "Moyenne en sprint : " + str(sum(tab)/len(tab)) + "\n"
            resultat += "Coequipier battu en sprint : " + str(self.__coeqBattuS) + "\n"
        return resultat

    def __statsC(self) -> str:
            
        resultat = ""

        # enregistrement des résultats des courses
        tab = []
        for manche in self.__course:
            if manche[0] != False:
                tab.append(manche[1])

        # calcul des statistiques
        resultat += "Participations en course : " + str(len(tab)) + "\n"
        if len(tab) > 0:
            resultat += "Entrees dans les points : " + str(len([x for x in tab if x < 9])) + "\n"
            resultat += "Podiums : " + str(len([x for x in tab if x < 4])) + "\n"
            resultat += "Victoires : " + str(len([x for x in tab if x < 2])) + "\n"
            resultat += "Meilleur resultat : P" + str(min(tab)) + "\n"
            resultat += "Moyenne en course : " + str(sum(tab)/len(tab)) + "\n"
            resultat += "Coequipier battu en course : " + str(self.__coeqBattuC) + "\n"
        return resultat