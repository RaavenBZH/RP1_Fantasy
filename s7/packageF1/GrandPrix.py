from packageF1.Fonctions import *
from packageF1.Pilote import *

class GrandPrix:
    '''
    Cette classe mémorise le résultat d'un grand prix.

    Attributs : 
        - __estSprint (bool) : True si le grand prix est un sprint, False sinon
        - __dico (dict <str : int>) : les points pour chaque pilote.
        - __circuit (str) : le circuit du grand prix.
        - __qualif (list <Pilote>) : le classement de la qualification.
        - __sprint (list <Pilote>) : le classement de la sprint.
        - __course (list <Pilote>) : le classement de la course.

    Méthodes :
        - __init__(circuit : str, sprint : bool) -> None : construit les objets <GrandPrix>.
        - __str__() -> str : affiche les résultats d'un grand prix.
        - getCircuit() -> str : recupère le circuit.
        - getQualification() -> list : récupère le classement de la qualification.
        - getSprint() -> list : récupère le classement de la sprint.
        - getCourse() -> list : récupère le classement de la course.
        - getPoints() -> dict : récupère les points.
        - setCircuit(circuit : str) -> None : modifie le circuit.
        - setQualification(qualif : list) -> None : enregistre le classement de la qualification.
        - setSprint(sprint : list) -> None : enregistre le classement de la sprint.
        - setCourse(course : list) -> None : enregistre le classement de la course.
        - getQualifName() -> list : récupère les noms des pilotes de la qualification.
        - getSprintName() -> list : récupère les noms des pilotes de la sprint.
        - getCourseName() -> list : récupère les noms des pilotes de la course.
        - __checkCircuit(circuit : str) -> bool : vérifie si le circuit est connu.
        - __checkSession(session : list) -> bool : vérifie que la session est bien constituée.
        - __checkCorrelation() -> bool : vérifie que les sessions sont bien liées.
        - calcul(absentsQualif : int, absentsSprint : int, abandonsSprint : int, abandonsCourse : int) -> None : calcule les points.
        - historique() -> None : affiche l'historique des points.
        - __resetHistorique() -> None : réinitialise l'historique des pilotes.
        - __statsPilotes(absentsQualif : int, absentsSprint : int, abandonsSprint : int, abandonsCourse : int) -> None : enregistre les statistiques du grand prix.
    ''' 

    # INITIALISATION

    def __init__(self, circuit : str, sprint = False) -> None:

        self.__estSprint = sprint
        self.__dico = {}
        self.__circuit = None
        self.__qualif = None
        self.__sprint = None
        self.__course = None

        if self.__checkCircuit(circuit):
            self.__circuit = circuit
        else:
            print("GrandPrix.Erreur : circuit inconnu.")

    # GETTERS & SETTERS

    def getCircuit(self) -> list:
        return self.__circuit

    def getQualification(self) -> list:
        return self.__qualif

    def getSprint(self) -> list:
        return self.__sprint

    def getCourse(self) -> list:
        return self.__course

    def getPoints(self) -> dict:
        return sortedDict(self.__dico)

    def setCircuit(self, circuit : str) -> None:
        if self.__checkCircuit(circuit):
            self.__circuit = circuit
        else:
            print("GrandPrix.setCircuit.Erreur : circuit inconnu.")

    def setQualification(self, qualif : list) -> None:
        if self.__checkSession(qualif):
            self.__qualif = qualif
        else:
            print("GrandPrix.setQualificaction.Erreur : la qualification n'est pas correcte.")

    def setSprint(self, sprint : list) -> None:
        if self.__checkSession(sprint):
            self.__sprint = sprint
        else:
            print("GrandPrix.setSprint.Erreur : la sprint n'est pas correcte.")

    def setCourse(self, course : list) -> None:
        if self.__checkSession(course):
            self.__course = course
        else:
            print("GrandPrix.setCourse.Erreur : la course n'est pas correcte.")

    def getQualifName(self) -> None:
        return list(map(lambda x: x.getGamertag(), self.__qualif))

    def getSprintName(self) -> None:
        return list(map(lambda x: x.getGamertag(), self.__sprint))

    def getCourseName(self) -> None:
        return list(map(lambda x: x.getGamertag(), self.__course))
    
    # METHODES

    def __checkCircuit(self, circuit : str) -> bool:

        listeCircuits = [
            'Barhein',
            'Imola',
            'Portugal',
            'Espagne',
            'Monaco',
            'Azerbaidjan',
            'Canada',
            'France',
            'Autriche',
            'RoyaumeUni',
            'Hongrie',
            'Belgique',
            'PaysBas',
            'Italie',
            'Russie',
            'Singapour',
            'Japon',
            'EtatsUnis',
            'Mexique',
            'Bresil',
            'Australie',
            'ArabieSaoudite',
            'AbuDhabi',
            'Chine'
        ]

        if circuit in listeCircuits:
            return True
        else:
            return False

    def __checkSession(self, session : list) -> bool:

        for i in session:
            if not isinstance(i, Pilote):
                return False

        if len(set(session)) == len(session):
            return True
        else:
            return False
    
    def __checkCorrelation(self) -> bool:

        check = True

        if self.__estSprint:
            if self.__qualif == None or self.__sprint == None or self.__course == None:
                check = False
            else:
                check = (len(self.__qualif) == len(self.__sprint) == len(self.__course) == 20)

        else:
            if self.__qualif == None or self.__course == None:
                check = False
            else:
                check = (len(self.__qualif) == len(self.__course) == 20)

        if check == False:
            return check

        tab = []
        for i in self.__qualif:
            tab.append(i.getEcurie())
        if 2*len(set(tab)) == len(tab):
            check = True

        tab = []
        for i in self.__sprint:
            tab.append(i.getEcurie())
        if 2*len(set(tab)) == len(tab):
            check = True

        tab = []
        for i in self.__course:
            tab.append(i.getEcurie())
        if 2*len(set(tab)) == len(tab):
            check = True

        return check      

    def calcul(self, absentsQualif = 0, absentsSprint = 0, abandonsSprint = 0, absentsCourse = 0, abandonsCourse = 0) -> None:
        if self.__checkCorrelation():

            self.__resetHistorique()

            # Calcul des points pour la qualification

            bonus = 0
            desc = ""
            ecuries = []

            for i in range(len(self.__qualif)):

                gamertag = self.__qualif[i].getGamertag()
                ecurie = self.__qualif[i].getEcurie()

                if i < len(self.__qualif)-absentsQualif:

                    if i < 1:
                        bonus = 5
                        desc = ("Pole (Q)", bonus)
                    elif i < 10:
                        bonus = 3
                        desc = ("Q3", bonus)
                    elif i < 15:
                        bonus = 2
                        desc = ("Q2", bonus)
                    else:
                        bonus = 1
                        desc = ("Q1", bonus)

                    self.__qualif[i].ajoutHistorique(desc)

                    if gamertag in self.__dico:
                        self.__dico[gamertag] += bonus
                    else:
                        self.__dico[gamertag] = bonus

                    if ecurie not in ecuries:
                        ecuries.append(ecurie)
                        self.__dico[gamertag] += 1
                        self.__qualif[i].ajoutHistorique(("Coequipier battu (Q)", 1))

                else:
                    self.__dico[gamertag] = 0
                    self.__qualif[i].ajoutHistorique(("Absent (Q)", 0))

            ##############################################################
                
            # Calcul des points pour la sprint
            if self.__estSprint:

                bonus = 0
                desc = ""
                ecuries = []

                for i in range(len(self.__sprint)):

                    gamertag = self.__sprint[i].getGamertag()
                    ecurie = self.__sprint[i].getEcurie()

                    if i < len(self.__sprint)-absentsSprint:

                        if i < 1:
                            bonus = 4
                            desc = ("Victoire (S)", bonus)
                        elif i < 3:
                            bonus = 3
                            desc = ("Podium (S)", bonus)
                        elif i < 8:
                            bonus = 2
                            desc = ("Top 8 (S)", bonus)
                        else:
                            bonus = 1
                            desc = ("Course terminee (S)", bonus)

                        if i >= len(self.__sprint)-absentsSprint-abandonsSprint:
                            bonus = 0
                            desc = ("DNF (S)", 0)

                        self.__sprint[i].ajoutHistorique(desc)
                    
                        if gamertag in self.__dico:
                            self.__dico[gamertag] += bonus
                        else:
                            self.__dico[gamertag] = bonus

                        if ecurie not in ecuries:
                            ecuries.append(ecurie)
                            self.__dico[gamertag] += 1
                            self.__sprint[i].ajoutHistorique(("Coequipier battu (S)", 1))

                        # changement de position

                        posDepart, posArrivee = 0, i
                        for posDepart in range(len(self.__qualif)):
                            if self.__qualif[posDepart].getGamertag() == gamertag:
                                break

                        gain = posDepart - posArrivee
                        if gain > 3 : gain = 3
                        if gain < -3 : gain = -3

                        self.__dico[gamertag] += gain
                        self.__sprint[i].ajoutHistorique(("Gain pos. (S)", gain))

                    else:
                        self.__sprint[i].ajoutHistorique(("Absent (S)", 0))
                
            ##############################################################

            # Calcul des points pour la course

            bonus = 0
            desc = ""
            ecuries = []

            for i in range(len(self.__course)):

                gamertag = self.__course[i].getGamertag()
                ecurie = self.__course[i].getEcurie()

                if i < len(self.__course)-absentsCourse:

                    if i < 1:
                        bonus = 6
                        desc = ("Victoire (C)", bonus)
                    elif i < 3:
                        bonus = 4
                        desc = ("Podium (C)", bonus)
                    elif i < 6:
                        bonus = 3
                        desc = ("Top 6 (C)", bonus)
                    elif i < 10:
                        bonus = 2
                        desc = ("Top 10 (C)", bonus)
                    else:
                        bonus = 1
                        desc = ("Course terminee", bonus)

                    if i >= len(self.__course)-absentsCourse-abandonsCourse:
                        bonus = 0
                        desc = ("DNF (C)", 0)

                    self.__course[i].ajoutHistorique(desc)
                    
                    if gamertag in self.__dico:
                        self.__dico[gamertag] += bonus
                    else:
                        self.__dico[gamertag] = bonus

                    if ecurie not in ecuries:
                        ecuries.append(ecurie)
                        self.__dico[gamertag] += 1
                        self.__course[i].ajoutHistorique(("Coequipier battu (C)", 1))

                    # changement de position

                    if self.__estSprint:
                        reference = self.__sprint
                    else:
                        reference = self.__qualif

                    posDepart, posArrivee = 0, i
                    for posDepart in range(len(reference)):
                        if reference[posDepart].getGamertag() == gamertag:
                            break

                    gain = posDepart - posArrivee
                    if gain > 3 : gain = 3
                    if gain < -3 : gain = -3

                    self.__dico[gamertag] += gain
                    self.__sprint[i].ajoutHistorique(("Gain pos. (C)", gain))

                else:
                    self.__course[i].ajoutHistorique(("Absent (C)", 0))

            ##############################################################

            # Statistiques
            self.__statsPilotes(absentsQualif, absentsSprint, abandonsSprint, absentsCourse, abandonsCourse)
            self.__statsEcuries()

        else:
            print("GrandPrix.calcul.Erreur : les sessions ne sont pas correctes.")

    def historique(self) -> None:
        for i in self.__qualif:
            print(i.getGamertag() + " : " + str(i.getHistorique()))

    def __resetHistorique(self) -> None:
        for i in self.__dico:
            i.resetHistorique()

    def __statsPilotes(self, absentsQualif, absentsSprint, abandonsSprint, absentsCourse, abandonsCourse) -> None:

        # Qualifications
        for i in range(len(self.__qualif)):
            pilote = self.__qualif[i]
            position = i + 1
            if i < len(self.__qualif)-absentsQualif:
                resultat = (position, position)
            else:
                resultat = (False, position)
            pilote.getDonnees().addQualif(resultat)

        # Sprint
        if self.__estSprint:
            for i in range(len(self.__sprint)):
                pilote = self.__sprint[i]
                position = i + 1
                if i < len(self.__sprint)-absentsSprint:
                    # Abandon
                    if i >= len(self.__sprint)-absentsSprint-abandonsSprint:
                        resultat = (True, position)
                    # Pas abandon
                    else:
                        resultat = (position, position)
                # Absent
                else:
                    resultat = (False, position)
                pilote.getDonnees().addSprint(resultat)    
        else:
            for i in range(len(self.__sprint)):
                pilote = self.__sprint[i]
                pilote.getDonnees().addSprint(resultat)

        # Course
        for i in range(len(self.__course)):
            pilote = self.__course[i]
            position = i + 1
            if i < len(self.__course)-absentsCourse:
                # Abandon
                if i >= len(self.__course)-absentsCourse-abandonsCourse:
                    resultat = (True, position)
                # Pas abandon
                else:
                    resultat = (position, position)
            # Absent
            else:
                resultat = (False, position)
            pilote.getDonnees().addCourse(resultat)

    def __statsEcuries(self) -> None:

        # Qualifications
        for pilote in self.__qualif:
            ecurie = pilote.getEcurie()
            resultat = ecurie.getResultat()

            if len(resultat) < 1:
                resultat.append(pilote.getDonnees().getQualif()[-1])
                pilote.getDonnees().vsCoequipier(True, "q")
                ecurie.setResultat(resultat)
            
            elif len(resultat) < 2:
                resultat.append(pilote.getDonnees().getQualif()[-1])
                pilote.getDonnees().vsCoequipier(False, "q")
                ecurie.getDonnees().addQualif(resultat)
                ecurie.setResultat([])

            else:
                print("Erreur")

        # Sprint
        for pilote in self.__sprint:
            ecurie = pilote.getEcurie()
            resultat = ecurie.getResultat()

            if len(resultat) < 1:
                resultat.append(pilote.getDonnees().getSprint()[-1])
                pilote.getDonnees().vsCoequipier(True, "s")
                ecurie.setResultat(resultat)
            
            elif len(resultat) < 2:
                resultat.append(pilote.getDonnees().getSprint()[-1])
                pilote.getDonnees().vsCoequipier(False, "s")
                ecurie.getDonnees().addSprint(resultat)
                ecurie.setResultat([])

            else:
                print("Erreur")

        # Course
        for pilote in self.__course:
            ecurie = pilote.getEcurie()
            resultat = ecurie.getResultat()

            if len(resultat) < 1:
                resultat.append(pilote.getDonnees().getCourse()[-1])
                pilote.getDonnees().vsCoequipier(True, "c")
                ecurie.setResultat(resultat)
            
            elif len(resultat) < 2:
                resultat.append(pilote.getDonnees().getCourse()[-1])
                pilote.getDonnees().vsCoequipier(False, "c")
                ecurie.getDonnees().addCourse(resultat)
                ecurie.setResultat([])

            else:
                print("Erreur")