'''
    Ce fichier fourni des méthodes utiles à l'application.

    Méthodes :

        - sortedDict(entree : dict) -> dict : permet de trier un dictionnaire selon ses valeurs.
'''

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