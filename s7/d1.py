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
    rp1_okwaru = Pilote("RP1 Okwaru", Ferrari)
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

    final = gp01.getPoints()

    return final

    ###############################################################################################