


def addIonization(elementName, lowerBound, higherBound, wantedSpins, temperature, addMass):
    ionizationFile = open("ionizationEnergy.txt","r")
    energyList = ionizationFile.readlines()
    kelvinToElectronVolts = 8.651738*10**(-5)
    mElectron = 510998.9461
    E=temperature*kelvinToElectronVolts

    energy ={}
    masschange = {}

    energyList = energyList[2:]
    energyList = energyList[:-1]

    for line in energyList:
        elementTitle = line[10:12].replace(" ","")
        masschange[elementTitle] = 0

    for line in energyList:
        element = line[10:12].replace(" ","")
        energy[element] = line[148:186].replace(" ","")
        if masschange[element] == "":
            masschange[element] = float(0)
        if len(energy[element]) >= 2:
            if energy[element][-2] == ')':
                energy[element] = energy[element][1:]
                energy[element] = energy[element][:-1]
                energy[element] = energy[element].split("(")
                energy[element][1] = energy[element][1].replace(")","")
                energy[element][0] = float(energy[element][0])
            else:
                if energy[element][0] == "(" or energy[element][0] == "[":
                    energy[element] = energy[element][1:]
                    energy[element] = energy[element][:-1]
                energy[element] = energy[element].split("(")
                energy[element][0] = float(energy[element][0])
            if E >= energy[element][0]:
                masschange[element] = masschange[element] + energy[element][0]

    for title in elementName:
        print(masschange[title])
        for i in range(lowerBound,higherBound+1):
            filenameopen = (str(i)+str(title)+wantedSpins+"_Fil.dat").replace("/","_")

            datafile = open("Output/gnuPlot/"+filenameopen,'r+')

            datafilelines = datafile.readlines()
            datafile.seek(0)
            datafile.truncate()

            for line in datafilelines:
                splitline = line.split(';')
                splitline[1] = str(float(splitline[1]) + masschange[title]/10**3)
                unsplitline = splitline[0] + ';' + splitline[1] + ';' + splitline[2] + ';' + splitline[3]
                datafile.write(unsplitline)


