# -*- coding: utf-8 -*-
#Author: l1ghtg3m
#How to use: input subkey in MakeAAudio.py(line 11) and rename text file in line 15
from mergeFile import mergefile
import os
from getline import getfile
from MakesAAudio import MakeAAudio
from clearFile import clear
import time
from pathlib import Path


#Make split file

listFilename = getfile("te2.txt") #rename in here!!
listFileAudio =[]
print(listFilename)
listForDel=listFilename.copy()
#del listFilename[len(listFilename)-1]

#Create check list
CheckList = ['0']*len(listFilename);
i=0
#make a audio file output


while listFilename != CheckList:
    for name in listFilename:
        if name != '0':
            print("Processing "+ name)                   #get audio
            stream = MakeAAudio(name)
            stream.save_to_wav_file(name+".wav")
            listFileAudio.extend([name+'.wav'])
            print("Exported: "+ name +".wav"  )
            time.sleep(0.5)
    for rename in listFilename:
        print("Checking "+rename+".wav")                 #check file successed
        if Path(rename+".wav").stat().st_size != 0:
            listFilename[listFilename.index(rename)]=str(0)
            print("deleted "+ rename)
    i+=1
    if i==10 or i==19 or i==23 :
        time.sleep(120)
    elif i== 53:
        time.sleep(239)
    elif i== 59:
        break

    print(listFilename)


#merge all file 
print(listFileAudio)
mergefile(listFileAudio)

#Clear all file
clear(listForDel)
clear(listFileAudio)
