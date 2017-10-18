#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 16:55:55 2017

@author: bill
"""

import os
import nltk
from nltk.corpus import cess_esp
from pdf2txt import pdf2txt
from img2txt import img2txt
from pdf2img2txt import pdf2img2txt
from dic_check import word_check

#Routine: if pdf -> pdf2txt, if pdf not searchable -> pdf2img2txt
#         else if img -> img2txt
#Then:
#Compare outputs with the dictionary and get the best one

path = "/home/bill/Projects/Python Projects/OCR"

os.chdir(path)

file = "main.pdf"

out_pdf = pdf2txt(file)
out_img = pdf2img2txt(file)



#print(out_img)
