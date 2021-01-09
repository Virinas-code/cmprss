#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""
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

def desurcompress(scmprss):
    r = ""
    for a in range(0, len(scmprss)):
        r += complete(str(ord(scmprss[a])), 4)
    return r

print(desurcompress(open("surcompresse.scmprss", encoding="utf-8").read()))
