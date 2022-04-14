import csv
from encodings import utf_8

def sortedDict(dico) -> dict:
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

def input() -> list:
    '''
    Permet de lire le fichier en entrée.
    '''

    theFile = open('entrees_rp1.csv')
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

    f = open('sorties_rp1.csv', 'w', newline="")
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
