# -*- coding: utf-8 -*-
"""
Fonctions de déboguage
"""
# TODO Supression du fichier
with open("miserables_non_compresse.ctxt") as file:
    text = file.read()


def min_val(a, b):
    """
    Trouve le caractère le moins présent dans l'intervalle [a;b] du fichier ctxt
    :param a: Début de l'intervalle
    :param b: Fin de l'intervalle
    :return: Le caractère le moins présent dans l'intervalle [a;b] du fichier ctxt
    """
    text_intrvll = text[a:b]
    txtl = []
    for char in text_intrvll:
        txtl.append(int(char))
    txtlc = [txtl.count(0), txtl.count(1), txtl.count(2), txtl.count(3), txtl.count(4), txtl.count(5), txtl.count(6),
             txtl.count(7), txtl.count(8), txtl.count(9)]
    return txtlc.index(min(txtlc))
