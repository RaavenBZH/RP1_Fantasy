import copy

"""
    Ce fichier fourni des méthodes utiles à l'application.

    Méthodes :

        - sortedDict(entree : dict) -> dict : permet de trier un dictionnaire selon ses valeurs.
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
    print(d1)
    print(d2)
    newDico = copy.deepcopy(d1)
    for i in d2:
        newDico[i] = d2[i]

    print(newDico)
    return newDico