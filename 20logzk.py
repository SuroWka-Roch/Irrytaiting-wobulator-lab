#!/usr/bin/env python3.5
wzmfile= open('wzm.dat')
listwzm=[]
for line in wzmfile:
  listwzm.append(line.strip().replace(',','.').split('\t'))
from glob import glob
import math
names=glob('*.dat')
min=0.0
from os import mkdir
try:
  mkdir('gotowepliki')
except:
  pass
for i in names:
  with open(i) as file:
    templist=[]
    for numer,line in enumerate(file):
      templist.append(line.strip().replace(',','.').split('\t'))
      try:
        templist[-1][1]=str(20*math.log(float(templist[-1][1])/float(listwzm[numer][1]),10))
        if float(templist[-1][1])<min:
          min=float(templist[-1][1])
      except ValueError:
        print(templist[-1][1], listwzm[numer][1],i)
        templist.pop()
    with open(r'gotowepliki/' + i,'w') as dest:
      for record in templist:
        dest.write("{}\t{}\n".format(record[0],record[1]).replace('.',','))

print(min)