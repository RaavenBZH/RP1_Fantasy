from packageF1.rp1 import *

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

    lrt_coach = Pilote("LRT Coach", "McLaren")
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

    crz_iquazz = Pilote("CRZ iQuaZz", "Williams")
    ert_ricky = Pilote("ERT Ricky", "Williams")

    tx3_soap = Pilote("TX3 Soap", "Haas")
    is_honoka = Pilote("IS Honoka", "Haas")

    ###################################################################################################

    # Course 1

    result01 = GrandPrix(None)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    qualif01 = [
    ]

    course01 = [
    ]

    # classements
    result01.resultat("q", qualif01)
    result01.resultat("c", course01)

    # évènements ponctuels