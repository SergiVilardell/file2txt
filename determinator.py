#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 16:55:55 2017

@author: bill
"""

import os
import sys
sys.path.append('C:\\Users\\I.SERRA\\Desktop\\Script python')

from pdf2txt import pdf2txt
from img2txt import img2txt
from pdf2img2txt import pdf2img2txt
from att2table import att_data 


#Routine: if pdf -> pdf2txt, if pdf not searchable -> pdf2img2txt
#         else if img -> img2txt
#Then:
#Compare outputs with the dictionary and get the best one

#path = "C:\\Users\\I.SERRA\\Desktop\\1 Datos\\HEGEO\\Administración\\20 - Anulación póliza\\6308184"

#os.chdir(path)

#file = "20161230DOC-1442.pdf"

#out_pdf = pdf2txt(file)
#out_pdfimg = pdf2img2txt(file)


processed_text = [""]*len(att_data) 


def process_pdf():
    file_name = att_data["Filename"].tolist()
    file_ext = att_data["Ext"].tolist()
    filepath = att_data["Path"].tolist()
    count = 0
    for i in range(len(file_name)):
        if(file_ext[i] == "pdf"):
            count+=1
            if( count%10 == 0):
                print("Processed files: "+str(count))
            path = filepath[i]
            os.chdir(path)
            file = file_name[i]
            processed_text[i] = pdf2txt(file)

def process_scanned_pdf():
    file_name = att_data["Filename"].tolist()
    file_ext = att_data["Ext"].tolist()
    filepath = att_data["Path"].tolist()
    count = 0
    for i in range(len(file_name)):
        if(file_ext[i] == "pdf" or file_ext[i] == "PDF"):
            count+=1
            print("Analizando: "+file_name[i])
            path = filepath[i]
            os.chdir(path)
            file = file_name[i]
            try:
                processed_text[i] = pdf2img2txt(file)
            except:
                pass
            print("Procesados: "+str(count))
            
            
        
            
def process_img():
    img_ext = ["jpg", "jpeg", "JPG", "gif", "png", "PNG", "tif", "TIF"]
    file_name = att_data["Filename"].tolist()
    file_ext = att_data["Ext"].tolist()
    filepath = att_data["Path"].tolist()
    count = 0
    for i in range(len(file_name)):
        if (file_ext[i] in img_ext):
            count+=1
            if( count%10 == 0):
                print("Processed files: "+str(count))
            path = filepath[i]
            os.chdir(path)
            file = file_name[i]
            processed_text[i]= img2txt(file)
            

process_pdf()
process_scanned_pdf()
process_img()       
    
#print(data["Cuerpo"][50])   
    
    
    
#out = img2txt(file)





#print(out_img)
