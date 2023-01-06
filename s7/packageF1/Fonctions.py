import copy
import csv

"""
    Ce fichier fournit des méthodes utiles à l'application.
"""

def sortedDict(entree) -> dict:
    """
    Permet de trier un dictionnaire selon ses valeurs.
    """

    newDico = {}
    dico = entree.copy()
    v = sorted(dico.values(), reverse = True)
    
    for i in range(len(v)):
        elem = v[i]
        for i in dico:
            if dico[i] == elem:
                newDico[i] = elem
                dico[i] = None

    return newDico

def mergeDict(d1, d2) -> dict:
    """
    Permet de fusionner deux dictionnaires.
    """

    newDico = None
    if (d1 != None and d2 != None):
        newDico = copy.deepcopy(d1)
        for i in d2:
            newDico[i] = d2[i]

    if (d1 == None and d2 != None):
        newDico = copy.deepcopy(d2)
    
    if (d1 != None and d2 == None):
        newDico = copy.deepcopy(d1)

    return newDico

def sumDict(d1, d2) -> dict:
    """
    Permet de sommer les valeurs de deux dictionnaires de forme {str : int}.
    """
    
    newDico = copy.deepcopy(d1)
    for i in d2:
        if i in newDico:
            newDico[i] += d2[i]
        else:
            newDico[i] = d2[i]

    return newDico


def printd(dico):
    """
    Permet d'afficher un dictionnaire.
    """
    print("{")
    count = 0
    loops = len(dico)
    for i in dico:
        print("\t" + str(i) + " : " + str(dico[i]), end="")
        count += 1
        if (loops != count):
            print(",")
    print("\n}")

def writeDriverStats(courses, mode, filename) -> None:

    pilotes = {}
    for course in courses:
        participants = course.getQualification()
        for pilote in participants:
            gt = pilote.getGamertagRemplacant()
            pilotes[gt] = pilote

    f = open('.\s7\stats_{}.csv'.format(filename), mode, newline="")
    writer = csv.writer(f)

    writer.writerow(["Pilote;Nombre;Top 15;Top 10;Poles;Best;Moyenne;Coequipier battu;Taux;Sprints;Top 8;Podiums;Victoires;Best;Moyenne;Coequipier battu;Taux;Nombre;Abandons;Fiabilite;Top 10;Podiums;Victoires;Best;Moyenne;Coequipier battu;Taux;Moy. Positions Gagnees"])

    for gt in pilotes:

        p = pilotes[gt]
        donnees = p.getDonnees()
        tabQ = donnees.tabQ()
        tabS = donnees.tabS()
        tabC = donnees.tabC()

        line = p.getGamertagRemplacant() + ";"

        line += "{};{};{};{};{};{};{};{};".format(
            donnees.nbQ(tabQ),
            donnees.nbQ2(tabQ),
            donnees.nbQ3(tabQ),
            donnees.nbPoles(tabQ),
            donnees.bestQ(tabQ),
            donnees.avgQ(tabQ),
            donnees.getCoeqBattuQ(),
            donnees.tauxCoeqBattuQ()
        )
        line += "{};{};{};{};{};{};{};{};".format(
            donnees.nbS(tabS),
            donnees.nbT8S(tabS),
            donnees.nbT3S(tabS),
            donnees.nbVicS(tabS),
            donnees.bestS(tabS),
            donnees.avgS(tabS),
            donnees.getCoeqBattuS(),
            donnees.tauxCoeqBattuS()
        )
        line += "{};{};{};{};{};{};{};{};{};{};{}".format(
            donnees.nbC(tabC),
            donnees.nbAbandons(),
            donnees.fiabilite(),
            donnees.nbT10C(tabC),
            donnees.nbT3C(tabC),
            donnees.nbVicC(tabC),
            donnees.bestC(tabC),
            donnees.avgC(tabC),
            donnees.getCoeqBattuC(),
            donnees.tauxCoeqBattuC(),
            donnees.moyPosGagnees()
        )

        writer.writerow([line])

    f.close()

def writeTeamStats(equipes, mode) -> None:
    f = open('.\s7\stats_equipes.csv', mode, newline="")
    writer = csv.writer(f)

    if mode == "w":
        writer.writerow(["Nom;Q_Nombre;Q_Top15;Q_Top10;Q_Poles;Q_Meilleur;Q_Moyenne;S_Nombre;S_Top8;S_Podiums;S_Victoires;S_Meilleur;S_Moyenne;C_Nombre;C_Abandons;C_Top10;C_Podiums;C_Victoires;C_Meilleur;C_Moyenne"])
    else:
        writer.writerow([])

    for e in equipes:

        nom = e.getNom()
        donnees = e.getDonnees()
        tabQ = donnees.tabQ()
        tabS = donnees.tabS()
        tabC = donnees.tabC()

        line = nom + ";"

        line += "{};{};{};{};{};{};".format(
            donnees.nbQ(tabQ),
            donnees.nbQ2(tabQ),
            donnees.nbQ3(tabQ),
            donnees.nbPoles(tabQ),
            donnees.bestQ(tabQ),
            donnees.avgQ(tabQ)
        )
        line += "{};{};{};{};{};{};".format(
            donnees.nbS(tabS),
            donnees.nbT8S(tabS),
            donnees.nbT3S(tabS),
            donnees.nbVicS(tabS),
            donnees.bestS(tabS),
            donnees.avgS(tabS)
        )
        line += "{};{};{};{};{};{};{}".format(
            donnees.nbC(tabC),
            donnees.nbAbandons(),
            donnees.nbT10C(tabC),
            donnees.nbT3C(tabC),
            donnees.nbVicC(tabC),
            donnees.bestC(tabC),
            donnees.avgC(tabC)
        )

        writer.writerow([line])

    f.close()