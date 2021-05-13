# -*- coding: utf-8 -*-
def getfile(filename):
    #Hardcode make xml file
    head="""<speak version="1.0" xmlns="https://www.w3.org/2001/10/synthesis" xml:lang="vi-VN">
  <voice name="vi-VN-NamMinhNeural">
  <prosody rate="medium">
    """
    tail="""</prosody></voice>
</speak>"""


#Get line
    f=open(filename,'r',encoding='utf-8')
    i=0
    listFile=[]
    if f.mode=='r':
        line_count = 0
        for line in f:
            if line != "\n":
                line_count += 1
        print(line_count)
        f.seek(0)
        for i in range(line_count-1):
            content=f.readline()
            outText=open(str(i)+'.xml',"w",encoding='utf-8') #output file
            outText.write(head+content+tail)
            #print(content+"+++++++++++++++++++++++++++++++++")
            outText.close()
            listFile.extend([str(i)+'.xml'])
    return listFile
    f.close()
#getfile('te2.txt')
