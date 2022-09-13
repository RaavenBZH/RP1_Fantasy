### Saison 7 - RP1 ################################################################################

# Importation des modules #########################################################################

import pandas as pd

from packageF1.Pilote import *
from packageF1.GrandPrix import *
from packageF1.Fonctions import *

from d1 import *
from d2 import *
from d3 import *
from d4 import *

# Importation des équipes des joueurs #############################################################

entrees = pd.read_excel(r'./s7/entrees.xlsx').values.tolist()

### Récupération des points des 4 divisons ########################################################

d1, d2, d3, d4 = {}, {}, {}, {}

d1 = getPointsD1()
d2 = getPointsD2()
d3 = getPointsD3()
d4 = getPointsD4()

totalPoints = sortedDict(mergeDict(mergeDict(mergeDict(d1, d2), d3), d4)) # fusion de toutes les div

# Programme principal #############################################################################
