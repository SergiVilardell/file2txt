#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 17:04:13 2017

@author: bill
"""

import pytesseract
from PIL import Image

Image.warnings.simplefilter('error', Image.DecompressionBombWarning)


def img2txt(fname):
    im = Image.open(fname)
    text = pytesseract.image_to_string(im, lang = 'spa')
    im.close()
    return(text)
    
