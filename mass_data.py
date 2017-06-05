

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
                                if data[k][59]=='#':
                                    splitline[2] = splitline[2]+'*'
                                splitline[1] = str((float(splitline[1])-float(data[k][55:63].replace('#','.')))/1000)
                                unsplitline = splitline[0] + ',' + splitline[1] + ',' + splitline[2] + ',' + splitline[3]
                                datafile.write(unsplitline)
                k=k+1

