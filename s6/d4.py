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

    pur_ultraaa = Pilote("PuR Ultraaa", "AlphaTauri")
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
        pur_ultraaa
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
        pur_ultraaa,
        rp1_lito
    ]

    # classements
    result01.resultat("q", qualif01)
    result01.resultat("c", course01)

    result01.calcPointsQ()
    result01.calcPointsC()

    # évènements ponctuels
    result01.crash("q", pur_ultraaa)
    result01.crash("q", rp1_owain)

    result01.crash("c", rp1_lito)
    result01.crash("c", pur_ultraaa)
    result01.crash("c", yozana)
    result01.crash("c", non4me_jordy)
    
    result01.meilleurTour(jancker21)

    # final
    pt01 = result01.getPoints()

    """
    print(sortedDict(result01.getPoints()))

    for i in result01.getCourse():
        print(i.getGamertag(), i.getHistorique())
    """
    
    # Ideal : Non4me Pagaa, RP1 Owain, ERT Ricky

    result01.resetHist()

    ###################################################################################################
    # Course 2

    result02 = GrandPrix("Chine")

    qualif02 = [
        rp1_owain,
        non4me_livai,
        yozana,
        playnum11,
        rp1_ice,
        ert_redevils,
        non4me_jordy,
        pur_ultraaa,
        non4me_pagaa,
        ert_tiiste,
        ltr_coach,
        tx3_soap,
        jancker21,
        rp1_lito,
        ert_iquazz,
        rp1_durtom,
        ert_ricky,
        alexsch71,
        rp1_fifou,
        is_honoka
    ]

    course02 = [
        rp1_owain,
        yozana,
        pur_ultraaa,
        playnum11,
        ltr_coach,
        ert_tiiste,
        non4me_jordy,
        non4me_pagaa,
        rp1_ice,
        ert_iquazz,
        rp1_lito,
        rp1_durtom,
        non4me_livai,
        alexsch71,
        ert_redevils,
        ert_ricky,
        rp1_fifou,
        jancker21,
        is_honoka,
        tx3_soap
    ]

    # classements
    result02.resultat("q", qualif02)
    result02.resultat("c", course02)

    result02.calcPointsQ()
    result02.calcPointsC()

    # évènements ponctuels
    result02.crash("q", tx3_soap)

    result02.crash("c", tx3_soap)
    result02.crash("c", is_honoka)

    result02.meilleurTour(rp1_durtom)

    # final 
    pt02 = result02.getPoints()

    """
    print(sortedDict(result02.getPoints()))
    
    for i in result02.getCourse():
        print(i.getGamertag(), i.getHistorique())
    """
    
    # Ideal : ERT iQuaZz, LTR Coach, PuR Ultraaa

    ###################################################################################################
    
    final = sumDict(pt01, pt02)
    
    # print(final)

    return final