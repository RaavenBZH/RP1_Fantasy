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

    non4me_sanzz = Pilote("Non4me Sanzz", "Alpine")
    xrt_alpha = Pilote("XRT Alpha", "Alpine")

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
        non4me_sanzz,
        non4me_pagaa,
        ert_tiiste,
        non4me_livai,
        non4me_jordy,
        xrt_alpha,
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
        non4me_sanzz,
        ert_iquazz, # remplacé par NxS xTiga
        rp1_fifou,
        xrt_alpha,
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
        xrt_alpha,
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
        non4me_sanzz,
        rp1_fifou,
        is_honoka
    ]

    course02 = [
        rp1_owain,
        yozana,
        pur_ultraaa,
        xrt_alpha,
        ltr_coach,
        ert_tiiste,
        non4me_jordy,
        non4me_pagaa,
        rp1_ice,
        ert_iquazz,
        rp1_lito,
        rp1_durtom,
        non4me_livai,
        non4me_sanzz,
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

    result02.resetHist()

    ###################################################################################################
    # Course 3

    result03 = GrandPrix("Imola")

    qualif03 = [
        ltr_coach,
        non4me_pagaa,
        rp1_ice,
        xrt_alpha, # remplacé par X7PK KaranoX
        ert_iquazz,
        ert_ricky,
        non4me_livai,
        tx3_soap,
        ert_tiiste,
        yozana,
        rp1_fifou,
        is_honoka,
        rp1_lito,
        rp1_durtom,
        rp1_owain,
        non4me_jordy,
        pur_ultraaa,
        jancker21,
        non4me_sanzz, # remplacé par NathanHrx
        ert_redevils        
    ]

    course03 = [
        ltr_coach,
        ert_ricky,
        non4me_pagaa,
        rp1_ice,
        ert_redevils,
        yozana,
        pur_ultraaa,
        ert_tiiste,
        non4me_jordy,
        rp1_fifou,
        non4me_sanzz,
        ert_iquazz,
        xrt_alpha,
        jancker21,
        rp1_lito,
        tx3_soap,
        rp1_owain,
        rp1_durtom,
        non4me_livai,
        is_honoka
    ]

    # classements
    result03.resultat("q", qualif03)
    result03.resultat("c", course03)

    result03.calcPointsQ()
    result03.calcPointsC()

    # évènements ponctuels
    result03.crash("c", is_honoka)
    result03.crash("c", non4me_livai)
    result03.crash("c",rp1_durtom)

    result03.meilleurTour(rp1_owain)

    # final 
    pt03 = result03.getPoints()

    """
    print(sortedDict(result03.getPoints()))
    
    for i in result03.getCourse():
        print(i.getGamertag(), i.getHistorique())
    """

    # Ideal

    result03.resetHist()

    ###################################################################################################
    # Course 4

    result04 = GrandPrix("EtatsUnis")

    qualif04 = [
        non4me_sanzz,
        rp1_owain,
        pur_ultraaa,
        non4me_livai,
        xrt_alpha, # remplacé par XRT Alpha
        rp1_durtom,
        ert_tiiste,
        ert_ricky,
        ert_redevils,
        rp1_fifou,
        tx3_soap,
        is_honoka,
        jancker21,
        non4me_pagaa,
        rp1_ice,
        rp1_lito, # remplacé par X7PK Karanox
        yozana, # remplacé par vNiicklass
        non4me_jordy,
        ert_iquazz, # remplacé par NathanHrx
        ltr_coach
    ]

    course04 = [
        rp1_owain,
        non4me_sanzz,
        pur_ultraaa,
        tx3_soap,
        rp1_durtom,
        non4me_livai,
        non4me_pagaa,
        ert_tiiste,
        is_honoka,
        jancker21,
        ltr_coach,
        non4me_jordy,
        ert_redevils,
        rp1_ice,
        yozana,
        ert_ricky,
        rp1_fifou,
        xrt_alpha,
        rp1_lito,
        ert_iquazz
    ]

    # classements
    result04.resultat("q", qualif04)
    result04.resultat("c", course04)

    result04.calcPointsQ()
    result04.calcPointsC()

    # évènements ponctuels
    result04.crash("q", rp1_ice)
    result04.crash("q", non4me_pagaa)
    
    result04.crash("c", ert_iquazz)
    result04.crash("c", rp1_lito)
    result04.crash("c", xrt_alpha)

    result04.meilleurTour(xrt_alpha)

    # final
    pt04 = result04.getPoints()

    """
    print(sortedDict(result04.getPoints()))

    for i in result04.getCourse():
        print(i.getGamertag(), i.getHistorique())
    """

    # Ideal :

    result04.resetHist()

    ###################################################################################################
    # Course 5

    result05 = GrandPrix("Jeddah")

    qualif05 = [
        xrt_alpha, # remplacé par XRT Alpha
        rp1_ice,
        ert_iquazz,
        ltr_coach,
        non4me_livai,
        ert_redevils,
        pur_ultraaa,
        ert_ricky,
        rp1_owain,
        non4me_pagaa,
        non4me_jordy,
        tx3_soap,
        ert_tiiste,
        is_honoka,
        non4me_sanzz,
        rp1_durtom,
        rp1_fifou,
        jancker21,
        rp1_lito
        # Yozana absent et non remplacé
    ]

    course05 = [
        xrt_alpha,
        non4me_livai,
        rp1_ice,
        ert_iquazz,
        rp1_fifou,
        jancker21,
        rp1_owain,
        ert_tiiste,
        rp1_durtom,
        pur_ultraaa,
        tx3_soap,
        ltr_coach,
        non4me_pagaa,
        is_honoka,
        rp1_lito,
        ert_redevils,
        ert_ricky,
        non4me_jordy,
        non4me_sanzz
        # Yozana absent et non remplacé
    ]

    # classements
    result05.resultat("q", qualif05)
    result05.resultat("c", course05)

    result05.calcPointsQ()
    result05.calcPointsC()

    # évènements ponctuels
    result05.crash("c", non4me_sanzz)
    result05.crash("c", non4me_jordy)
    result05.crash("c", ert_ricky)
    result05.crash("c", ert_redevils)

    result05.meilleurTour(non4me_livai)

    # final
    pt05 = result05.getPoints()

    """
    print(sortedDict(result05.getPoints()))
    
    for i in result05.getCourse():
        print(i.getGamertag(), i.getHistorique())
    """

    # Ideal :

    result05.resetHist()

    ###################################################################################################
    # Course 6

    result06 = GrandPrix("Hongrie")

    qualif06 = [
        pur_ultraaa,
        rp1_owain,
        rp1_ice,
        ert_ricky,
        tx3_soap,
        non4me_livai,
        ert_redevils,
        non4me_pagaa,
        non4me_sanzz, # remplacé par X7PK KaranoX
        is_honoka,
        non4me_jordy,
        yozana,
        rp1_fifou,
        ert_tiiste,
        rp1_durtom,
        ert_iquazz, # remplacé par NxS xTiGa
        xrt_alpha , # remplacé par NathanHrx
        rp1_lito, # remplacé par YoanN0 SKLL
        ltr_coach,
        jancker21
    ]

    course06 = [
        non4me_sanzz,
        ert_ricky,
        rp1_durtom,
        non4me_livai,
        rp1_owain,
        ltr_coach,
        ert_iquazz,
        rp1_fifou,
        non4me_pagaa,
        rp1_lito,
        ert_redevils,
        ert_tiiste,
        xrt_alpha,
        rp1_ice,
        tx3_soap,
        non4me_jordy,
        pur_ultraaa,
        jancker21,
        is_honoka,
        yozana
    ]

    # classements
    result06.resultat("q", qualif06)
    result06.resultat("c", course06)

    result06.calcPointsQ()
    result06.calcPointsC()

    # evenements ponctuels
    result06.crash("q", ert_redevils)

    result06.crash("c", yozana)
    result06.crash("c", is_honoka)
    result06.crash("c", jancker21)
    result06.crash("c", pur_ultraaa)
    result06.crash("c", non4me_jordy)
    result06.crash("c", tx3_soap)
    result06.crash("c", rp1_ice)

    result06.meilleurTour(xrt_alpha)

    # final
    pt06 = result06.getPoints()

    """
    print(sortedDict(result06.getPoints()))

    for i in result06.getCourse():
        print(i.getGamertag(), i.getHistorique())
    """

    # Ideal :

    result06.resetHist()

    ###############################################################################################

    final = sumDict(pt01, pt02)
    final = sumDict(final, pt03)
    final = sumDict(final, pt04)
    final = sumDict(final, pt05)
    final = sumDict(final, pt06)
    
    # print(final)

    return final