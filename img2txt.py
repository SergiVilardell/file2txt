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
    im = Image.open(fname) # the second one 
    im = im.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(im)
    im = enhancer.enhance(2)
    im = im.convert('1')
    im.save('temp.jpg')
    text = pytesseract.image_to_string(Image.open('temp.jpg'))
    os.remove("temp.jpg")
    return(text)
    
