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

    mclaren_d1_02 = Pilote("McLaren D1 02", "McLaren")
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
    pur_rosberg = Pilote("PuR Rosberg", "AlfaRomeo")

    mcr_path = Pilote("MCR Path", "Williams")
    xrt_arthur = Pilote("XRT Arthur", "Williams")

    haas_d1_01 = Pilote("Haas D1 01", "Haas")
    haas_d1_02 = Pilote("Haas D1 02", "Haas")

    ###################################################################################################
    # Course 1
    
    result01 = GrandPrix("Autriche")

    qualif01 = [
        fct_theo,
        fct_adam,
        ert_niloboo,
        rp1_winterr,
        mclaren_d1_02,
        pur_voltha,
        ldl_oli,
        ldl_saumon,
        rp1_chadoo,
        rp1_okwaru,
        vinboy,
        shz_noctis,
        ripply_spl,
        pur_rosberg, # remplacé par PuR Vicent
        pur_varane,
        mcr_path,
        xrt_arthur, # remplacé par MCR Skriniar
        haas_d1_02,
        mcr_jayrko,
        haas_d1_01
    ]

    course01 = [
        fct_theo,
        mclaren_d1_02,
        ldl_oli,
        pur_varane,
        fct_adam,
        pur_voltha,
        rp1_winterr,
        ert_niloboo,
        vinboy,
        pur_rosberg,
        ldl_saumon,
        mcr_jayrko,
        shz_noctis,
        haas_d1_01,
        rp1_chadoo,
        xrt_arthur,
        haas_d1_02,
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
    """
    
    print(result01.getCircuit())
    for i in result01.getCourse():
        print(i.getGamertag(), i.getHistorique())
    

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
        mclaren_d1_02,
        pur_voltha,
        ldl_oli,
        vinboy,
        rp1_chadoo,
        pur_rosberg,
        shz_noctis,
        ldl_saumon,
        ripply_spl,
        xrt_arthur, # remplacé par MCR Skriniar
        haas_d1_01, # remplacé par RaavenBZH
        mcr_jayrko,
        haas_d1_02,
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
        pur_rosberg,
        haas_d1_01,
        mcr_path,
        rp1_chadoo,
        fct_adam,
        xrt_arthur,
        haas_d1_02,
        ripply_spl,
        mclaren_d1_02
    ]

    # classements
    result02.resultat("q", qualif02)
    result02.resultat("c", course02)

    result02.calcPointsQ()
    result02.calcPointsC()

    # évènements ponctuels
    result02.crash("q", ripply_spl)

    result02.crash("c", mclaren_d1_02)
    result02.crash("c", ripply_spl)
    result02.crash("c", haas_d1_02)
    result02.crash("c", xrt_arthur)
    result02.crash("c", fct_adam)

    result02.meilleurTour(fct_adam)

    # final
    pt02 = result02.getPoints()

    """
    print(sortedDict(result02.getPoints()))
    """    
    print(result02.getCircuit())
    for i in result02.getCourse():
        print(i.getGamertag(), i.getHistorique())


    result02.resetHist()

    ###################################################################################################
    # Course 3

    result03 = GrandPrix("Imola")

    qualif03 = [
        fct_adam,
        rp1_winterr,
        rp1_okwaru,
        pur_varane,
        mclaren_d1_02,
        ldl_oli,
        shz_noctis,
        pur_voltha,
        vinboy,
        ldl_saumon,
        rp1_chadoo,
        pur_rosberg,
        xrt_arthur,
        fct_theo,
        ert_niloboo,
        haas_d1_01, # remplacé par RaavenBZH
        ripply_spl,
        mcr_jayrko,
        haas_d1_02, # remplacé par Modz ScBoy
        mcr_path
    ]

    course03 = [
        mclaren_d1_02,
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
        haas_d1_01,
        haas_d1_02,
        mcr_path,
        xrt_arthur,
        mcr_jayrko,
        pur_varane,
        rp1_okwaru,
        rp1_chadoo,
        pur_rosberg
    ]

    # classements
    result03.resultat("q", qualif03)
    result03.resultat("c", course03)

    result03.calcPointsQ()
    result03.calcPointsC()

    # évènements ponctuels
    result03.crash("q", ert_niloboo)
    result03.crash("q", mcr_path)

    result03.crash("c", pur_rosberg)
    result03.crash("c", rp1_chadoo)
    result03.crash("c", rp1_okwaru)

    result03.meilleurTour(rp1_winterr)

    # final 
    pt03 = result03.getPoints()

    """
    print(sortedDict(result03.getPoints()))
    """    
    print(result03.getCircuit())
    for i in result03.getCourse():
        print(i.getGamertag(), i.getHistorique())


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
        mclaren_d1_02,
        pur_varane,
        ldl_oli,
        shz_noctis,
        ldl_saumon,
        ripply_spl,
        vinboy,
        rp1_chadoo,
        pur_rosberg, # remplacé par PuR Vincent
        xrt_arthur,
        mcr_path,
        haas_d1_01, # remplacé par ERT BatXOne
        mcr_jayrko,
        haas_d1_02 # remplacé par MCR Skriniar
    ]

    course04 = [
        fct_adam,
        fct_theo,
        ert_niloboo,
        rp1_okwaru,
        rp1_winterr,
        pur_voltha,
        mclaren_d1_02,
        ldl_saumon,
        pur_rosberg,
        mcr_jayrko,
        haas_d1_02,
        vinboy,
        xrt_arthur,
        rp1_chadoo,
        pur_varane,
        mcr_path,
        shz_noctis,
        haas_d1_01,
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
    result04.crash("c",haas_d1_01)
    result04.crash("c",shz_noctis)
    result04.crash("c",mcr_path)
    result04.crash("c",pur_varane)

    result04.meilleurTour(fct_theo)

    # final
    pt04 = result04.getPoints()

    """
    print(sortedDict(result04.getPoints()))
    """
    print(result04.getCircuit())
    for i in result04.getCourse():
        print(i.getGamertag(), i.getHistorique())


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
        pur_rosberg,
        mclaren_d1_02,
        mcr_jayrko,
        mcr_path,
        haas_d1_01, # remplacé par BatXOne
        xrt_arthur,
        haas_d1_02 #remplacé par RP1 Woody
    ]

    course05 = [
        fct_theo,
        rp1_winterr,
        ert_niloboo,
        ldl_oli,
        shz_noctis,
        mclaren_d1_02,
        rp1_okwaru,
        pur_rosberg,
        mcr_jayrko,
        xrt_arthur,
        pur_varane,
        haas_d1_01,
        fct_adam,
        rp1_chadoo,
        mcr_path,
        haas_d1_02,
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
    result05.crash("q", mclaren_d1_02)

    result05.crash("c", vinboy)
    result05.crash("c", pur_voltha)
    result05.crash("c", ldl_saumon)

    result05.meilleurTour(fct_adam)

    # final
    pt05 = result05.getPoints()

    """
    print(sortedDict(result05.getPoints()))
    """
    
    print(result05.getCircuit())
    for i in result05.getCourse():
        print(i.getGamertag(), i.getHistorique())


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
        mclaren_d1_02, # remplacé par PuR Vincent
        ldl_saumon,
        rp1_chadoo,
        pur_varane,
        pur_rosberg,
        ripply_spl,
        vinboy,
        shz_noctis,
        haas_d1_01, # remplacé par BatXOne 
        xrt_arthur,
        mcr_jayrko,
        mcr_path,
        haas_d1_02 # remplacé par RP1 Woody
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
        pur_rosberg,
        ldl_saumon,
        mclaren_d1_02,
        mcr_path,
        mcr_jayrko,
        haas_d1_02,
        rp1_chadoo,
        haas_d1_01,
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

    result06.crash("c", haas_d1_01)
    result06.crash("c", rp1_winterr)
    result06.crash("c", ripply_spl)

    result06.meilleurTour(fct_adam)

    # final
    pt06 = result06.getPoints()

    """
    print(sortedDict(result06.getPoints()))
    """
    
    print(result06.getCircuit())
    for i in result06.getCourse():
        print(i.getGamertag(), i.getHistorique())


    result06.resetHist()

    ################################################################################################## #
    # Course 7

    result07 = GrandPrix("Bresil")

    qualif07 = [
        fct_theo,
        rp1_winterr,
        fct_adam, # remplacé par ERT BatXOne
        ert_niloboo,
        rp1_okwaru,
        mclaren_d1_02,
        pur_voltha,
        vinboy,
        ldl_oli, # remplacé par PuR Vincent
        ldl_saumon, # remplacé par MCR Skriniar
        shz_noctis, # remplacé par RaavenBZH
        rp1_chadoo,
        ripply_spl,
        pur_rosberg,
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
        pur_rosberg,
        xrt_arthur,
        ripply_spl,
        ldl_saumon,
        mcr_path,
        mclaren_d1_02
    ]

    # classements
    result07.resultat("q", qualif07)
    result07.resultat("c", course07)

    result07.calcPointsQ()
    result07.calcPointsC()

    # evenements ponctuels
    result07.crash("q", pur_varane)
    result07.crash("q", rp1_chadoo)

    result07.crash("c", mclaren_d1_02)
    result07.crash("c", mcr_path)
    result07.crash("c", ldl_saumon)
    result07.crash("c", ripply_spl)

    result07.meilleurTour(fct_theo)

    # final
    pt07 = result07.getPoints()

    """
    print(sortedDict(result07.getPoints()))
    """
    print(result07.getCircuit())
    for i in result07.getCourse():
        print(i.getGamertag(), i.getHistorique())


    result07.resetHist()

    ###################################################################################################
    # Course 8

    result08 = GrandPrix("Italie")

    qualif08 = [
        fct_adam,
        fct_theo,
        rp1_winterr,
        mclaren_d1_02, # RaavenBZH
        ert_niloboo,
        pur_voltha,
        rp1_okwaru,
        ripply_spl,
        vinboy,
        shz_noctis,
        ldl_oli,
        ldl_saumon,
        rp1_chadoo,
        mcr_path,
        pur_varane,
        pur_rosberg,
        xrt_arthur,
        haas_d1_01, # PuR Vincent
        haas_d1_02, # O2 Oxygen
        mcr_jayrko
    ]

    course08 = [
        pur_varane,
        fct_adam,
        ert_niloboo,
        fct_theo,
        ldl_oli,
        vinboy,
        xrt_arthur,
        ldl_saumon,
        haas_d1_01,
        pur_voltha,
        mclaren_d1_02,
        mcr_path,
        mcr_jayrko,
        ripply_spl,
        pur_rosberg,
        rp1_chadoo,
        haas_d1_02,
        rp1_winterr,
        shz_noctis,
        rp1_okwaru
    ]

    # classements
    result08.resultat("q", qualif08)
    result08.resultat("c", course08)

    result08.calcPointsQ()
    result08.calcPointsC()

    # evenements ponctuels
    result08.crash("q", pur_varane)
    result08.crash("q", shz_noctis)
    
    result08.crash("c", rp1_chadoo)
    result08.crash("c", haas_d1_02)
    result08.crash("c", rp1_winterr)
    result08.crash("c", shz_noctis)
    result08.crash("c", rp1_okwaru)

    result08.meilleurTour(fct_theo)

    # final
    pt08 = result08.getPoints()

    """
    print(sortedDict(result08.getPoints()))
    """
    print(result08.getCircuit())
    for i in result08.getCourse():
        print(i.getGamertag(), i.getHistorique())


    result08.resetHist()

    ###################################################################################################
    # Course 9

    result09 = GrandPrix("Barhein")

    qualif09 = [
        fct_theo,
        ert_niloboo,
        rp1_winterr,
        mclaren_d1_02,
        rp1_okwaru,
        pur_voltha,
        pur_varane,
        ldl_oli,
        vinboy,
        ripply_spl,
        shz_noctis, # remplacé par O2 Oxygen
        rp1_chadoo, # remplacé par Lowky
        ldl_saumon,
        pur_rosberg,
        xrt_arthur,
        mcr_jayrko,
        mcr_path,
        haas_d1_01, # remplacé par Pur Vincent
        haas_d1_02, # remplacé par XRT Darkfly
        fct_adam
    ]

    course09 = [
        ert_niloboo,
        fct_theo,
        rp1_winterr,
        rp1_okwaru,
        ldl_oli,
        vinboy,
        pur_rosberg,
        rp1_chadoo,
        shz_noctis,
        xrt_arthur,
        haas_d1_01,
        mcr_jayrko,
        ldl_saumon,
        fct_adam,
        mclaren_d1_02,
        pur_varane,
        ripply_spl,
        pur_voltha,
        haas_d1_02,
        mcr_path
    ]

    # classements
    result09.resultat("q", qualif09)
    result09.resultat("c", course09)

    result09.calcPointsQ()
    result09.calcPointsC()

    # evenements ponctuels
    result09.crash("q", mcr_path)
    result09.crash("q", ripply_spl)

    result09.crash("c", mclaren_d1_02)
    result09.crash("c", pur_varane)
    result09.crash("c", ripply_spl)
    result09.crash("c", pur_voltha)
    result09.crash("c", haas_d1_02)
    result09.crash("c", mcr_path)

    result09.meilleurTour(fct_adam)

    # final
    pt09 = result09.getPoints()

    """
    print(sortedDict(result09.getPoints()))
    """
    print(result09.getCircuit())
    for i in result09.getCourse():
        print(i.getGamertag(), i.getHistorique())


    result09.resetHist()

    ###############################################################################################
    
    final = sumDict(pt01, pt02)
    final = sumDict(final, pt03)
    final = sumDict(final, pt04)
    final = sumDict(final, pt05)
    final = sumDict(final, pt06)
    final = sumDict(final, pt07)
    final = sumDict(final, pt08)
    final = sumDict(final, pt09)
    
    print(sortedDict(final))

    return final