#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""
def surcompress(cmprss):
    print("Hello !")
    r = ""
    for a in range(0, len(cmprss), 4):
        r += chr(int(cmprss[a:a+4]))
    return r

f = open("surcompresse.scmprss", "w", encoding="utf-8")
f.write(surcompress(open("compresse.cmprss").read()))
