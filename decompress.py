#!/usr/bin/env python3
#-*- coding:utf-8 -*-
"""
Projet Algorithme de Compression
Fichier decompress.py
================================
Décompresse le fichier compressé
"""
def decompress(cmprss_filename):
    print("Décompression de", cmprss_filename)
    print("Lecture du fichier...", end=" ")
    cmprss_data = open(cmprss_filename).read()
    print(cmprss_data)
    print("Fait.")
    print("Décompression...")
    print(" Lecture du nombre d'itérations...", end=" ")
    str_iter = cmprss_data[0:4]
    nb_iter = int(str_iter) + 1
    print("Fait.")
    for i in range(nb_iter):    # La boucle pour les différentes compressions
        print(" Détection de la chaîne absente...", end=" ")
        lch_absent = int(cmprss_data[4])
        ch_absent = cmprss_data[5:5+lch_absent]
        print(ch_absent)
        print("Fait.")
        print(" Détection de la chaîne longue...", end=" ")
        pos = 5+len(ch_absent)
        lch_longue = int(cmprss_data[pos])
        ch_longue = cmprss_data[pos+1:pos+1+lch_longue]
        print(ch_longue)
        print("Fait.")
        print(" Échange chaîne longue / chaîne absente...", end=" ")
        print(cmprss_data[pos+1+lch_longue:])
        print("DATA :", cmprss_data[pos+1+lch_longue:])
        cmprss_data_c = cmprss_data[pos+1+lch_longue:].replace(ch_absent, ch_longue)
        cmprss_data = cmprss_data_c
        print("Fait.")
    return cmprss_data

def decode_ctxt(text_param):
    r = ""
    for a in range(0, len(text_param), 4):
        r += chr(int(text_param[a:a+4]))
    return r


decode_ctxt(decompress("compresse.cmprss"))
