from packageF1.Ecurie import *
from packageF1.Pilote import *
from packageF1.GrandPrix import *

#
# Saison 7
#
# Calcul des points pour les pilotes de division 2
#

def getPointsD2() -> dict:

    # Création des équipes

    Mercedes = Ecurie("Mercedes")
    RedBull = Ecurie("RedBull")
    Ferrari = Ecurie("Ferrari")
    McLaren = Ecurie("McLaren")
    Alpine = Ecurie("Alpine")
    AlphaTauri = Ecurie("AlphaTauri")
    AstonMartin = Ecurie("AstonMartin")
    Williams = Ecurie("Williams")
    AlfaRomeo = Ecurie("AlfaRomeo")
    Haas = Ecurie("Haas")

    # Création des pilotes

    pur_vincent = Pilote("PuR Vincent", Mercedes)
    mvt_thomas = Pilote("MVT Thomas", Mercedes)
    pur_ripply = Pilote("PuR Ripply", RedBull)
    ert_flyart = Pilote("ERT Flyart", RedBull)
    pur_nygraal = Pilote("PuR Nygraal", Ferrari)
    pur_racing = Pilote("PuR Racing", Ferrari)
    rp1_tribion = Pilote("RP1 Tribion", McLaren)
    heroziah = Pilote("Heroziah", McLaren)
    xrt_darkfly = Pilote("XRT Darkfly", Alpine)
    rp1_gachette = Pilote("RP1 Gachette", Alpine)
    if1_supreme = Pilote("iF1 Supr3me", AlphaTauri)
    ldl_zepro = Pilote("LDL Zepro", AlphaTauri)
    mcr_spacex = Pilote("MCR SpaceX", AstonMartin)
    fct_deadpool = Pilote("FcT Deadpool", AstonMartin)
    rp1_owain = Pilote("RP1 Owain", Williams)
    ecs_finesse = Pilote("ECS Finesse", Williams)
    ert_aurelius = Pilote("ERT Aurelius", AlfaRomeo)
    fct_lasouche = Pilote("FcT LaSouche", AlfaRomeo)
    yozana = Pilote("Yozana", Haas)
    pura_tomoe = Pilote("PuRa Tomoe", Haas)

    ###############################################################################################

    # Course 1
    gp01 = GrandPrix("RoyaumeUni", sprint = False)

    # Remplaçants
    ert_niloboo_01 = Pilote("ERT Flyart", RedBull)
    istoozen_eko_01 = Pilote("LDL Zepro", AlphaTauri)

    # Pénalites en qualification
    # Aucune

    q01 = [
        mvt_thomas,
        pur_nygraal,
        pur_ripply,
        pur_racing,
        ert_niloboo_01,
        rp1_tribion,
        ert_aurelius,
        fct_lasouche,
        yozana,
        fct_deadpool,
        pura_tomoe,
        rp1_gachette,
        mcr_spacex,
        pur_vincent,
        if1_supreme,
        xrt_darkfly,
        rp1_owain,
        heroziah,
        ecs_finesse,
        istoozen_eko_01
    ]
    c01 = [
        mvt_thomas,
        pur_nygraal,
        pur_ripply,
        ert_aurelius,
        ert_niloboo_01,
        mcr_spacex,
        yozana,
        xrt_darkfly,
        pura_tomoe,
        pur_vincent,
        rp1_tribion,
        if1_supreme,
        fct_lasouche,
        fct_deadpool,
        istoozen_eko_01,
        rp1_gachette,
        rp1_owain,
        ecs_finesse,
        heroziah,
        pur_racing
    ]

    gp01.setQualification(q01)
    gp01.setCourse(c01)
    gp01.calcul(abandonsCourse=3)

    final = gp01.getPoints()

    return final