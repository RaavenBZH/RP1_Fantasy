from unittest import SkipTest
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

    tx3_matt = Pilote("TX3 Matt", "Ferrari")
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
    rp1_woody = Pilote("RP1 Woody", "Haas")

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
        rp1_woody,
        pur_racing, # remplacé par SHZ Ewan
        tx3_matt,
        o2_oxygen,
        xrt_baka, # remplacé par DucPasCharlie
        fct_coco,
        legion_tomoe,
        mvt_thomas,
        mcr_skriniar,
        xrt_nico2a,
        rp1_virlix, # remplacé par MCR FeFe13
        fct_deadpool
        #benbdby
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
        tx3_matt,
        legion_tomoe,
        mcr_skriniar,
        fct_deadpool,
        pur_racing,
        xrt_baka,
        ert_batxone,
        xrt_nico2a,
        rp1_virlix,
        rp1_woody
        #benbdby
    ]

    # classements
    result01.resultat("q", qualif01)
    result01.resultat("c", course01)

    result01.calcPointsQ()
    result01.calcPointsC()

    # évènements ponctuels
    result01.crash("q", tx3_matt)
    result01.crash("q", pur_racing)
    result01.crash("q", mvt_thomas)

    result01.crash("q", rp1_woody)
    result01.crash("q", rp1_virlix)
    result01.crash("q", xrt_nico2a)
    result01.crash("q", ert_batxone)
    result01.crash("q", xrt_baka)
    result01.crash("q", pur_racing)

    result01.meilleurTour(tx3_matt)

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
        tx3_matt, # remplacé par PuR Nygraal
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
        rp1_woody# remplacé par FcT Julien
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
        rp1_woody,
        tx3_matt
    ]

    # classements
    result02.resultat("q", qualif02)
    result02.resultat("c", course02)

    result02.calcPointsQ()
    result02.calcPointsC()

    # évènements ponctuels
    result02.crash("c", tx3_matt)
    result02.crash("c", rp1_woody)
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
        tx3_matt,
        fct_coco,
        fct_deadpool,
        xrt_baka,
        xrt_nico2a,
        rp1_woody # remplacé par iF1 Meister
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
        tx3_matt,
        rp1_woody,
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
    result03.crash("c", rp1_woody)
    result03.crash("c", tx3_matt)
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
        rp1_woody, # remplacé par iF1 Supreme
        aft_lowky,
        xrt_nico2a,
        fct_coco,
        xrt_baka, # remplacé par RP1 Fifi93
        tx3_matt 
        
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
        rp1_woody,
        fct_coco,
        pur_ilton,
        mvt_thomas,
        xrt_baka,
        benbdby,
        pur_racing,
        xrt_nico2a,
        aft_lowky,
        rp1_virlix,
        tx3_matt
    ]

    # classements
    result04.resultat("q", qualif04)
    result04.resultat("c", course04)

    result04.calcPointsQ()
    result04.calcPointsC()

    # évènements ponctuels
    result04.crash("c",tx3_matt)
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

    ###############################################################################################
    
    final = sumDict(pt01, pt02)
    final = sumDict(final, pt03)
    final = sumDict(final, pt04)
    
    # print(final)

    return final