

def addMass(elementName,lowerBound,higherBound,wantedSpins):
    massfile = open("mass16.txt","r+")
    data = massfile.readlines()
    splitdatafilelines = []

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

                            filenameopen = (str(i)+str(element)+wantedSpins+"_Fil.dat").replace('/','_')

                            datafile = open("Output/gnuPlot/"+filenameopen,'r+')

                            datafilelines = datafile.readlines()
                            datafile.seek(0)
                            datafile.truncate()

                            for line in datafilelines:
                                splitline = line.split(',')
                                if splitline[1] != "--":
                                    replaceline = str((float(splitline[1])-float(data[k][52:62])*int(massA))/1000)
                                    datafile.write(line.replace(splitline[1],replaceline))
                k=k+1

