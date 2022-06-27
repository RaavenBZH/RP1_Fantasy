###################################################################################################
# Course 9

result09 = GrandPrix("Barhein")

qualif09 = [
]

course09 = [
]

# classements
result09.resultat("q", qualif09)
result09.resultat("c", course09)

result09.calcPointsQ()
result09.calcPointsC()

# evenements ponctuels

result09.meilleurTour()

# final
pt09 = result09.getPoints()

"""
print(sortedDict(result09.getPoints()))

for i in result09.getCourse():
	print(i.getGamertag(), i.getHistorique())
"""

# Ideal :

result09.resetHist()
