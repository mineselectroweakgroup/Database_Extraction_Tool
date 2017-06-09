#This is a single function which sorts through the mass data file and includes the atomic mass and uncertainty
#with a unit conversion factor into the data set.

def addMass(elementName,lowerBound,higherBound,wantedSpins):
    massfile = open("mass16.txt","r+")
    data = massfile.readlines()
    splitdatafilelines = []
    #Thesse next two lines take C12 as absolute and use that to calculate the conversion factor between amu and keV
    BEC12 = 92161.753
    conversion = BEC12/(6*float(data[39][96:112].replace(" ",""))+6*float(data[40][96:112].replace(" ",""))-12000000)


    for element in elementName:
        for i in range(lowerBound,higherBound+1):
            k=0
            while k <= len(data)-1:
                if len(data[k]) != 1:

                    masselement = str(data[k][20])+str(data[k][21])
                    masselement = masselement.replace(" ","")

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
                                atomicMass = float(data[k][96:112].replace(" ","").replace("#","."))*conversion/10**6
                                aMassError = float(data[k][113:123].replace(" ","").replace("#","."))*(conversion/10**6)
                                splitline[1] = str(float(splitline[1])/10**6 + atomicMass)
                                splitline[3] = str(float(splitline[3])/10**6 + aMassError)
                                unsplitline = splitline[0] + ';' + splitline[1] + ';' + splitline[2]+';'+splitline[3]+'\n'
                                datafile.write(unsplitline)
                k=k+1








