#!/usr/bin/env python3.5
from glob import glob
from  math import sqrt
from functools import reduce
def calkuj(*doublelist):
  sum=0
  temp=None
  for value in doublelist[0]:
    if temp is None:
      temp=value
      continue
    else:
      a=(temp[1]+value[1])/2
      a=a*(value[0]-temp[0])
      sum+=a
      temp = value
  zwrot= sum#/(doublelist[0][-1][0]-doublelist[0][0][0])
  return sqrt(zwrot)
list = glob('*.dat')
listawynikow =[]
templist=[]
for name in list:
  with open(name) as file:
    listofdata= file.readlines()
    modifiedlist=[[float(record.split('\t')[0].replace(',','.')),float(record.split('\t')[1].strip().replace(',','.'))**2] for record in listofdata]
    if len(modifiedlist)==0:
      print("error błąd pliku ",name)
      templist.append(("error błąd pliku plik pusty",name))
      continue
    listawynikow.append( (calkuj(modifiedlist),name))
print(listawynikow)
listawynikow.sort(key=lambda x:x[ 0],reverse= True)
with open("wyniki calkowania.txt","w") as file:
  for item in listawynikow:
      file.write("{} {}\r\n".format(item[0],item[1]))
  for item in templist:
      file.write("{} {}\r\n".format(item[0],item[1]))