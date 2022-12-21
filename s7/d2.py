from packageF1.Ecurie import *
from packageF1.Pilote import *
from packageF1.GrandPrix import *

import packageF1.Fonctions as Fonctions

#
# Saison 7
#
# Calcul des points pour les pilotes de division 2
#

def getPointsD2(stats = False) -> dict:

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
    pur_nygraal = Pilote("PuR Voltha", Ferrari) # remplacé ... PuR Voltha
    pur_racing = Pilote("F1M AlexGT500", Ferrari) # remplacé ... F1M AlexGT500
    rp1_tribion = Pilote("RP1 Tribion", McLaren)
    heroziah = Pilote("PuRa Jager", McLaren) # remplacé ... PuRa Jager
    xrt_darkfly = Pilote("XRT Darkfly", Alpine)
    rp1_gachette = Pilote("RP1 Gachette", Alpine)
    if1_supreme = Pilote("iF1 Supr3me", AlphaTauri)
    loc_warf1 = Pilote("LOC WarF1", AlphaTauri)
    mcr_spacex = Pilote("Non4me Stuno", AstonMartin) # remplacé ... Non4me Stuno
    fct_deadpool = Pilote("Mirage9150", AstonMartin) # remplacé ... Mirage9150
    rp1_owain = Pilote("GL Tharsi", Williams) # remplacé ... ASE Luisnts1 ... GL Tharsi
    ecs_finesse = Pilote("ECS Finesse", Williams)
    ert_aurelius = Pilote("ERT Aurelius", AlfaRomeo)
    fct_lasouche = Pilote("FcT LaSouche", AlfaRomeo)
    yozana = Pilote("Yozana", Haas)
    pura_tomoe = Pilote("PuRa Tomoe", Haas)

    ###############################################################################################

    rp1_owain.setGamertagRemplacant("RP1 Owain")
    pur_nygraal.setGamertagRemplacant("PuR Nygraal")
    heroziah.setGamertagRemplacant("Heroziah")
    fct_deadpool.setGamertagRemplacant("FcT Deadpool")
    pur_racing.setGamertagRemplacant("PuR Racing")
    mcr_spacex.setGamertagRemplacant("MCR SpaceX")

    ###############################################################################################

    # Course 1
    gp01 = GrandPrix("RoyaumeUni", sprint = False)

    # Remplaçants
    ert_niloboo_01 = Pilote("ERT Flyart", RedBull)
    istoozen_eko_01 = Pilote("LOC WarF1", AlphaTauri)

    ert_niloboo_01.setGamertagRemplacant("ERT Niloboo")
    istoozen_eko_01.setGamertagRemplacant("Istoozen Eko")

    # Pénalités en qualification
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
    ert_niloboo_02 = Pilote("LOC WarF1", AlphaTauri)
    pura_jager_02 = Pilote("PuRa Jager", McLaren)
    rp1_woody_02 = Pilote("GL Tharsi", Williams)

    ert_niloboo_02.setDonnees(ert_niloboo_01.getDonnees())

    ert_niloboo_02.setGamertagRemplacant("ERT Niloboo")
    pura_jager_02.setGamertagRemplacant("PuRa Jager")
    rp1_woody_02.setGamertagRemplacant("RP1 Woody")

    # Pénalités en qualification
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
    ase_luisnts1 = Pilote("GL Tharsi", Williams)
    pur_voltha_03 = Pilote("LOC WarF1", AlphaTauri)
    pura_jager_03 = Pilote("PuRa Jager", McLaren)
    non4me_cramer_03 = Pilote("Yozana", Haas)
    f1m_alexgt500_03 = Pilote("PuR Voltha", Ferrari)

    pura_jager_03.setDonnees(pura_jager_02.getDonnees())

    ase_luisnts1.setGamertagRemplacant("ASE Luisnts1")
    pur_voltha_03.setGamertagRemplacant("PuR Voltha")
    pura_jager_03.setGamertagRemplacant("PuRa Jager")
    non4me_cramer_03.setGamertagRemplacant("Non4me Cramer")
    f1m_alexgt500_03.setGamertagRemplacant("F1M AlexGT500")
    
    # Pénalités en qualification
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
    ert_niloboo_04 = Pilote("LOC WarF1", AlphaTauri)
    pura_jager_04 = Pilote("RP1 Tribion", McLaren)
    istoozen_eko_04 = Pilote("GL Tharsi", Williams)
    mirage9150_04 = Pilote("Mirage9150", AstonMartin)

    pur_voltha.setDonnees(pur_voltha_03.getDonnees())
    ert_niloboo_04.setDonnees(ert_niloboo_02.getDonnees())
    pura_jager_04.setDonnees(pura_jager_03.getDonnees())
    istoozen_eko_04.setDonnees(istoozen_eko_01.getDonnees())
    
    pur_voltha.setGamertagRemplacant("PuR Voltha")
    ert_niloboo_04.setGamertagRemplacant("ERT Niloboo")
    pura_jager_04.setGamertagRemplacant("PuRa Jager")
    istoozen_eko_04.setGamertagRemplacant("Istoozen Eko")
    mirage9150_04.setGamertagRemplacant("Mirage9150")
    
    # Pénalités en qualification
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

    # Course 5
    gp05 = GrandPrix("Canada", sprint = False)

    # Remplaçants
    pur_ilton_05 = Pilote("iF1 Supr3me", AlphaTauri)
    pur_vinboy_05 = Pilote("LOC WarF1", AlphaTauri)
    rp1_skyzzz_05 = Pilote("ECS Finesse", Williams)
    istoozen_eko_05 = Pilote("Yozana", Haas)

    istoozen_eko_05.setDonnees(istoozen_eko_04.getDonnees())

    pur_ilton_05.setGamertagRemplacant("PuR Ilton")
    pur_vinboy_05.setGamertagRemplacant("PuR Vinboy")
    rp1_skyzzz_05.setGamertagRemplacant("RP1 Skyzzz")
    istoozen_eko_05.setGamertagRemplacant("Istoozen Eko")

    # Pénalités en qualification
    # Aucune

    q05 = [
        pur_thomas,
        pur_ilton_05,
        pur_vinboy_05,
        pur_ripply,
        fct_lasouche,
        ert_aurelius,
        ase_luisnts1,
        rp1_skyzzz_05,
        istoozen_eko_05,
        mcr_spacex,
        pur_voltha,
        pur_vincent,
        rp1_tribion,
        fct_deadpool,
        ert_flyart,
        xrt_darkfly,
        heroziah,
        pura_tomoe,
        rp1_gachette,
        pur_racing
    ]
    c05 = [
        ert_flyart,
        pur_voltha,
        rp1_tribion,
        ert_aurelius,
        rp1_skyzzz_05,
        pur_vinboy_05,
        mcr_spacex,
        pur_racing,
        pur_vincent,
        rp1_gachette,
        fct_lasouche,
        pura_tomoe,
        pur_thomas,
        fct_deadpool,
        pur_ilton_05,
        istoozen_eko_05,
        ase_luisnts1,
        heroziah,
        pur_ripply,
        xrt_darkfly
    ]

    gp05.setQualification(q05)
    gp05.setCourse(c05)
    gp05.calcul(abandonsCourse=6)

    ###############################################################################################

    # Course 6
    gp06 = GrandPrix("Mexique", sprint = False)

    # Remplaçants
    ert_niloboo_06 = Pilote("FcT LaSouche", AlfaRomeo)
    pur_ilton_06 = Pilote("PuR Vincent", Mercedes)
    non4me_jordy_06 = Pilote("Non4me Stuno", AstonMartin)
    pur_vinboy_06 = Pilote("Mirage9150", AstonMartin)
    istoozen_eko_06 = Pilote("GL Tharsi", Williams)

    ert_niloboo_06.setDonnees(ert_niloboo_04.getDonnees())
    pur_ilton_06.setDonnees(pur_ilton_05.getDonnees())
    pur_vinboy_06.setDonnees(pur_vinboy_05.getDonnees())
    istoozen_eko_06.setDonnees(istoozen_eko_05.getDonnees())

    ert_niloboo_06.setGamertagRemplacant("ERT Niloboo")
    pur_ilton_06.setGamertagRemplacant("PuR Ilton")
    non4me_jordy_06.setGamertagRemplacant("Non4me Jordy")
    pur_vinboy_06.setGamertagRemplacant("PuR Vinboy")
    istoozen_eko_06.setGamertagRemplacant("Istoozen Eko")

    # Pénalités en qualification
    # Aucune

    q06 = [
        pur_racing,
        pur_thomas,
        pur_ripply,
        ert_niloboo_06,
        yozana,
        pur_ilton_06,
        ert_aurelius,
        non4me_jordy_06,
        rp1_tribion,
        pur_vinboy_06,
        pura_tomoe,
        loc_warf1,
        xrt_darkfly,
        pur_voltha,
        rp1_gachette,
        ecs_finesse,
        ert_flyart,
        if1_supreme,
        istoozen_eko_06,
        heroziah
    ]
    c06 = [
        pur_thomas,
        pur_ripply,
        ert_niloboo_06,
        pur_vinboy_06,
        ert_flyart,
        pur_ilton_06,
        xrt_darkfly,
        ert_aurelius,
        yozana,
        rp1_tribion,
        istoozen_eko_06,
        loc_warf1,
        non4me_jordy_06,
        pura_tomoe,
        pur_voltha,
        pur_racing,
        ecs_finesse,
        rp1_gachette,
        heroziah,
        if1_supreme
    ]

    gp06.setQualification(q06)
    gp06.setCourse(c06)
    gp06.calcul(abandonsCourse=4)

    ###############################################################################################

    # Course 7
    gp07 = GrandPrix("Japon", sprint = False)

    # Remplaçants
    istoozen_eko_07 = Pilote("ECS Finesse", Williams)
    fct_coco_07 = Pilote("PuR Voltha", Ferrari)
    rp1_skyzzz_07 = Pilote("Mirage9150", AstonMartin)
    ert_niloboo_07 = Pilote("ERT Aurelius", AlfaRomeo)

    istoozen_eko_07.setDonnees(istoozen_eko_06.getDonnees())
    rp1_skyzzz_07.setDonnees(rp1_skyzzz_05.getDonnees())
    ert_niloboo_07.setDonnees(ert_niloboo_06.getDonnees())

    istoozen_eko_07.setGamertagRemplacant("Istoozen Eko")
    fct_coco_07.setGamertagRemplacant("FcT Coco")
    rp1_skyzzz_07.setGamertagRemplacant("RP1 Skyzzz")
    ert_niloboo_07.setGamertagRemplacant("ERT Niloboo")

    # Pénalités en qualification
    # Aucune

    q07 = [
        pur_racing,
        pur_thomas,
        pur_vincent,
        fct_lasouche,
        ert_niloboo_07,
        istoozen_eko_07,
        pur_ripply,
        rp1_skyzzz_07,
        pura_tomoe,
        yozana,
        fct_coco_07,
        loc_warf1,
        rp1_gachette,
        mcr_spacex,
        heroziah, 
        rp1_tribion,
        xrt_darkfly,
        ert_flyart,
        ase_luisnts1,
        if1_supreme
    ]
    c07 = [
        ert_niloboo_07,
        pur_vincent,
        pura_tomoe,
        yozana,
        pur_thomas,
        xrt_darkfly,
        ert_flyart,
        pur_ripply,
        rp1_skyzzz_07,
        if1_supreme,
        pur_racing,
        loc_warf1,
        rp1_tribion,
        heroziah,
        ase_luisnts1,
        fct_coco_07,
        istoozen_eko_07,
        fct_lasouche,
        rp1_gachette,
        mcr_spacex
    ]

    gp07.setQualification(q07)
    gp07.setCourse(c07)
    gp07.calcul(abandonsCourse=9, absentsQualif=1)

    ###############################################################################################

    # Course 8
    gp08 = GrandPrix("France", sprint = True)

    # Remplaçants
    ert_niloboo_08 = Pilote("FcT LaSouche", AlfaRomeo)
    rp1_papash_08 = Pilote("PuRa Tomoe", Haas)
    rp1_skyzzz_08 = Pilote("Non4me Stuno", AstonMartin)
    mirage9150_08 = Pilote("Mirage9150", AstonMartin)
    if1_meister_08 = Pilote("XRT Darkfly", Alpine)
    fct_specktre_08 = Pilote("RP1 Tribion", McLaren)
    fct_coco_08 = Pilote("LOC WarF1", AlphaTauri)

    ert_niloboo_08.setDonnees(ert_niloboo_07.getDonnees())
    rp1_skyzzz_08.setDonnees(rp1_skyzzz_07.getDonnees())
    mirage9150_08.setDonnees(mirage9150_04.getDonnees())
    fct_coco_08.setDonnees(fct_coco_07.getDonnees())

    ert_niloboo_08.setGamertagRemplacant("ERT Niloboo")
    rp1_papash_08.setGamertagRemplacant("RP1 Papash")
    rp1_skyzzz_08.setGamertagRemplacant("RP1 Skyzzz")
    mirage9150_08.setGamertagRemplacant("Mirage9150")
    if1_meister_08.setGamertagRemplacant("IF1 Meister")
    fct_specktre_08.setGamertagRemplacant("FcT Specktre")
    fct_coco_08.setGamertagRemplacant("FcT Coco")

    # Pénalités en qualification
    # Aucune

    q08 = [
        pur_racing,
        rp1_papash_08,
        pur_thomas,
        pur_voltha,
        ert_aurelius,
        ert_niloboo_08,
        pur_ripply,
        rp1_skyzzz_08,
        if1_meister_08,
        pur_vincent,
        mirage9150_08,
        fct_specktre_08,
        ase_luisnts1,
        yozana,
        if1_supreme,
        fct_coco_08,
        ecs_finesse,
        heroziah,
        ert_flyart,
        rp1_gachette
    ]
    s08 = [
        pur_racing,
        rp1_papash_08,
        pur_voltha,
        ert_niloboo_08,
        pur_vincent,
        if1_meister_08,
        pur_thomas,
        if1_supreme,
        rp1_skyzzz_08,
        fct_coco_08,
        pur_ripply,
        ert_aurelius,
        ecs_finesse,
        yozana,
        fct_specktre_08,
        ase_luisnts1,
        rp1_gachette,
        ert_flyart,
        mirage9150_08,
        heroziah
    ]
    c08 = [
        pur_racing,
        if1_meister_08,
        pur_vincent,
        if1_supreme,
        ert_niloboo_08,
        yozana,
        fct_coco_08,
        pur_ripply,
        ecs_finesse,
        rp1_papash_08,
        ase_luisnts1,
        mirage9150_08,
        rp1_skyzzz_08,
        ert_aurelius,
        pur_thomas,
        pur_voltha,
        heroziah,
        rp1_gachette,
        ert_flyart,
        fct_specktre_08
    ]

    gp08.setQualification(q08)
    gp08.setSprint(s08)
    gp08.setCourse(c08)
    gp08.calcul(abandonsCourse=7, abandonsSprint=3)

    ###############################################################################################

    # Course 9
    gp09 = GrandPrix("Azerbaidjan", sprint = False)

    # Remplaçants
    pura_jager = Pilote("PuRa Jager", McLaren)
    mirage9150 = Pilote("Mirage9150", AstonMartin)
    non4me_stuno_09 = Pilote("iF1 Supr3me", AlphaTauri)
    if1_meister_09 = Pilote("ERT Aurelius", AlfaRomeo)
    vega_elsass_09 = Pilote("FcT LaSouche", AlfaRomeo)
    f1m_alexgt500_09 = Pilote("PuR Voltha", Ferrari)
    pur_ilton_09 = Pilote("PuR Vincent", Mercedes)
    fct_specktre_09 = Pilote("Non4me Stuno", AstonMartin)
    fct_coco_09 = Pilote("GL Tharsi", Williams)

    pura_jager.setDonnees(pura_jager_04.getDonnees())
    if1_meister_09.setDonnees(if1_meister_08.getDonnees())
    f1m_alexgt500_09.setDonnees(f1m_alexgt500_03.getDonnees())
    pur_ilton_09.setDonnees(pur_ilton_06.getDonnees())
    fct_specktre_09.setDonnees(fct_specktre_08.getDonnees())
    fct_coco_09.setDonnees(fct_coco_08.getDonnees())

    pura_jager.setGamertagRemplacant("PuRa Jager")
    mirage9150.setGamertagRemplacant("Mirage9150")
    non4me_stuno_09.setGamertagRemplacant("NoN4me Stuno")
    if1_meister_09.setGamertagRemplacant("iF1 Meister")
    vega_elsass_09.setGamertagRemplacant("Vega Elsass")
    f1m_alexgt500_09.setGamertagRemplacant("F1M AlexGT500")
    pur_ilton_09.setGamertagRemplacant("PuR Ilton")
    fct_specktre_09.setGamertagRemplacant("FcT Specktre")
    fct_coco_09.setGamertagRemplacant("FcT Coco")

    # Pénalités en qualification
    # Aucune

    q09 = [
        pur_racing,
        pur_thomas,
        non4me_stuno_09,
        if1_meister_09,
        f1m_alexgt500_09,
        mirage9150,
        pur_ilton_09,
        xrt_darkfly,
        pura_tomoe,
        ecs_finesse,
        yozana,
        fct_specktre_09,
        pur_ripply,
        rp1_gachette,
        pura_jager, 
        ert_flyart,
        vega_elsass_09,
        fct_coco_09,
        loc_warf1,
        rp1_tribion
    ]
    c09 = [
        pur_ilton_09,
        pur_ripply,
        f1m_alexgt500_09,
        if1_meister_09,
        loc_warf1,
        ert_flyart,
        pur_racing,
        ecs_finesse,
        vega_elsass_09,
        pura_tomoe,
        fct_specktre_09,
        fct_coco_09,
        mirage9150,
        pur_thomas,
        yozana,
        rp1_gachette,
        non4me_stuno_09,
        pura_jager,
        xrt_darkfly,
        rp1_tribion
    ]

    gp09.setQualification(q09)
    gp09.setCourse(c09)
    gp09.calcul(absentsQualif=2, absentsCourse=1, abandonsCourse=7)

    ###############################################################################################

    # Course 10
    gp10 = GrandPrix("Singapour", sprint = False)

    # Remplaçants
    ert_karanox_10 = Pilote("Yozana", Haas)
    pur_ilton_10 = Pilote("PuR Thomas", Mercedes)
    tonati2514_10 = Pilote("iF1 Meister", AlphaTauri)
    non4me_cramer_10 = Pilote("PuRa Tomoe", Haas)
    non4me_geckoz_10 = Pilote("ERT Aurelius", AlfaRomeo)
    ert_niloboo_10 = Pilote("FcT LaSouche", AlfaRomeo)
    rp1_skyzzz_10 = Pilote("F1M AlexGT500", Ferrari)
    mcr_papyx_10 = Pilote("Non4me Stuno", AstonMartin)
    sithar07_10 = Pilote("GL Tharsi", Williams)

    pur_ilton_10.setDonnees(pur_ilton_09.getDonnees())
    non4me_cramer_10.setDonnees(non4me_cramer_03.getDonnees())
    ert_niloboo_10.setDonnees(ert_niloboo_08.getDonnees())
    rp1_skyzzz_10.setDonnees(rp1_skyzzz_08.getDonnees())

    ert_karanox_10.setGamertagRemplacant("ERT Karanox")
    pur_ilton_10.setGamertagRemplacant("PuR Ilton")
    tonati2514_10.setGamertagRemplacant("Tonati2514")
    non4me_cramer_10.setGamertagRemplacant("NoN4me Cramer")
    non4me_geckoz_10.setGamertagRemplacant("NoN4me Geckoz")
    ert_niloboo_10.setGamertagRemplacant("ERT Niloboo")
    rp1_skyzzz_10.setGamertagRemplacant("RP1 Skyzzz")
    mcr_papyx_10.setGamertagRemplacant("MCR PapyX")
    sithar07_10.setGamertagRemplacant("Sithar07")

    # Pénalités en qualification
    # sithar07_10 : 5 places de pénalité (4)

    q10 = [
        ert_karanox_10,
        pur_ilton_10,
        tonati2514_10,
        non4me_cramer_10,
        pur_vincent,
        non4me_geckoz_10,
        ert_niloboo_10,
        rp1_tribion,
        pur_voltha,
        rp1_skyzzz_10,
        xrt_darkfly,
        mirage9150,
        loc_warf1,
        ecs_finesse,
        ert_flyart,
        pura_jager,
        mcr_papyx_10,
        pur_ripply,
        rp1_gachette,
        sithar07_10
    ]
    c10 = [
        pur_vincent,
        pur_ilton_10,
        ert_karanox_10,
        mirage9150,
        rp1_gachette,
        ert_niloboo_10,
        rp1_skyzzz_10,
        ert_flyart,
        mcr_papyx_10,
        non4me_geckoz_10,
        sithar07_10,
        pur_ripply,
        rp1_tribion,
        pur_voltha,
        loc_warf1,
        non4me_cramer_10,
        ecs_finesse,
        pura_jager,
        xrt_darkfly,
        tonati2514_10
    ]

    gp10.setQualification(q10)
    gp10.setCourse(c10)
    gp10.calcul(abandonsCourse=10)

    ###############################################################################################

    # Course 11
    gp11 = GrandPrix("Barhein", sprint = False)

    # Remplaçants
    non4me_stuno = Pilote("Non4me Stuno", AstonMartin)
    rp1_skyzzz_11 = Pilote("ECS Finesse", Williams)
    ert_niloboo_11 = Pilote("FcT LaSouche", AlfaRomeo)
    ert_wartors_11 = Pilote("ERT Aurelius", AlfaRomeo)
    pur_vinboy_11 = Pilote("PuRa Tomoe", Haas)
    ert_karanox_11 = Pilote("iF1 Supreme", AlphaTauri)
    f1m_alexgt500 = Pilote("F1M AlexGT500", Ferrari)
    tonati2514_11 = Pilote("LOC WarF1", AlphaTauri)
    gl_tharsi = Pilote("GL Tharsi", Williams)

    non4me_stuno.setDonnees(non4me_stuno_09.getDonnees())
    rp1_skyzzz_11.setDonnees(rp1_skyzzz_10.getDonnees())
    ert_niloboo_11.setDonnees(ert_niloboo_10.getDonnees())
    pur_vinboy_11.setDonnees(pur_vinboy_06.getDonnees())
    ert_karanox_11.setDonnees(ert_karanox_10.getDonnees())
    f1m_alexgt500.setDonnees(f1m_alexgt500_09.getDonnees())
    tonati2514_11.setDonnees(tonati2514_10.getDonnees())

    non4me_stuno.setGamertagRemplacant("Non4me Stuno")
    rp1_skyzzz_11.setGamertagRemplacant("RP1 Skyzzz")
    ert_niloboo_11.setGamertagRemplacant("ERT Niloboo")
    pur_vinboy_11.setGamertagRemplacant("PuR Vinboy")
    ert_karanox_11.setGamertagRemplacant("ERT Karanox")
    f1m_alexgt500.setGamertagRemplacant("F1M AlexGT500")
    tonati2514_11.setGamertagRemplacant("Tonati2514")
    gl_tharsi.setGamertagRemplacant("GL Tharsi")

    # Pénalités en qualification
    # Aucune

    q11 = [
        pur_thomas,
        non4me_stuno,
        pur_voltha,
        rp1_skyzzz_11,
        pur_vincent,
        ert_niloboo_11,
        pur_ripply,
        rp1_tribion,
        ert_wartors_11,
        xrt_darkfly,
        pur_vinboy_11,
        ert_karanox_11,
        rp1_gachette,
        f1m_alexgt500,
        yozana,
        pura_jager,
        gl_tharsi,
        tonati2514_11,
        mirage9150,
        ert_flyart
    ]
    c11 = [
        pur_thomas,
        non4me_stuno,
        pur_vincent,
        pur_vinboy_11,
        pura_jager,
        ert_karanox_11,
        rp1_tribion,
        pur_ripply,
        rp1_skyzzz_11,
        ert_wartors_11,
        pur_voltha,
        ert_niloboo_11,
        tonati2514_11,
        xrt_darkfly,
        yozana,
        rp1_gachette,
        f1m_alexgt500,
        mirage9150,
        gl_tharsi,
        ert_flyart
    ]

    gp11.setQualification(q11)
    gp11.setCourse(c11)
    gp11.calcul(absentsQualif=1, absentsCourse=1, abandonsCourse=8)

    ###############################################################################################

    # Course 12
    gp12 = GrandPrix("AbuDhabi", sprint = False)

    # Remplacants
    non4me_geckoz_12 = Pilote("FcT LaSouche", AlfaRomeo)
    pur_vinboy_12 = Pilote("PuRa Tomoe", Haas)
    pura_chime_12 = Pilote("PuR Voltha", Ferrari)
    pur_ilton_12 = Pilote("PuR Thomas", Mercedes)
    non4me_jordy_12 = Pilote("RP1 Tribion", McLaren)
    crl_bikette_12 = Pilote("ERT Aurelius", AlfaRomeo)
    baptiste_heche_12 = Pilote("PuR Ripply", RedBull)
    lucas_lulu_12 = Pilote("ECS Finesse", Williams)
    pura_matex_12 = Pilote("RP1 Gachette", Alpine)
    fct_coco_12 = Pilote("PuR Vincent", Mercedes)
    niko77_12 = Pilote("LOC WarF1", AlphaTauri)
    fct_specktre_12 = Pilote("Mirage9150", AstonMartin)

    non4me_geckoz_12.setDonnees(non4me_geckoz_10.getDonnees())
    pur_vinboy_12.setDonnees(pur_vinboy_11.getDonnees())
    pur_ilton_12.setDonnees(pur_ilton_12.getDonnees())
    non4me_jordy_12.setDonnees(non4me_jordy_06.getDonnees())
    fct_coco_12.setDonnees(fct_coco_09.getDonnees())
    fct_specktre_12.setDonnees(fct_specktre_09.getDonnees())

    non4me_geckoz_12.setGamertagRemplacant("Non4me Geckoz")
    pur_vinboy_12.setGamertagRemplacant("PuR Vinboy")
    pura_chime_12.setGamertagRemplacant("PuRa Chime")
    pur_ilton_12.setGamertagRemplacant("PuR Ilton")
    non4me_jordy_12.setGamertagRemplacant("Non4me Jordy")
    crl_bikette_12.setGamertagRemplacant("CRL Bikette")
    baptiste_heche_12.setGamertagRemplacant("Baptiste Heche")
    lucas_lulu_12.setGamertagRemplacant("Lucas Lulu")
    pura_matex_12.setGamertagRemplacant("PuRa Matex")
    fct_coco_12.setGamertagRemplacant("FcT Coco")
    niko77_12.setGamertagRemplacant("Niko77")
    fct_specktre_12.setGamertagRemplacant("FcT Specktre")

    # Pénalités en qualification
    # Aucune

    q12 = [
        non4me_stuno,
        non4me_geckoz_12,
        pur_vinboy_12,
        pura_chime_12,
        f1m_alexgt500,
        pur_ilton_12,
        xrt_darkfly,
        pura_jager,
        non4me_jordy_12,
        crl_bikette_12,
        baptiste_heche_12,
        lucas_lulu_12,
        if1_supreme,
        pura_matex_12,
        fct_coco_12,
        yozana,
        niko77_12,
        fct_specktre_12,
        gl_tharsi,
        ert_flyart
    ]

    c12 = [
        non4me_stuno,
        pur_ilton_12,
        f1m_alexgt500,
        crl_bikette_12,
        yozana,
        fct_coco_12,
        lucas_lulu_12,
        non4me_jordy_12,
        pura_matex_12,
        gl_tharsi,
        pur_vinboy_12,
        non4me_geckoz_12,
        fct_specktre_12,
        pura_jager,
        niko77_12,
        pura_chime_12,
        baptiste_heche_12,
        ert_flyart,
        xrt_darkfly,
        if1_supreme
    ]

    gp12.setQualification(q12)
    gp12.setCourse(c12)
    gp12.calcul(abandonsCourse=3)

    ###############################################################################################

    final = gp01.getPoints()
    final = sumDict(final, gp02.getPoints())
    final = sumDict(final, gp03.getPoints())
    final = sumDict(final, gp04.getPoints())
    final = sumDict(final, gp05.getPoints())
    final = sumDict(final, gp06.getPoints())
    final = sumDict(final, gp07.getPoints())
    final = sumDict(final, gp08.getPoints())
    final = sumDict(final, gp09.getPoints())
    final = sumDict(final, gp10.getPoints())
    final = sumDict(final, gp11.getPoints())
    final = sumDict(final, gp12.getPoints())

    # Statistiques ################################################################################

    if (stats):

        """
        Pénalités en qualification :
        > Miami
            - rp1_gachette : 5 places de pénalité
            - pur_vincent : 5 places de pénalité
        > Singapour
            - sithar07_10 : 5 places de pénalité (4)
        """

        courses = [gp01, gp02, gp03, gp04, gp05, gp06, gp07, gp08, gp09, gp10, gp11, gp12]
        Fonctions.write(courses, "a")

    ###############################################################################################

    return final