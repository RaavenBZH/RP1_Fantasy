class StatsEcurie():
    """
    Cette classe mémorise les statistiques d'une écurie.
    """

    # INITIALISATION

    def __init__(self, nom) -> None:

        self.__nom = nom
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

    def stats(self) -> str:
        return "\nStatistiques de " + self.__nom + " :\n\n" + str(self.__statsQ()) + "\n" + str(self.__statsS()) + "\n" + str(self.__statsC())
    
    def __statsQ(self) -> str:

        resultat = ""

        # enregistrement des résultats des qualifications
        tab = []
        for manche in self.__qualif:
            for etat in manche:
                if etat[0] != False:
                    tab.append(etat[1])

        # calcul des statistiques
        resultat += "Participations en qualification : " + str(len(tab)) + "\n"
        resultat += "Passages en Q2 : " + str(len([x for x in tab if x < 16])) + "\n"
        resultat += "Passages en Q3 : " + str(len([x for x in tab if x < 11])) + "\n"
        resultat += "Meilleur resultat : P" + str(min(tab)) + "\n" 
        resultat += "Moyenne en qualification : " + str(sum(tab)/len(tab)) + "\n"

        return resultat

    def __statsS(self) -> str:

        resultat = ""
        nbAbandons = 0

        # enregistrement des résultats des sprints
        tab = []
        for manche in self.__sprint:
            for etat in manche:
                if etat[0] == False and etat[1] == False:
                    break
                elif etat[0] != False:
                    tab.append(etat[1])
                    if etat[0] == True:
                        nbAbandons += 1

        # calcul des statistiques
        resultat += "Participations en sprint : " + str(len(tab)) + "\n"
        if len(tab) > 0:
            resultat += "Sprints termines : " + str(len(tab)-nbAbandons) + "\n"
            resultat += "Entrees dans les points : " + str(len([x for x in tab if x < 9])) + "\n"
            resultat += "Meilleur resultat : P" + str(min(tab)) + "\n"
            resultat += "Moyenne en sprint : " + str(sum(tab)/len(tab)) + "\n"

        return resultat
        
    def __statsC(self) -> str:
            
        resultat = ""
        nbAbandons = 0

        # enregistrement des résultats des courses
        tab = []
        for manche in self.__course:
            for etat in manche:
                if etat[0] != False:
                    tab.append(etat[1])
                    if etat[0] == True:
                        nbAbandons += 1
            
        # calcul des statistiques
        resultat += "Participations en course : " + str(len(tab)) + "\n"
        resultat += "Courses terminees : " + str(len(tab)-nbAbandons) + "\n"
        resultat += "Entrees dans les points : " + str(len([x for x in tab if x < 11])) + "\n"
        resultat += "Meilleur resultat : P" + str(min(tab)) + "\n"
        resultat += "Moyenne en course : " + str(sum(tab)/len(tab)) + "\n"

        return resultat