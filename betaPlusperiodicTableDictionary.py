import os

massfile = open("mass16.txt","r+")
data=massfile.readlines()

writetofile = '"Beta-Plus Decay Q Values"\n'
for i in range(39,len(data)):
    N = str(data[i][6:9])
    Z = str(data[i][11:14])
    stability = data[i-1][76:86].replace(" ","").replace("#","")
    if stability == '*' or stability == '(keV)':
        stability = 0
    stability = -float(stability)-1022
    if stability <= 0:
        stabilityvalue = 0
    elif stability <= 100:
        stabilityvalue = 1
    elif stability <= 500:
        stabilityvalue = 2
    elif stability <= 1000:
        stabilityvalue = 3
    elif stability <= 3000:
        stabilityvalue = 4
    else:
        stabilityvalue = 5
    stabilityvalue = str(stabilityvalue)
    writetofile = writetofile + N + ',' + Z + ',' + stabilityvalue + '\n'



WriteFile = open("IsotopeList.txt","wb")
WriteFile.write(str.encode(writetofile))
