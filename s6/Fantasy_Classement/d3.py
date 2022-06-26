from packageF1.Pilote import *
from packageF1.GrandPrix import *
from packageF1.Joueur import *
from packageF1.EnsembleJoueur import *
from packageF1.fonctions import *

#
# Saison 6
#
# Calcul des points pour les pilotes de division 3
#

def getPointsD3() -> dict:

    ###################################################################################################

    # Création des pilotes

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    ecs_finesse = Pilote("ECS Finesse", "Mercedes")
    non4me_geckozz = Pilote("Non4me Geckozz", "Mercedes")

    non4me_cami = Pilote("Non4me Cami", "RedBull")
    soo_skyzzz = Pilote("Soo Skyzzz", "RedBull")

    knacki_ball = Pilote("Knacki Ball", "McLaren")
    pur_marth = Pilote("PuR Marth", "McLaren") 

    pur_nygraal = Pilote("PuR Nygraal", "Ferrari")
    chr_olivz = Pilote("CHR Olivz", "Ferrari") 

    eroziah_spl = Pilote("EroziaH SPL", "AlphaTauri")
    ert_mirage = Pilote("ERT Mirage", "AlphaTauri") 

    rp1_fifi = Pilote("RP1 Fifi", "Alpine")
    non4me_sanzz = Pilote("Non4me Sanzz", "Alpine")

    rp1_gachette = Pilote("RP1 Gachette", "AstonMartin")
    if1_supr3me = Pilote("iF1 Supr3me", "AstonMartin")

    sks_flyart = Pilote("SKS Flyart", "AlfaRomeo")
    mcr_papyx = Pilote("MCR Papyx", "AlfaRomeo")

    ert_aurelius = Pilote("ERT Aurelius", "Williams")
    ert_matfax = Pilote("ERT Matfax", "Williams")

    ldl_shermy = Pilote("LDL Shermy", "Haas")
    vmlf_zer = Pilote("VMLF Zer", "Haas") 

    ###################################################################################################
    # Course 1

    result01 = GrandPrix("Autriche")

    qualif01 = [
        knacki_ball,
        non4me_sanzz,
        if1_supr3me,
        non4me_cami,
        ecs_finesse,
        soo_skyzzz,
        ert_matfax,
        pur_marth, # remplacé par LTR Coach
        pur_nygraal,
        ert_aurelius,
        ldl_shermy,
        chr_olivz, # remplacé par Yozana
        vmlf_zer, # remplacé par QRL Blanco
        ert_mirage, # remplacé par Pur Ultraaa
        sks_flyart,
        non4me_geckozz,
        mcr_papyx,
        rp1_fifi,
        eroziah_spl,
        rp1_gachette
    ]

    course01 = [
        knacki_ball,
        eroziah_spl,
        non4me_geckozz, 
        mcr_papyx,
        pur_marth,
        ert_mirage,
        soo_skyzzz,
        chr_olivz,
        ldl_shermy,
        ert_aurelius,
        ecs_finesse,
        rp1_gachette,
        non4me_sanzz,
        rp1_fifi,
        non4me_cami,  
        vmlf_zer,
        ert_matfax,
        if1_supr3me,
        pur_nygraal,
        sks_flyart
    ]

    # classements
    result01.resultat("q", qualif01)
    result01.resultat("c", course01)

    result01.calcPointsQ()
    result01.calcPointsC()

    # évènements ponctuels
    result01.crash("q", sks_flyart)
    result01.crash("q", eroziah_spl)
    result01.crash("q", rp1_gachette)
    result01.crash("q", soo_skyzzz)

    result01.crash("c", sks_flyart)
    result01.crash("c", pur_nygraal)
    result01.crash("c", if1_supr3me)
    result01.crash("c", ert_matfax)

    result01.meilleurTour(rp1_gachette)

    # final
    pt01 = result01.getPoints()

    """
    print(sortedDict(result01.getPoints()))
    
    for i in result01.getCourse():
        print(i.getGamertag(), i.getHistorique())
    """
    
    # Ideal : Knacki Ball, ERT Wartors, MCR Papyx

    result01.resetHist()

    ###################################################################################################
    # Course 2

    result02 = GrandPrix("Chine")

    qualif02 = [
        ert_aurelius,
        pur_nygraal,
        soo_skyzzz,
        non4me_geckozz, # remplacé par RP1 Ice
        rp1_fifi, # remplacé par XRT Alpha
        non4me_sanzz,
        knacki_ball,
        chr_olivz, # remplacé par Yozana
        ldl_shermy,
        ert_matfax,
        sks_flyart,
        ecs_finesse,
        eroziah_spl,
        if1_supr3me, # remplacé par RP1 Durtom
        rp1_gachette,
        vmlf_zer, # remplacé par QRL Blanco
        non4me_cami,
        ert_mirage,
        mcr_papyx,
        pur_marth
    ]

    course02 = [
        pur_nygraal,
        ert_aurelius,
        sks_flyart,
        ecs_finesse,
        chr_olivz,
        rp1_fifi,
        pur_marth,
        mcr_papyx,
        rp1_gachette,
        non4me_cami,
        non4me_geckozz,
        vmlf_zer,
        ert_mirage,
        ert_matfax,
        eroziah_spl,
        non4me_sanzz,
        soo_skyzzz,
        ldl_shermy,
        knacki_ball,
        if1_supr3me
    ]

    # classements
    result02.resultat("q", qualif02)
    result02.resultat("c", course02)

    result02.calcPointsQ()
    result02.calcPointsC()

    # évènements ponctuels
    result02.crash("q", rp1_gachette)

    result02.crash("c", if1_supr3me)
    result02.crash("c", knacki_ball)
    result02.crash("c", ldl_shermy)
    result02.crash("c", soo_skyzzz)
    result02.crash("c", non4me_sanzz)
    result02.crash("c", eroziah_spl,)
    result02.crash("c", ert_matfax)
    result02.crash("c", ert_mirage)

    result02.meilleurTour(ert_mirage)

    # final
    pt02 = result02.getPoints()

    """
    print(sortedDict(result02.getPoints()))
    
    for i in result02.getCourse():
        print(i.getGamertag(), i.getHistorique())
    """

    # Ideal : ECS Finesse, SKS Flyart, PuR Marth

    result02.resetHist()

    ###################################################################################################
    # Course 3

    result03 = GrandPrix("Imola")

    qualif03 = [
        pur_nygraal,
        ldl_shermy,
        ert_aurelius,
        vmlf_zer,
        if1_supr3me,
        ecs_finesse,
        chr_olivz,
        pur_marth, # remplacé par LTR Coach
        soo_skyzzz,
        knacki_ball,
        ert_matfax, # remplacé par ERT Apollo
        non4me_cami,
        sks_flyart,
        eroziah_spl,
        non4me_sanzz,
        non4me_geckozz,
        ert_mirage,
        rp1_gachette,
        mcr_papyx,
        rp1_fifi
    ]

    course03 = [
        ert_aurelius,
        vmlf_zer,
        pur_nygraal,
        ldl_shermy,
        ecs_finesse,
        non4me_cami,
        ert_mirage,
        chr_olivz,
        non4me_geckozz,
        if1_supr3me,
        rp1_gachette,
        soo_skyzzz,
        non4me_sanzz,
        sks_flyart,
        mcr_papyx,
        rp1_fifi,
        knacki_ball,
        ert_matfax, # remplacé par ERT Apollo
        eroziah_spl,
        pur_marth # remplacé par LTR Coach
    ]

    # classements
    result03.resultat("q", qualif03)
    result03.resultat("c", course03)

    result03.calcPointsQ()
    result03.calcPointsC()

    # évènements ponctuels
    result03.crash("q", knacki_ball)

    result03.crash("c", pur_marth)
    result03.crash("c", eroziah_spl)
    result03.crash("c", ert_matfax)
    result03.crash("c", knacki_ball)

    result03.meilleurTour(soo_skyzzz)

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
        ldl_shermy,
        rp1_gachette,
        ert_aurelius,
        non4me_geckozz, # rempalcé par Non4meGeckoz
        chr_olivz,
        ert_matfax,
        non4me_cami,
        ecs_finesse,
        knacki_ball, # remplacé par Pur Ultraaa
        eroziah_spl,
        non4me_sanzz,
        ert_mirage,
        if1_supr3me, # remplacé par Jancker 21
        mcr_papyx,
        sks_flyart,
        pur_marth,
        rp1_fifi,
        vmlf_zer, # remplacé par iF1 Supreme        
        pur_nygraal,
        soo_skyzzz
    ]

    course04 = [
        ldl_shermy,
        ert_aurelius,
        ert_matfax,
        rp1_gachette,
        non4me_cami,
        non4me_geckozz,
        non4me_sanzz,
        sks_flyart,
        mcr_papyx,
        if1_supr3me,
        ecs_finesse,
        rp1_fifi,
        soo_skyzzz,
        chr_olivz,
        vmlf_zer,
        pur_nygraal,
        eroziah_spl,
        ert_mirage,
        knacki_ball,
        pur_marth
    ]

    # classements
    result04.resultat("q", qualif04)
    result04.resultat("c", course04)

    result04.calcPointsQ()
    result04.calcPointsC()

    # évènements ponctuels
    result04.crash("q", soo_skyzzz)
    result04.crash("q", sks_flyart)

    result04.crash("c",pur_marth)
    result04.crash("c",knacki_ball)
    result04.crash("c",ert_mirage)
    result04.crash("c",eroziah_spl)
    result04.crash("c",pur_nygraal)
    result04.crash("c",vmlf_zer)

    result04.meilleurTour(chr_olivz)

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
        pur_nygraal,
        non4me_geckozz, # remplacé par Non4meGeckoz
        ert_aurelius,
        ert_matfax,
        soo_skyzzz,
        non4me_cami,
        if1_supr3me,
        sks_flyart, # remplacé par LDL ZePro
        ldl_shermy,
        non4me_sanzz,
        ecs_finesse,
        ert_mirage, # remplacé par PuR Ultraaa
        pur_marth,
        vmlf_zer,
        eroziah_spl,
        rp1_gachette,
        knacki_ball,
        chr_olivz,
        mcr_papyx,
        rp1_fifi
    ]

    course05 = [
        knacki_ball,
        soo_skyzzz,
        ldl_shermy,
        ert_matfax,
        ert_aurelius,
        chr_olivz,
        ecs_finesse,
        ert_mirage,
        pur_nygraal,
        if1_supr3me,
        non4me_geckozz,
        rp1_fifi,
        mcr_papyx,
        non4me_sanzz,
        rp1_gachette,
        non4me_cami,
        sks_flyart,
        pur_marth,
        eroziah_spl,
        vmlf_zer
    ]

    # classements
    result05.resultat("q", qualif05)
    result05.resultat("c", course05)

    result05.calcPointsQ()
    result05.calcPointsC()

    # évènements ponctuels
    result05.crash("q", rp1_fifi)
    result05.crash("q", pur_marth)
    result05.crash("q", eroziah_spl)

    result05.crash("c", vmlf_zer)
    result05.crash("c", eroziah_spl)
    result05.crash("c", pur_marth)
    result05.crash("c", sks_flyart)
    result05.crash("c", non4me_cami)
    result05.crash("c", rp1_gachette)
    result05.crash("c", non4me_sanzz)

    result05.meilleurTour(ert_matfax)

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
        pur_nygraal,
        soo_skyzzz,
        ert_matfax,
        ldl_shermy,
        ert_aurelius,
        eroziah_spl,
        ecs_finesse,
        non4me_sanzz,
        chr_olivz,
        sks_flyart, # remplacé par Non4me STUNO
        pur_marth,
        ert_mirage,
        knacki_ball, # remplacé par LTR Coach
        if1_supr3me,
        non4me_geckozz,
        vmlf_zer,
        rp1_gachette,
        mcr_papyx,
        rp1_fifi,
        non4me_cami
    ]

    course06 = [
        pur_nygraal,
        eroziah_spl,
        vmlf_zer,
        rp1_gachette,
        mcr_papyx,
        non4me_cami,
        ecs_finesse,
        non4me_sanzz,
        ldl_shermy,
        chr_olivz,
        rp1_fifi,
        sks_flyart,
        ert_matfax,
        ert_aurelius,
        knacki_ball,
        soo_skyzzz,
        pur_marth,
        ert_mirage,
        non4me_geckozz,
        if1_supr3me
    ]

    # classements
    result06.resultat("q", qualif06)
    result06.resultat("c", course06)

    result06.calcPointsQ()
    result06.calcPointsC()

    # evenements ponctuels
    result06.crash("q", non4me_cami)
    result06.crash("q", non4me_geckozz)
    result06.crash("q", if1_supr3me)
    result06.crash("q", sks_flyart)
    result06.crash("q", chr_olivz)
    result06.crash("q", non4me_sanzz)

    result06.crash("q", if1_supr3me)
    result06.crash("q", non4me_geckozz)
    result06.crash("q", ert_mirage)
    result06.crash("q", pur_marth)
    result06.crash("q", soo_skyzzz)
    result06.crash("q", knacki_ball)
    result06.crash("q", ert_aurelius)
    result06.crash("q", ert_matfax)

    result06.meilleurTour(pur_nygraal)

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
        soo_skyzzz,
        pur_nygraal,
        ldl_shermy,
        ert_aurelius,
        ecs_finesse,
        if1_supr3me,
        knacki_ball,
        ert_matfax,
        chr_olivz,
        non4me_geckozz,
        ert_mirage,
        non4me_cami,
        pur_marth,
        mcr_papyx,
        rp1_gachette,
        rp1_fifi,
        eroziah_spl,
        sks_flyart,
        vmlf_zer,
        non4me_sanzz
    ]

    course07 = [
        pur_nygraal,
        ert_aurelius,
        soo_skyzzz,
        sks_flyart,
        ecs_finesse,
        if1_supr3me,
        non4me_cami,
        chr_olivz,
        mcr_papyx,
        ert_matfax,
        non4me_geckozz,
        rp1_gachette,
        eroziah_spl,
        rp1_fifi,
        knacki_ball,
        ldl_shermy,
        ert_mirage,
        vmlf_zer, # remplacé par LDL Shermy
        pur_marth,
        non4me_sanzz,
    ]


    # classements
    result07.resultat("q", qualif07)
    result07.resultat("c", course07)

    result07.calcPointsQ()
    result07.calcPointsC()

    # evenements ponctuels
    result07.crash("q", sks_flyart)
    result07.crash("q", non4me_cami)
    result07.crash("q", pur_marth)
    result07.crash("q", non4me_geckozz)
    result07.crash("q", knacki_ball)

    result07.crash("c", non4me_sanzz)
    result07.crash("c", pur_marth)
    result07.crash("c", vmlf_zer)
    result07.crash("c", ert_mirage)
    result07.crash("c", ldl_shermy)
    result07.crash("c", knacki_ball)
    result07.crash("c", rp1_fifi)
    result07.crash("c", eroziah_spl)
    result07.crash("c", rp1_gachette)
    result07.crash("c", non4me_geckozz)

    result07.meilleurTour(ert_matfax)

    # final
    pt07 = result07.getPoints()
    
    """
    print(sortedDict(result07.getPoints()))

    for i in result07.getCourse():
        print(i.getGamertag(), i.getHistorique())
    
    """

    # print(pt07)

    # Ideal :

    result07.resetHist()

    ###################################################################################################
    # Course 8

    result08 = GrandPrix("Italie")

    qualif08 = [
        ert_aurelius,
        knacki_ball,
        if1_supr3me,
        non4me_geckozz,
        rp1_fifi,
        pur_nygraal,
        chr_olivz,
        eroziah_spl,
        ert_mirage,
        soo_skyzzz,
        sks_flyart,
        rp1_gachette,
        non4me_cami,
        ecs_finesse,
        pur_marth,
        vmlf_zer,
        ert_matfax,
        ldl_shermy,
        mcr_papyx,
        non4me_sanzz
    ]

    course08 = [
        knacki_ball,
        ert_aurelius,
        non4me_cami,
        non4me_geckozz,
        if1_supr3me,
        pur_nygraal,
        chr_olivz,
        ert_mirage,
        ecs_finesse,
        ert_matfax, # remplacé par ERT Ricky
        pur_marth, # remplacé par LTR Coach
        rp1_gachette, # remplacé par RP1 Durtom
        vmlf_zer,
        ldl_shermy,
        rp1_fifi, # remplacé par XRT Alpha
        mcr_papyx,
        eroziah_spl,
        sks_flyart,
        soo_skyzzz,
        non4me_sanzz # remplacé par LDL Zepro
    ]
    # classements
    result08.resultat("q", qualif08)
    result08.resultat("c", course08)

    result08.calcPointsQ()
    result08.calcPointsC()

    # evenements ponctuels
    result08.crash("q", pur_marth)
    result08.crash("q", soo_skyzzz)

    result08.crash("c", rp1_fifi)
    result08.crash("c", mcr_papyx)
    result08.crash("c", eroziah_spl)
    result08.crash("c", sks_flyart)
    result08.crash("c", soo_skyzzz)
    result08.crash("c", non4me_sanzz)

    result08.meilleurTour(vmlf_zer)

    # final
    pt08 = result08.getPoints()

    """
    print(sortedDict(result08.getPoints()))

    for i in result08.getCourse():
        print(i.getGamertag(), i.getHistorique())
    """

    # Ideal :

    result08.resetHist()

    ###################################################################################################
    # Course 9

    result09 = GrandPrix("Barhein")

    qualif09 = [
        pur_nygraal,
        non4me_geckozz,
        soo_skyzzz,
        rp1_gachette,
        non4me_sanzz,
        ldl_shermy,
        ecs_finesse,
        ert_aurelius,
        ert_mirage,
        chr_olivz,
        ert_matfax,
        vmlf_zer,
        sks_flyart,
        non4me_cami,
        knacki_ball,
        if1_supr3me,
        rp1_fifi,
        eroziah_spl,
        pur_marth,
        mcr_papyx
    ]

    course09 = [
        pur_nygraal,
        non4me_geckozz,
        soo_skyzzz,
        ert_matfax,
        vmlf_zer,
        if1_supr3me,
        rp1_gachette,
        ecs_finesse,
        pur_marth, # remplacé par LTR Coach
        ert_aurelius,
        rp1_fifi,
        mcr_papyx,
        ldl_shermy, # remplacé par Non4me Stuno
        non4me_cami,
        ert_mirage,
        eroziah_spl,
        chr_olivz,
        non4me_sanzz, # remplacé par XRT Alpha
        knacki_ball,
        sks_flyart
    ]

    # classements
    result09.resultat("q", qualif09)
    result09.resultat("c", course09)

    result09.calcPointsQ()
    result09.calcPointsC()

    # evenements ponctuels
    result09.crash("c", mcr_papyx)

    result09.crash("c", sks_flyart)
    result09.crash("c", knacki_ball)
    result09.crash("c", non4me_sanzz)
    result09.crash("c", chr_olivz)

    result09.meilleurTour(non4me_sanzz)

    # final
    pt09 = result09.getPoints()

    """
    print(sortedDict(result09.getPoints()))
    
    for i in result09.getCourse():
        print(i.getGamertag(), i.getHistorique())
    """

    # Ideal :

    result09.resetHist()

    ###################################################################################################
    
    final = sumDict(pt01, pt02)
    final = sumDict(final, pt03)
    final = sumDict(final, pt04)
    final = sumDict(final, pt05)
    final = sumDict(final, pt06)
    final = sumDict(final, pt07)
    final = sumDict(final, pt08)
    final = sumDict(final, pt09)
    
    # print(sortedDict(final))

    return final