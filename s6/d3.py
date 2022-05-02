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
    ert_wartors = Pilote("ERT Wartors", "Mercedes")

    non4me_cami = Pilote("Non4me Cami", "RedBull")
    soo_skyzzz = Pilote("Soo Skyzzz", "RedBull")

    knacki_ball = Pilote("Knacki Ball", "McLaren")
    pur_marth = Pilote("PuR Marth", "McLaren") 

    pur_nygraal = Pilote("PuR Nygraal", "Ferrari")
    chr_olivz = Pilote("CHR Olivz", "Ferrari") 

    eroziah_spl = Pilote("EroziaH SPL", "AlphaTauri")
    ert_mirage = Pilote("ERT Mirage", "AlphaTauri") 

    rp1_fifi = Pilote("RP1 Fifi", "Alpine")
    ducpascharlie = Pilote("DucPasCharlie", "Alpine")

    rp1_gachette = Pilote("RP1 Gachette", "AstonMartin")
    istoozen_eko = Pilote("Istoozen eKo", "AstonMartin")

    sks_flyart = Pilote("SKS Flyart", "AlfaRomeo")
    mcr_papyx = Pilote("MCR Papyx", "AlfaRomeo")

    ert_aurelius = Pilote("ERT Aurelius", "Williams")
    ert_matfax = Pilote("ERT Matfax", "Williams")

    alexgt500 = Pilote("AlexGT500", "Haas")
    ert_toon = Pilote("ERT Toon", "Haas") 

    ###################################################################################################
    # Course 1

    result01 = GrandPrix("Autriche")

    qualif01 = [
        knacki_ball,
        ducpascharlie,
        istoozen_eko,
        non4me_cami,
        ecs_finesse,
        soo_skyzzz,
        ert_matfax,
        pur_marth, # remplacé par LTR Coach
        pur_nygraal,
        ert_aurelius,
        alexgt500,
        chr_olivz, # remplacé par Yozana
        ert_toon, # remplacé par QRL Blanco
        ert_mirage, # remplacé par Pur Ultraaa
        sks_flyart,
        ert_wartors,
        mcr_papyx,
        rp1_fifi,
        eroziah_spl,
        rp1_gachette
    ]

    course01 = [
        knacki_ball,
        eroziah_spl,
        ert_wartors, 
        mcr_papyx,
        pur_marth,
        ert_mirage,
        soo_skyzzz,
        chr_olivz,
        alexgt500,
        ert_aurelius,
        ecs_finesse,
        rp1_gachette,
        ducpascharlie,
        rp1_fifi,
        non4me_cami,  
        ert_toon,
        ert_matfax,
        istoozen_eko,
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
    result01.crash("c", istoozen_eko)
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
        ert_wartors, # remplacé par RP1 Ice
        rp1_fifi, # remplacé par XRT Alpha
        ducpascharlie,
        knacki_ball,
        chr_olivz, # remplacé par Yozana
        alexgt500,
        ert_matfax,
        sks_flyart,
        ecs_finesse,
        eroziah_spl,
        istoozen_eko, # remplacé par RP1 Durtom
        rp1_gachette,
        ert_toon, # remplacé par QRL Blanco
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
        ert_wartors,
        ert_toon,
        ert_mirage,
        ert_matfax,
        eroziah_spl,
        ducpascharlie,
        soo_skyzzz,
        alexgt500,
        knacki_ball,
        istoozen_eko
    ]

    # classements
    result02.resultat("q", qualif02)
    result02.resultat("c", course02)

    result02.calcPointsQ()
    result02.calcPointsC()

    # évènements ponctuels
    result02.crash("q", rp1_gachette)

    result02.crash("c", istoozen_eko)
    result02.crash("c", knacki_ball)
    result02.crash("c", alexgt500)
    result02.crash("c", soo_skyzzz)
    result02.crash("c", ducpascharlie)
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
    ]

    course03 = [
    ]

    # classements
    result03.resultat("q", qualif03)
    result03.resultat("c", course03)

    result03.calcPointsQ()
    result03.calcPointsC()

    # évènements ponctuels
    

    result03.meilleurTour()

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