#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 17:29:22 2017

@author: bill
"""
from wand.image import Image
from img2txt import img2txt,img2txt_90,img2txt_180,img2txt_270
import os


#This function basically opens the pdf, converts to jpeg and calls img2txt, returning the text.
#TODO: check which rotation gives the best result with the help of a dictionary,
def pdf2img2txt(fname):
    text = []
    req_image=[]
    image_pdf = Image(filename = fname, resolution = 300)
    image_jpeg = image_pdf.convert('jpeg')
    img = image_jpeg.sequence[0]
    image_jpeg.close()
    temp = "temp.jpg"
    img_page = Image(image=img)
    req_image.append(img_page.make_blob('jpeg'))
    img_page.save(filename= temp)
    img_page.close()
    txt = img2txt(temp)
    #TODO: check with dictionary: if result not good, rotate with **img_page.rotate(90)**
    text.append(txt)
    image_pdf.close()
    os.remove(temp)
    return(text)
        
def pdf2img2txt_90(fname):
    text = []
    req_image=[]
    image_pdf = Image(filename = fname, resolution = 300)
    image_jpeg = image_pdf.convert('jpeg')
    img = image_jpeg.sequence[0]
    image_jpeg.close()
    temp = "temp.jpg"
    img_page = Image(image=img)
    req_image.append(img_page.make_blob('jpeg'))
    img_page.save(filename= temp)
    img_page.close()
    txt = img2txt_90(temp)
    text.append(txt)
    image_pdf.close()
    os.remove(temp)
    return(text)

def pdf2img2txt_180(fname):
    text = []
    req_image=[]
    image_pdf = Image(filename = fname, resolution = 300)
    image_jpeg = image_pdf.convert('jpeg')
    img = image_jpeg.sequence[0]
    image_jpeg.close()
    temp = "temp.jpg"
    img_page = Image(image=img)
    req_image.append(img_page.make_blob('jpeg'))
    img_page.save(filename= temp)
    img_page.close()
    txt = img2txt_180(temp)
    text.append(txt)
    image_pdf.close()
    os.remove(temp)
    return(text)

def pdf2img2txt_270(fname):
    text = []
    req_image=[]
    image_pdf = Image(filename = fname, resolution = 300)
    image_jpeg = image_pdf.convert('jpeg')
    img = image_jpeg.sequence[0]
    image_jpeg.close()
    temp = "temp.jpg"
    img_page = Image(image=img)
    req_image.append(img_page.make_blob('jpeg'))
    img_page.save(filename= temp)
    img_page.close()
    txt = img2txt_270(temp)
    text.append(txt)
    image_pdf.close()
    os.remove(temp)
    return(text)

