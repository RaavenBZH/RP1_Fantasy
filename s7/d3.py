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
    non4me_cami = Pilote("Non4me Cami", RedBull)
    non4me_livai = Pilote("Non4me Livai", Ferrari)
    f1m_alexgt500 = Pilote("F1M AlexGT500", Ferrari)
    pura_jager = Pilote("PuRa Jager", McLaren)
    pur_ultraaa = Pilote("PuR Ultraaa", McLaren)
    xrt_nico2a = Pilote("XRT Nico2a", Alpine)
    ert_karanox = Pilote("ERT Karanox", Alpine)
    xrt_marth = Pilote("XRT Marth", AlphaTauri)
    str_pagaa = Pilote("STR Pagaa", AlphaTauri)
    non4me_jordy = Pilote("Non4me Jordy", AstonMartin)
    fct_spektre = Pilote("FcT Spektre", AstonMartin)
    rp1_ice = Pilote("RP1 Ice", Williams)
    rp1_durtom = Pilote("RP1 Durtom", Williams)
    ert_matfax = Pilote("ERT Matfax", AlfaRomeo)
    non4me_geckoz = Pilote("Non4me Geckoz", AlfaRomeo)
    fct_tweekaz = Pilote("FcT Tweekaz", Haas)
    non4me_cramer = Pilote("Non4me Cramer", Haas)

    ###############################################################################################