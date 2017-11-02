#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 17:04:13 2017

@author: bill
"""

import pytesseract
from PIL import Image

Image.warnings.simplefilter('error', Image.DecompressionBombWarning)

#Calls Tesseract and returns the text, nothing fancy.
def img2txt(fname):
    im = Image.open(fname)
    text = pytesseract.image_to_string(im, lang = 'spa')
    im.close()
    return(text)
    
def img2txt_90(fname):
    im = Image.open(fname)
    rot_im = im.rotate(90)
    text = pytesseract.image_to_string(rot_im, lang = 'spa')
    im.close()
    rot_im.close()
    return(text)
    
def img2txt_180(fname):
    im = Image.open(fname)
    rot_im = im.rotate(180)
    text = pytesseract.image_to_string(rot_im, lang = 'spa')
    im.close()
    rot_im.close()
    return(text)
    
def img2txt_270(fname):
    im = Image.open(fname)
    rot_im = im.rotate(270)
    text = pytesseract.image_to_string(rot_im, lang = 'spa')
    im.close()
    rot_im.close()
    return(text)