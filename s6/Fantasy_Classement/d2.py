from packageF1.Pilote import *
from packageF1.GrandPrix import *
from packageF1.Joueur import *
from packageF1.EnsembleJoueur import *
from packageF1.fonctions import *

#
# Saison 6
#
# Calcul des points pour les pilotes de division 2
#

def getPointsD2() -> dict:

    ###################################################################################################

    # Création des pilotes

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    mvt_thomas = Pilote("MVT Thomas", "Mercedes")
    rp1_virlix = Pilote("RP1 Virlix", "Mercedes")

    raavenbzh = Pilote("RaavenBZH", "RedBull")
    ert_batxone = Pilote("ERT BatXone", "RedBull")

    vrt_tribion = Pilote("VRT Tribion", "McLaren")
    fct_deadpool = Pilote("FcT Deadpool", "McLaren")

    alexgt500 = Pilote("AlexGT500", "Ferrari")
    aft_lowky = Pilote("AfT Lowky", "Ferrari")

    o2_oxygen = Pilote("O2 Oxygen", "AlphaTauri")
    xrt_nico2a = Pilote("XRT Nico2a", "AlphaTauri")

    xrt_darkfly = Pilote("XRT Darkfly", "Alpine")
    xrt_baka = Pilote("XRT Baka", "Alpine")

    mcr_skriniar = Pilote("MCR Skriniar", "AstonMartin")
    legion_tomoe = Pilote("Legion Tomoe", "AstonMartin")

    pur_ilton = Pilote("PuR Ilton", "AlfaRomeo")
    pur_vincent = Pilote("PuR Vincent", "AlfaRomeo")

    pur_racing = Pilote("PuR Racing", "Williams")
    fct_coco = Pilote("FcT Coco", "Williams")

    benbdby = Pilote("BenBdBy", "Haas")
    haas_d2_02 = Pilote("Haas D2 02", "Haas")

    ###################################################################################################
    # Course 1

    result01 = GrandPrix("Autriche")

    qualif01 = [
        raavenbzh,
        pur_vincent,
        ert_batxone,
        aft_lowky,
        vrt_tribion,
        xrt_darkfly,
        pur_ilton,
        haas_d2_02,
        pur_racing, # remplacé par SHZ Ewan
        alexgt500,
        o2_oxygen,
        xrt_baka, # remplacé par DucPasCharlie
        fct_coco,
        legion_tomoe,
        mvt_thomas,
        mcr_skriniar,
        xrt_nico2a,
        rp1_virlix, # remplacé par MCR FeFe13
        fct_deadpool
        # BenBdBy
    ]

    course01 = [
        raavenbzh,
        pur_vincent,
        pur_ilton,
        vrt_tribion,
        xrt_darkfly,
        mvt_thomas,
        fct_coco,
        aft_lowky,
        o2_oxygen,
        alexgt500,
        legion_tomoe,
        mcr_skriniar,
        fct_deadpool,
        pur_racing,
        xrt_baka,
        ert_batxone,
        xrt_nico2a,
        rp1_virlix,
        haas_d2_02
        # BenBdBy
    ]

    # classements
    result01.resultat("q", qualif01)
    result01.resultat("c", course01)

    result01.calcPointsQ()
    result01.calcPointsC()

    # évènements ponctuels
    result01.crash("q", alexgt500)
    result01.crash("q", pur_racing)
    result01.crash("q", mvt_thomas)

    result01.crash("q", haas_d2_02)
    result01.crash("q", rp1_virlix)
    result01.crash("q", xrt_nico2a)
    result01.crash("q", ert_batxone)
    result01.crash("q", xrt_baka)
    result01.crash("q", pur_racing)

    result01.meilleurTour(alexgt500)

    # final
    pt01 = result01.getPoints()

    """
    print(sortedDict(result01.getPoints()))

    for i in result01.getCourse():
        print(i.getGamertag(), i.getHistorique())
    """
    
    # Ideal : RaavenBZH, MVT Thomas, FcT Coco

    result01.resetHist()

    ###################################################################################################
    # Course 2

    result02 = GrandPrix("Chine")

    qualif02 = [
        raavenbzh,
        ert_batxone,
        vrt_tribion,
        rp1_virlix, # remplacé par SHZ Ewan,
        pur_racing,
        mvt_thomas,
        xrt_darkfly,
        alexgt500, # remplacé par PuR Nygraal
        aft_lowky,
        mcr_skriniar, #remplacé par RP1 Gachette
        pur_ilton,
        pur_vincent,
        o2_oxygen,
        benbdby,
        legion_tomoe,
        fct_coco,
        xrt_nico2a,
        xrt_baka,
        fct_deadpool,
        haas_d2_02# remplacé par FcT Julien
    ]

    course02 = [
        raavenbzh,
        rp1_virlix,
        ert_batxone,
        pur_racing,
        o2_oxygen,
        aft_lowky,
        xrt_baka,
        legion_tomoe,
        pur_ilton,
        fct_coco,
        vrt_tribion,
        fct_deadpool,
        pur_vincent,
        xrt_darkfly,
        xrt_nico2a,
        mvt_thomas,
        benbdby,
        mcr_skriniar,
        haas_d2_02,
        alexgt500
    ]

    # classements
    result02.resultat("q", qualif02)
    result02.resultat("c", course02)

    result02.calcPointsQ()
    result02.calcPointsC()

    # évènements ponctuels
    result02.crash("c", alexgt500)
    result02.crash("c", haas_d2_02)
    result02.crash("c", mcr_skriniar)
    result02.crash("c", benbdby)

    result02.meilleurTour(xrt_nico2a)

    # final
    pt02 = result02.getPoints()

    """
    print(sortedDict(result02.getPoints()))
    
    for i in result02.getCourse():
        print(i.getGamertag(), i.getHistorique())
    """

    # Ideal : RP1 Virlix, O2 Oxygen, Legion Tomoe

    result02.resetHist()

    ###################################################################################################
    # Course 3

    result03 = GrandPrix("Imola")

    qualif03 = [
        pur_racing,
        mvt_thomas,
        aft_lowky,
        vrt_tribion,
        raavenbzh,
        ert_batxone,
        xrt_darkfly,
        pur_vincent,
        o2_oxygen,
        legion_tomoe,
        mcr_skriniar, # remplacé par RP1 Gachette
        benbdby,
        pur_ilton, # remplacé par SkS Flyart
        rp1_virlix, # remplacé par iF1 Supreme
        alexgt500,
        fct_coco,
        fct_deadpool,
        xrt_baka,
        xrt_nico2a,
        haas_d2_02 # remplacé par iF1 Meister
    ]

    course03 = [
        rp1_virlix,
        aft_lowky,
        pur_ilton,
        o2_oxygen,
        legion_tomoe,
        fct_coco,
        raavenbzh,
        xrt_darkfly,
        pur_racing,
        benbdby,
        mcr_skriniar,
        mvt_thomas,
        fct_deadpool,
        vrt_tribion,
        xrt_baka,
        ert_batxone,
        alexgt500,
        haas_d2_02,
        xrt_nico2a,
        pur_vincent
    ]

    # classements
    result03.resultat("q", qualif03)
    result03.resultat("c", course03)

    result03.calcPointsQ()
    result03.calcPointsC()

    # évènements ponctuels
    result03.crash("q", o2_oxygen)

    result03.crash("c", pur_vincent)
    result03.crash("c", xrt_nico2a)
    result03.crash("c", haas_d2_02)
    result03.crash("c", alexgt500)
    result03.crash("c", ert_batxone)
    result03.crash("c", xrt_baka)
    result03.crash("c", vrt_tribion)
    result03.crash("c", fct_deadpool)

    result03.meilleurTour(pur_racing)

    # final 
    pt03 = result03.getPoints()

    """
    print(sortedDict(result03.getPoints()))
    
    for i in result03.getCourse():
        print(i.getGamertag(), i.getHistorique())
    """
    
    # Ideal : 

    result03.resetHist()

    ###################################################################################################
    # Course 4

    result04 = GrandPrix("EtatsUnis")

    qualif04 = [
        xrt_darkfly,
        fct_deadpool, # remplacé par SHZ Ewan
        raavenbzh,
        mvt_thomas,
        pur_racing,
        mcr_skriniar, # remplacé par RP1 Maldini
        benbdby, # remplacé par AlexGT500
        pur_vincent,
        vrt_tribion,
        rp1_virlix,
        ert_batxone,
        pur_ilton,
        o2_oxygen,
        legion_tomoe,
        haas_d2_02, # remplacé par iF1 Supreme
        aft_lowky,
        xrt_nico2a,
        fct_coco,
        xrt_baka, # remplacé par RP1 Fifi93
        alexgt500 
        
    ]

    course04 = [
        ert_batxone,
        fct_deadpool,
        xrt_darkfly,
        raavenbzh,
        o2_oxygen,
        vrt_tribion,
        mcr_skriniar,
        legion_tomoe,
        pur_vincent,
        haas_d2_02,
        fct_coco,
        pur_ilton,
        mvt_thomas,
        xrt_baka,
        benbdby,
        pur_racing,
        xrt_nico2a,
        aft_lowky,
        rp1_virlix,
        alexgt500
    ]

    # classements
    result04.resultat("q", qualif04)
    result04.resultat("c", course04)

    result04.calcPointsQ()
    result04.calcPointsC()

    # évènements ponctuels
    result04.crash("c",alexgt500)
    result04.crash("c",rp1_virlix)
    result04.crash("c",aft_lowky)

    result04.meilleurTour(xrt_nico2a)

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
        ert_batxone,
        vrt_tribion,
        mvt_thomas,
        alexgt500, # remplacé par PuR NyGraal
        xrt_baka,
        aft_lowky,
        pur_vincent, # remplacé par Soo Skyzzz
        o2_oxygen,
        raavenbzh,
        pur_racing,
        pur_ilton, # remplacé par ERT Aurelius
        fct_deadpool,
        haas_d2_02, # remplacé par AlexGT500
        xrt_nico2a, # remplacé par DucPasCharlie
        benbdby,
        fct_coco,
        legion_tomoe,
        xrt_darkfly,
        rp1_virlix,
        mcr_skriniar
    ]

    course05 = [
        mvt_thomas,
        alexgt500,
        raavenbzh,
        aft_lowky,
        legion_tomoe,
        rp1_virlix,
        o2_oxygen,
        ert_batxone,
        mcr_skriniar,
        fct_coco,
        xrt_darkfly,
        pur_vincent,
        pur_ilton,
        haas_d2_02,
        xrt_baka,
        vrt_tribion,
        benbdby,
        xrt_nico2a,
        fct_deadpool
    ]

    # classements
    result05.resultat("q", qualif05)
    result05.resultat("c", course05)

    result05.calcPointsQ()
    result05.calcPointsC()

    # évènements ponctuels
    result05.crash("q", legion_tomoe)
    result05.crash("q", pur_racing)
    result05.crash("q", aft_lowky)

    result05.crash("c", fct_deadpool)
    result05.crash("c", xrt_nico2a)
    result05.crash("c", benbdby)
    result05.crash("c", vrt_tribion)
    result05.crash("c", xrt_baka)

    result05.meilleurTour(pur_ilton)

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
        mvt_thomas,
        mcr_skriniar, # remplacé par iF1 Meister
        xrt_baka,
        raavenbzh,
        pur_ilton,
        rp1_virlix, # remplacé par ERT Toon
        haas_d2_02,
        aft_lowky,
        benbdby, # remplacé par AlexGT500 GAME
        xrt_darkfly,
        xrt_nico2a, # remplacé par Eroziah SPL
        alexgt500,
        o2_oxygen,
        pur_vincent, # remplacé par RP1 Vara
        ert_batxone,
        vrt_tribion, # remplacé par cedric dauby
        fct_deadpool,
        legion_tomoe,
        fct_coco,
        pur_racing
    ]

    course06 = [
        ert_batxone,
        aft_lowky,
        xrt_darkfly,
        mvt_thomas,
        o2_oxygen,
        raavenbzh,
        mcr_skriniar,
        legion_tomoe,
        xrt_nico2a,
        fct_coco,
        haas_d2_02,
        benbdby,
        pur_ilton,
        pur_vincent,
        rp1_virlix,
        fct_deadpool,
        xrt_baka,
        vrt_tribion,
        pur_racing,
        alexgt500
    ]

    # classements
    result06.resultat("q", qualif06)
    result06.resultat("c", course06)

    result06.calcPointsQ()
    result06.calcPointsC()

    # evenements ponctuels
    result06.crash("q", ert_batxone)

    result06.crash("c", alexgt500)
    result06.crash("c", pur_racing)
    result06.crash("c", vrt_tribion)
    result06.crash("c", xrt_baka)
    result06.crash("c", fct_deadpool)

    result06.meilleurTour(pur_ilton)

    # final
    pt06 = result06.getPoints()

    """
    print(sortedDict(result06.getPoints()))

    for i in result06.getCourse():
        print(i.getGamertag(), i.getHistorique())
    """

    # Ideal :

    result06.resetHist()

    ###################################################################################################
    # Course 7

    result07 = GrandPrix("Bresil")

    qualif07 = [
        pur_racing,
        mvt_thomas,
        o2_oxygen,
        fct_deadpool, # remplacé par SHZ Ewan,
        alexgt500, # remplacé par AlexGT500 GAME
        vrt_tribion,
        ert_batxone,
        raavenbzh,
        benbdby, # remplacé par Eroziah SPL
        pur_vincent,
        aft_lowky,
        rp1_virlix, # remplacé par SKS Flyart
        pur_ilton,
        mcr_skriniar,
        xrt_baka, # remplacé par RP1 Fifi93,
        fct_coco,
        legion_tomoe,
        xrt_nico2a,
        xrt_darkfly,
        haas_d2_02
    ]

    course07 = [
        pur_racing,
        mvt_thomas,
        ert_batxone,
        vrt_tribion,
        raavenbzh,
        o2_oxygen,
        aft_lowky,
        fct_deadpool,
        alexgt500,
        xrt_nico2a,
        xrt_darkfly,
        fct_coco,
        mcr_skriniar,
        pur_ilton,
        xrt_baka,
        pur_vincent,
        legion_tomoe,
        haas_d2_02,
        rp1_virlix,
        benbdby
    ]

    # classements
    result07.resultat("q", qualif07)
    result07.resultat("c", course07)

    result07.calcPointsQ()
    result07.calcPointsC()

    # evenements ponctuels
    result07.crash("q", haas_d2_02)

    result07.crash("c", benbdby)
    result07.crash("c", rp1_virlix)
    result07.crash("c", haas_d2_02)
    result07.crash("c", legion_tomoe)
    result07.crash("c", pur_vincent)
    result07.crash("c", xrt_baka)
    result07.crash("c", pur_ilton)

    result07.meilleurTour(mcr_skriniar)

    # final
    pt07 = result07.getPoints()

    """
    print(sortedDict(result07.getPoints()))

    for i in result07.getCourse():
        print(i.getGamertag(), i.getHistorique())
    """

    # Ideal :

    result07.resetHist()

    ###################################################################################################
    # Course 8

    result08 = GrandPrix("Italie")

    qualif08 = [
        raavenbzh,
        pur_vincent,
        vrt_tribion,
        rp1_virlix, # remplacé par Soo Skyzzz
        mvt_thomas,
        o2_oxygen,
        ert_batxone,
        pur_ilton,
        benbdby,
        xrt_nico2a, # remplacé par Eroziah SPL
        pur_racing,
        xrt_darkfly,
        alexgt500,
        aft_lowky,
        legion_tomoe,
        haas_d2_02, # SKS Flyart
        xrt_baka,
        fct_deadpool,
        fct_coco,
        mcr_skriniar # remplacé par iF1 Supr3me
    ]

    course08 = [
        mcr_skriniar,
        rp1_virlix,
        pur_vincent,
        xrt_darkfly,
        mvt_thomas,
        ert_batxone,
        vrt_tribion,
        o2_oxygen,
        haas_d2_02,
        raavenbzh,
        xrt_nico2a,
        aft_lowky,
        legion_tomoe,
        alexgt500,
        pur_ilton,
        fct_deadpool,
        fct_coco,
        xrt_baka,
        benbdby,
        pur_racing
    ]

    # classements
    result08.resultat("q", qualif08)
    result08.resultat("c", course08)

    result08.calcPointsQ()
    result08.calcPointsC()

    # evenements ponctuels
    result08.crash("q", alexgt500)

    result08.crash("c",fct_deadpool)
    result08.crash("c",fct_coco)
    result08.crash("c",xrt_baka)
    result08.crash("c",benbdby)
    result08.crash("c",pur_racing)

    result08.meilleurTour(pur_ilton)

    # final
    pt08 = result08.getPoints()

    """
    print(sortedDict(result08.getPoints()))

    for i in result08.getCourse():
        print(i.getGamertag(), i.getHistorique())
    """

    # Ideal :

    result08.resetHist()

    ###############################################################################################
    
    final = sumDict(pt01, pt02)
    final = sumDict(final, pt03)
    final = sumDict(final, pt04)
    final = sumDict(final, pt05)
    final = sumDict(final, pt06)
    final = sumDict(final, pt07)
    final = sumDict(final, pt08)
    
    # print(final)

    return final