# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 16:20:25 2017

@author: I.SERRA
"""
import os
import sys
import random as rand
sys.path.append('C:\\Users\\I.SERRA\\Desktop\\Script python')


from pdf2txt import pdf2txt
from img2txt import img2txt,img2txt_90,img2txt_180,img2txt_270
from pdf2img2txt import pdf2img2txt,pdf2img2txt_90,pdf2img2txt_180,pdf2img2txt_270
from att2table import att_data #Aqui importa un dataframe que es una variable 
from filenet_table import filenet_data #Aqui importa un dataframe que es una variable


#Not useful atm, tesseract gives equal results on searchable pdfs
def process_pdf():
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
                processed_text[i] = pdf2txt(file)
            except:
                pass
            print("Procesados: "+str(count))



def process_scanned_pdf():
    #-------------------------------------------------------------------------------    
    #Make behorefand the directory with the Ys as names and the 0,1,2,3 directories
    # just like "p docs" or "p images" in Script python
    #-------------------------------------------------------------------------------    
    file_name = att_data["Filename"].tolist()
    file_ext = att_data["Ext"].tolist()
    filepath = att_data["Path"].tolist()
    y = att_data["Y"].tolist()
    dest_path = "C:\\Users\\I.SERRA\\Desktop\\Script python\\pr docs"
    count = 0
    #Veo en el iterado donde se quedo congelado y a partir de ese iterado comienza el siguiente for (iter,len(file_name))
    for i in range(8):
        print("Iteracion: "+str(i))
        if(file_ext[i] == "pdf" or file_ext[i] == "PDF"):
            count+=1
            print("Analizando: "+file_name[i])
            path = filepath[i]
            g = path.split("\\")
            group = g[len(g)-1]
            os.chdir(path)
            file = file_name[i]
            text_rot = [""]*4
            try:
                text_rot[0] = pdf2img2txt(file)
                text_rot[1] = pdf2img2txt_90(file)
                text_rot[2] = pdf2img2txt_180(file)
                text_rot[3] = pdf2img2txt_270(file)
            except:
                pass
            for k in range(len(text_rot)):
                 #Make the directory and 4 subfolders named 0,1,2,3. One for each rotation
                pathrot = dest_path +"\\"+str(y[i])+"\\"+str(k)
                for j in range(len(text_rot[k])):
                    os.chdir(pathrot)
                    filen = group+"-"+file.split(".")[0]+"-"+str(j)+".txt"
                    text = text_rot[k]
                    f = open(filen, "w", encoding = "utf-8")
                    f.write(text[j])
                    f.close()
            print("Procesados: "+str(count))

def process_scanned_pdf_siniestros():
    #-------------------------------------------------------------------------------    
    #Make behorefand the directory with the Ys as names and the 0,1,2,3 directories
    # just like "p docs" or "p images" in Script python
    #-------------------------------------------------------------------------------    
    file_name = filenet_data["Filename"].tolist()
    filepath = filenet_data["Path"].tolist()
    y = filenet_data["Y"].tolist()
    dest_path = "C:\\Users\\I.SERRA\\Desktop\\Script python\\pr docs sin"
    count = 0
    #Veo en el iterado donde se quedo congelado y a partir de ese iterado comienza el siguiente for (iter,len(file_name))
    for i in range(len(file_name)):
        print("Iteracion: "+str(i))
        count+=1
        print("Analizando: "+file_name[i])
        path = filepath[i]
        g = path.split("\\")
        group = g[len(g)-1]
        os.chdir(path)
        file = file_name[i]
        text_rot = [""]*4
        try:
            text_rot[0] = pdf2img2txt(file)
            text_rot[1] = pdf2img2txt_90(file)
            text_rot[2] = pdf2img2txt_180(file)
            text_rot[3] = pdf2img2txt_270(file)
        except:
            pass
        for k in range(len(text_rot)):
            #Make the directory and 4 subfolders named 0,1,2,3. One for each rotation
            pathrot = dest_path +"\\"+str(y[i])+"\\"+str(k)
            for j in range(len(text_rot[k])):
                os.chdir(pathrot)
                filen = group+"-"+file.split(".")[0]+"-"+str(j)+".txt"
                text = text_rot[k]
                f = open(filen, "w", encoding = "utf-8")
                f.write(text[j])
                f.close()
        print("Procesados: "+str(count))
    


        
def process_img():
    #-------------------------------------------------------------------------------    
    #Make behorefand the directory with the Ys as names and the 0,1,2,3 directories
    # just like "p docs" or "p images" in Script python
    #------------------------------------------------------------------------------- 
    img_ext = ["jpg", "jpeg", "JPG", "gif", "png", "PNG", "tif", "TIF"]
    file_name = att_data["Filename"].tolist()
    file_ext = att_data["Ext"].tolist()
    filepath = att_data["Path"].tolist()
    y = att_data["Y"].tolist()
    dest_path = "C:\\Users\\I.SERRA\\Desktop\\Script python\\pr images"
    count = 0
    for i in range(len(file_name)):
        if (file_ext[i] in img_ext):
            count+=1
            print("Analizando: "+file_name[i])
            path = filepath[i]
            g = path.split("\\")
            group = g[len(g)-1]
            os.chdir(path)
            file = file_name[i]
            text_rot = [""]*4
            try:
                text_rot[0] = img2txt(file)
                text_rot[1] = img2txt_90(file)
                text_rot[2] = img2txt_180(file)
                text_rot[3] = img2txt_270(file)
            except:
                pass
            for j in range(len(text_rot)):
                #Make the directory and 4 subfolders named 0,1,2,3. One for each rotation
                pathnn = dest_path+"\\"+str(y[i])+"\\"+str(j)
                os.chdir(pathnn)
                text = text_rot[j]
                filen = group+"-"+file.split(".")[0]+"-"+str(j)+".txt"
                f = open(filen, "w", encoding = "utf-8")
                f.write(text)
                f.close()
            print("Processed files: "+str(count))
            