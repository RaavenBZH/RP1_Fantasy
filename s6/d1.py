from unittest import result
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
    rp1_winterr = Pilote("RP1 Winterr", "RedBull")

    rp1_luca = Pilote("RP1 Luca", "McLaren")
    pur_varane = Pilote("PuR Varane", "McLaren")

    rp1_okwaru = Pilote("RP1 Okwaru", "Ferrari")
    pur_voltha = Pilote("PuR Voltha", "Ferrari")

    vinboy = Pilote("Vinboy", "AlphaTauri")
    ripply_spl = Pilote("Ripply SPL", "AlphaTauri")

    ldl_oli = Pilote("LDL Oli", "Alpine")
    ldl_saumon = Pilote("LDL Saumon", "Alpine")

    shz_noctis = Pilote("SHZ Noctis", "AstonMartin")
    rp1_chadoo = Pilote("RP1 Chadoo", "AstonMartin")

    mcr_jayrko = Pilote("MCR Jayrko", "AlfaRomeo")
    pur_stitoxxe = Pilote("PuR Stitoxxe", "AlfaRomeo")

    mcr_path = Pilote("MCR Path", "Williams")
    xrt_arthur = Pilote("XRT Arthur", "Williams")

    tx3_enzo = Pilote("TX3 Enzo", "Haas")
    modz_scboy = Pilote("Modz Scboy", "Haas")

    ###################################################################################################

    # Course 1
    
    result01 = GrandPrix("Autriche")

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    qualif01 = [
        fct_theo,
        fct_adam,
        ert_niloboo,
        rp1_winterr,
        rp1_luca,
        pur_voltha,
        ldl_oli,
        ldl_saumon,
        rp1_chadoo,
        rp1_okwaru,
        vinboy,
        shz_noctis,
        ripply_spl,
        pur_stitoxxe, # remplacé par PuR Vicent
        pur_varane,
        mcr_path,
        xrt_arthur, # remplacé par MCR Skriniar
        modz_scboy,
        mcr_jayrko,
        tx3_enzo
    ]

    course01 = [
        fct_theo,
        rp1_luca,
        ldl_oli,
        pur_varane,
        fct_adam,
        pur_voltha,
        rp1_winterr,
        ert_niloboo,
        vinboy,
        pur_stitoxxe,
        ldl_saumon,
        mcr_jayrko,
        shz_noctis,
        tx3_enzo,
        rp1_chadoo,
        xrt_arthur,
        modz_scboy,
        mcr_path,
        rp1_okwaru,
        ripply_spl
    ]

    # classements
    result01.resultat("q", qualif01)
    result01.resultat("c", course01)

    result01.calcPointsQ()
    result01.calcPointsC()

    # évènements ponctuels
    result01.crash("q", pur_varane)
    result01.crash("q", rp1_okwaru)

    result01.crash("c", ripply_spl)
    result01.crash("c", rp1_okwaru)
    result01.crash("c", mcr_path)

    result01.meilleurTour(fct_adam)
    
    """
    for i in result01.getCourse():
        print(i.getGamertag(), i.getHistorique())
    """

    # Ideal : FcT Theo, LDL Oli, PuR Stitoxxe

    return result01.getPoints()