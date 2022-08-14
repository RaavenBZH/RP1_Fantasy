### Saison 7 - RP1 ################################################################################

# Importation des modules #########################################################################

import pandas as pd

from packageF1 import *

# Importation des équipes des joueurs #############################################################

out = pd.read_excel(r'C:\Users\emali\OneDrive\Documents\Work\Perso\Projets\RP1\RP1_Fantasy\s6\entrees_rp1.xlsx').drop(columns="Horodateur")

# Traitement des équipes des joueurs ##############################################################

joueurs = out.values.tolist()

for i in range(len(joueurs)):
    for j in range(len(joueurs[i])):
        for k in range(len(joueurs[i][j])):
            if joueurs[i][j][k] == "(":
                joueurs[i][j] = (joueurs[i][j])[:k-1]
                break

print(joueurs)