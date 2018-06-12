#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from MyQR.mylibs import theqrmodule
from PIL import Image,ImageDraw,ImageOps,ImageEnhance, ImageFilter
from MyQR.mylibs.constant import alig_location
import tempfile

# Positional parameters
#   words: str
#
# Optional parameters
#   version: int, from 1 to 40
#   level: str, just one of ('L','M','Q','H')
#   picutre: str, a filename of a image
#   colorized: bool
#   constrast: float
#   brightness: float
#   save_name: str, the output filename like 'example.png'
#   save_dir: str, the output directory
#
# See [https://github.com/sylnsfar/qrcode] for more details!

def combine(ver, qr_name):
    qr = Image.open(qr_name)
    aligs = []
    if ver > 1:
        aloc = alig_location[ver-2]
        for a in range(len(aloc)):
            for b in range(len(aloc)):
                if not ((a==b==0) or (a==len(aloc)-1 and b==0) or (a==0 and b==len(aloc)-1)):
                    for i in range(3*(aloc[a]-2), 3*(aloc[a]+3)):
                        for j in range(3*(aloc[b]-2), 3*(aloc[b]+3)):
                            aligs.append((i,j))

    for i in range(qr.size[0]-24):
        for j in range(qr.size[1]-24):
            if not ((i in (18,19,20)) or (j in (18,19,20)) or (i<24 and j<24) or (i<24 and j>qr.size[1]-49) or (i>qr.size[0]-49 and j<24) or ((i,j) in aligs) or (i%3==1 and j%3==1)):
                qr.putpixel((i+12,j+12), 0)
    # qr.resize((qr.size[0]*3, qr.size[1]*3)).save(qr_name)
    qr = ImageOps.expand(qr.crop(qr.getbbox()),border=3,fill=0) #添加边界
    d = ImageDraw.Draw(qr)
    #填补马眼
    x_end = qr.size[0]-1
    y_end = qr.size[1]-1
    d.rectangle([0,0,26,2],'white')# 左上
    d.rectangle([0,0,2,26],'white')
    d.rectangle([x_end, 0, x_end - 26,2],'white') #右上
    d.rectangle([x_end, 0, x_end - 2,26],'white')
    d.rectangle([0, y_end, 2,y_end-26],'white') #右下
    d.rectangle([0, y_end, 26, y_end-2],'white')
    return qr

def run(words, version=1, level='H', scale=1):
    supported_chars = r"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ··,.:;+-*/\~!@#$%^&`'=<>[]()?_{}|"
    # check every parameter
    if not isinstance(words, str) or any(i not in supported_chars for i in words):
        raise ValueError('Wrong words! Make sure the characters are supported!')
    if not isinstance(version, int) or version not in range(1, 41):
        raise ValueError('Wrong version! Please choose a int-type value from 1 to 40!')
    if not isinstance(level, str) or len(level)>1 or level not in 'LMQH':
        raise ValueError("Wrong level! Please choose a str-type level from {'L','M','Q','H'}!")

    # tempdir = os.path.join(os.path.expanduser('~'), '.myqr')
    tempdir=tempfile.mkdtemp(prefix='myqr_')
    try:
        if not os.path.exists(tempdir):
            os.makedirs(tempdir)

        ver, qr_name = theqrmodule.get_qrcode(version, level, words, tempdir)
        qr = combine(ver, qr_name)
        if scale != 1:
            qr = qr.resize((qr.size[0]*scale, qr.size[1]*scale))
        return qr

    except:
        raise
    finally:
        import shutil
        if os.path.exists(tempdir):
            shutil.rmtree(tempdir)
