import os
import csv
import re
from typing import Text
from bs4 import BeautifulSoup
rows=[]
with open('LDAGibbs 5 TopicProbabilities.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    # extracting field names through first row
    fields = next(csv_reader)
  
    # extracting each data row one by one
    for row in csv_reader:
        rows.append(row)
print(rows)
def Find_max(Lista,j):
    ma1=0.0
    A=Lista
    ix1=0
    im=0
    for i in range(len(A)):
        if (float(A[i][j]) > float(ma1)):
            ma1=float(A[i][j])
            ix1=int(A[i][0])
            im=i
    
    
    A.pop(im)
    
    return A,ix1
Lidx1=[]
Lidx2=[]
Lidx3=[]
Lidx4=[]
Lidx5=[]
ListaNueva1,idx=Find_max(rows,1)
Lidx1.append(idx)
ListaNueva2,idx2=Find_max(rows,2)
Lidx2.append(idx2)
ListaNueva3,idx3=Find_max(rows,3)
Lidx3.append(idx3)
ListaNueva4,idx4=Find_max(rows,4)
Lidx4.append(idx4)
ListaNueva5,idx5=Find_max(rows,5)
Lidx5.append(idx5)

for i in range(4):
    ListaNueva1,idx=Find_max(ListaNueva1,1)
    Lidx1.append(idx)
    ListaNueva2,idx=Find_max(ListaNueva2,2)
    Lidx2.append(idx)
    ListaNueva3,idx=Find_max(ListaNueva3,3)
    Lidx3.append(idx)
    ListaNueva4,idx=Find_max(ListaNueva4,4)
    Lidx4.append(idx)
    ListaNueva5,idx=Find_max(ListaNueva5,5)
    Lidx5.append(idx)

ListaTendencias=[Lidx1,Lidx2,Lidx3,Lidx4,Lidx5]
print(ListaTendencias)
Terminos=[]
with open('LDAGibbs 5 DocsToTopics.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    # extracting field names through first row
    fields = next(csv_reader)
    m=0
    # extracting each data row one by one
    for row in (csv_reader):
        m+=1
        for i in ListaTendencias:
            if(m==i):
                t=row[0]
                titulo=t[:-3]
                Terminos.append(titulo)

def Find(string):
  
    # findall() has been used 
    # with valid conditions for urls in string
    regex = r"(?i)\b((?:https?://|t.co\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)      
    return [x[0] for x in url]
Links=[]
for j in ListaTendencias:
    for i in j:
      
        csv_reader=open("txts/tweet"+str(i)+".txt","r") 
        #fields = next(csv_reader)
        for row in (csv_reader):
          
            links=Find(row)
            if(links != [] and (links not in Links)):
           
            
                Links.append(links)
print((Links))
