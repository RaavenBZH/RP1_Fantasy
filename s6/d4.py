from unittest import result
from packageF1.Pilote import *
from packageF1.GrandPrix import *
from packageF1.Joueur import *
from packageF1.EnsembleJoueur import *
from packageF1.fonctions import *

#
# Saison 6
#
# Calcul des points pour les pilotes de division 4
#

def getPointsD4() -> dict:

    ###################################################################################################

    # Création des pilotes

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    non4me_pagaa = Pilote("Non4me Pagaa", "Mercedes")
    rp1_ice = Pilote("RP1 Ice", "Mercedes")

    non4me_jordy = Pilote("Non4me Jordy", "RedBull")
    ert_redevils = Pilote("ERT Redevils", "RedBull")

    ltr_coach = Pilote("LTR Coach", "McLaren")
    rp1_fifou = Pilote("RP1 Fifou", "McLaren")

    yozana = Pilote("Yozana", "Ferrari")
    non4me_livai = Pilote("Non4me Livai", "Ferrari")

    xrt_aots = Pilote("XRT Aots", "AlphaTauri")
    rp1_lito = Pilote("RP1 Lito", "AlphaTauri")

    alexsch71 = Pilote("AlexSCH71", "Alpine")
    playnum11 = Pilote("Playnum11", "Alpine")

    rp1_durtom = Pilote("RP1 Durtom", "AstonMartin")
    jancker21 = Pilote("Jancker21", "AstonMartin")

    rp1_owain = Pilote("RP1 Owain", "AlfaRomeo")
    ert_tiiste = Pilote("ERT Tiiste", "AlfaRomeo")

    ert_iquazz = Pilote("ERT iQuaZz", "Williams") 
    ert_ricky = Pilote("ERT Ricky", "Williams")

    tx3_soap = Pilote("TX3 Soap", "Haas") 
    is_honoka = Pilote("IS Honoka", "Haas")

    ###################################################################################################

    # Course 1

    result01 = GrandPrix("Autriche")

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    qualif01 = [
        rp1_ice,
        rp1_durtom,
        ert_redevils,
        ltr_coach,
        yozana,
        tx3_soap, # remplacé par PuR Ultraaa
        alexsch71,
        non4me_pagaa,
        ert_tiiste,
        non4me_livai,
        non4me_jordy,
        playnum11,
        jancker21,
        rp1_lito,
        rp1_owain,
        ert_iquazz, # remplacé par NxS xTiga
        ert_ricky,
        rp1_fifou,
        is_honoka,
        xrt_aots
    ]

    course01 = [
        rp1_durtom,
        non4me_pagaa,
        rp1_owain,
        non4me_jordy,
        tx3_soap, # remplacé par PuR Ultraaa
        ert_tiiste,
        ert_ricky,
        rp1_ice,
        ltr_coach,
        alexsch71,
        ert_iquazz, # remplacé par NxS xTiga
        rp1_fifou,
        playnum11,
        jancker21,
        ert_redevils,
        is_honoka,
        non4me_livai,
        yozana,
        xrt_aots,
        rp1_lito
    ]

    # classements
    result01.resultat("q", qualif01)
    result01.resultat("c", course01)

    result01.calcPointsQ()
    result01.calcPointsC()

    # évènements ponctuels
    result01.crash("q", xrt_aots)
    result01.crash("q", rp1_owain)

    result01.crash("c", rp1_lito)
    result01.crash("c", xrt_aots)
    result01.crash("c", yozana)
    result01.crash("c", non4me_jordy)
    
    result01.meilleurTour(jancker21)

    """
    for i in result01.getCourse():
        if i.getGamertag() == "ERT iQuaZz":
            print(i.getHistorique())
    """
    
    return result01.getPoints()
