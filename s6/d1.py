from packageF1.Pilote import *
from packageF1.GrandPrix import *
from packageF1.Joueur import *
from packageF1.EnsembleJoueur import *
from packageF1.fonctions import *

#
# Saison 6
#
# Calcul des points pour les pilotes de division 1
#

def getPointsD1() -> dict:

    ###################################################################################################

    # Création des pilotes

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    fct_theo = Pilote("FcT Theo", "Mercedes")
    ert_niloboo = Pilote("ERT Niloboo", "Mercedes")

    fct_adam = Pilote("FcT Adam", "RedBull")
    pur_winterr = Pilote("PuR Winterr", "RedBull")

    rp1_luca = Pilote("RP1 Luca", "McLaren")
    pur_varane = Pilote("PuR Varane", "McLaren")

    rp1_okwaru = Pilote("RP1 Okwaru", "Ferrari")
    pur_voltha = Pilote("PuR Voltha", "Ferrari")

    vinboy = Pilote("Vinboy", "AlphaTauri")
    spl_ripply = Pilote("SPL Ripply", "AlphaTauri")

    ldl_oli = Pilote("LDL Oli", "Alpine")
    ldl_saumon = Pilote("LDL Saumon", "Alpine")

    shz_noctis = Pilote("SHZ Noctis", "AstonMartin")
    rp1_chadoo = Pilote("RP1 Chadoo", "AstonMartin")

    mcr_jayrko = Pilote("MCR Jayrko", "AlfaRomeo")
    pur_stitoxxe = Pilote("PuR Sitoxxe", "AlfaRomeo")

    mcr_path = Pilote("MCR Path", "Williams")
    ert_bison = Pilote("ERT Bison", "Williams")

    tx3_enzo = Pilote("TX3 Enzo", "Haas")
    modz_scboy = Pilote("Modz Scboy", "Haas")

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