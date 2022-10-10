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
    pur_thomas = Pilote("PuR Thomas", Mercedes)
    pur_ripply = Pilote("PuR Ripply", RedBull)
    ert_flyart = Pilote("ERT Flyart", RedBull)
    pur_nygraal = Pilote("PuR Voltha", Ferrari)
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
        pur_thomas,
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
        pur_thomas,
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

    ###############################################################################################

    # Course 2
    gp02 = GrandPrix("Belgique", sprint = True)

    # Remplaçants
    ert_niloboo_02 = Pilote("LDL Zepro", AlphaTauri)
    pura_jager_02 = Pilote("Heroziah", McLaren)
    rp1_woody_02 = Pilote("RP1 Owain", Williams)

    # Pénalites en qualification
    # Aucune

    q02 = [
        pur_thomas,
        pur_nygraal,
        pur_racing,
        ert_niloboo_02,
        ert_aurelius,
        pur_ripply,
        fct_lasouche,
        mcr_spacex,
        rp1_tribion,
        yozana,
        xrt_darkfly,
        fct_deadpool,
        pura_tomoe,
        pur_vincent,
        pura_jager_02,
        ecs_finesse,
        rp1_gachette,
        rp1_woody_02,
        ert_flyart,
        if1_supreme
    ]
    s02 = [
        pur_nygraal,
        pur_thomas,
        ert_niloboo_02,
        pur_ripply,
        pur_racing,
        yozana,
        pur_vincent,
        pura_jager_02,
        if1_supreme,
        pura_tomoe,
        rp1_woody_02,
        ert_flyart,
        ecs_finesse,
        rp1_tribion,
        ert_aurelius,
        mcr_spacex,
        xrt_darkfly,
        fct_deadpool,
        rp1_gachette,
        fct_lasouche
    ]
    c02 = [
        pur_nygraal,
        pur_thomas,
        pur_racing,
        rp1_tribion,
        yozana,
        ert_aurelius,
        ert_niloboo_02,
        if1_supreme,
        rp1_woody_02,
        pura_tomoe,
        pur_ripply,
        pur_vincent,
        ert_flyart,
        fct_deadpool,
        mcr_spacex,
        xrt_darkfly,
        pura_jager_02,
        fct_lasouche,
        ecs_finesse,
        rp1_gachette
    ]

    gp02.setQualification(q02)
    gp02.setSprint(s02)
    gp02.setCourse(c02)
    gp02.calcul(abandonsSprint=2, abandonsCourse=6)

    ###############################################################################################

    # Course 3
    gp03 = GrandPrix("Espagne", sprint = False)

    # Remplaçants
    ase_luisnts1 = Pilote("RP1 Owain", Williams)
    pur_voltha_03 = Pilote("LDL Zepro", AlphaTauri)
    pura_jager_03 = Pilote("Heroziah", McLaren)
    non4me_cramer_03 = Pilote("Yozana", Haas)
    f1m_alexgt500_03 = Pilote("PuR Nygraal", Ferrari)
    
    # Pénalités
    # Aucune

    q03 = [
        pur_thomas,
        pur_racing,
        ase_luisnts1,
        pur_voltha_03,
        pur_vincent,
        rp1_tribion,
        pur_ripply,
        fct_lasouche,
        pura_jager_03,
        non4me_cramer_03,
        f1m_alexgt500_03,
        ert_aurelius,
        xrt_darkfly,
        fct_deadpool,
        ecs_finesse,
        mcr_spacex,
        pura_tomoe,
        if1_supreme,
        rp1_gachette,
        ert_flyart
    ]
    c03 = [
        ase_luisnts1,
        pur_thomas,
        non4me_cramer_03,
        ert_aurelius,
        xrt_darkfly,
        pur_vincent,
        pur_ripply,
        pura_jager_03,
        ecs_finesse,
        rp1_gachette,
        pura_tomoe,
        f1m_alexgt500_03,
        rp1_tribion,
        mcr_spacex,
        ert_flyart,
        fct_deadpool,
        pur_voltha_03,
        if1_supreme,
        fct_lasouche,
        pur_racing
    ]

    gp03.setQualification(q03)
    gp03.setCourse(c03)
    gp03.calcul(abandonsCourse=9)

    ###############################################################################################

    # Course 4
    gp04 = GrandPrix("Miami", sprint = False)

    # Remplaçants
    pur_voltha = Pilote("PuR Voltha", Ferrari)
    ert_niloboo_04 = Pilote("LDL Zepro", AlphaTauri)
    pura_jager_04 = Pilote("RP1 Tribion", McLaren)
    istoozen_eko_04 = Pilote("RP1 Owain", Williams)
    mirage9150_04 = Pilote("FcT Deadpool", AstonMartin)
    
    # Pénalités
    # rp1_gachette : 5 places de pénalité
    # pur_vincent : 5 places de pénalité

    q04 = [
        pur_thomas,
        pur_racing,
        ert_aurelius,
        pur_voltha,
        yozana,
        ert_niloboo_04,
        pur_ripply,
        if1_supreme,
        pura_jager_04,
        pura_tomoe,
        istoozen_eko_04,
        ecs_finesse,
        heroziah,
        pur_vincent,
        mirage9150_04,
        xrt_darkfly,
        mcr_spacex,
        ert_flyart,
        fct_lasouche,
        rp1_gachette
    ]
    c04 = [
        pur_racing,
        ert_niloboo_04,
        pur_vincent,
        ert_aurelius,
        pura_tomoe,
        fct_lasouche,
        if1_supreme,
        xrt_darkfly,
        istoozen_eko_04,
        mcr_spacex,
        mirage9150_04,
        yozana,
        ecs_finesse,
        pura_jager_04,
        ert_flyart,
        rp1_gachette,
        pur_ripply,
        pur_voltha,
        pur_thomas,
        heroziah
    ]

    gp04.setQualification(q04)
    gp04.setCourse(c04)
    gp04.calcul(abandonsCourse=3)

    ###############################################################################################

    final = gp01.getPoints()
    final = sumDict(final, gp02.getPoints())
    final = sumDict(final, gp03.getPoints())
    final = sumDict(final, gp04.getPoints())

    return final