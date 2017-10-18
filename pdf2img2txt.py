#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 17:29:22 2017

@author: bill
"""
from wand.image import Image
from img2txt import img2txt


def pdf2img2txt(fname):
    req_image=[]
    text = []
    image_pdf = Image(filename=fname,resolution = 300)
    image_jpeg = image_pdf.convert('jpeg')

    count = 0
    for img in image_jpeg.sequence:
        count+=1
        img_page = Image(image=img)
        req_image.append(img_page.make_blob('jpeg'))
        img_page.save(filename="temp"+"-"+str(count)+".jpg")
        count = 0
        for img in req_image:
            count+=1
            txt = img2txt("temp"+"-"+str(count)+".jpg")
        text.append(txt)
        final_text = "".join(text)
    return(final_text)
