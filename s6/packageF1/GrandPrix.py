from packageF1.Pilote import *

class GrandPrix:
    '''
    Cette classe mémorise le résultat d'un grand prix.

    Attributs : 
        - __dico (dict <Pilote : int>) : les points pour chaque pilote.
        - __circuit (str) : le circuit du grand prix.
        - __qualif (list <Pilote>) : le classement de la qualification.
        - __course (list <Pilote>) : le classement de la course.

    Méthodes :
        - __init__(circuit : str) -> None : construit les objets <GrandPrix>.
        - __str__() -> str : affiche les résultats d'un grand prix.
        - getCircuit() -> str : recupère le circuit.
        - getQualification() -> str : récupère le classement de la qualification.
        - getCourse() -> str : récupère le classement de la course.
        - resultat(mode : str, resultat : list <Pilote>) -> None : enregistre un résultat de session.
        - calcPointsQ() -> None : calcule les points selon la qualification.
        - calcPointsC() -> None : calcule les points selon la course.
        - crash(mode : str, gamertag : str) -> None : retire des points au pilote s'étant crash.
        - meileurTour(gamertag : str) -> None : attribue un bonus pour le meilleur tour.
    ''' 

    def __init__(self, circuit : str) -> None:

        self.__dico = {}
        self.__circuit = None
        self.__qualif = None
        self.__course = None

        listeCircuits = [
            'Barhein',
            'Imola',
            'Portugal',
            'Espagne',
            'Monaco',
            'Azerbaidjan',
            'Montreal',
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
            'Melbourne',
            'Jeddah',
            'AbuDhabi',
            'Shanghai'
        ]
        if circuit in listeCircuits:
            self.__circuit = circuit
        else:
            print("GrandPrix.Erreur : circuit invalide.")

    def __str__(self) -> str:
        affichage = "Grand Prix de " + self.__circuit + " :\n"
        affichage += "\tRésultat de la qualification :\n"
        for i in range(1,21):
            try:
                affichage += "\t\t" + str(i) + " : " + self.__qualif[i-1].getGamertag() + "\n"
            except:
                break
        affichage += "\n"
        affichage += "\tRésultat de la course :\n"
        for i in range(1,21):
            try:
                affichage += "\t\t" + str(i) + " : " + self.__course[i-1].getGamertag() + "\n"
            except:
                break
        return affichage

    def getCircuit(self) -> str:
        return self.__circuit

    def getQualification(self) -> str:
        return self.__qualif

    def getCourse(self) -> str:
        return self.__course

    def getPoints(self) -> dict:
        return self.__dico

    def resultat(self, mode : str, resultat : list) -> None:
        
        if mode in ("q", "c"):
            estValide = True
            if len(resultat) <= 0:
                estValide = False
            else:
                a = Pilote("a", "Mercedes")
                for i in resultat:
                    if type(i) != type(a):
                        estValide = False
            if estValide:
                if mode == "q":
                    self.__qualif = resultat
                elif mode == "c":
                    self.__course = resultat
                else:
                    print("GrandPrix.resultat.Erreur : mode invalide.")
            else:
                print("GrandPrix.resultat.Erreur : résultat invalide.")
        else:
            print("GrandPrix.resultat.Erreur : mode {'q','c'} invalide.")

    def calcPointsQ(self) -> None:

        # Calcul qualif
        memo = []
        for i in range(len(self.__qualif)):

            p = self.__qualif[i] # pilote
            e = p.getEcurie() # son écurie

            # Passage en Q2 & Q3
            bonus = 1

            if i < 1:
                bonus = 5
                p.addAction(("Pole", 2))
                p.addAction(("Q3", 3))
            elif i < 10:
                bonus = 3
                p.addAction(("Q3", 3))
            elif i < 15:
                bonus = 2
                p.addAction(("Q2", 2))
            else:
                p.addAction(("Q1", 1))

            # Vs coéquipier
            if e not in memo:
                bonus += 2
                memo.append(e)
                p.addAction(("Coequipier battu (Q)", 2))
            
            # Ajout du bonus
            try:
                self.__dico[p.getGamertag()] += bonus
            except:
                try:
                    self.__dico[p.getGamertag()] = bonus
                except:
                    print("GrandPrix.calcPointsQ.Erreur : erreur inconnue.")
                    break

    def calcPointsC(self) -> None:

        # Calcul course
        memo = []
        for i in range(len(self.__course)):

            p1 = self.__course[i] # pilote
            e = p1.getEcurie() # son écurie
            p1.addAction(("Course terminee", 1))

            # Course terminée
            bonus = 1
            
            # Bonus fin de course
            if i < 1:
                bonus = 4
                p1.addAction(("Victoire", 3))
            elif i < 6:
                bonus = 3
                p1.addAction(("Top 6", 2))
            elif i < 10:
                bonus = 2
                p1.addAction(("Top 10", 1))

            
            # Vs coéquipier
            if e not in memo:
                bonus += 3
                memo.append(e)
                p1.addAction(("Coequipier battu (C)", 3))

            # Différence position
            difference = None
            for j in range(len(self.__qualif)):

                p2 = self.__qualif[j]
                if p2 == p1:
                    difference = j-i
                    code = str("Pos. "+ str(difference))
            
            difference *= 2
            while abs(difference) > 10:
                if difference < -10:
                    difference += 1
                elif difference > 10:
                    difference -= 1
            bonus += difference
            p1.addAction((code,difference))

            try:
                self.__dico[p1.getGamertag()] += bonus
            except:
                try:
                    self.__dico[p1.getGamertag()] = bonus
                except:
                    print("GrandPrix.calcPointsC.Erreur : erreur inconnue.")
                    break
        
    def crash(self, mode : str, gamertag : str) -> None:
        if mode in ("q", "c"):
            if mode == "q":
                value = 5
                for i in self.__qualif:
                    if i.getGamertag() == gamertag:
                        i.addAction(("Crash (Q)", -5))
                        break
            elif mode == "c":
                value = 6
                for i in self.__course:
                    if i.getGamertag() == gamertag:
                        i.addAction(("Crash (C)", -5))
                        i.removeAction(("Course terminee", 1))
                        break
            else:
                print("GrandPrix.crash.Erreur : mode invalide.")
                value = 0

            try:
                self.__dico[gamertag] -= value
            except:
                print("GrandPrix.crash.Erreur : pilote non trouvé.")
        else:
            print("GrandPrix.crash.Erreur : mode {'q','c'} invalide.")

    def meilleurTour(self, gamertag : str) -> None:
        try:
            self.__dico[gamertag] += 2
            for p in self.__course:
                if p.getGamertag() == gamertag:
                    p.addAction(("FL", 2))

        except:
            print("GrandPrix.meilleurTour.Erreur : pilote non trouvé.")