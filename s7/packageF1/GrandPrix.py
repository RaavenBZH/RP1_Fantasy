import copy
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
        - calcul(abandonsSprint : int, abandonsCourse : int) -> None : calcule les points.
        - historique() -> None : affiche l'historique des points.
        - resetHistorique() -> None : réinitialise l'historique des pilotes.
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

    def getPoints(self) -> list:
        return self.__dico

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

        if self.__estSprint:
            if self.__qualif == None or self.__sprint == None or self.__course == None:
                return False
            else:
                return set(self.__qualif).issubset(set(self.__sprint)) and set(self.__sprint).issubset(set(self.__course))

        else:
            if self.__qualif == None or self.__course == None:
                return False
            else:
                return set(self.__qualif).issubset(set(self.__course))

    def calcul(self, absentQualif = 0, abandonsSprint = 0, abandonsCourse = 0) -> None:
        if self.__checkCorrelation():

            # Calcul des points pour la qualification
            bonus = 0
            desc = ""
            ecuries = []
            for i in range(len(self.__qualif)):
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
                
                gt = self.__qualif[i].getGamertag()
                if gt in self.__dico:
                    self.__dico[gt] += bonus
                else:
                    self.__dico[gt] = bonus

                if self.__qualif[i].getEcurie() not in ecuries:
                    ecuries.append(self.__qualif[i].getEcurie())
                    self.__dico[gt] += 1
                    self.__qualif[i].ajoutHistorique(("Coequipier battu (Q)", 1))

            for i in range(absentQualif):
                gt = self.__sprint[-(i+1)].getGamertag()
                self.__dico[gt] = 0
                self.__sprint[-(i+1)].setHistorique([])
            ##############################################################
                
            # Calcul des points pour la sprint
            if self.__estSprint:
                bonus = 0
                desc = ""
                ecuries = []
                for i in range(len(self.__sprint)):
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
                        desc = ("Participation (S)", bonus)

                    self.__sprint[i].ajoutHistorique(desc)
                    
                    gt = self.__sprint[i].getGamertag()
                    if gt in self.__dico:
                        self.__dico[gt] += bonus
                    else:
                        self.__dico[gt] = bonus

                    if self.__sprint[i].getEcurie() not in ecuries:
                        ecuries.append(self.__sprint[i].getEcurie())
                        self.__dico[gt] += 1
                        self.__sprint[i].ajoutHistorique(("Coequipier battu (S)", 1))

                    # changement de position
                    if self.__sprint[i] in self.__qualif:
                        j = 0
                        for j in range(len(self.__qualif)):
                            if self.__qualif[j] == self.__sprint[i]:
                                break
                        difference = j - i
                        if difference > 3:
                            difference = 3
                        if difference < -3:
                            difference = -3
                        self.__dico[gt] += difference
                        self.__sprint[i].ajoutHistorique(("Pos. (S)", difference))
                    else:
                        print("GrandPrix.calcul.Erreur : un nouveau pilote apparait (err1).")

                for i in range(abandonsSprint):
                    gt = self.__sprint[-(i+1)].getGamertag()
                    self.__dico[gt] -= 1
                    self.__sprint[-(i+1)].ajoutHistorique(("Abandon (S)", -1))
                
            ##############################################################

            # Calcul des points pour la course
            bonus = 0
            desc = ""
            ecuries = []
            for i in range(len(self.__course)):
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
                    desc = ("Participation (C)", bonus)

                self.__course[i].ajoutHistorique(desc)
                
                gt = self.__course[i].getGamertag()
                if gt in self.__dico:
                    self.__dico[gt] += bonus
                else:
                    self.__dico[gt] = bonus

                if self.__course[i].getEcurie() not in ecuries:
                    ecuries.append(self.__course[i].getEcurie())
                    self.__dico[gt] += 1
                    self.__course[i].ajoutHistorique(("Coequipier battu (C)", 1))

                # changement de position
                difference = 0
                if self.__estSprint:
                    reference = self.__sprint
                else:
                    reference = self.__qualif

                if self.__course[i] in reference:
                    j = 0
                    for j in range(len(reference)):
                        if reference[j] == self.__course[i]:
                            break
                    difference = j - i
                    if difference > 3:
                        difference = 3
                    if difference < -3:
                        difference = -3
                    self.__dico[gt] += difference
                    self.__course[i].ajoutHistorique(("Pos. (C)", difference))
                else:
                    print("GrandPrix.calcul.Erreur : un nouveau pilote apparait (err2).")

            for i in range(abandonsCourse):
                gt = self.__course[-(i+1)].getGamertag()
                self.__dico[gt] -= 1
            ##############################################################

        else:
            print("GrandPrix.calcul.Erreur : les sessions ne sont pas correctes.")

    def historique(self) -> None:
        for i in self.__qualif:
            print(i.getGamertag() + " : " + str(i.getHistorique()))

    def resetHistorique(self) -> None:
        for i in self.__dico:
            i.resetHistorique()