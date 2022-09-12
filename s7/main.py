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

out = pd.read_excel(r'./s7/entrees.xlsx') # .drop(columns="Horodateur")
joueurs = out.values.tolist()

print(joueurs)

### Récupération des points des 4 divisons ########################################################

d1, d2, d3, d4 = {}, {}, {}, {}

d1 = getPointsD1()
d2 = getPointsD2()
d3 = getPointsD3()
d4 = getPointsD4()

print(">>>")
totalPoints = mergeDict(mergeDict(mergeDict(d1, d2), d3), d4) # fusion de toutes les div

# Programme principal #############################################################################
"""
Mercedes = Ecurie("Mercedes")
RedBull = Ecurie("RedBull")
Ferrari = Ecurie("Ferrari")
McLaren = Ecurie("McLaren")
Alpine = Ecurie("Alpine")
AlphaTauri = Ecurie("AlphaTauri")
AstonMartin = Ecurie("AstonMartin")
Williams = Ecurie("Williams")
AlfaRomeo = Ecurie("AlfaRomeo")
Haas = Ecurie("Haas")

A = Pilote("A", Mercedes)
B = Pilote("B", RedBull)
C = Pilote("C", Ferrari)
D = Pilote("D", McLaren)
E = Pilote("E", Alpine)
F = Pilote("F", AlphaTauri)
G = Pilote("G", AstonMartin)
H = Pilote("H", Williams)
I = Pilote("I", AlfaRomeo)
J = Pilote("J", Haas)
K = Pilote("K", Mercedes)
L = Pilote("L", RedBull)
M = Pilote("M", Ferrari)
N = Pilote("N", McLaren)
O = Pilote("O", Alpine)
P = Pilote("P", AlphaTauri)
Q = Pilote("Q", AstonMartin)
R = Pilote("R", Williams)
S = Pilote("S", AlfaRomeo)
T = Pilote("T", Haas)

c01 = GrandPrix("Australie", sprint = True)

q = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T]
s = [E, N, P, S, F, L, B, H, G, J, D, Q, M, A, T, I, K, O, R, C]
c = [R, N, L, O, P, A, I, J, Q, D, H, E, S, T, K, C, F, B, G, M]

# teste toutes les méthodes

c01.setQualification(q)
c01.setSprint(s)
c01.setCourse(c)
c01.calcul(absentsQualif=3, absentsSprint=3, abandonsSprint=2, absentsCourse=3, abandonsCourse=1)

"""

