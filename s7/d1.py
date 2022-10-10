from packageF1.Ecurie import *
from packageF1.Pilote import *
from packageF1.GrandPrix import *

#
# Saison 7
#
# Calcul des points pour les pilotes de division 1
#

def getPointsD1() -> dict:

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
    rp1_okwaru = Pilote("PuR Nygraal", Ferrari)
    rp1_theo = Pilote("RP1 Theo", Ferrari)
    rp1_montoya = Pilote("RP1 Montoya", McLaren)
    rp1_varane = Pilote("RP1 Varane", McLaren)
    ldl_oli = Pilote("LDL Oli", Alpine)
    ldl_saumon = Pilote("LDL Saumon", Alpine)
    rp1_chadoo = Pilote("RP1 Chadoo", AlphaTauri)
    rp1_winterr = Pilote("RP1 Winterr", AlphaTauri)
    mcr_jayrko = Pilote("MCR Jayrko", AstonMartin)
    mcr_path = Pilote("MCR Path", AstonMartin)
    xrt_oxygen = Pilote("XRT Oxygen", Williams)
    pur_snika = Pilote("PuR Snika", Williams)
    rp1_adam = Pilote("RP1 Adam", AlfaRomeo)
    xrt_arthur = Pilote("XRT Arthur", AlfaRomeo)
    pur_lowky = Pilote("PuR Lowky", Haas)
    fct_daigoro = Pilote("FcT Daigoro", Haas)

    ###############################################################################################

    # Course 1
    gp01 = GrandPrix("RoyaumeUni", sprint = False)

    # Remplaçants
    ert_niloboo_01 = Pilote("LDL Oli", Alpine)

    # Pénalites en qualification
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
    pur_nygraal_02 = Pilote("RP1 Okwaru", Ferrari)
    ert_niloboo_02 = Pilote("LDL Saumon", Alpine)
    xrt_darkfly_02 = Pilote("LDL Oli", Alpine)

    # Pénalites en qualification
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

    # Pénalites en qualification
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

    # Pénalites en qualification
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

    final = gp01.getPoints()
    final = sumDict(final, gp02.getPoints())
    final = sumDict(final, gp03.getPoints())
    final = sumDict(final, gp04.getPoints())

    return final

    ###############################################################################################