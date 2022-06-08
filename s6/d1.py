from operator import mod
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
    # Course 4

    result04 = GrandPrix("EtatsUnis")

    qualif04 = [
        fct_theo, # remplacé par RP1 Virlix
        rp1_winterr,
        fct_adam,
        ert_niloboo,
        pur_voltha,
        rp1_okwaru,
        rp1_luca,
        pur_varane,
        ldl_oli,
        shz_noctis,
        ldl_saumon,
        ripply_spl,
        vinboy,
        rp1_chadoo,
        pur_stitoxxe, # remplacé par PuR Vincent
        xrt_arthur,
        mcr_path,
        tx3_enzo, # remplacé par ERT BatXOne
        mcr_jayrko,
        modz_scboy # remplacé par MCR Skriniar
    ]

    course04 = [
        fct_adam,
        fct_theo,
        ert_niloboo,
        rp1_okwaru,
        rp1_winterr,
        pur_voltha,
        rp1_luca,
        ldl_saumon,
        pur_stitoxxe,
        mcr_jayrko,
        modz_scboy,
        vinboy,
        xrt_arthur,
        rp1_chadoo,
        pur_varane,
        mcr_path,
        shz_noctis,
        tx3_enzo,
        ldl_oli,
        ripply_spl
    ]

    # classements
    result04.resultat("q", qualif04)
    result04.resultat("c", course04)

    result04.calcPointsQ()
    result04.calcPointsC()

    # évènements ponctuels
    result04.crash("c",ripply_spl)
    result04.crash("c",ldl_oli)
    result04.crash("c",tx3_enzo)
    result04.crash("c",shz_noctis)
    result04.crash("c",mcr_path)
    result04.crash("c",pur_varane)

    result04.meilleurTour(fct_theo)

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
        rp1_winterr,
        fct_adam,
        ert_niloboo,
        pur_varane,
        fct_theo,
        ldl_oli,
        ldl_saumon, # remplacé par RaavenBZH
        rp1_okwaru,
        vinboy,
        shz_noctis,
        pur_voltha,
        ripply_spl,
        rp1_chadoo,
        pur_stitoxxe,
        rp1_luca,
        mcr_jayrko,
        mcr_path,
        tx3_enzo, # remplacé par BatXOne
        xrt_arthur,
        modz_scboy #remplacé par RP1 Woody
    ]

    course05 = [
        fct_theo,
        rp1_winterr,
        ert_niloboo,
        ldl_oli,
        shz_noctis,
        rp1_luca,
        rp1_okwaru,
        pur_stitoxxe,
        mcr_jayrko,
        xrt_arthur,
        pur_varane,
        tx3_enzo,
        fct_adam,
        rp1_chadoo,
        mcr_path,
        modz_scboy,
        ripply_spl,
        ldl_saumon,
        pur_voltha,
        vinboy
    ]

    # classements
    result05.resultat("q", qualif05)
    result05.resultat("c", course05)

    result05.calcPointsQ()
    result05.calcPointsC()

    # évènements ponctuels
    result05.crash("q", rp1_luca)

    result05.crash("c", vinboy)
    result05.crash("c", pur_voltha)
    result05.crash("c", ldl_saumon)

    result05.meilleurTour(fct_adam)

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
        fct_theo,
        fct_adam,
        ert_niloboo,
        rp1_winterr,
        rp1_okwaru,
        pur_voltha,
        ldl_oli,
        rp1_luca, # remplacé par PuR Vincent
        ldl_saumon,
        rp1_chadoo,
        pur_varane,
        pur_stitoxxe,
        ripply_spl,
        vinboy,
        shz_noctis,
        tx3_enzo, # remplacé par BatXOne 
        xrt_arthur,
        mcr_jayrko,
        mcr_path,
        modz_scboy # remplacé par RP1 Woody
    ]

    course06 = [
        fct_theo,
        ert_niloboo,
        rp1_okwaru,
        fct_adam,
        pur_voltha,
        pur_varane,
        ldl_oli,
        vinboy,
        xrt_arthur,
        shz_noctis,
        pur_stitoxxe,
        ldl_saumon,
        rp1_luca,
        mcr_path,
        mcr_jayrko,
        modz_scboy,
        rp1_chadoo,
        tx3_enzo,
        rp1_winterr,
        ripply_spl
    ]

    # classements
    result06.resultat("q", qualif06)
    result06.resultat("c", course06)

    result06.calcPointsQ()
    result06.calcPointsC()

    # evenements ponctuels
    result06.crash("q", shz_noctis)

    result06.crash("c", tx3_enzo)
    result06.crash("c", rp1_winterr)
    result06.crash("c", ripply_spl)

    result06.meilleurTour(fct_adam)

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
        fct_theo,
        rp1_winterr,
        fct_adam, # remplacé par BatXOne
        ert_niloboo,
        rp1_okwaru,
        rp1_luca,
        pur_voltha,
        vinboy,
        ldl_oli, # remplacé par PuR Vincent
        ldl_saumon, # remplacé par MCR Skriniar
        shz_noctis, # remplacé par RaavenBZH
        rp1_chadoo,
        ripply_spl,
        pur_stitoxxe,
        pur_varane,
        xrt_arthur, # remplacé par RP1 Maldini
        mcr_jayrko,
        mcr_path
    ]

    course07 = [
        rp1_winterr,
        fct_adam,
        ert_niloboo,
        rp1_okwaru,
        fct_theo,
        pur_varane,
        vinboy,
        shz_noctis,
        pur_voltha,
        rp1_chadoo,
        ldl_oli,
        mcr_jayrko,
        pur_stitoxxe,
        xrt_arthur,
        ripply_spl,
        ldl_saumon,
        mcr_path,
        rp1_luca
    ]

    # classements
    result07.resultat("q", qualif07)
    result07.resultat("c", course07)

    result07.calcPointsQ()
    result07.calcPointsC()

    # evenements ponctuels
    result07.crash("q", pur_varane)
    result07.crash("q", rp1_chadoo)

    result07.crash("c", rp1_luca)
    result07.crash("c", mcr_path)
    result07.crash("c", ldl_saumon)
    result07.crash("c", ripply_spl)

    result07.meilleurTour(fct_theo)

    # final
    pt07 = result07.getPoints()

    """
    print(sortedDict(result07.getPoints()))

    for i in result07.getCourse():
        print(i.getGamertag(), i.getHistorique())
    """

    # Ideal :

    result07.resetHist()

    ###############################################################################################
    
    final = sumDict(pt01, pt02)
    final = sumDict(final, pt03)
    final = sumDict(final, pt04)
    final = sumDict(final, pt05)
    final = sumDict(final, pt06)
    final = sumDict(final, pt07)
    
    # print(final)

    return final