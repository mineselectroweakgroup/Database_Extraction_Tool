## This is a test file for importing the newDataClass.py file

import newDataClass as dc

i=65 ## Testing Zn 65 up to 5000 keV
itervar = '65Zn'
energyLim = 90000


indata = dc.data('ensdf.'+str(i).zfill(3),itervar,'EoL',energyLim)
indata.export("_Fil.dat")

#for j in indata.data:
    #print (j)
