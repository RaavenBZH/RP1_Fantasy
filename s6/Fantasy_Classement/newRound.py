###################################################################################################
# Course 8

result08 = GrandPrix("Italie")

qualif08 = [
]

course08 = [
]

# classements
result08.resultat("q", qualif08)
result08.resultat("c", course08)

result08.calcPointsQ()
result08.calcPointsC()

# evenements ponctuels

result08.meilleurTour()

# final
pt08 = result08.getPoints()

"""
print(sortedDict(result08.getPoints()))

for i in result08.getCourse():
	print(i.getGamertag(), i.getHistorique())
"""

# Ideal :

result08.resetHist()
