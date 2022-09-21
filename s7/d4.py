from packageF1.Ecurie import *
from packageF1.Pilote import *
from packageF1.GrandPrix import *

#
# Saison 7
#
# Calcul des points pour les pilotes de division 2
#

def getPointsD4() -> dict:

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

    arac_zer = Pilote("aRAC Zer", Mercedes)
    ldl_shermy = Pilote("LDL Shermy", Mercedes)
    non4me_bappe = Pilote("NoN4me Bappe", RedBull)
    leptit03 = Pilote("LePtit03", RedBull)
    non4me_lucas = Pilote("NoN4me Lucas", Ferrari)
    tnor_chime = Pilote("TNOR Chime", Ferrari)
    jnpjd = Pilote("JNPJD", McLaren)
    emeric = Pilote("Emeric", McLaren)
    leonh4rte = Pilote("Leonh4rte", Alpine)
    arac_pafael = Pilote("ARAC Pafael", Alpine)
    shadd = Pilote("Shadd", AlphaTauri)
    rp1_fifou = Pilote("RP1 Fifou", AlphaTauri)
    f1xr_noich = Pilote("F1XR Noich", AstonMartin)
    ecs_flower = Pilote("ECS Flower", AstonMartin)
    mvt_kaio = Pilote("MVT Kaio", Williams)
    mvt_fly = Pilote("MVT Fly", Williams)
    crl_bikette = Pilote("CRL Bikette", AlfaRomeo)
    knf_fradj = Pilote("KNF Fradj", AlfaRomeo)
    rs_al3xx = Pilote("RS Al3xx", Haas)
    ks_virtuozz = Pilote("KS Virtuozz", Haas)

    ###############################################################################################

    # Course 1
    gp01 = GrandPrix("RoyaumeUni", sprint = False)

    # Remplaçants
    # Aucun

    # Pénalites en qualification
    # Aucune

    q01 = [
        crl_bikette,
        tnor_chime,
        ecs_flower,
        arac_zer,
        jnpjd,
        non4me_lucas,
        mvt_kaio,
        leptit03,
        mvt_fly,
        emeric,
        rp1_fifou,
        shadd,
        knf_fradj,
        rs_al3xx,
        f1xr_noich,
        non4me_bappe, 
        arac_pafael,
        ks_virtuozz,
        leonh4rte,
        ldl_shermy
    ]
    c01 = [
        crl_bikette,
        jnpjd,
        knf_fradj,
        emeric,
        arac_zer,
        mvt_fly,
        rp1_fifou,
        mvt_kaio,
        arac_pafael,
        ks_virtuozz,
        ldl_shermy,
        shadd,
        f1xr_noich,
        non4me_bappe,
        tnor_chime,
        leptit03,
        ecs_flower,
        non4me_lucas,
        rs_al3xx,
        leonh4rte
    ]

    gp01.setQualification(q01)
    gp01.setCourse(c01)
    gp01.calcul(abandonsCourse = 3)

    final = gp01.getPoints()

    print(non4me_lucas.getHistorique())

    return final