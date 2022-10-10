from packageF1.Ecurie import *
from packageF1.Pilote import *
from packageF1.GrandPrix import *

import csv
import pandas as pd

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
    pura_chime = Pilote("PuRa Chime", Ferrari)
    jnpjd = Pilote("JNPJD", McLaren)
    emeric = Pilote("Emeric", McLaren)
    leonh4rte = Pilote("PuRa Matex", Alpine) # remplaçé
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

    leonh4rte.setGamertagRemplacant("Leonh4rte")

    ###############################################################################################

    # Course 1
    gp01 = GrandPrix("RoyaumeUni", sprint = False)

    # Remplaçants
    # Aucun

    # Pénalites en qualification
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

    ###############################################################################################

    # Course 2
    gp02 = GrandPrix("Belgique", sprint = True)

    # Remplaçants
    djedjam_02 = Pilote("KS Virtuozz", Haas)
    legion_rambow_02 = Pilote("RS Al3xx", Haas)
    pura_matex = Pilote("PuRa Matex", Alpine)

    djedjam_02.setGamertagRemplacant("DJedjam")
    legion_rambow_02.setGamertagRemplacant("Legion Rambow")

    # Pénalites en qualification
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

    ###############################################################################################

    # Course 3
    gp03 = GrandPrix("Espagne", sprint = False)

    # Remplaçants
    mcr_raiko_03 = Pilote("ARAC Pafael", Alpine)
    wissam_03 = Pilote("RS Al3xx", Haas)
    nxs_tiga_03 = Pilote("aRAC Zer", Mercedes)

    mcr_raiko_03.setGamertagRemplacant("MCR Raiko")
    wissam_03.setGamertagRemplacant("Wissam")
    nxs_tiga_03.setGamertagRemplacant("NXS Tiga")

    # Pénalites en qualification
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

    ###############################################################################################

    # Course 4
    gp04 = GrandPrix("Miami", sprint = False)

    # Remplaçants
    tonati2514_04 = Pilote("RS Al3xx", Haas)
    chr_kaloz_04 = Pilote("ARAC Pafael", Alpine)
    wissam_04 = Pilote("F1XR Noich", AstonMartin)

    tonati2514_04.setGamertagRemplacant("Tonati2514")
    chr_kaloz_04.setGamertagRemplacant("CHR Kaloz")
    wissam_04.setGamertagRemplacant("Wissam")

    # Pénalites en qualification
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

    # Classement final ############################################################################

    final = gp01.getPoints()
    final = sumDict(final, gp02.getPoints())
    final = sumDict(final, gp03.getPoints())
    final = sumDict(final, gp04.getPoints())

    # Statistiques ################################################################################

    """
    Remplacements :
        pura_matex = Pilote("PuRa Matex", Alpine)
    djedjam_02 = Pilote("KS Virtuozz", Haas)
    legion_rambow_02 = Pilote("RS Al3xx", Haas)
    mcr_raiko_03 = Pilote("ARAC Pafael", Alpine)
    nxs_tiga_03 = Pilote("aRAC Zer", Mercedes)
    tonati2514_04 = Pilote("RS Al3xx", Haas)
    chr_kaloz_04 = Pilote("ARAC Pafael", Alpine)
    wissam_03 = Pilote("RS Al3xx", Haas)
    wissam_04 = Pilote("F1XR Noich", AstonMartin)

    Pénalités en qualifications :
    /
    """
    
    pilotes = []
    courses = [gp01, gp02, gp03, gp04]
    for course in courses:
        participants = course.getQualification()
        for pilote in participants:
            if pilote not in pilotes:
                pilotes.append(pilote)

    # print(len(pilotes))

    f = open('.\s7\stats.csv', 'w', newline="")
    writer = csv.writer(f)

    writer.writerow(["pilote;division;nb_q;nb_q2;nb_q3;best_q;nb_poles_q;moy_q;vsCoeq_q;nb_s;nb_top8_s;nb_podium_s;nb_win_s:best_s;moy_s;vsCoeq_s;nb_c;nb_top10_c;nb_podium_c;nb_win_c;best_c;moy_c;vsCoeq_c"])

    for p in pilotes:

        donnees = p.getDonnees()
        tabQ = donnees.tabQ()
        tabS = donnees.tabS()
        tabC = donnees.tabC()

        line = p.getGamertagRemplacant() + ";4;"

        line += "{};{};{};{};{};{};{};".format(
            donnees.nbQ(tabQ),
            donnees.nbQ2(tabQ),
            donnees.nbQ3(tabQ),
            donnees.nbPoles(tabQ),
            donnees.bestQ(tabQ),
            donnees.avgQ(tabQ),
            donnees.getCoeqBattuQ()
        )
        line += "{};{};{};{};{};{};".format(
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

    df = pd.read_csv(".\s7\stats.csv")
    print(df)
    new_df = df.groupby(["pilote"]).sum()
    new_df.to_excel("stats.xlsx")

    # Classement final ############################################################################

    final = gp01.getPoints()
    final = sumDict(final, gp02.getPoints())
    final = sumDict(final, gp03.getPoints())
    final = sumDict(final, gp04.getPoints())

    return final

