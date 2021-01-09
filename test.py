# -*- coding: utf-8 -*-
"""
Compression du tome 1 des misérables en chiffres
"""
nombre_compressions = 0


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

def compress():
    global ctxt, nombre_compressions
    """
    La fonction qui écrit le fichier compressé
    """
    psize = len(ctxt)
    pctxt = ctxt
    csize = 0
    while (True):
        print("Compression...")
        print(" Génération des en-têtes...")
        headers = str()
        headers += complete(nombre_compressions, 4)
        ca = chaine_absent(ctxt)
        print("  Chaîne absente :", ca[1])
        headers += str(len(ca[1]))
        headers += ca[1]
        print(" Terminé.")
        print(" Compression...")
        # Génération de la chaîne longue :
        for a in range(32):
            print("  Itération.")
            plen = len(ctxt)
            print("  Longueur avant :", plen)
            print("  Texte avant :", ctxt)
            cl = chaine_longue(a, ctxt)
            print("  Chaine longue :", cl)
            ctxt = ctxt.replace(cl, ca[1])
            print("  Texte après :", ctxt)
            if len(ctxt) < plen :
                print("  Longueur après :", len(ctxt))
                print(" Terminé.")
                break
            else:
                print("  Err.")
                print("  Texte avant :", ctxt)
                ctxt = ctxt.replace(ca[1], cl)
                print("  Texte après :", ctxt)
        headers += str(len(cl))
        headers += cl
        ctxt = headers + ctxt
        csize = len(ctxt)
        if (csize > psize):
            ctxt = pctxt
            print("INVALID  HEADERS :", headers)
            print("BODY :", ctxt)
            print("INVALID  CHAINE LONGUE :", cl)
            print("INVALID  CHAINE ABSENTE :", ca)
            print("LONGUEUR FINALE :", len(ctxt))
            print("TEXTE FINAL :", ctxt)
            print("TERMINE")
            with open("compresse.cmprss", 'w') as f:
                f.write(ctxt)
            break
        nombre_compressions+=1
        print("HEADERS :", headers)
        print("BODY :", ctxt)
        print("CHAINE LONGUE :", cl)
        print("CHAINE ABSENTE :", ca)
        print("LONGUEUR FINALE :", csize)
        pctxt = ctxt
        psize = len(ctxt)


# TODO chaine_longue
with open("miserables-tome1-Copy2.txt") as file:
    text = file.read()

ctxt = ""
print("Génération du fichier ctxt...")
print(len(text), "lignes.")
ctxtfile = open("miserables_non_compresse.ctxt", 'w')
for i in range(0, len(text)):
    tplus = str(ord(text[i]))
    for j in range(0, (4-len(tplus))):
        tplus = "0" + tplus
    ctxt += tplus
print("Terminé.")
ctxtfile.write(ctxt)
def decode_ctxt(text_param):
    r = ""
    for a in range(0, len(text_param), 4):
        r += chr(int(text_param[a:a+4]))
    return r
print(decode_ctxt(ctxt))
compress()
