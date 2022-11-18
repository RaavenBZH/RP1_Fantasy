### Saison 7 - RP1 ################################################################################

# Importation des modules #########################################################################

import pandas as pd
import csv

from packageF1.EnsembleJoueur import *
from packageF1.Fonctions import *
from packageF1.GrandPrix import *
from packageF1.Joueur import *
from packageF1.Pilote import *

from d1 import *
from d2 import *
from d3 import *
from d4 import *

# Importation des équipes des joueurs #############################################################

out = pd.read_excel(r'./s7/entrees.xlsx')
entrees = out.values.tolist()

# Traitement du fichier d'entrees #################################################################

rp1_fantasy = EnsembleJoueur()
for i in entrees:
    joueur = Joueur(i[0])
    joueur.addEquipe([j for j in i[1:]])
    rp1_fantasy.add(joueur)

# Récupération des points des 4 divisons ##########################################################

d1, d2, d3, d4 = {}, {}, {}, {}

stats = True

d1 = getPointsD1(stats)
d2 = getPointsD2(stats)
d3 = getPointsD3(stats)
d4 = getPointsD4(stats)

total = sortedDict(mergeDict(mergeDict(mergeDict(d1, d2), d3), d4)) # fusion de toutes les div

# Traitement du classement ########################################################################

classement = {}

rp1_fantasy.update(total)
for i in rp1_fantasy.getListeJoueurs():
    classement[i.getDiscord()] = i.calcScore()

classement = sortedDict(classement)
# printd(classement)

# Ecriture du fichier de sortie ###################################################################

f = open('.\s7\sorties.csv', 'w', newline="")
writer = csv.writer(f)

for i in classement:

    discord = i
    score = classement[i]
    line = discord+";"+str(score)+";"
    equipe = {}

    # recherche de l'équipe du joueur
    for e in rp1_fantasy.getListeJoueurs():
        if e.getDiscord() == discord:
            equipe = e.getEquipe()
            break
    
    for i in equipe:
        line += i + ";" + str(equipe[i]) + ";"

    writer.writerow([line[:-1]])

f.close()

###################################################################################################