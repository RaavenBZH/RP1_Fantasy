from packageF1.Ecurie import *
from packageF1.Pilote import *
from packageF1.GrandPrix import *

import csv

#
# Saison 7
#
# Calcul des points pour les pilotes de division 1
#

def getPointsD1(stats = False) -> dict:

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

    fra_raaven = Pilote("FRA Raaven", Mercedes)
    pur_rosberg = Pilote("PuR Rosberg", Mercedes)
    rp1_noctis = Pilote("WOR Noctis", RedBull)
    ert_batxone = Pilote("ERT BatXone", RedBull)
    rp1_okwaru = Pilote("PuR Nygraal", Ferrari) # remplacé ... PuR Nygraal
    rp1_theo = Pilote("RP1 Theo", Ferrari)
    rp1_montoya = Pilote("RP1 Montoya", McLaren)
    rp1_varane = Pilote("PuR Lowky", McLaren) # remplacé ... PuR Lowky
    ldl_oli = Pilote("LDL Oli", Alpine)
    ldl_saumon = Pilote("LDL Saumon", Alpine)
    rp1_chadoo = Pilote("RP1 Chadoo", AlphaTauri)
    rp1_winterr = Pilote("RP1 Winterr", AlphaTauri)
    mcr_jayrko = Pilote("MCR Jayrko", AstonMartin)
    mcr_path = Pilote("MCR Path", AstonMartin)
    xrt_oxygen = Pilote("XRT Oxygen", Williams)
    pur_snika = Pilote("RP1 Varane", Williams) # remplacé ... RP1 Varane
    rp1_adam = Pilote("RP1 Adam", AlfaRomeo)
    xrt_arthur = Pilote("XRT Arthur", AlfaRomeo)
    pur_lowky = Pilote("TX3 Enzo", Haas) # remplacé ... TX3 Enzo
    fct_daigoro = Pilote("RP1 Maldini", Haas) # remplacé ... SHZ Piccolo ... RP1 Maldini

    ###############################################################################################

    rp1_okwaru.setGamertagRemplacant("RP1 Okwaru")
    pur_lowky.setGamertagRemplacant("PuR Lowky")
    fct_daigoro.setGamertagRemplacant("FcT Daigoro")
    rp1_varane.setGamertagRemplacant("RP1 Varane")
    pur_snika.setGamertagRemplacant("PuR Snika")

    ###############################################################################################

    # Course 1
    gp01 = GrandPrix("RoyaumeUni", sprint = False)

    # Remplaçants
    ert_niloboo_01 = Pilote("LDL Oli", Alpine)

    ert_niloboo_01.setGamertagRemplacant("ERT Niloboo")

    # Pénalités en qualification
    # Aucune

    q01 = [
        rp1_noctis,
        rp1_theo,
        rp1_okwaru,
        pur_rosberg,
        ert_batxone,
        fra_raaven,
        ert_niloboo_01,
        rp1_montoya,
        rp1_winterr,
        ldl_saumon,
        rp1_adam,
        pur_lowky,
        rp1_varane,
        rp1_chadoo,
        xrt_arthur,
        xrt_oxygen,
        mcr_path,
        fct_daigoro,
        mcr_jayrko,
        pur_snika
    ]
    c01 = [
        rp1_theo,
        pur_rosberg,
        ldl_saumon,
        fra_raaven,
        ert_batxone,
        fct_daigoro,
        xrt_oxygen,
        pur_lowky,
        rp1_montoya,
        rp1_okwaru,
        pur_snika,
        mcr_jayrko,
        mcr_path,
        rp1_winterr,
        rp1_chadoo,
        ert_niloboo_01,
        rp1_adam,
        xrt_arthur,
        rp1_varane,
        rp1_noctis
    ]

    gp01.setQualification(q01)
    gp01.setCourse(c01)
    gp01.calcul(abandonsCourse=3)

    ###############################################################################################

    # Course 2
    gp02 = GrandPrix("Belgique", sprint = True)

    # Remplaçants
    pur_nygraal_02 = Pilote("PuR Nygraal", Ferrari)
    ert_niloboo_02 = Pilote("LDL Saumon", Alpine)
    xrt_darkfly_02 = Pilote("LDL Oli", Alpine)

    ert_niloboo_02.setDonnees(ert_niloboo_01.getDonnees())

    pur_nygraal_02.setGamertagRemplacant("PuR Nygraal")
    ert_niloboo_02.setGamertagRemplacant("ERT Niloboo")
    xrt_darkfly_02.setGamertagRemplacant("XRT Darkfly")

    # Pénalités en qualification
    # Aucune

    q02 = [
        rp1_noctis,
        pur_nygraal_02,
        pur_rosberg,
        rp1_theo,
        ert_niloboo_02,
        fra_raaven,
        ert_batxone,
        rp1_winterr,
        xrt_darkfly_02,
        pur_lowky,
        rp1_montoya,
        rp1_chadoo,
        rp1_adam,
        rp1_varane,
        fct_daigoro,
        xrt_arthur,
        xrt_oxygen,
        mcr_jayrko,
        pur_snika,
        mcr_path
    ]
    s02 = [
        pur_nygraal_02,
        ert_batxone,
        rp1_noctis,
        rp1_theo,
        ert_niloboo_02,
        pur_lowky,
        pur_rosberg,
        rp1_winterr,
        fra_raaven,
        rp1_chadoo,
        rp1_montoya,
        rp1_varane,
        fct_daigoro,
        xrt_arthur,
        xrt_darkfly_02,
        mcr_path,
        xrt_oxygen,
        mcr_jayrko,
        pur_snika,
        rp1_adam
    ]
    c02 = [
        rp1_noctis,
        pur_nygraal_02,
        pur_rosberg,
        ert_niloboo_02,
        fra_raaven,
        pur_lowky,
        rp1_montoya,
        rp1_winterr,
        mcr_jayrko,
        xrt_arthur,
        pur_snika,
        rp1_theo,
        xrt_oxygen,
        fct_daigoro,
        rp1_adam,
        xrt_darkfly_02,
        ert_batxone,
        rp1_chadoo,
        mcr_path,
        rp1_varane
    ]

    gp02.setQualification(q02)
    gp02.setSprint(s02)
    gp02.setCourse(c02)
    gp02.calcul(abandonsSprint=1, abandonsCourse=7)

    ###############################################################################################

    # Course 3
    gp03 = GrandPrix("Espagne", sprint = False)

    # Remplaçants
    ert_niloboo_03 = Pilote("LDL Oli", Alpine)
    pur_voltha_03 = Pilote("RP1 Chadoo", AlphaTauri)

    ert_niloboo_03.setDonnees(ert_niloboo_02.getDonnees())

    ert_niloboo_03.setGamertagRemplacant("ERT Niloboo")
    pur_voltha_03.setGamertagRemplacant("PuR Voltha")

    # Pénalités en qualification
    # rp1_varane : 5 places de pénalité

    q03 = [
        ert_batxone,
        rp1_noctis,
        rp1_okwaru,
        pur_rosberg,
        fra_raaven,
        rp1_winterr,
        ert_niloboo_03,
        rp1_montoya,
        rp1_adam,
        pur_lowky,
        rp1_varane,
        ldl_saumon,
        pur_voltha_03,
        xrt_arthur,
        fct_daigoro,
        pur_snika,
        xrt_oxygen,
        mcr_jayrko,
        mcr_path,
        rp1_theo
    ]
    c03 = [
        rp1_noctis,
        rp1_okwaru,
        ert_niloboo_03,
        rp1_montoya,
        fra_raaven,
        rp1_theo,
        ldl_saumon,
        rp1_winterr,
        pur_lowky,
        xrt_arthur,
        mcr_path,
        pur_rosberg,
        pur_voltha_03,
        fct_daigoro,
        pur_snika,
        xrt_oxygen,
        rp1_varane,
        mcr_jayrko,
        rp1_adam,
        ert_batxone
    ]

    gp03.setQualification(q03)
    gp03.setCourse(c03)
    gp03.calcul(abandonsCourse=2)

    ###############################################################################################

    # Course 4
    gp04 = GrandPrix("Espagne", sprint = False)

    # Remplaçants
    fct_lasouche_04 = Pilote("RP1 Adam", AlfaRomeo)
    ert_niloboo_04 = Pilote("LDL Saumon", Alpine)
    pur_ripply_04 = Pilote("RP1 Chadoo", AlphaTauri)
    pur_thomas_04 = Pilote("RP1 Winterr", AlphaTauri)
    pur_nygraal = Pilote("PuR Nygraal", Ferrari)

    ert_niloboo_04.setDonnees(ert_niloboo_03.getDonnees())
    pur_nygraal.setDonnees(pur_nygraal_02.getDonnees())

    fct_lasouche_04.setGamertagRemplacant("FcT LaSouche")
    ert_niloboo_04.setGamertagRemplacant("ERT Niloboo")
    pur_ripply_04.setGamertagRemplacant("PuR Ripply")
    pur_thomas_04.setGamertagRemplacant("PuR Thomas")

    # Pénalités en qualification
    # Aucune

    q04 = [
        rp1_noctis,
        rp1_theo,
        pur_nygraal,
        pur_rosberg,
        ert_batxone,
        pur_thomas_04,
        fra_raaven,
        ert_niloboo_04,
        ldl_oli,
        rp1_montoya,
        pur_lowky,
        pur_ripply_04,
        rp1_varane,
        fct_lasouche_04,
        xrt_arthur,
        xrt_oxygen,
        pur_snika,
        mcr_path,
        fct_daigoro,
        mcr_jayrko
    ]
    c04 = [
        rp1_noctis,
        pur_nygraal,
        rp1_theo,
        ert_batxone,
        fra_raaven,
        pur_lowky,
        ert_niloboo_04,
        pur_thomas_04,
        rp1_montoya,
        pur_ripply_04,
        xrt_arthur,
        xrt_oxygen,
        pur_snika,
        ldl_oli,
        mcr_path,
        mcr_jayrko,
        fct_lasouche_04,
        rp1_varane,
        fct_daigoro,
        pur_rosberg
    ]

    gp04.setQualification(q04)
    gp04.setCourse(c04)
    gp04.calcul(abandonsCourse=3)

    ###############################################################################################

    # Course 5
    gp05 = GrandPrix("Canada", sprint = False)

    # Remplaçants
    xrt_darkfly_05 = Pilote("RP1 Montoya", McLaren)
    tx3_enzo_05 = Pilote("RP1 Varane", Williams)
    pur_ripply_05 = Pilote("RP1 Chadoo", AlphaTauri)
    pur_thomas_05 = Pilote("RP1 Winterr", AlphaTauri)

    xrt_darkfly_05.setDonnees(xrt_darkfly_02.getDonnees())
    pur_ripply_05.setDonnees(pur_ripply_04.getDonnees())
    pur_thomas_05.setDonnees(pur_thomas_04.getDonnees())

    xrt_darkfly_05.setGamertagRemplacant("XRT Darkfly")
    tx3_enzo_05.setGamertagRemplacant("TX3 Enzo")
    pur_ripply_05.setGamertagRemplacant("PuR Ripply")
    pur_thomas_05.setGamertagRemplacant("PuR Thomas")

    # Pénalités en qualification
    # Aucune

    q05 = [
        pur_nygraal,
        pur_rosberg,
        rp1_theo,
        ldl_oli,
        rp1_varane,
        fra_raaven,
        pur_lowky,
        rp1_adam,
        pur_thomas_05,
        ldl_saumon,
        pur_ripply_05,
        mcr_jayrko,
        fct_daigoro,
        xrt_oxygen,
        rp1_noctis,
        mcr_path,
        xrt_darkfly_05,
        xrt_arthur,
        tx3_enzo_05,
        ert_batxone
    ]
    c05 = [
        pur_nygraal,
        rp1_theo,
        ert_batxone,
        ldl_oli,
        fra_raaven,
        rp1_noctis,
        pur_rosberg,
        fct_daigoro,
        mcr_path,
        ldl_saumon,
        pur_ripply_05,
        rp1_adam,
        pur_lowky,
        xrt_arthur,
        xrt_darkfly_05,
        rp1_varane,
        xrt_oxygen,
        pur_thomas_05,
        mcr_jayrko,
        tx3_enzo_05
    ]

    gp05.setQualification(q05)
    gp05.setCourse(c05)
    gp05.calcul(abandonsCourse=7)

    ###############################################################################################

    # Transferts
    pur_lowky.setEcurie(McLaren)
    pur_lowky.setGamertag("PuR Lowky")
    pur_lowky.setGamertagRemplacant("PuR Lowky")

    rp1_varane.setEcurie(Williams)
    rp1_varane.setGamertag("RP1 Varane")
    rp1_varane.setGamertagRemplacant("RP1 Varane")

    ###############################################################################################

    # Course 7
    gp07 = GrandPrix("Japon", sprint = False)

    # Remplaçants
    pur_ilton_07 = Pilote("RP1 Chadoo", AlphaTauri)
    shz_piccolo = Pilote("RP1 Maldini", Haas)
    tx3_enzo = Pilote("TX3 Enzo", Haas)

    tx3_enzo.setDonnees(tx3_enzo_05.getDonnees())

    pur_ilton_07.setGamertagRemplacant("PuR Ilton")
    shz_piccolo.setGamertagRemplacant("SHZ Piccolo")

    # Pénalités en qualification
    # Aucune

    q07 = [
        pur_nygraal,
        rp1_noctis,
        rp1_theo,
        ert_batxone,
        fra_raaven,
        ldl_oli,
        ldl_saumon,
        pur_rosberg,
        rp1_adam,
        shz_piccolo,
        rp1_winterr,
        pur_lowky,
        pur_ilton_07,
        rp1_varane,
        rp1_montoya,
        xrt_arthur,
        tx3_enzo,
        xrt_oxygen,
        mcr_jayrko,
        mcr_path
    ]
    c07 = [
        rp1_noctis,
        pur_nygraal,
        ert_batxone,
        rp1_theo,
        pur_rosberg,
        ldl_saumon,
        ldl_oli,
        rp1_adam,
        pur_ilton_07,
        rp1_winterr,
        xrt_oxygen,
        xrt_arthur,
        tx3_enzo,
        rp1_varane,
        rp1_montoya,
        mcr_jayrko,
        fra_raaven,
        mcr_path,
        pur_lowky,
        shz_piccolo
    ]

    gp07.setQualification(q07)
    gp07.setCourse(c07)
    gp07.calcul(abandonsCourse=4)

    ###############################################################################################

    # Course 8
    gp08 = GrandPrix("France", sprint = True)

    # Remplaçants
    pur_thomas_08 = Pilote("FRA Raaven", Mercedes)
    pur_ilton_08 = Pilote("RP1 Chadoo", AlphaTauri)

    pur_thomas_08.setDonnees(pur_thomas_05.getDonnees())
    pur_ilton_08.setDonnees(pur_ilton_07.getDonnees())

    pur_thomas_08.setGamertagRemplacant("PuR Thomas")
    pur_ilton_08.setGamertagRemplacant("PuR Ilton")

    # Pénalités en qualification

    q08 = [
        pur_nygraal,
        rp1_noctis,
        rp1_theo,
        ert_batxone,
        pur_lowky,
        pur_thomas_08,
        pur_rosberg,
        rp1_montoya,
        ldl_saumon,
        ldl_oli,
        pur_ilton_08,
        rp1_winterr,
        rp1_adam,
        xrt_arthur,
        mcr_path,
        tx3_enzo,
        rp1_varane,
        mcr_jayrko,
        shz_piccolo,
        xrt_oxygen
    ]
    s08 = [
        pur_nygraal,
        rp1_noctis,
        ert_batxone,
        rp1_theo,
        pur_lowky,
        pur_thomas_08,
        pur_rosberg,
        ldl_saumon,
        ldl_oli,
        pur_ilton_08,
        rp1_adam,
        xrt_arthur,
        rp1_winterr,
        mcr_path,
        rp1_varane,
        mcr_jayrko,
        tx3_enzo,
        xrt_oxygen, 
        shz_piccolo,
        rp1_montoya
    ]
    c08 = [
        pur_nygraal,
        ert_batxone,
        ldl_oli,
        rp1_theo,
        pur_rosberg,
        ldl_saumon,
        pur_thomas_08,
        rp1_noctis,
        pur_ilton_08,
        rp1_adam,
        xrt_oxygen,
        mcr_jayrko,
        tx3_enzo,
        rp1_varane,
        xrt_arthur,
        mcr_path,
        rp1_winterr,
        rp1_montoya,
        pur_lowky,
        shz_piccolo
    ]

    gp08.setQualification(q08)
    gp08.setSprint(s08)
    gp08.setCourse(c08)
    gp08.calcul(abandonsCourse=5, abandonsSprint=2)

    ###############################################################################################

    # Course 9
    gp09 = GrandPrix("Azerbaidjan", sprint = False)

    # Remplaçants
    rp1_maldini = Pilote("RP1 Maldini", Haas)
    pur_thomas_09 = Pilote("FRA Raaven", Mercedes)
    if1_meister_09 = Pilote("RP1 Chadoo", AlphaTauri)

    pur_thomas_09.setDonnees(pur_thomas_08.getDonnees())
    
    pur_thomas_09.setGamertagRemplacant("PuR Thomas")
    if1_meister_09.setGamertagRemplacant("IF1 Meister")

    # Pénalités en qualification
    # Aucune

    q09 = [
        pur_nygraal,
        rp1_noctis,
        pur_lowky,
        pur_rosberg,
        pur_thomas_09,
        ldl_oli,
        rp1_adam,
        xrt_arthur,
        rp1_theo,
        ert_batxone,
        ldl_saumon,
        rp1_winterr,
        rp1_montoya,
        rp1_maldini,
        rp1_varane,
        mcr_path,
        mcr_jayrko,
        if1_meister_09,
        tx3_enzo,
        xrt_oxygen
    ]
    c09 = [
        pur_nygraal,
        pur_thomas_09,
        rp1_noctis,
        rp1_montoya,
        rp1_varane,
        ldl_oli,
        rp1_theo,
        ldl_saumon,
        xrt_arthur,
        tx3_enzo,
        rp1_winterr,
        mcr_jayrko,
        rp1_adam,
        ert_batxone,
        rp1_maldini,
        pur_lowky,
        pur_rosberg,
        mcr_path,
        if1_meister_09,
        xrt_oxygen
    ]

    gp09.setQualification(q09)
    gp09.setCourse(c09)
    gp09.calcul(absentsQualif=1, absentsCourse=1, abandonsCourse=4)

    ###############################################################################################

    # Course 10
    gp10 = GrandPrix("Singapour", sprint = False)

    # Remplaçants
    pur_vincent_10 = Pilote("RP1 Winterr", AlphaTauri)
    pur_ripply_10 = Pilote("RP1 Noctis", RedBull)
    pur_thomas_10 = Pilote("PuR Rosberg", Mercedes)
    pur_ilton_10 = Pilote("FRA Raaven", Mercedes)

    pur_ripply_10.setDonnees(pur_ripply_05.getDonnees())
    pur_thomas_10.setDonnees(pur_thomas_09.getDonnees())
    pur_ilton_10.setDonnees(pur_ilton_08.getDonnees())

    pur_vincent_10.setGamertagRemplacant("PuR Vincent")
    pur_ripply_10.setGamertagRemplacant("PuR Ripply")

    # Pénalités en qualification
    # Aucune

    q10 = [
        pur_nygraal,
        pur_thomas_10,
        pur_ilton_10,
        ert_batxone,
        ldl_saumon,
        rp1_montoya,
        rp1_theo,
        rp1_varane,
        pur_lowky,
        xrt_arthur,
        rp1_maldini,
        rp1_adam,
        xrt_oxygen,
        mcr_path,
        pur_ripply_10,
        pur_vincent_10,
        mcr_jayrko,
        ldl_oli,
        tx3_enzo,
        rp1_chadoo
    ]
    c10 = [
        pur_nygraal,
        pur_thomas_10,
        ldl_saumon,
        pur_ilton_10,
        ert_batxone,
        xrt_oxygen,
        pur_vincent_10,
        rp1_adam,
        ldl_oli,
        rp1_montoya,
        tx3_enzo,
        mcr_jayrko,
        rp1_varane,
        xrt_arthur,
        mcr_path,
        rp1_maldini,
        pur_ripply_10,
        pur_lowky,
        rp1_theo,
        rp1_chadoo
    ]

    gp10.setQualification(q10)
    gp10.setCourse(c10)
    gp10.calcul(absentsQualif=1, absentsCourse=1, abandonsCourse=2)

    ###############################################################################################

    # Course 11
    gp11 = GrandPrix("Barhein", sprint = False)

    # Remplaçants
    ert_niloboo_11 = Pilote("RP1 Noctis", RedBull)
    rp1_papash_11 = Pilote("RP1 Winterr", AlphaTauri)
    pur_thomas_11 = Pilote("FRA Raaven", Mercedes)
    pur_ilton_11 = Pilote("PuR Lowky", McLaren)
    rp1_skyzz_11 = Pilote("TX3 Enzo", Haas)
    pur_vincent_11 = Pilote("RP1 Chadoo", AlphaTauri)
    pur_lowky_11 = Pilote("RP1 Theo", Ferrari)

    ert_niloboo_11.setDonnees(ert_niloboo_04.getDonnees())
    pur_thomas_11.setDonnees(pur_thomas_10.getDonnees())
    pur_ilton_11.setDonnees(pur_ilton_10.getDonnees())
    pur_vincent_11.setDonnees(pur_vincent_10.getDonnees())
    pur_lowky_11.setDonnees(pur_lowky.getDonnees())

    ert_niloboo_11.setGamertagRemplacant("ERT Niloboo")
    rp1_papash_11.setGamertagRemplacant("RP1 Papash")
    pur_thomas_11.setGamertagRemplacant("PuR Thomas")
    pur_ilton_11.setGamertagRemplacant("PuR Ilton")
    rp1_skyzz_11.setGamertagRemplacant("RP1 Skyzz")
    pur_vincent_11.setGamertagRemplacant("PuR Vincent")
    pur_lowky_11.setGamertagRemplacant("PuR Lowky")

    # Pénalités en qualification
    # Aucune

    q11 = [
        pur_lowky_11,
        pur_nygraal,
        pur_rosberg,
        ert_niloboo_11,
        ert_batxone,
        rp1_papash_11,
        pur_thomas_11,
        ldl_saumon,
        pur_ilton_11,
        rp1_skyzz_11,
        ldl_oli,
        rp1_maldini,
        pur_vincent_11,
        rp1_adam,
        xrt_arthur,
        rp1_varane,
        mcr_path,
        mcr_jayrko,
        rp1_montoya,
        xrt_oxygen
    ]
    c11 = [
        pur_lowky_11,
        pur_nygraal,
        ert_niloboo_11,
        ert_batxone,
        pur_rosberg,
        rp1_papash_11,
        ldl_oli,
        ldl_saumon,
        rp1_montoya,
        xrt_arthur,
        rp1_varane,
        mcr_path,
        rp1_adam,
        rp1_maldini,
        mcr_jayrko,
        rp1_skyzz_11,
        pur_thomas_11,
        pur_vincent_11,
        pur_ilton_11,
        xrt_oxygen
    ]

    gp11.setQualification(q11)
    gp11.setCourse(c11)
    gp11.calcul(absentsQualif=1, absentsCourse=1, abandonsCourse=3)

    ###############################################################################################

    final = gp01.getPoints()
    final = sumDict(final, gp02.getPoints())
    final = sumDict(final, gp03.getPoints())
    final = sumDict(final, gp04.getPoints())
    final = sumDict(final, gp05.getPoints())
    #
    final = sumDict(final, gp07.getPoints())
    final = sumDict(final, gp08.getPoints())
    final = sumDict(final, gp09.getPoints())
    final = sumDict(final, gp10.getPoints())
    final = sumDict(final, gp11.getPoints())
    
    # Statistiques ################################################################################

    if (stats):

        """
        Pénalités en qualification :
        > Espagne (1)
            - rp1_varane : 5 places de pénalité
        
        """
        
        pilotes = {}
        courses = [gp01, gp02, gp03, gp04, gp05]
        for course in courses:
            participants = course.getQualification()
            for pilote in participants:
                gt = pilote.getGamertagRemplacant()
                pilotes[gt] = pilote    

        # print(len(pilotes))

        f = open('.\s7\stats.csv', 'w', newline="")
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

        ###########################################################################################

    return final

    ###############################################################################################