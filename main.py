# -*- coding: utf-8 -*-
"""
Compression du tome 1 des misérables en chiffres
"""


def complete(complete_param_nombre, complete_param_longueur):
    """
    Complete le nombre complete_param_nombre avec des zéros pour qu'il ait une longueur égale à complete_param_longueur
    :type complete_param_nombre: int
    :param complete_param_nombre: Le nombre à compléter
    :param complete_param_longueur: La longueur à atteindre
    :return: le nombre complété avec des zéros sous la forme d'une chaine de caractères
    """
    complete_chaine = str(complete_param_nombre)
    complete_l1 = len(complete_chaine)
    for a in range(complete_param_longueur-complete_l1):
        complete_chaine = "0"+complete_chaine
    return complete_chaine


def chaine_absent(absent_param_contenuctxt):
    """
    Renvoie une chaine qui n'apparait pas dans absent_param_contenuctxt et de longueur la plus faible possible
    :param absent_param_contenuctxt: Le texte dans lequel chercher la chaine qui n'apparait pas
    :return: La chaine qui n'apparait pas
    """
    absent_trouve = False
    absent_l = 0
    absent_chainetest = ""
    while not absent_trouve:
        absent_l += 1
        if absent_l == 9:
            break
        absent_nombretest = 0
        while (not absent_trouve) and (absent_nombretest < 10**absent_l):
            absent_chainetest = complete(absent_nombretest, absent_l)
            absent_n = absent_param_contenuctxt.count(absent_chainetest)
            if absent_n == 0:
                absent_trouve = True
            absent_nombretest += 1
    return absent_trouve, absent_chainetest


def chaine_longue(chainelongue_param_lmin, chainelongue_param_contenuctxt):
    """
    Renvoie la chaine qui apparait le plus souvent dans le contenu du fichier ctxt, dont la longueur minimum est égale à
    L_min, et dont la longueur maximum est égale à 32
    :param chainelongue_param_lmin: La longueur minimumu (L_min)
    :param chainelongue_param_contenuctxt: Le contenu du fichier ctxt
    :return: la chaine qui apparait le plus souvent dans le contenu du fichier ctxt, dont la longueur minimum est égale
    à L_min, et dont la longueur maximum est égale à 32
    """
    # TODO Vider inutiles
    chainelongue_trouve = False
    chainelongue_nmaxi = 0
    chainelongue_countmaxi = 0
    chainelongue_l = chainelongue_param_lmin
    chainelongue_chainetest = ''
    chainelongue_test = 0
    while (not chainelongue_trouve) and (chainelongue_test < 10**chainelongue_l):
        chainelongue_chainetest = complete(chainelongue_test, chainelongue_l)
        chainelongue_r = chainelongue_param_contenuctxt.count(chainelongue_chainetest)
        if chainelongue_r > chainelongue_countmaxi:
            chainelongue_nmaxi = chainelongue_chainetest
            chainelongue_countmaxi = chainelongue_r
        chainelongue_test += 1
    chainelongue_gain1 = (chainelongue_countmaxi * len(chainelongue_nmaxi)) - \
                         (chainelongue_countmaxi * chainelongue_param_lmin)
    chainelongue_gain2 = 0
    chainelongue_lg = len(chainelongue_nmaxi) + 1
    print(chainelongue_nmaxi)
    chainelongue_ntest = ''
    chainelongue_simplifie = True
    return chainelongue_nmaxi


# TODO chaine_longue
with open("miserables-tome1.txt") as file:
    text = file.read()

ctxt = ""
ctxtfile = open("miserables_non_compresse.ctxt", 'w')

for i in range(0, len(text)):
    tplus = str(ord(text[i]))
    for j in range(0, (4-len(tplus))):
        tplus = "0" + tplus
    ctxt += tplus

ctxtfile.write(ctxt)
