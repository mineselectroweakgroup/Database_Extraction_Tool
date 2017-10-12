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

                if dataObj.data[i].isotope == isoName:
                    A = int(massA)
                    N = int(massdata[k][6:9].replace(" ",""))
                    Z = int(massdata[k][11:14].replace(" ",""))
                    if massdata[k][106]=='#':
                        dataObj.data[i].jpi = dataObj.data[i].jpi + '*'
                    atomicMass = float(massdata[k][96:112].replace(" ","").replace("#","."))*conversion
                    
                    aMassError = unc.multuncert(float(massdata[k][96:112].replace(" ","").replace("#",".")),conversion,float(massdata[k][113:123].replace(" ","").replace("#",".")),dconversion)
                    dataObj.data[i].energy = str(float(dataObj.data[i].energy) + atomicMass)
                    dataObj.data[i].energy_uncert = str(unc.adduncert(float(dataObj.data[i].energy_uncert),aMassError))
            k=k+1
