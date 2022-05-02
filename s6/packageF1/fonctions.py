import csv

def sortedDict(entree) -> dict:
    '''
    Permet de trier un dictionnaire selon ses valeurs.
    '''

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

def mergeDict(dico1 : dict, dico2 : dict) -> None:
    '''
    Permet de fusionner deux dictionnaires aux clés strictements différentes.
    '''

    newDico = dico1.copy()

    for i in dico2:
        if i == None:
            print("mergeDict.Erreur : element nul.")
            return -1
        if i in newDico:
            print("mergeDict.Erreur : element commun.")
            return -1
        else:
            newDico[i] = dico2[i]

    return newDico

def sumDict(dico1 : dict, dico2 : dict) -> dict:
    '''
    Permet d'ajouter à un dictionnaire les valeurs d'un autre. Les clés des deux dictionnaires sont les mêmes.
    '''

    dico = dico1.copy()

    for i in dico2 :
        try:
            dico[i] = dico1[i] + dico2[i]
        except:
            print("nouvelle clé :", i)
            dico[i] = dico2[i]

    if len(dico) != max(len(dico1), len(dico2)):
        print("Le dicitonnaire de retour a une taille non maximale.")

    return dico

def input() -> list:
    '''
    Permet de lire le fichier en entrée.
    '''

    theFile = open('GitHub\entrees_rp1.csv')
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

def output(classement : dict, equipes : dict = {}) -> None:
    '''
    Permet d'écrire le classement dans un fichier csv.
    '''

    f = open('GitHub\sorties_rp1.csv', 'w', newline="")
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

def generateRound(roundNum : int, track : str = "") -> None:
    '''
    Génère le corps du code pour une manche.
    '''
    f = open("newRound.py", "w")
    w = f.write

    if roundNum < 1:
        w("# Error.generateRound : inférieur à 0.")

    elif roundNum < 10:
        num = "0"+str(roundNum)

        w("###################################################################################################\n")
        w(f"# Course {str(roundNum)}\n")
        w("\n")
        w(f"result03 = GrandPrix(\"{track}\")\n")
        w("\n")
        w(f"qualif{num} = [\n]\n")
        w("\n")
        w(f"course{num} = [\n]\n")
        w("\n")
        w("# classements\n")
        w(f"result{num}.resultat(\"q\", qualif{num})\n")
        w(f"result{num}.resultat(\"q\", course{num}\n")
        w("\n")
        w(f"result{num}.calcPointsQ()\n")
        w(f"result{num}.calcPointsC()\n")
        w("\n")
        w("# évènements ponctuels\n")
        w("\n")
        w(f"result{num}.meilleurTour()\n")
        w("\n")
        w("# final\n")
        w(f"pt{num} = result{num}.getPoints()\n")
        w("\n")
        w("\"\"\"\n")
        w(f"print(sortedDict(result{num}.getPoints()))\n")
        w("\n")
        w(f"for i in result{num}.getCourse():\n")
        w("\tprint(i.getGamertag(), i.getHistorique())\n")
        w("\"\"\"\n")
        w("\n")
        w("# Ideal :\n")
        w("\n")
        w(f"result{num}.resetHist()")
        w("\n")
