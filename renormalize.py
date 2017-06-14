def renormalize(elementName,lowerBound,higherBound,wantedSpins):
    minimum = 9999999999999999999
    for element in elementName:
        for i in range(lowerBound,higherBound+1):
            filenameopen = (str(i)+str(element)+wantedSpins+"_Fil.dat").replace("/","_")

            datafile = open("Output/gnuPlot/"+filenameopen,'r+')

            datafilelines = datafile.readlines()

            for line in datafilelines:
                splitline = line.split(';')
                if str(splitline[2]) == "--" or str(splitline[2]) == "--*":
                    break
                if float(splitline[1]) < float(minimum):
                    minimum = splitline[1]

    for element in elementName:
        for i in range(lowerBound,higherBound+1):
            filenameopen = (str(i)+str(element)+wantedSpins+"_Fil.dat").replace("/","_")

            datafile = open("Output/gnuPlot/"+filenameopen,'r+')

            datafilelines = datafile.readlines()
            datafile.seek(0)
            datafile.truncate()

            for line in datafilelines:
                splitline = line.split(';')
                splitline[1] = str(float(splitline[1])-float(minimum))
                unsplitline = splitline[0] + ';' + splitline[1] + ';' + splitline[2] + ';' + splitline[3]
                datafile.write(unsplitline)

