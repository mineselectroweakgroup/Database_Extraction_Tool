#This is a single function which sorts through the mass data file and includes the atomic mass and uncertainty
#with a unit conversion factor into the data set.

import uncertainty as unc

def addMass(elementName,lowerBound,higherBound,wantedSpins):
    massfile = open("mass16.txt","r+")
    data = massfile.readlines()
    splitdatafilelines = []
    #These next two values take the conversion factor from micro amu to keV, along with its uncertainty
    conversion = 0.93149409541
    dconversion = 0.00000000057


    for element in elementName:
        element = element.upper()
        for i in range(lowerBound,higherBound+1):
            k=0
            while k <= len(data)-1:
                if len(data[k]) != 1:

                    masselement = str(data[k][20])+str(data[k][21])
                    masselement = masselement.replace(" ","")
                    masselement = masselement.upper()

                    if element == masselement:

                        massA = str(data[k][16])+str(data[k][17])+str(data[k][18])
                        massA = massA.lstrip()

                        if str(i) == massA:
                            A = int(massA)

                            filenameopen = (str(i)+str(element)+wantedSpins+"_Fil.dat").replace('/','_')

                            datafile = open("Output/gnuPlot/"+filenameopen,'r+')


                            datafilelines = datafile.readlines()
                            datafile.seek(0)
                            datafile.truncate()

                            for line in datafilelines:
                                splitline = line.split(';')
                                N = int(data[k][6:9].replace(" ",""))
                                Z = int(data[k][11:14].replace(" ",""))
                                if data[k][106]=='#':
                                    splitline[2] = splitline[2] + '*'
                                atomicMass = float(data[k][96:112].replace(" ","").replace("#","."))*conversion
                                aMassError = unc.multuncert(float(data[k][96:112].replace(" ","").replace("#",".")),conversion,float(data[k][113:123].replace(" ","").replace("#",".")),dconversion)
                                splitline[1] = str(float(splitline[1]) + atomicMass)
                                splitline[3] = str(unc.adduncert(float(splitline[3]),aMassError))
                                unsplitline = splitline[0] + ';' + splitline[1] + ';' + splitline[2]+';'+splitline[3]+'\n'
                                datafile.write(unsplitline)
                k=k+1








