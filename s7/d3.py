from packageF1.Ecurie import *
from packageF1.Pilote import *
from packageF1.GrandPrix import *

import csv

#
# Saison 7
#
# Calcul des points pour les pilotes de division 2
#

def getPointsD3(stats = False) -> dict:

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
    xrt_marth = Pilote("Tonati2514", AlphaTauri) # remplaçé ... Tonati2514
    str_pagaa = Pilote("STR Pagaa", AlphaTauri)
    non4me_jordy = Pilote("NoN4me Jordy", AstonMartin)
    fct_specktre = Pilote("FcT Specktre", AstonMartin)
    rp1_ice = Pilote("RP1 Ice", Williams)
    rp1_durtom = Pilote("Istoozen Eko", Williams) # remplaçé ... Istoozen Eko
    ert_matfax = Pilote("ERT Matfax", AlfaRomeo)
    non4me_geckoz = Pilote("NoN4me Geckoz", AlfaRomeo)
    fct_tweekaz = Pilote("FcT Tweekaz", Haas)
    non4me_cramer = Pilote("NoN4me Cramer", Haas)

    ###############################################################################################

    xrt_marth.setGamertagRemplacant("XRT Marth")
    rp1_durtom.setGamertagRemplacant("RP1 Durtom")

    ###############################################################################################

    # Course 1
    gp01 = GrandPrix("RoyaumeUni", sprint = False)

    # Remplaçants
    istoozen_eko_01 = Pilote("PuR Ilton", Mercedes)
    mcr_papyx_01 = Pilote("F1M AlexGT500", Ferrari)
    shadd_01 = Pilote("Tonati2514", AlphaTauri)

    istoozen_eko_01.setGamertagRemplacant("Istoozen Eko")
    mcr_papyx_01.setGamertagRemplacant("MCR Papyx")
    shadd_01.setGamertagRemplacant("Shadd")

    # Pénalités en qualification
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

    non4me_stuno_02.setGamertagRemplacant("NoN4me Stuno")

    # Pénalités en qualification
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
    
    # Pénalités en qualification
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

    wanbmt63_04.setGamertagRemplacant("WanBMT63")
    
    # Pénalités en qualification
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

    # Course 5
    gp05 = GrandPrix("Canada", sprint = False)

    # Remplaçants
    istoozen_eko_05 = Pilote("STR Pagaa", AlphaTauri)
    mirage9150_05 = Pilote("Tonati2514", AlphaTauri)

    istoozen_eko_05.setDonnees(istoozen_eko_01.getDonnees())

    istoozen_eko_05.setGamertagRemplacant("Istoozen Eko")

    # Pénalités en qualification
    # rp1_ice : : 5 places de pénalité

    q05 = [
        f1m_alexgt500,
        pur_ilton,
        rp1_skyzzz,
        non4me_cramer,
        non4me_geckoz,
        non4me_livai,
        istoozen_eko_05,
        fct_tweekaz,
        ert_matfax,
        pura_jager,
        rp1_ice,
        non4me_cami,
        non4me_jordy,
        fct_coco,
        ert_karanox,
        pur_ultraaa,
        xrt_nico2a,
        fct_specktre,
        mirage9150_05,
        rp1_durtom
    ]
    c05 = [
        f1m_alexgt500,
        non4me_geckoz,
        pur_ilton,
        rp1_skyzzz,
        rp1_ice,
        ert_karanox,
        non4me_cramer,
        non4me_cami,
        non4me_jordy,
        fct_specktre,
        non4me_livai,
        fct_tweekaz,
        fct_coco,
        ert_matfax,
        rp1_durtom,
        mirage9150_05,
        pura_jager,
        istoozen_eko_05,
        pur_ultraaa,
        xrt_nico2a
    ]

    gp05.setQualification(q05)
    gp05.setCourse(c05)
    gp05.calcul(abandonsCourse = 7)

    ###############################################################################################

    # Course 6
    gp06 = GrandPrix("Mexique", sprint = False)

    # Remplaçants
    non4me_stuno_06 = Pilote("FcT Tweekaz", Haas)
    istoozen_eko_06 = Pilote("Istoozen Eko", Williams)
    ldl_zepro_06 = Pilote("Tonati2514", AlphaTauri)
    f1xl_fanfan_06 = Pilote("PuRa Jager", McLaren)

    non4me_stuno_06.setDonnees(non4me_stuno_02.getDonnees())
    istoozen_eko_06.setDonnees(istoozen_eko_05.getDonnees())

    non4me_stuno_06.setGamertagRemplacant("NoN4me Stuno")
    istoozen_eko_06.setGamertagRemplacant("Istoozen Eko")
    ldl_zepro_06.setGamertagRemplacant("LDL Zepro")
    f1xl_fanfan_06.setGamertagRemplacant("F1XL Fanfan")

    # Pénalités en qualification
    # Aucune

    q06 = [
        non4me_geckoz,
        ert_matfax,
        rp1_ice,
        f1m_alexgt500,
        non4me_cramer,
        fct_coco,
        non4me_stuno_06,
        istoozen_eko_06,
        non4me_cami,
        ert_karanox,
        pur_ilton,
        rp1_skyzzz,
        fct_specktre,
        non4me_livai,
        pur_ultraaa,
        ldl_zepro_06,
        str_pagaa,
        f1xl_fanfan_06,
        xrt_nico2a,
        non4me_jordy
    ]
    c06 = [
        rp1_skyzzz,
        non4me_geckoz,
        ert_matfax,
        non4me_cramer,
        non4me_cami,
        non4me_livai,
        istoozen_eko_06,
        fct_specktre,
        non4me_jordy,
        xrt_nico2a,
        f1xl_fanfan_06,
        rp1_ice,
        fct_coco,
        ldl_zepro_06,
        pur_ultraaa,
        f1m_alexgt500,
        ert_karanox,
        pur_ilton,
        non4me_stuno_06,
        str_pagaa
    ]

    gp06.setQualification(q06)
    gp06.setCourse(c06)
    gp06.calcul(abandonsCourse = 7)

    ###############################################################################################

    # Course 7
    gp07 = GrandPrix("Japon", sprint = False)

    # Remplaçants
    ldl_zepro_07 =  Pilote("STR Pagaa", AlphaTauri)
    xrt_alpha_07 = Pilote("XRT Nico2a", Alpine)
    f1xl_fanfan_07 = Pilote("RP1 Skyzzz", RedBull)
    ert_tiiste_07 = Pilote("Istoozen Eko", Williams)
    nathanhrx_07 = Pilote("NoN4me Livai", Ferrari)
    tonati2514 = Pilote("Tonati2514", AlphaTauri)

    ldl_zepro_07.setDonnees(ldl_zepro_06.getDonnees())
    f1xl_fanfan_07.setDonnees(f1xl_fanfan_06.getDonnees())

    ldl_zepro_07.setGamertagRemplacant("LDL Zepro")
    xrt_alpha_07.setGamertagRemplacant("XRT Alpha")
    f1xl_fanfan_07.setGamertagRemplacant("F1XL Fanfan")
    ert_tiiste_07.setGamertagRemplacant("ERT Tiiste")
    nathanhrx_07.setGamertagRemplacant("NathanHrx")

    # Pénalités en qualification
    # Aucune

    q07 = [
        non4me_cramer,
        non4me_geckoz,
        ert_matfax,
        f1m_alexgt500,
        ert_karanox,
        tonati2514,
        pur_ilton,
        non4me_cami,
        non4me_jordy,
        rp1_ice,
        fct_tweekaz,
        fct_specktre,
        ldl_zepro_07,
        pura_jager,
        pur_ultraaa,
        fct_coco,
        xrt_alpha_07,
        f1xl_fanfan_07,
        ert_tiiste_07,
        nathanhrx_07
    ]
    c07 = [
        non4me_cramer,
        non4me_geckoz,
        f1m_alexgt500,
        ert_matfax,
        ert_karanox,
        pur_ilton,
        rp1_ice,
        non4me_cami,
        fct_tweekaz,
        fct_coco,
        tonati2514,
        fct_specktre,
        pura_jager,
        non4me_jordy,
        nathanhrx_07,
        ert_tiiste_07,
        f1xl_fanfan_07,
        xrt_alpha_07,
        pur_ultraaa,
        ldl_zepro_07
    ]

    gp07.setQualification(q07)
    gp07.setCourse(c07)
    gp07.calcul(abandonsCourse = 2)

    ###############################################################################################

    # Course 8
    gp08 = GrandPrix("France", sprint = True)

    # Remplaçants
    qsr_lajoya_08 = Pilote("Istoozen Eko", Williams)
    djedjam_08 = Pilote("FcT Tweekaz", Haas)
    fct_deadpool_08 = Pilote("NoN4me Cami", RedBull)

    qsr_lajoya_08.setGamertagRemplacant("QSR LaJoya")
    djedjam_08.setGamertagRemplacant("Djedjam")
    fct_deadpool_08.setGamertagRemplacant("FcT Deadpool")

    # Pénalités en qualification
    # Aucune

    q08 = [
        pur_ilton,
        non4me_cramer,
        non4me_geckoz,
        rp1_skyzzz,
        f1m_alexgt500,
        qsr_lajoya_08,
        djedjam_08,
        pur_ultraaa,
        non4me_livai,
        pura_jager,
        ert_matfax,
        non4me_jordy,
        fct_specktre,
        str_pagaa,
        rp1_ice,
        ert_karanox,
        fct_coco,
        xrt_nico2a,
        fct_deadpool_08,
        tonati2514
    ]
    s08 = [
        pur_ilton,
        non4me_cramer,
        f1m_alexgt500,
        non4me_geckoz,
        qsr_lajoya_08,
        djedjam_08,
        ert_karanox,
        str_pagaa,
        tonati2514,
        fct_coco,
        non4me_livai,
        pur_ultraaa,
        rp1_ice,
        fct_specktre,
        rp1_skyzzz,
        non4me_jordy,
        fct_deadpool_08,
        xrt_nico2a,
        pura_jager,
        ert_matfax
    ]
    c08 = [
        qsr_lajoya_08,
        non4me_geckoz,
        pur_ilton,
        non4me_cramer,
        djedjam_08,
        ert_karanox,
        ert_matfax,
        f1m_alexgt500,
        str_pagaa,
        rp1_ice,
        fct_coco,
        rp1_skyzzz,
        fct_specktre,
        non4me_jordy,
        xrt_nico2a,
        non4me_livai,
        pur_ultraaa,
        fct_deadpool_08,
        pura_jager,
        tonati2514
    ]

    gp08.setQualification(q08)
    gp08.setSprint(s08)
    gp08.setCourse(c08)
    gp08.calcul(abandonsCourse = 6)

    ###############################################################################################

    final = gp01.getPoints()
    final = sumDict(final, gp02.getPoints())
    final = sumDict(final, gp03.getPoints())
    final = sumDict(final, gp04.getPoints())
    final = sumDict(final, gp05.getPoints())
    final = sumDict(final, gp06.getPoints())
    final = sumDict(final, gp07.getPoints())
    final = sumDict(final, gp08.getPoints())

    # Statistiques ################################################################################

    if (stats):

        """
        Pénalités en qualification :
        > Canada
            - rp1_ice : 5 places de pénalité
        """
        
        pilotes = {}
        courses = [gp01, gp02, gp03, gp04, gp05]
        for course in courses:
            participants = course.getQualification()
            for pilote in participants:
                gt = pilote.getGamertagRemplacant()
                pilotes[gt] = pilote                  

        # print(len(pilotes))

        f = open('.\s7\stats.csv', 'a', newline="")
        writer = csv.writer(f)

        writer.writerow(["pilote;nb_q;nb_q2;nb_q3;nb_poles_q;best_q;moy_q;vsCoeq_q;nb_s;nb_top8_s;nb_podium_s;nb_win_s;best_s;moy_s;vsCoeq_s;nb_c;nb_top10_c;nb_podium_c;nb_win_c;best_c;moy_c;vsCoeq_c"])

        for gt in pilotes:

            p = pilotes[gt]
            donnees = p.getDonnees()
            tabQ = donnees.tabQ()
            tabS = donnees.tabS()
            tabC = donnees.tabC()

            line = p.getGamertagRemplacant() + ";"

            line += "{};{};{};{};{};{};{};".format(
                donnees.nbQ(tabQ),
                donnees.nbQ2(tabQ),
                donnees.nbQ3(tabQ),
                donnees.nbPoles(tabQ),
                donnees.bestQ(tabQ),
                donnees.avgQ(tabQ),
                donnees.getCoeqBattuQ()
            )
            line += "{};{};{};{};{};{};{};".format(
                donnees.nbS(tabS),
                donnees.nbT8S(tabS),
                donnees.nbT3S(tabS),
                donnees.nbVicS(tabS),
                donnees.bestS(tabS),
                donnees.avgS(tabS),
                donnees.getCoeqBattuS()
            )
            line += "{};{};{};{};{};{};{}".format(
                donnees.nbC(tabC),
                donnees.nbT10C(tabC),
                donnees.nbT3C(tabC),
                donnees.nbVicC(tabC),
                donnees.bestC(tabC),
                donnees.avgC(tabC),
                donnees.getCoeqBattuC()
            )

            writer.writerow([line])

        f.close()

    ###############################################################################################

    return final