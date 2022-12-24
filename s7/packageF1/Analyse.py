from packageF1.Fonctions import *

class Analyse:

    def __init__(self):
        self.__qualif = {}
        self.__sprint = {}
        self.__course = {}

    def getQualif(self) -> None:
        return self.__qualif

    def getSprint(self) -> None:
        return self.__sprint

    def getCourse(self) -> None:
        return self.__course

    def analyse(self, gp):

        sessions = [gp.getQualification(), gp.getCourse()]
        if gp.estSprint() == True:
            sessions.append(gp.getSprint())
        
        for session in sessions:

            if session == gp.getQualification():
                seance = self.__qualif
            
            if session == gp.getSprint():
                seance = self.__sprint

            if session == gp.getCourse():
                seance = self.__course

            compos = {}

            for pilote in session:
                nom = pilote.getEcurie().getNom()
                gt = pilote.getGamertagRemplacant()
                if nom not in compos.keys():
                    compos[nom] = gt
                else:
                    compos[nom] = compos[nom] + "_" + gt

            for i in compos.values():
                pilotes = i.split("_")
                pilotes_s = sorted(pilotes)
                key = pilotes_s[0] + "_" + pilotes_s[1]
                keys = list(seance.keys())

                if key not in keys:
                    if pilotes_s[0] == pilotes[0]:
                        seance[key] = [1,0]   
                    else:
                        seance[key] = [0,1]
                
                else:
                    if pilotes_s[0] == pilotes[0]:
                        seance[key][0] += 1
                    else:
                        seance[key][1] += 1