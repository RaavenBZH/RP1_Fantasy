import copy

"""
    Ce fichier fournit des méthodes utiles à l'application.

    Méthodes :

        - sortedDict(entree : dict) -> dict : permet de trier un dictionnaire selon ses valeurs.
        - mergeDict(d1 : dict, d2 : dict) -> dict : permet de fusionner deux dictionnaires.
        - printd(dico : dict) : permet d'afficher un dictionnaire.
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