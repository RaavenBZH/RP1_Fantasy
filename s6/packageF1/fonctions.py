import csv

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
