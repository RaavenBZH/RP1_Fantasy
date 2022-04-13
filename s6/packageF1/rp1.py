import csv

###################################################################################################

class Pilote:
    '''
    Cette classe simule un pilote.

    Attributs :
        - __gamertag (str) : le gamertag du pilote.
        - __ecurie (str) : l'écurie du pilote.
        - __historique (list) : l'historique des actions d'un pilote

    Méthodes :
        - __init__(gamertag : str, ecurie : str) -> None : construit les objets <Pilote>.
        - getGamertag() -> str : récupère le gamertag.
        - getEcurie() -> str : récupère l'écurie.
        - setEcurie(ecurie : str) -> None : modifie l'écurie.
        - addAction(desc : str) -> None : ajoute la description des bonus à l'historique.
        - resetHistorique() -> None : efface l'historique.
        - getHistorique() -> list : permet de récupérer l'historique.
    ''' 

    def __init__(self, gamertag : str, ecurie : str) -> None:

        self.__gamertag = None
        self.__ecurie = None
        self.__historique = []
        
        listeEcuries = ["Mercedes", "RedBull", "Ferrari", "McLaren", "Alpine", "AlphaTauri", "AstonMartin", "Williams", "AlfaRomeo", "Haas", None]
        if ecurie in listeEcuries:
            self.__gamertag = gamertag
            self.__ecurie = ecurie
        else:
            print("Pilote.Erreur : écurie invalide.")

    def getGamertag(self) -> str:
        return self.__gamertag

    def getEcurie(self) -> str: 
        return self.__ecurie

    def setEcurie(self, ecurie : str) -> None:
        listeEcuries = ["Mercedes", "RedBull", "Ferrari", "McLaren", "Alpine", "AlphaTauri", "AstonMartin", "Williams", "AlfaRomeo", "Haas", None]
        if ecurie in listeEcuries:
            self.__ecurie = ecurie
        else:
            print("Pilote.setEcurie.Erreur : paramètre invalide.")

    def addAction(self, desc : tuple) -> None:
        self.__historique.append(desc)

    def removeAction(self, desc : tuple) -> None:
        for i in self.__historique:
            if i == desc:
                self.__historique.remove(i)
                break

    def resetHistorique(self) -> None:
        self.__historique = []

    def getHistorique(self) -> list:
        return self.__historique

###################################################################################################

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
        - calculePointsQ() -> None : calcule les points selon la qualification.
        - calculePointsC() -> None : calcule les points selon la course.
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
            'Shanghai',
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

    def calculePointsQ(self) -> None:

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
                    print("GrandPrix.calculePointsQ.Erreur : erreur inconnue.")
                    break

    def calculePointsC(self) -> None:

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
                    print("GrandPrix.calculePointsC.Erreur : erreur inconnue.")
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

###################################################################################################

class Joueur():
    '''
    Cette classe simule les choix d'un joueur et calcule ses points.

    Attributs :
        - __equipe (dict<str : int>) : l'équipe du joueur et points associés.
        - __discord (str) : le discord du joueur.

    Méthodes :
        - __init__(discord : str) -> None : construit les objets <Joueur>.
        - getEquipe() -> str : récupère l'équipe du joueur.
        - getDiscord() -> str : récupère le discord du joueur.
        - ajoutEquipe(listePilotes : list<str>) -> None : ajoute l'équipe de pilotes représentés par leur gamertag.
        - updatePoints(generalPoints : dict<str : int>) -> None : actualise les points de l'équipe du joueur.
        - calculeScore() -> int : calcule et renvoie le score du joueur.
    '''

    def __init__(self, discord : str) -> None:
        self.__equipe = {}
        self.__discord = discord
                         
    def getEquipe(self) -> str:
        return self.__equipe

    def getDiscord(self) -> str:
        return self.__discord

    def ajoutEquipe(self, listePilotes : list) -> None:
        if len(listePilotes)%3 == 0:
            for i in listePilotes:
                self.__equipe[i] = 0
        else:
            print("Pilote.ajoutEquipe.Erreur : listePilote fausse.")

    def updatePoints(self, generalPoints : dict) -> None:
        for i in self.__equipe:
            try:
                self.__equipe[i] = generalPoints[i]
            except:
                pass

    def calculeScore(self) -> int: 
        liste = [i for i in self.__equipe.values()]
        for i in range(len(liste)):
            if i%3 == 0:
                liste[i] *= 2
        return sum(liste)

###################################################################################################

class EnsembleJoueur():
    '''
    Cette classe regroupe tous les participants au jeu.

    Attributs :
        - __listeJoueurs (list<Joueur>) -> None : liste des participants.

    Méthodes :
        - __init__(str) -> None : construit les objets <EnsembleJoueur>.
        - __str__() -> str : affiche le score de chaque joueurs.
        - getListeJoueurs() -> list<Joueur> : récupère la liste des joueurs.
        - addJoueur(j : Joueur) -> None : ajoute un joueur dans la liste.
        - update(generalPoints : dict<str : int>) -> None : actualise les points de chaque joueur.
    '''

    def __init__(self) -> None:
        self.__listeJoueurs = []

    def __str__(self) -> str:
        affichage = "Classement : \n"
        for i in self.__listeJoueurs:
            affichage += i.getDiscord() + " : " + str(i.calculeScore()) + "\n"
        return affichage[:-1]

    def getListeJoueurs(self):
        return self.__listeJoueurs

    def addJoueur(self, j : Joueur) -> None:
        self.__listeJoueurs.append(j)

    def update(self, generalPoints : dict) -> None:
        for i in self.__listeJoueurs:
            i.updatePoints(generalPoints)    
    
###################################################################################################

def triParValeur(dico) -> dict:
    '''
    Permet de trier un dictionnaire selon ses valeurs.
    '''

    newDico = {}
    v = sorted(dico.values(), reverse = True)
    
    for i in range(len(v)):
        elem = v[i]
        for i in dico:
            if dico[i] == elem:
                newDico[i] = elem
                dico[i] = None
    return newDico

def fusionDico(dico1 : dict, dico2 : dict) -> None:
    '''
    Permet de fusionner deux dictionnaires aux clés strictements différentes.
    '''

    newDico = {}

    for i in dico1:
        if i in newDico:
            print("Elément commun.")
            return -1
        else:
            newDico[i] = dico1[i]

    for i in dico2:
        if i in newDico:
            print("Elément commun.")
            return -1
        else:
            newDico[i] = dico2[i]

    return newDico

def lecture() -> list:
    '''
    Permet de lire le fichier en entrée.
    '''

    theFile = open(r'C:\Users\emali\OneDrive\Documents\Work\Perso\Projets\RP1\entrees_rp1.csv')
    theReader = csv.reader(theFile)

    # Récupération des lignes
    rows=[]
    for row in theReader:
        rows.append(row)

    # Exclusion des ";" en trop (dernières lignes)
    traitement1 = []
    for line in rows:
        theLine = line[0]
        if theLine[0] != ";":
            traitement1.append(theLine)

    # Séparations des colonnes délimitées par des ";"
    traitement2 = []
    for i in traitement1:
        traitement2.append(i.split(";"))

    # Suppression des colonnes vides
    for i in range(len(traitement2)):
        for j in range(6):
            traitement2[i].pop(-1)
        traitement2[i].pop(0)

    # Suppression de l'affichage des équipes des pilotes.
    for i in range(len(traitement2)):
        for j in range(len(traitement2[i])):
            cell = traitement2[i][j]
            for k in range(len(cell)):
                if cell[k] == "(":
                    cell = cell[:k-1]
                    break
            traitement2[i][j] = cell

    # traitement2 prêt...

    return traitement2

def ecritureSortie(classement : dict, equipes : dict = {}) -> None:
    '''
    Permet d'écrire dans un fichier csv le classement
    '''

    f = open(r'C:\Users\emali\OneDrive\Documents\Work\Perso\Projets\RP1\sorties_rp1.csv', 'w', newline="")
    writer = csv.writer(f)

    for i in classement:

        d = i
        score = classement[i]
        line = d+";"+str(score)+";"
        equipe = {}

        # recherche de l'équipe du joueur d
        for e in equipes:
            if e.getDiscord() == d:
                equipe = e.getEquipe()
                break
        
        for i in equipe:
            line += i + ";" + str(equipe[i]) + ";"

        writer.writerow([line[:-1]])
