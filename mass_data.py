#This is a single function which sorts through the mass data file and includes the atomic mass and uncertainty
#with a unit conversion factor into the data set.

import uncertainty as unc

def addMass(dataObj):
    massfile = open("mass16.txt","r+")
    massdata = massfile.readlines()
    splitdatafilelines = []
    #These next two values take the conversion factor from micro amu to keV, along with its uncertainty
    conversion = 0.93149409541
    dconversion = 0.00000000057

    for i in range(len(dataObj.data)):
        k=0
        while k <= len(massdata)-1:
            if len(massdata[k]) != 1:
    
                #FIXME clean up string parsing 
                masselement = str(massdata[k][20])+str(massdata[k][21])
                masselement = masselement.replace(" ","").upper()
                massA = str(massdata[k][16])+str(massdata[k][17])+str(massdata[k][18])
                massA = massA.lstrip()
                isoName = massA+masselement

                if dataObj.data[i][0] == isoName:
                    A = int(massA)
                    ## splitline is dataObj.data[i]
                    #splitline = line.split(';')
                    N = int(massdata[k][6:9].replace(" ",""))
                    Z = int(massdata[k][11:14].replace(" ",""))
                    if massdata[k][106]=='#':
                        dataObj.data[i][2] = dataObj.data[i][2] + '*'
                    atomicMass = float(massdata[k][96:112].replace(" ","").replace("#","."))*conversion
                    aMassError = unc.multuncert(float(massdata[k][96:112].replace(" ","").replace("#",".")),conversion,float(massdata[k][113:123].replace(" ","").replace("#",".")),dconversion)
                    dataObj.data[i][1] = str(float(dataObj.data[i][1]) + atomicMass)
                    dataObj.data[i][3] = str(unc.adduncert(float(dataObj.data[i][3]),aMassError))
                    #unsplitline = splitline[0] + ';' + splitline[1] + ';' + splitline[2]+';'+splitline[3]+';'+splitline[4]+';'+splitline[5]+';'+splitline[6]+';'+splitline[7]
                    #datafile.write(unsplitline)
            k=k+1
