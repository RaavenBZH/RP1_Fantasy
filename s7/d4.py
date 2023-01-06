from packageF1.Analyse import *
from packageF1.Ecurie import *
from packageF1.Fonctions import *
from packageF1.GrandPrix import *
from packageF1.Pilote import *

import packageF1.Fonctions as Fonctions

#
# Saison 7
#
# Calcul des points pour les pilotes de division 2
#

def getPointsD4(stats = False) -> dict:

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

    # Création de l'analyseur
    al = Analyse()

    # Création des pilotes

    arac_zer = Pilote("aRAC Zer", Mercedes)
    ldl_shermy = Pilote("LDL Shermy", Mercedes)
    non4me_bappe = Pilote("NoN4me Bappe", RedBull)
    leptit03 = Pilote("LePtit03", RedBull)
    non4me_lucas = Pilote("NoN4me Lucas", Ferrari)
    pura_chime = Pilote("PuRa Chime", Ferrari)
    jnpjd = Pilote("JNPJD", McLaren)
    emeric = Pilote("Emeric", McLaren)
    leonh4rte = Pilote("PuRa Matex", Alpine) # remplaçé ... PuRa Matex
    arac_pafael = Pilote("Ripeur Delite", Alpine) # remplacé ... Ripeur Delite
    shadd = Pilote("Shadd", AlphaTauri)
    rp1_fifou = Pilote("RP1 Fifou", AlphaTauri)
    f1xr_noich = Pilote("Wissam", AstonMartin) # remplacé ... Wissam
    ecs_flower = Pilote("NXS Tiga", AstonMartin) #remplacé ... NXS Tiga
    mvt_kaio = Pilote("MVT Kaio", Williams)
    mvt_fly = Pilote("MVT Fly", Williams)
    crl_bikette = Pilote("CRL Bikette", AlfaRomeo)
    knf_fradj = Pilote("KNF Fradj", AlfaRomeo)
    rs_al3xx = Pilote("Rocha1307", Haas) # remplacé ... Rocha1307
    ks_virtuozz = Pilote("Djedjam", Haas) # remplacé ... Djedjam

    ###############################################################################################

    leonh4rte.setGamertagRemplacant("Leonh4rte")
    f1xr_noich.setGamertagRemplacant("F1XR Noich")
    rs_al3xx.setGamertagRemplacant("RS Al3xx")
    ks_virtuozz.setGamertagRemplacant("KS Virtuozz")
    arac_pafael.setGamertagRemplacant("aRAC Pafael")
    ecs_flower.setGamertagRemplacant("ECS Flower")

    ###############################################################################################

    # Course 1
    gp01 = GrandPrix("RoyaumeUni", sprint = False)

    # Remplaçants
    # Aucun

    # Pénalités en qualification
    # Aucune

    q01 = [
        crl_bikette,
        pura_chime,
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
        pura_chime,
        leptit03,
        ecs_flower,
        non4me_lucas,
        rs_al3xx,
        leonh4rte
    ]

    gp01.setQualification(q01)
    gp01.setCourse(c01)
    gp01.calcul(abandonsCourse = 3)

    al.compareCoequipiers(gp01)

    ###############################################################################################

    # Course 2
    gp02 = GrandPrix("Belgique", sprint = True)

    # Remplaçants
    djedjam_02 = Pilote("Djedjam", Haas) 
    legion_rambow_02 = Pilote("Rocha1307", Haas)
    pura_matex = Pilote("PuRa Matex", Alpine)

    djedjam_02.setGamertagRemplacant("Djedjam")
    legion_rambow_02.setGamertagRemplacant("Legion Rambow")
    pura_matex.setGamertagRemplacant("PuRa Matex")

    # Pénalités en qualification
    # Aucune

    q02 = [
        djedjam_02,
        pura_chime,
        crl_bikette,
        pura_matex,
        legion_rambow_02,
        arac_zer,
        jnpjd,
        knf_fradj,
        emeric,
        ldl_shermy,
        non4me_lucas,
        mvt_fly,
        rp1_fifou,
        non4me_bappe,
        ecs_flower,
        mvt_kaio,
        leptit03,
        f1xr_noich,
        shadd,
        arac_pafael
    ]
    s02 = [
        djedjam_02,
        crl_bikette,
        arac_zer,
        pura_chime,
        mvt_fly,
        pura_matex,
        mvt_kaio,
        non4me_lucas,
        knf_fradj,
        f1xr_noich,
        non4me_bappe,
        legion_rambow_02,
        shadd,
        ldl_shermy,
        ecs_flower,
        rp1_fifou,
        leptit03,
        arac_pafael,
        jnpjd,
        emeric
    ]
    c02 = [
        crl_bikette,
        djedjam_02,
        non4me_bappe,
        emeric,
        mvt_fly,
        shadd,
        non4me_lucas,
        jnpjd,
        arac_pafael,
        legion_rambow_02,
        f1xr_noich,
        mvt_kaio,
        rp1_fifou,
        arac_zer,
        knf_fradj,
        pura_matex,
        leptit03,
        ldl_shermy,
        ecs_flower,
        pura_chime
    ]

    gp02.setQualification(q02)
    gp02.setSprint(s02)
    gp02.setCourse(c02)
    gp02.calcul(abandonsCourse = 10, abandonsSprint=2)

    al.compareCoequipiers(gp02)

    ###############################################################################################

    # Course 3
    gp03 = GrandPrix("Espagne", sprint = False)

    # Remplaçants
    mcr_raiko_03 = Pilote("Ripeur Delite", Alpine)
    wissam_03 = Pilote("Rocha1307", Haas)
    nxs_tiga_03 = Pilote("aRAC Zer", Mercedes)

    mcr_raiko_03.setGamertagRemplacant("MCR Raiko")
    wissam_03.setGamertagRemplacant("Wissam")
    nxs_tiga_03.setGamertagRemplacant("NXS Tiga")

    # Pénalités en qualification
    # Aucune

    q03 = [
        crl_bikette,
        pura_chime,
        mcr_raiko_03,
        rp1_fifou,
        jnpjd,
        knf_fradj,
        pura_matex,
        emeric,
        mvt_kaio,
        ecs_flower,
        f1xr_noich,
        non4me_bappe,
        leptit03,
        mvt_fly,
        ldl_shermy,
        shadd,
        ks_virtuozz,
        wissam_03,
        nxs_tiga_03,
        non4me_lucas
    ]
    c03 = [
        crl_bikette,
        emeric,
        knf_fradj,
        ecs_flower,
        rp1_fifou,
        shadd,
        non4me_lucas,
        pura_chime,
        mvt_fly,
        nxs_tiga_03,
        f1xr_noich,
        leptit03,
        ks_virtuozz,
        pura_matex,
        ldl_shermy,
        non4me_bappe,
        mvt_kaio,
        jnpjd,
        mcr_raiko_03,
        wissam_03
    ]

    gp03.setQualification(q03)
    gp03.setCourse(c03)
    gp03.calcul(abandonsCourse = 7)

    al.compareCoequipiers(gp03)

    ###############################################################################################

    # Course 4
    gp04 = GrandPrix("Miami", sprint = False)

    # Remplaçants
    tonati2514_04 = Pilote("Rocha1307", Haas)
    chr_kaloz_04 = Pilote("Ripeur Delite", Alpine)
    wissam_04 = Pilote("Wissam", AstonMartin)

    wissam_04.setDonnees(wissam_03.getDonnees())

    tonati2514_04.setGamertagRemplacant("Tonati2514")
    chr_kaloz_04.setGamertagRemplacant("CHR Kaloz")
    wissam_04.setGamertagRemplacant("Wissam")

    # Pénalités en qualification
    # Aucune

    q04 = [
        emeric,
        crl_bikette,
        tonati2514_04,
        pura_chime,
        arac_zer,
        knf_fradj,
        chr_kaloz_04,
        mvt_fly,
        jnpjd,
        pura_matex,
        shadd,
        ecs_flower,
        non4me_lucas,
        leptit03,
        wissam_04,
        ldl_shermy,
        rp1_fifou,
        non4me_bappe,
        ks_virtuozz,
        mvt_kaio
    ]
    c04 = [
        emeric,
        arac_zer,
        non4me_lucas,
        jnpjd,
        mvt_kaio,
        non4me_bappe,
        mvt_fly,
        crl_bikette,
        leptit03,
        knf_fradj,
        wissam_04,
        rp1_fifou,
        pura_chime,
        ldl_shermy,
        ks_virtuozz,
        chr_kaloz_04,
        tonati2514_04,
        pura_matex,
        ecs_flower,
        shadd
    ]

    gp04.setQualification(q04)
    gp04.setCourse(c04)
    gp04.calcul(abandonsCourse = 6)

    al.compareCoequipiers(gp04)
    
    ###############################################################################################

    # Course 5
    gp05 = GrandPrix("Canada", sprint = False)

    # Remplaçants
    tonati2514_05 = Pilote("Emeric", McLaren)
    djedjam_05 = Pilote("CRL Bikette", AlfaRomeo)
    rocha1307_05 = Pilote("Ripeur Delite", Alpine)
    nxs_tiga_05 = Pilote("NoN4me Lucas", Ferrari)
    wissam_05 = Pilote("Shadd", AlphaTauri)

    tonati2514_05.setDonnees(tonati2514_04.getDonnees())
    djedjam_05.setDonnees(djedjam_02.getDonnees())
    nxs_tiga_05.setDonnees(nxs_tiga_03.getDonnees())
    wissam_05.setDonnees(wissam_04.getDonnees())

    tonati2514_05.setGamertagRemplacant("Tonati2514")
    djedjam_05.setGamertagRemplacant("Djedjam")
    rocha1307_05.setGamertagRemplacant("Rocha1307")
    nxs_tiga_05.setGamertagRemplacant("NXS Tiga")
    wissam_05.setGamertagRemplacant("Wissam")

    # Pénalités en qualification
    # Aucune

    q05 = [
        tonati2514_05,
        djedjam_05,
        pura_chime,
        arac_zer,
        ecs_flower,
        knf_fradj,
        rp1_fifou,
        jnpjd,
        mvt_fly,
        rs_al3xx,
        leptit03,
        pura_matex,
        rocha1307_05,
        ldl_shermy,
        mvt_kaio,
        non4me_bappe,
        ks_virtuozz,
        nxs_tiga_05,
        f1xr_noich,
        wissam_05
    ]
    c05 = [
        tonati2514_05,
        djedjam_05,
        pura_chime,
        pura_matex,
        rp1_fifou,
        arac_zer,
        jnpjd,
        non4me_bappe,
        rocha1307_05,
        f1xr_noich,
        ks_virtuozz,
        leptit03,
        mvt_fly,
        wissam_05,
        mvt_kaio,
        nxs_tiga_05,
        knf_fradj,
        rs_al3xx,
        ecs_flower,
        ldl_shermy
    ]

    gp05.setQualification(q05)
    gp05.setCourse(c05)
    gp05.calcul(abandonsCourse = 7)

    al.compareCoequipiers(gp05)

    ###############################################################################################

    # Course 6
    gp06 = GrandPrix("Mexique", sprint = False)

    # Remplaçants
    str_la_atge_06 = Pilote("Ripeur Delite", Alpine)
    darkyol_06 = Pilote("Rocha1307", Haas)
    djedjam_06 = Pilote("Djedjam", Haas)
    rocha1307_06 = Pilote("NXS Tiga", AstonMartin)

    djedjam_06.setDonnees(djedjam_05.getDonnees())
    rocha1307_06.setDonnees(rocha1307_05.getDonnees())

    str_la_atge_06.setGamertagRemplacant("STR La Atge")
    darkyol_06.setGamertagRemplacant("Darkyol")
    djedjam_06.setGamertagRemplacant("Djedjam")
    rocha1307_06.setGamertagRemplacant("Rocha1307")

    # Pénalités en qualification
    # Aucune

    q06 = [
        crl_bikette,
        emeric,
        pura_chime,
        djedjam_06,
        rocha1307_06,
        pura_matex,
        mvt_fly,
        non4me_lucas,
        knf_fradj,
        arac_zer,
        mvt_kaio,
        leptit03,
        ldl_shermy,
        darkyol_06,
        rp1_fifou,
        jnpjd,
        shadd,
        non4me_bappe,
        str_la_atge_06,
        f1xr_noich
    ]
    c06 = [
        crl_bikette,
        djedjam_06,
        arac_zer,
        rocha1307_06,
        jnpjd,
        knf_fradj,
        rp1_fifou,
        non4me_lucas,
        ldl_shermy,
        pura_chime,
        mvt_fly,
        mvt_kaio,
        f1xr_noich,
        non4me_bappe,
        darkyol_06,
        pura_matex,
        leptit03,
        str_la_atge_06,
        shadd,
        emeric
    ]

    gp06.setQualification(q06)
    gp06.setCourse(c06)
    gp06.calcul(abandonsCourse = 5)

    al.compareCoequipiers(gp06)

    ###############################################################################################

    # Course 7
    gp07 = GrandPrix("Japon", sprint = False)

    # Remplaçants
    rp1_eria_07 = Pilote("PuRa Chime", Ferrari)
    nfr_shadow_07 = Pilote("MVT Fly", Williams)
    str_la_atge_07 = Pilote("NXS Tiga", AstonMartin)
    wissam = Pilote("Wissam", AstonMartin)
    rocha1307 = Pilote("Rocha1307", Haas)
    djedjam = Pilote("Djedjam", Haas)

    str_la_atge_07.setDonnees(str_la_atge_06.getDonnees())
    wissam.setDonnees(wissam_05.getDonnees())
    rocha1307.setDonnees(rocha1307_06.getDonnees())
    djedjam.setDonnees(djedjam_06.getDonnees())

    rp1_eria_07.setGamertagRemplacant("RP1 Eria")
    nfr_shadow_07.setGamertagRemplacant("NFR Shadow")
    str_la_atge_07.setGamertagRemplacant("STR La Atge")
    wissam.setGamertagRemplacant("Wissam")
    rocha1307.setGamertagRemplacant("Rocha1307")
    djedjam.setGamertagRemplacant("Djedjam")

    # Pénalités en qualification
    # Aucune

    q07 = [
        djedjam,
        crl_bikette,
        pura_matex,
        emeric,
        jnpjd,
        mvt_kaio,
        knf_fradj,
        arac_zer,
        rp1_fifou,
        rp1_eria_07,
        nfr_shadow_07,
        non4me_lucas,
        shadd,
        ldl_shermy,
        arac_pafael,
        leptit03,
        str_la_atge_07,
        rocha1307,
        non4me_bappe,
        wissam
    ]
    c07 = [
        emeric,
        arac_pafael,
        jnpjd,
        knf_fradj,
        leptit03,
        mvt_kaio,
        rp1_eria_07,
        non4me_bappe,
        shadd,
        djedjam,
        rocha1307,
        crl_bikette,
        arac_zer,
        rp1_fifou,
        ldl_shermy,
        str_la_atge_07,
        pura_matex,
        non4me_lucas,
        wissam,
        nfr_shadow_07
    ]

    gp07.setQualification(q07)
    gp07.setCourse(c07)
    gp07.calcul(abandonsCourse = 5)

    al.compareCoequipiers(gp07)

    ###############################################################################################

    # Course 8
    gp08 = GrandPrix("France", sprint = True)

    # Remplacants
    nfr_shadow_08 = Pilote("CRL Bikette", AlfaRomeo)
    f1xr_elamous_08 = Pilote("RP1 Fifou", AlphaTauri)
    vieux_raleur_08 = Pilote("Ripeur Delite", Alpine)

    nfr_shadow_08.setDonnees(nfr_shadow_07.getDonnees())

    nfr_shadow_08.setGamertagRemplacant("NFR Shadow")
    f1xr_elamous_08.setGamertagRemplacant("F1XR Elamous")
    vieux_raleur_08.setGamertagRemplacant("Vieux Raleur")

    # Pénalités en qualification
    # Aucune

    q08 = [
        nfr_shadow_08,
        wissam,
        mvt_fly,
        knf_fradj,
        arac_zer,
        pura_chime,
        mvt_kaio,
        non4me_bappe,
        djedjam,
        jnpjd,
        leptit03,
        ecs_flower,
        f1xr_elamous_08,
        emeric,
        rocha1307,
        shadd,
        vieux_raleur_08,
        pura_matex,
        non4me_lucas,
        ldl_shermy
    ]
    s08 = [
        nfr_shadow_08,
        wissam,
        knf_fradj,
        djedjam,
        pura_matex,
        pura_chime,
        mvt_fly,
        non4me_bappe,
        f1xr_elamous_08,
        mvt_kaio,
        emeric,
        ldl_shermy,
        leptit03,
        non4me_lucas,
        vieux_raleur_08,
        shadd,
        arac_zer,
        rocha1307,
        ecs_flower,
        jnpjd
    ]
    c08 = [
        pura_chime,
        arac_zer,
        non4me_bappe,
        djedjam,
        jnpjd,
        pura_matex,
        mvt_kaio,
        emeric,
        ldl_shermy,
        wissam,
        knf_fradj,
        ecs_flower,
        non4me_lucas,
        mvt_fly,
        rocha1307,
        f1xr_elamous_08,
        vieux_raleur_08,
        shadd,
        nfr_shadow_08,
        leptit03
    ]

    gp08.setQualification(q08)
    gp08.setSprint(s08)
    gp08.setCourse(c08)
    gp08.calcul(abandonsCourse = 5, abandonsSprint = 5)

    al.compareCoequipiers(gp08)

    ###############################################################################################

    # Course 9
    gp09 = GrandPrix("Azerbaidjan", sprint = False)

    # Remplacants
    mcr_raiko_09 = Pilote("aRAC Zer", Mercedes)
    rp1_eria_09 = Pilote("PuRa Matex", Alpine)
    vniicklass_09 = Pilote("Ripeur Delite", Alpine)
    vieux_raleur_09 = Pilote("NXS Tiga", AstonMartin)
    cedric_dauby_09 = Pilote("CRL Bikette", AlfaRomeo)

    mcr_raiko_09.setDonnees(mcr_raiko_03.getDonnees())
    rp1_eria_09.setDonnees(rp1_eria_07.getDonnees())
    vieux_raleur_09.setDonnees(vieux_raleur_08.getDonnees())
    
    mcr_raiko_09.setGamertagRemplacant("MCR Raiko")
    rp1_eria_09.setGamertagRemplacant("RP1 Eria")
    vniicklass_09.setGamertagRemplacant("vNiicklass")
    vieux_raleur_09.setGamertagRemplacant("Vieux Raleur")
    cedric_dauby_09.setGamertagRemplacant("Cedric Dauby")

    # Pénalités en qualification
    # Aucune

    q09 = [
        pura_chime,
        rocha1307,
        djedjam,
        knf_fradj,
        mvt_fly,
        mvt_kaio,
        mcr_raiko_09,
        cedric_dauby_09,
        wissam,
        emeric,
        leptit03,
        rp1_fifou,
        non4me_bappe,
        non4me_lucas,
        jnpjd,
        rp1_eria_09,
        vniicklass_09,
        ldl_shermy,
        vieux_raleur_09,
        shadd
    ]
    c09 = [
        djedjam,
        pura_chime,
        wissam,
        non4me_lucas,
        mvt_kaio,
        jnpjd,
        emeric,
        non4me_bappe,
        cedric_dauby_09,
        ldl_shermy,
        rp1_fifou,
        leptit03,
        rp1_eria_09,
        shadd,
        rocha1307,
        vniicklass_09,
        mcr_raiko_09,
        knf_fradj,
        vieux_raleur_09,
        mvt_fly
    ]

    gp09.setQualification(q09)
    gp09.setCourse(c09)
    gp09.calcul(abandonsCourse = 7)

    al.compareCoequipiers(gp09)

    ###############################################################################################

    # Course 10
    gp10 = GrandPrix("Singapour", sprint = False)

    # Remplacants
    str_la_atge_10 = Pilote("NXS Tiga", AstonMartin)
    ripeur_delite_10 = Pilote("Ripeur Delite", Alpine)
    vieux_raleur_10 = Pilote("MVT Kaio", Williams)

    str_la_atge_10.setDonnees(str_la_atge_07.getDonnees())
    vieux_raleur_10.setDonnees(vieux_raleur_09.getDonnees())

    str_la_atge_10.setGamertagRemplacant("STR La Atge")
    ripeur_delite_10.setGamertagRemplacant("Ripeur Delite")
    vieux_raleur_10.setGamertagRemplacant("Vieux Raleur")

    # Pénalités en qualification
    # Aucune

    q10 = [
        pura_chime,
        crl_bikette,
        djedjam,
        jnpjd,
        arac_zer,
        rocha1307,
        ripeur_delite_10,
        non4me_lucas,
        emeric,
        rp1_fifou,
        mvt_fly,
        shadd,
        leptit03,
        wissam,
        ldl_shermy,
        vieux_raleur_10,
        pura_matex,
        knf_fradj,
        non4me_bappe,
        str_la_atge_10
    ]
    c10 = [
        crl_bikette,
        djedjam,
        emeric,
        knf_fradj,
        non4me_bappe,
        jnpjd,
        shadd,
        arac_zer,
        pura_matex,
        wissam,
        pura_chime,
        rp1_fifou,
        vieux_raleur_10,
        non4me_lucas,
        ripeur_delite_10,
        str_la_atge_10,
        mvt_fly,
        rocha1307,
        leptit03,
        ldl_shermy
    ]

    gp10.setQualification(q10)
    gp10.setCourse(c10)
    gp10.calcul(abandonsCourse = 5)

    al.compareCoequipiers(gp10)

    ###############################################################################################

    # Course 11
    gp11 = GrandPrix("Barhein", sprint = False)

    # Remplacants
    bistoufly_11 = Pilote("PuRa Matex", Alpine)
    blackpanther291_11 = Pilote("Non4me Lucas", Ferrari)
    ripeur_delite = Pilote("Ripeur Delite", Alpine)
    nxs_tiga = Pilote("NXS Tiga", AstonMartin)

    ripeur_delite.setDonnees(ripeur_delite_10.getDonnees())
    nxs_tiga.setDonnees(nxs_tiga_05.getDonnees())

    bistoufly_11.setGamertagRemplacant("Bistoufly")
    blackpanther291_11.setGamertagRemplacant("BlackPanther291")
    ripeur_delite.setGamertagRemplacant("Ripeur Delite")
    nxs_tiga.setGamertagRemplacant("NXS Tiga")

    # Pénalités en qualification
    # Aucune

    q11 = [
        djedjam,
        crl_bikette,
        pura_chime,
        emeric,
        shadd,
        mvt_kaio,
        arac_zer,
        ripeur_delite,
        jnpjd,
        leptit03,
        rocha1307,
        non4me_bappe,
        knf_fradj,
        rp1_fifou,
        nxs_tiga,
        mvt_fly,
        ldl_shermy,
        bistoufly_11,
        blackpanther291_11,
        wissam
    ]
    c11 = [
        djedjam,
        crl_bikette,
        emeric,
        shadd,
        pura_chime,
        mvt_kaio,
        rocha1307,
        knf_fradj,
        arac_zer,
        rp1_fifou,
        mvt_fly,
        leptit03,
        ripeur_delite,
        nxs_tiga,
        jnpjd,
        bistoufly_11,
        ldl_shermy,
        non4me_bappe,
        blackpanther291_11,
        wissam
    ]

    gp11.setQualification(q11)
    gp11.setCourse(c11)
    gp11.calcul(absentsQualif=1, absentsCourse=1)

    al.compareCoequipiers(gp11)

    ###############################################################################################

    # Course 12
    gp12 = GrandPrix("AbuDhabi", sprint = False)

    # Remplacants
    # Aucun

    # Pénalités en qualification
    # Aucune

    q12 = [
        djedjam,
        pura_matex,
        crl_bikette,
        pura_chime,
        emeric,
        leptit03,
        non4me_lucas,
        rocha1307,
        mvt_kaio,
        jnpjd,
        knf_fradj,
        non4me_bappe,
        ripeur_delite,
        wissam,
        mvt_fly,
        arac_zer,
        nxs_tiga,
        ldl_shermy,
        rp1_fifou,
        shadd
    ]
    c12 = [
        pura_matex,
        djedjam,
        crl_bikette,
        arac_zer,
        non4me_bappe,
        rp1_fifou,
        wissam,
        ripeur_delite,
        ldl_shermy,
        nxs_tiga,
        knf_fradj,
        shadd,
        jnpjd,
        emeric,
        pura_chime,
        leptit03,
        non4me_lucas,
        mvt_kaio,
        mvt_fly,
        rocha1307
    ]

    gp12.setQualification(q12)
    gp12.setCourse(c12)
    gp12.calcul(abandonsCourse=10)

    al.compareCoequipiers(gp12)
    
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
        Pénalités en qualifications :
        /
        """

        courses = [gp01, gp02, gp03, gp04, gp05, gp06, gp07, gp08, gp09, gp10, gp11, gp12]
        Fonctions.writeDriverStats(courses, "w", "d4")
        Fonctions.writeTeamStats([Mercedes, RedBull, Ferrari, McLaren, Alpine, AlphaTauri, AstonMartin, Williams, AlfaRomeo, Haas], "a")

        """
        al.affiche()
        """

    ###############################################################################################

    return final