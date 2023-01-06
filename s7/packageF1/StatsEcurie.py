class StatsEcurie():
    """
Cette classe mémorise les statistiques d'une écurie.

    Attributs :
        - nom : nom de l'écurie
        - qualif : liste des résultats des qualifications
        - sprint : liste des résultats des sprints
        - course : liste des résultats des courses

    Méthodes :
        - getQualif : retourne la liste des résultats des qualifications
        - getSprint : retourne la liste des résultats des sprints
        - getCourse : retourne la liste des résultats des courses
        - addQualif : ajoute un résultat de qualification
        - addSprint : ajoute un résultat de sprint
        - addCourse : ajoute un résultat de course
        - __str__ : retourne les résultats des qualifications, sprints et courses
        - stats : retourne les statistiques de l'écurie
        - __statsQ : retourne les statistiques des qualifications
        - __statsS : retourne les statistiques des sprints
        - __statsC : retourne les statistiques des courses
        - tabQ : normalise les résultats des qualifications
        - nbQ(tab : list) -> str : retourne le nombre de qualifications.
        - nbQ2(tab : list) -> str : retourne le nombre de Q2.
        - nbQ3(tab : list) -> str : retourne le nombre de Q3.
        - nbPoles(tab : list) -> str : retourne le nombre de poles.
        - bestQ(tab : list) -> str : retourne le meilleur résultat en qualification.
        - avgQ(tab : list) -> str : retourne la moyenne des qualifications.
        - tabS : normalise les résultats des sprints
        - nbS : retourne le nombre de sprints disputés
        - nbT10S : retourne le nombre de top 10 en sprint
        - nbT3S : retourne le nombre de top 3 en sprint
        - nbVicS : retourne le nombre de victoires en sprint
        - bestS : retourne le meilleur résultat en sprint
        - avgS : retourne la moyenne des résultats en sprint
        - tabC : normalise les résultats des courses
        - nbC : retourne le nombre de courses disputées
        - nbT10C : retourne le nombre de top 10 en course
        - nbT3C : retourne le nombre de top 3 en course
        - nbVicC : retourne le nombre de victoires en course
        - bestC : retourne le meilleur résultat en course
        - avgC : retourne la moyenne des résultats en course
        - nbAbandons : retourne le nombre d'abandons en course
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
                if etat[0] is not False:
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
                if etat[0] is False and etat[1] is False:
                    break
                elif etat[0] is not False:
                    tab.append(etat[1])
                    if etat[0] is True:
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
                if etat[0] is not False:
                    tab.append(etat[1])
                    if etat[0] is True:
                        nbAbandons += 1
            
        # calcul des statistiques
        resultat += "Participations en course : " + str(len(tab)) + "\n"
        resultat += "Courses terminees : " + str(len(tab)-nbAbandons) + "\n"
        resultat += "Entrees dans les points : " + str(len([x for x in tab if x < 11])) + "\n"
        resultat += "Meilleur resultat : P" + str(min(tab)) + "\n"
        resultat += "Moyenne en course : " + str(sum(tab)/len(tab)) + "\n"

        return resultat

    def tabQ(self) -> list:
        tab = []
        for manche in self.__qualif:
            if manche[0][0] is not False or manche[1][0] is not False:
                tab.append(manche)
        return tab

    def nbQ(self, tab) -> list:
        return str(sum([sum([1 for resPilote in manche if resPilote[0] is not False]) for manche in tab]))

    def nbQ2(self, tab) -> list:
        return str(sum([sum([1 for resPilote in manche if resPilote[0] is not False and resPilote[1] < 16]) for manche in tab]))

    def nbQ3(self, tab) -> list:
        return str(sum([sum([1 for resPilote in manche if resPilote[0] is not False and resPilote[1] < 11]) for manche in tab]))

    def nbPoles(self, tab) -> list:
        return str(sum([1 for manche in tab if manche[0][0] is not False and manche[0][1] == 1]))

    def bestQ(self, tab) -> list:
        return str(min([min([resPilote[1] for resPilote in manche if resPilote[0] is not False]) for manche in tab]))

    def avgQ(self, tab) -> list:
        return str(round(sum([sum([resPilote[1] for resPilote in manche if resPilote[0] is not False]) for manche in tab])/sum([sum([1 for resPilote in manche if resPilote[0] is not False]) for manche in tab]),2))

    def tabS(self) -> list:
        tab = []
        for manche in self.__sprint:
            if manche[0][0] is not False or manche[1][0] is not False:
                tab.append(manche)
        return tab

    def nbS(self, tab) -> list:
        return str(sum([sum([1 for resPilote in manche if resPilote[0] is not False]) for manche in tab]))

    def nbT8S(self, tab) -> list:
        return str(sum([sum([1 for resPilote in manche if resPilote[0] is not False and resPilote[1] < 9]) for manche in tab]))

    def nbT3S(self, tab) -> str:
        return str(sum([sum([1 for resPilote in manche if resPilote[0] is not False and resPilote[1] < 4]) for manche in tab]))

    def nbVicS(self, tab) -> str:
        return str(sum([sum([1 for resPilote in manche if resPilote[0] is not False and resPilote[1] == 1]) for manche in tab]))

    def bestS(self, tab) -> str:
        return str(min([min([resPilote[1] for resPilote in manche if resPilote[0] is not False]) for manche in tab]))

    def avgS(self, tab) -> str:
        return str(round(sum([sum([resPilote[1] for resPilote in manche if resPilote[0] is not False]) for manche in tab])/sum([sum([1 for resPilote in manche if resPilote[0] is not False]) for manche in tab]),2))

    def tabC(self) -> list:
        tab = []
        for manche in self.__course:
            if manche[0][0] is not False or manche[1][0] is not False:
                tab.append(manche)
        return tab

    def nbC(self, tab) -> list:
        return str(sum([sum([1 for resPilote in manche if resPilote[0] is not False]) for manche in tab]))

    def nbT10C(self, tab) -> list:
        return str(sum([sum([1 for resPilote in manche if resPilote[0] is not False and resPilote[1] < 11]) for manche in tab]))

    def nbT3C(self, tab) -> str:
        return str(sum([sum([1 for resPilote in manche if resPilote[0] is not False and resPilote[1] < 4]) for manche in tab]))

    def nbVicC(self, tab) -> str:
        return str(sum([sum([1 for resPilote in manche if resPilote[0] is not False and resPilote[1] == 1]) for manche in tab]))

    def bestC(self, tab) -> str:
        return str(min([min([resPilote[1] for resPilote in manche if resPilote[0] is not False]) for manche in tab]))

    def avgC(self, tab) -> str:
        return str(round(sum([sum([resPilote[1] for resPilote in manche if resPilote[0] is not False]) for manche in tab])/sum([sum([1 for resPilote in manche if resPilote[0] is not False]) for manche in tab]),2))

    def nbAbandons(self) -> list:
        return str(sum([sum([1 for resPilote in manche if resPilote[0] is True]) for manche in self.__course]))
