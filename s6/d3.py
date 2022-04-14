from packageF1.Pilote import *
from packageF1.GrandPrix import *
from packageF1.Joueur import *
from packageF1.EnsembleJoueur import *
from packageF1.fonctions import *

#
# Saison 6
#
# Calcul des points pour les pilotes de division 3
#

def getPointsD3() -> dict:

    ###################################################################################################

    # Création des pilotes

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    ecs_finesse = Pilote("ESC Finesse", "Mercedes")
    ert_wartors = Pilote("ERT Wartors", "Mercedes")

    non4me_cami = Pilote("Non4ame Cami", "RedBull")
    soo_skyzzz = Pilote("Soo Skyzzz", "RedBull")

    knacki_ball = Pilote("Knacki Ball", "McLaren")
    pur_marth = Pilote("PuR Marth", "McLaren")

    nygraal = Pilote("Nygraal", "Ferrari")
    chr_olivz = Pilote("CHR Olivz", "Ferrari")

    spl_eroziah = Pilote("SPL EroziaH", "AlphaTauri")
    ert_mirage = Pilote("ERT Mirage", "AlphaTauri")

    rp1_fifi = Pilote("RP1 Fifi", "Alpine")
    ducpascharlie = Pilote("DucPasCharlie", "Alpine")

    rp1_gachette = Pilote("RP1 Gachette", "AstonMartin")
    istoozen_eko = Pilote("Istoozen eKo", "AstonMartin")

    sks_flyart = Pilote("SKS Flyart", "AlfaRomeo")
    mcr_papyx = Pilote("MCR Papyx", "AlfaRomeo")

    ert_aurelius = Pilote("ERT Aurelius", "Williams")
    ert_matfax = Pilote("ERT Matfax", "Williams")

    alexgt500 = Pilote("AlexGT500", "Haas")
    ert_toon = Pilote("ERT Toon", "Haas")

    ###################################################################################################

    # Course 1

    result01 = GrandPrix("Autriche")

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    qualif01 = [
    ]

    course01 = [
    ]

    # classements
    result01.resultat("q", qualif01)
    result01.resultat("c", course01)

    # évènements ponctuels

    return {}