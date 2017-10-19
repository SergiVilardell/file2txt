#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 17:04:13 2017

@author: bill
"""
import os
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

path = "/home/bill/Projects/Python Projects/OCR"

os.chdir(path)

def img2txt(fname):
    pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
    text = pytesseract.image_to_string(Image.open(fname))

    return(text)
    
