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

    # final
    pt01 = result01.getPoints()
    
    """
    print(sortedDict(result01.getPoints()))

    for i in result01.getCourse():
        print(i.getGamertag(), i.getHistorique())
    """

    # Ideal : FcT Theo, LDL Oli, PuR Stitoxxe

    result01.resetHist()

    ###################################################################################################
    # Course 2
    
    result02 = GrandPrix("Chine")

    qualif02 = [
        fct_adam,
        ert_niloboo,
        fct_theo,
        rp1_winterr,
        rp1_okwaru,
        pur_varane, # remplacé par SHZ Ewan
        rp1_luca,
        pur_voltha,
        ldl_oli,
        vinboy,
        rp1_chadoo,
        pur_stitoxxe,
        shz_noctis,
        ldl_saumon,
        ripply_spl,
        xrt_arthur, # remplacé par MCR Skriniar
        tx3_enzo, # remplacé par RaavenBZH
        mcr_jayrko,
        modz_scboy,
        mcr_path
    ]

    course02 = [
        rp1_winterr,
        fct_theo,
        rp1_okwaru,
        pur_voltha,
        ert_niloboo,
        pur_varane,
        shz_noctis,
        ldl_oli,
        vinboy,
        ldl_saumon,
        mcr_jayrko,
        pur_stitoxxe,
        tx3_enzo,
        mcr_path,
        rp1_chadoo,
        fct_adam,
        xrt_arthur,
        modz_scboy,
        ripply_spl,
        rp1_luca
    ]

    # classements
    result02.resultat("q", qualif02)
    result02.resultat("c", course02)

    result02.calcPointsQ()
    result02.calcPointsC()

    # évènements ponctuels
    result02.crash("q", ripply_spl)

    result02.crash("c", rp1_luca)
    result02.crash("c", ripply_spl)
    result02.crash("c", modz_scboy)
    result02.crash("c", xrt_arthur)
    result02.crash("c", fct_adam)

    result02.meilleurTour(fct_adam)

    # final
    pt02 = result02.getPoints()

    """
    print(sortedDict(result02.getPoints()))
    
    for i in result02.getCourse():
        print(i.getGamertag(), i.getHistorique())
    """

    # Ideal : RP1 Winterr, SHZ Noctis, TX3 Enzo

    result02.resetHist()

    ###################################################################################################
    # Course 3

    result03 = GrandPrix("Imola")

    qualif03 = [
        fct_adam,
        rp1_winterr,
        rp1_okwaru,
        pur_varane,
        rp1_luca,
        ldl_oli,
        shz_noctis,
        pur_voltha,
        vinboy,
        ldl_saumon,
        rp1_chadoo,
        pur_stitoxxe,
        xrt_arthur,
        fct_theo,
        ert_niloboo,
        tx3_enzo, # remplacé par RaavenBZH
        ripply_spl,
        mcr_jayrko,
        modz_scboy, # remplacé par Modz ScBoy
        mcr_path
    ]

    course03 = [
        rp1_luca,
        fct_adam,
        fct_theo,
        ert_niloboo,
        shz_noctis,
        ldl_oli,
        rp1_winterr,
        vinboy,
        ldl_saumon,
        ripply_spl,
        pur_voltha,
        tx3_enzo,
        modz_scboy,
        mcr_path,
        xrt_arthur,
        mcr_jayrko,
        pur_varane,
        rp1_okwaru,
        rp1_chadoo,
        pur_stitoxxe
    ]

    # classements
    result03.resultat("q", qualif03)
    result03.resultat("c", course03)

    result03.calcPointsQ()
    result03.calcPointsC()

    # évènements ponctuels
    result03.crash("q", ert_niloboo)
    result03.crash("q", mcr_path)

    result03.crash("c", pur_stitoxxe)
    result03.crash("c", rp1_chadoo)
    result03.crash("c", rp1_okwaru)

    result03.meilleurTour(rp1_winterr)

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
    
    final = sumDict(pt01, pt02)
    final = sumDict(final, pt03)
    
    # print(final)

    return final