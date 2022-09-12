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
    if1_supreme = Pilote("IF1 Supreme", AlphaTauri)
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