class StatsPilote:
    """
    Cette classe mémorise les statistiques d'un pilote.

    Attributs :
        - nom : nom du pilote.
        - __qualif (list) : résultats des qualifications.
        - __coeqBattuQ (int) : nombre de duels remportés face aux coequipiers en qualification.
        - __sprint (list) : résultats des sprints.
        - __coeqBattuS (int) : nombre de duels remportés face aux coequipiers en sprint.
        - __course (list) : résultats des courses.
        - __coeqBattuC (int) : nombre de duels remportés face aux coequipiers en course.

    Méthodes :
        - getQualif() -> list : retourne les résultats des qualifications.
        - getSprint() -> list : retourne les résultats des sprints.
        - getCourse() -> list : retourne les résultats des courses.
        - getCoeqBattuQ() -> str : retourne le nombre de duels remportés face aux coequipiers en qualification.
        - getCoeqBattuS() -> str : retourne le nombre de duels remportés face aux coequipiers en sprint.
        - getCoeqBattuC() -> str : retourne le nombre de duels remportés face aux coequipiers en course.
        - tauxCoeqBattuQ() -> str : retourne le taux de duels remportés face aux coequipiers en qualification.
        - tauxCoeqBattuS() -> str : retourne le taux de duels remportés face aux coequipiers en sprint.
        - tauxCoeqBattuC() -> str : retourne le taux de duels remportés face aux coequipiers en course.
        - addQualif(qualif : int) : ajoute une qualification.
        - addSprint(sprint : int) : ajoute un sprint.
        - addCourse(course : int) : ajoute une course.
        - __str__() -> str : retourne les résultats des qualifications, sprints et courses.
        - vsCoequipier(session : str) : ajoute un duel remporté face aux coequipiers.
        - stats() -> str : affiche les statistiques du pilote.
        - __statsQ() -> str : affiche les statistiques des qualifications.
        - tabQ() -> list : retourne les résultats des qualifications pour traitement.
        - nbQ(tab : list) -> str : retourne le nombre de qualifications.
        - nbQ2(tab : list) -> str : retourne le nombre de Q2.
        - nbQ3(tab : list) -> str : retourne le nombre de Q3.
        - nbPoles(tab : list) -> str : retourne le nombre de poles.
        - bestQ(tab : list) -> str : retourne le meilleur résultat en qualification.
        - avgQ(tab : list) -> str : retourne la moyenne des qualifications.
        - __statsS() -> str : affiche les statistiques des sprints.
        - tabS() -> list : retourne les résultats des sprints pour traitement.
        - nbS(tab : list) -> str : retourne le nombre de sprints.
        - nbT8S(tab : list) -> str : retourne le nombre de sprints terminés dans les 8 premiers.
        - nbT3S(tab : list) -> str : retourne le nombre de sprints terminés dans les 3 premiers.
        - nbVicS(tab : list) -> str : retourne le nombre de sprints remportés.
        - bestS(tab : list) -> str : retourne le meilleur résultat en sprint.
        - avgS(tab : list) -> str : retourne la moyenne des sprints.
        - __statsC() -> str : affiche les statistiques des courses.
        - tabC() -> list : retourne les résultats des courses pour traitement.
        - nbC(tab : list) -> str : retourne le nombre de courses.
        - nbT10C(tab : list) -> str : retourne le nombre de courses terminées dans les 10 premiers.
        - nbT3C(tab : list) -> str : retourne le nombre de courses terminées dans les 3 premiers.
        - nbVicC(tab : list) -> str : retourne le nombre de courses remportées.
        - bestC(tab : list) -> str : retourne le meilleur résultat en course.
        - avgC(tab : list) -> str : retourne la moyenne des courses.
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

    def getCoeqBattuQ(self) -> str:
        return str(self.__coeqBattuQ)

    def getCoeqBattuS(self) -> str:
        return str(self.__coeqBattuS)

    def getCoeqBattuC(self) -> str:
        return str(self.__coeqBattuC)

    # METHODES

    def tauxCoeqBattuQ(self) -> str:
        return str(round(self.__coeqBattuQ / len(self.tabQ()), 2))

    def tauxCoeqBattuS(self) -> str:
        if len(self.tabS()) == 0:
            return "0"
        return str(round(self.__coeqBattuS / len(self.tabS()), 2))

    def tauxCoeqBattuC(self) -> str:
        return str(round(self.__coeqBattuC / len(self.tabC()), 2))

    def addQualif(self, qualif) -> None:
        self.__qualif.append(qualif)

    def addSprint(self, sprint) -> None:
        self.__sprint.append(sprint)

    def addCourse(self, course) -> None:
        self.__course.append(course)

    def __str__(self) -> str:
        return "Qualif : " + str(self.__qualif) + "\nSprint : " + str(self.__sprint) + "\nCourse : " + str(self.__course)

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
        tab = self.tabQ()

        # calcul des statistiques
        resultat += "Participations en qualification : " + self.nbQ(tab) + "\n"
        if len(tab) > 0:
            resultat += "Passages en Q2 : " + self.nbQ2(tab) + "\n"
            resultat += "Passages en Q3 : " + self.nbQ3(tab) + "\n"
            resultat += "Poles : " + self.nbPoles(tab) + "\n"
            resultat += "Meilleur resultat : P" + self.bestQ(tab) + "\n"
            resultat += "Moyenne en qualification : " + self.avgQ(tab) + "\n"
            resultat += "Coequipier battu en qualification : " + str(self.__coeqBattuQ) + "\n"
        return resultat

    def tabQ(self) -> list:
        tab = []
        for manche in self.__qualif:
            if manche[0] != False:
                tab.append(manche[1])
        return tab

    def nbQ(self, tab) -> str:
        return str(len(tab))

    def nbQ2(self, tab) -> str:
        return str(len([x for x in tab if x < 16]))

    def nbQ3(self, tab) -> str:
        return str(len([x for x in tab if x < 11]))
   
    def nbPoles(self, tab) -> str:
        return str(len([x for x in tab if x < 2]))

    def bestQ(self, tab) -> str:
        return str(min(tab))

    def avgQ(self, tab) -> str:
        if len(tab) > 0:
            return str(round(sum(tab)/len(tab), 2))
        else:
            return "0"

    def __statsS(self) -> str:

        resultat = ""

        # enregistrement des résultats des sprints
        tab = self.tabS()

        # calcul des statistiques
        resultat += "Participations en sprint : " + self.nbS(tab) + "\n"
        if len(tab) > 0:
            resultat += "Top 8 : " + self.nbT8S(tab) + "\n"
            resultat += "Podiums : " + self.nbT3S(tab) + "\n"
            resultat += "Victoires : " + self.nbVicS(tab) + "\n"
            resultat += "Meilleur resultat : P" + self.bestS(tab) + "\n"
            resultat += "Moyenne en sprint : " + self.avgS(tab) + "\n"
            resultat += "Coequipier battu en sprint : " + str(self.__coeqBattuS) + "\n"
        return resultat

    def tabS(self) -> list:
        tab = []
        for manche in self.__sprint:
            if manche[0] != False:
                tab.append(manche[1])
        return tab

    def nbS(self, tab) -> str:
        return str(len(tab))

    def nbT8S(self, tab) -> str:
        return str(len([x for x in tab if x < 9]))

    def nbT3S(self, tab) -> str:
        return str(len([x for x in tab if x < 4]))

    def nbVicS(self, tab) -> str:
        return str(len([x for x in tab if x < 2]))

    def bestS(self, tab) -> str:
        if len(tab) > 0:
            return str(min(tab))
        else:
            return "0"

    def avgS(self, tab) -> str:
        if len(tab) > 0:
            return str(round(sum(tab)/len(tab), 2))
        else:
            return "0"

    def __statsC(self) -> str:
            
        resultat = ""

        # enregistrement des résultats des courses
        tab = self.tabC()

        # calcul des statistiques
        resultat += "Participations en course : " + self.nbC(tab) + "\n"
        if len(tab) > 0:
            resultat += "Entrees dans les points : " + self.nbT10C(tab) + "\n"
            resultat += "Podiums : " + self.nbT3C(tab) + "\n"
            resultat += "Victoires : " + self.nbVicC(tab) + "\n"
            resultat += "Meilleur resultat : P" + self.bestC(tab) + "\n"
            resultat += "Moyenne en course : " + self.avgC(tab) + "\n"
            resultat += "Coequipier battu en course : " + str(self.__coeqBattuC) + "\n"
        return resultat

    def tabC(self) -> list:
        tab = []
        for manche in self.__course:
            if manche[0] != False:
                tab.append(manche[1])
        return tab

    def nbC(self, tab) -> str:
        return str(len(tab))

    def nbT10C(self, tab) -> str:
        return str(len([x for x in tab if x < 11]))

    def nbT3C(self, tab) -> str:
        return str(len([x for x in tab if x < 4]))

    def nbVicC(self, tab) -> str:
        return str(len([x for x in tab if x < 2]))

    def bestC(self, tab) -> str:
        return str(min(tab))

    def avgC(self, tab) -> str:
        if len(tab) > 0:
            return str(round(sum(tab)/len(tab), 2))
        else:
            return "0"

    def nbAbandons(self) -> str:
        return str(len([x for x in self.__course if type(x[0]) == bool and x[0] == True]))

    def fiabilite(self) -> str:
        return str(round(1 - len([x for x in self.__course if type(x[0]) == bool and x[0] == True])/len(self.tabC()), 2))