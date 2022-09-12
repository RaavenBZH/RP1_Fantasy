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
    pur_stitoxxe = Pilote("PuR Stitoxxe", Mercedes)
    rp1_noctis = Pilote("RP1 Noctis", RedBull)
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
