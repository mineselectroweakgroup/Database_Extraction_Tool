import os
from collections import OrderedDict as od


thing = od()
perTable = open("ElementList.txt","r")
periodicTable = perTable.readline()
periodicTable = periodicTable.split(",")
periodicTable[-1] = periodicTable[-1][:-1]


for item in periodicTable:
    index = periodicTable.index(item)
    for i in range(1,300):
        sorting = str(item)+str(i)
        thing[sorting] = [index,i,-1]

for item in periodicTable:
    index = periodicTable.index(item)
    for i in range(1,300):
        sorting = str(item)+str(i)
        filenameopen = str(i)+str(item)+"_Fil.dat"
        if os.path.isfile("Output/gnuPlot/"+filenameopen):
            with open("Output/gnuPlot/"+filenameopen) as datafile:
                first_line = datafile.readline().split(';')
                thing[sorting] = [index,i,float(first_line[1])]


