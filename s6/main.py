from packageF1.Pilote import *
from packageF1.fonctions import *
from packageF1.Joueur import *
from packageF1.EnsembleJoueur import *
from packageF1.fonctions import *

from d1 import *
from d2 import *
from d3 import *
from d4 import *

### Récupération des points des 4 divisons ########################################################

d1, d2, d3, d4 = getPointsD1(), getPointsD2(), getPointsD3(), getPointsD4() # points de chaque div
totalPoints = fusionDico(fusionDico(fusionDico(d1, d2), d3), d4) # fusion de toutes les div

### Création du classement ########################################################################

# récupère les données
infosJoueurs = lecture()[1:] # récupère les équipes des joueurs
joueurs = EnsembleJoueur() # traite et opère

# infos vers un objet EnsembleJoueur
for i in range(len(infosJoueurs)):
    d = infosJoueurs[i][0] # discord
    j = Joueur(d) # joueur
    e = infosJoueurs[i][1:13] # equipe de pilotes
    j.ajoutEquipe(e)
    joueurs.addJoueur(j)

# update et création du classement
joueurs.update(totalPoints) # update les points
classementTemporaire = joueurs.getListeJoueurs() # récupération du dictionnaire des pilotes
classementFinal = {}

# écriture des points associés aux joueurs
for i in classementTemporaire:
    classementFinal[i.getDiscord()] = str(i.calculeScore())

classementFinal = triParValeur(classementFinal) # tri du classement

### Ecriture ######################################################################################

ecritureSortie(classementFinal)

###################################################################################################