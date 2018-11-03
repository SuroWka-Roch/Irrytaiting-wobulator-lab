#!/usr/bin/env python3.5
import glob
import re
list= glob.glob('*.dat')
intro ="""set terminal jpeg enhanced size 900,600
set decimalsign locale;
set decimalsign ','
set grid
set ylabel 'napięcie [mV]'
set xlabel 'częstotliwość [Hz]'
set logscale x\n"""
nazwy = [[x,x.strip().split('.')[0]] for x in list]
for i in range(len(nazwy)):
  m= re.search(r"\d0{0,2}[km]$", nazwy[i][1])
  if m:
    nazwy[i].append(nazwy[i][1].replace(m.group(0),''))
    nazwy[i].append(m.group(0))
for i in range(len(nazwy)):
  try:
    m = re.search(r"[^\^]\d", nazwy[i][2])
  except IndexError:
    continue
  if m:
    nazwy[i][2]= nazwy[i][2].replace(m.group(0)[1:],'^{} '.format(m.group(0)[1:]))
    print(nazwy[i][2])
  m = re.search(r"[^\^]\d$", nazwy[i][2])
  if m:
    nazwy[i][2] = nazwy[i][2].replace(m.group(0)[1:], '^{} '.format(m.group(0)[1:]))
    print(nazwy[i][2])
  nazwy[i][2] = nazwy[i][2].replace('rr', 'r r').strip()
for i in range(len(nazwy)):
  try:
    nazwy[i][3]=nazwy[i][3].replace('m','M')
  except IndexError:
    continue
print(nazwy)
dict ={}
for i in nazwy:
  try:
    dict[i[2]]=dict.setdefault(i[2],'plot ') + "'{}'  pt 7 ps 1 title '{} Hz',".format(i[0], i[3])
  except IndexError:
    continue
print(dict)
with open('gnuplot.skrypt','w') as file:
  file.write(intro)
  for key,value in dict.items():
    file.write("set output './python-files/{}.jpeg\n".format(key))
    file.write(value + "\n")
