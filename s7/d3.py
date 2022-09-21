from packageF1.Ecurie import *
from packageF1.Pilote import *
from packageF1.GrandPrix import *

#
# Saison 7
#
# Calcul des points pour les pilotes de division 2
#

def getPointsD3() -> dict:

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

    pur_ilton = Pilote("PuR Ilton", Mercedes)
    fct_coco = Pilote("FcT Coco", Mercedes)
    rp1_skyzzz = Pilote("RP1 Skyzzz", RedBull)
    non4me_cami = Pilote("NoN4me Cami", RedBull)
    non4me_livai = Pilote("NoN4me Livai", Ferrari)
    f1m_alexgt500 = Pilote("F1M AlexGT500", Ferrari)
    pura_jager = Pilote("PuRa Jager", McLaren)
    pur_ultraaa = Pilote("PuR Ultraaa", McLaren)
    xrt_nico2a = Pilote("XRT Nico2a", Alpine)
    ert_karanox = Pilote("ERT Karanox", Alpine)
    xrt_marth = Pilote("XRT Marth", AlphaTauri)
    str_pagaa = Pilote("STR Pagaa", AlphaTauri)
    non4me_jordy = Pilote("NoN4me Jordy", AstonMartin)
    fct_specktre = Pilote("FcT Specktre", AstonMartin)
    rp1_ice = Pilote("RP1 Ice", Williams)
    rp1_durtom = Pilote("RP1 Durtom", Williams)
    ert_matfax = Pilote("ERT Matfax", AlfaRomeo)
    non4me_geckoz = Pilote("NoN4me Geckoz", AlfaRomeo)
    fct_tweekaz = Pilote("FcT Tweekaz", Haas)
    non4me_cramer = Pilote("NoN4me Cramer", Haas)

    ###############################################################################################

    # Course 1
    gp01 = GrandPrix("RoyaumeUni", sprint = False)

    # Remplaçants
    istoozen_eko_01 = Pilote("PuR Ilton", Mercedes)
    mcr_papyx_01 = Pilote("F1M AlexGT500", Ferrari)
    shadd_01 = Pilote("XRT Marth", AlphaTauri)

    # Pénalites en qualification
    # Aucune

    q01 = [
        non4me_cramer,
        fct_tweekaz,
        non4me_jordy,
        rp1_skyzzz,
        ert_matfax,
        non4me_geckoz,
        rp1_ice,
        non4me_cami,
        pura_jager,
        non4me_livai,
        pur_ultraaa,
        fct_coco,
        rp1_durtom,
        str_pagaa,
        ert_karanox,
        istoozen_eko_01,
        fct_specktre,
        xrt_nico2a,
        mcr_papyx_01,
        shadd_01
    ]
    c01 = [
        rp1_skyzzz,
        ert_matfax,
        fct_tweekaz,
        rp1_ice,
        str_pagaa,
        non4me_jordy,
        fct_specktre,
        pura_jager,
        rp1_durtom,
        non4me_cami,
        xrt_nico2a,
        shadd_01,
        ert_karanox,
        mcr_papyx_01,
        non4me_cramer,
        non4me_geckoz,
        fct_coco,
        pur_ultraaa,
        istoozen_eko_01,
        non4me_livai
    ]

    gp01.setQualification(q01)
    gp01.setCourse(c01)
    gp01.calcul(abandonsCourse = 3)

    
    # for i in gp01.getCourse():
    #     print(i.getDonnees().stats())


    final = gp01.getPoints()

    return final