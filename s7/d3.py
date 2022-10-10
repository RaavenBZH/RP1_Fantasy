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

    ###############################################################################################

    # Course 2
    gp02 = GrandPrix("Belgique", sprint = True)

    # Remplaçants
    non4me_stuno_02 = Pilote("NoN4me Cramer", Haas)

    # Pénalites en qualification
    # Aucune

    q02 = [
        f1m_alexgt500,
        non4me_stuno_02,
        non4me_geckoz,
        rp1_skyzzz,
        pur_ilton,
        non4me_cami,
        rp1_ice,
        fct_tweekaz,
        ert_matfax,
        str_pagaa,
        non4me_jordy,
        non4me_livai,
        pura_jager,
        xrt_marth,
        pur_ultraaa,
        fct_coco,
        fct_specktre,
        rp1_durtom,
        xrt_nico2a,
        ert_karanox
    ]
    s02 = [
        f1m_alexgt500,
        non4me_geckoz,
        non4me_cami,
        pur_ilton,
        ert_matfax,
        rp1_ice,
        pura_jager,
        rp1_skyzzz,
        pur_ultraaa,
        non4me_livai,
        rp1_durtom,
        xrt_marth,
        ert_karanox,
        fct_specktre,
        non4me_jordy,
        fct_coco,
        xrt_nico2a,
        fct_tweekaz,
        non4me_stuno_02,
        str_pagaa
    ]
    c02 = [
        f1m_alexgt500,
        pur_ilton,
        ert_matfax,
        non4me_geckoz,
        pur_ultraaa,
        non4me_livai,
        rp1_ice,
        fct_coco,
        pura_jager,
        non4me_jordy,
        fct_specktre,
        rp1_skyzzz,
        rp1_durtom,
        xrt_nico2a,
        non4me_cami,
        non4me_stuno_02,
        ert_karanox,
        str_pagaa,
        fct_tweekaz,
        xrt_marth
    ]

    gp02.setQualification(q02)
    gp02.setSprint(s02)
    gp02.setCourse(c02)
    gp02.calcul(abandonsSprint = 2, abandonsCourse=5)

    ###############################################################################################

    # Course 3
    gp03 = GrandPrix("Espagne", sprint = False)

    # Remplaçants
    # Aucun
    
    # Pénalités
    # Aucune

    q03 = [
        non4me_cramer,
        ert_matfax,
        non4me_geckoz,
        rp1_skyzzz,
        rp1_ice,
        f1m_alexgt500,
        non4me_cami,
        non4me_livai,
        fct_coco,
        str_pagaa,
        fct_tweekaz,
        xrt_nico2a,
        pur_ultraaa,
        fct_specktre,
        ert_karanox,
        xrt_marth,
        rp1_durtom,
        non4me_jordy,
        pur_ilton,
        pura_jager
    ]
    c03 = [
        ert_matfax,
        non4me_cramer,
        rp1_skyzzz,
        non4me_geckoz,
        f1m_alexgt500,
        fct_coco,
        rp1_ice,
        non4me_livai,
        str_pagaa,
        fct_tweekaz,
        fct_specktre,
        rp1_durtom,
        non4me_cami,
        ert_karanox,
        xrt_nico2a,
        non4me_jordy,
        pur_ilton,
        pura_jager,
        xrt_marth,
        pur_ultraaa
    ]

    gp03.setQualification(q03)
    gp03.setCourse(c03)
    gp03.calcul(abandonsCourse = 4)

    ###############################################################################################

    # Course 4 
    gp04 = GrandPrix("Miami", sprint = False)

    # Remplaçants
    wanbmt63_04 = Pilote("F1M AlexGT500", Ferrari)
    
    # Pénalités
    # Aucune

    q04 = [
        non4me_geckoz,
        pur_ilton,
        non4me_cramer,
        ert_matfax,
        ert_karanox,
        pur_ultraaa,
        f1m_alexgt500,
        rp1_skyzzz,
        non4me_jordy,
        rp1_ice,
        pura_jager,
        str_pagaa,
        non4me_cami,
        fct_tweekaz,
        xrt_marth,
        fct_coco,
        xrt_nico2a,
        fct_specktre,
        wanbmt63_04,
        rp1_durtom
    ]
    c04 = [
        non4me_geckoz,
        non4me_cramer,
        f1m_alexgt500,
        non4me_cami,
        str_pagaa,
        ert_matfax,
        non4me_jordy,
        pur_ilton,
        xrt_nico2a,
        fct_coco,
        rp1_ice,
        rp1_durtom,
        ert_karanox,
        pura_jager,
        fct_specktre,
        fct_tweekaz,
        wanbmt63_04,
        pur_ultraaa,
        rp1_skyzzz,
        xrt_marth
    ]

    gp04.setQualification(q04)
    gp04.setCourse(c04)
    gp04.calcul(abandonsCourse = 3)

    ###############################################################################################

    final = gp01.getPoints()
    final = sumDict(final, gp02.getPoints())
    final = sumDict(final, gp03.getPoints())
    final = sumDict(final, gp04.getPoints())

    return final