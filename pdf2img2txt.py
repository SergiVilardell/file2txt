#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 17:29:22 2017

@author: bill
"""
from wand.image import Image
from img2txt import img2txt
import os

def pdf2img2txt(fname):
    req_image=[]
    text = []
    image_pdf = Image(filename = fname, resolution = 300)
    image_jpeg = image_pdf.convert('jpeg')
    for img in image_jpeg.sequence:
        temp = "temp.jpg"
        img_page = Image(image=img)
        req_image.append(img_page.make_blob('jpeg'))
        img_page.save(filename= temp)
        img_page.close()
        txt = img2txt(temp)
        text.append(txt)
    final_text = "".join(text)
    image_pdf.close()
    image_jpeg.close()
    os.remove(temp)
    return(final_text)
        

