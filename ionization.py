#This file adds the ionization energies for a given temperature.

import uncertainty as unc

def addIonization(elementName, lowerBound, higherBound, wantedSpins, temperature, addMass):
    ionizationFile = open("ionizationEnergy.txt","r")
    energyList = ionizationFile.readlines()
    kelvinToElectronVolts = 8.651738*10**(-5)
    mElectron = 510998.9461
    E=temperature*kelvinToElectronVolts

    energy ={}
    masschange = {}
    uncertainty = {}
    count = {}

    energyList = energyList[2:]
    energyList = energyList[:-1]

    elementName = removeElements(elementName)

    for line in energyList:
        elementTitle = line[10:12].replace(" ","").upper()
        masschange[elementTitle] = 0
        uncertainty[elementTitle]= 0
        count[elementTitle] = 0

    for line in energyList:
        element = line[10:12].replace(" ","")
        element = element.upper()
        energy[element] = line[148:186].replace(" ","")
        if len(energy[element]) >= 2:
            if energy[element][-2] == ')':
                energy[element] = energy[element][1:]
                energy[element] = energy[element][:-1]
                energy[element] = energy[element].split("(")
                s = energy[element][0].find(".")
                decimals = energy[element][0][s+1:]
                energy[element][1] = energy[element][1].replace(")","").replace("(","")
                energy[element][0] = float(energy[element][0])
                energy[element][1] = float(energy[element][1])
            elif energy[element][0] == '(' or energy[element][0] == '[':
                energy[element] = energy[element][1:]
                energy[element] = energy[element][:-1]
                energy[element] = energy[element].split("(")
                energy[element] = [energy[element][0],0.00]
                s = energy[element][0].find(".")
                decimals = energy[element][0][s+1:]
                energy[element][0] = float(energy[element][0])
            else:
                if energy[element][-1] == ")":
                    energy[element] = energy[element].split("(")
                    s = energy[element][0].find(".")
                    decimals = energy[element][0][s+1:]
                    energy[element][1] = energy[element][1].replace(")","").replace("(","")
                    energy[element][0] = float(energy[element][0])
                    energy[element][1] = float(energy[element][1])
                else:
                    energy[element] = energy[element].split("(")
                    energy[element] = [energy[element][0],0.00]
                    s = energy[element][0].find(".")
                    decimals = energy[element][0][s+1:]
                    energy[element][0] = float(energy[element][0])
            if s == -1:
                decimals = 0
            else:
                decimals = len(decimals)
            energy[element][1] = energy[element][1] * 10**(-decimals)
            if E >= energy[element][0]:
                masschange[element] = masschange[element] + energy[element][0]
                uncertainty[element] = unc.adduncert(uncertainty[element],energy[element][1])
                count[element] = count[element] + 1
        uncertainty[element] = uncertainty[element]/1000



    for title in elementName:
        title = title.upper()
        for i in range(lowerBound,higherBound+1):
            filenameopen = (str(i)+str(title)+wantedSpins+"_Fil.dat").replace("/","_")

            datafile = open("Output/gnuPlot/"+filenameopen,'r+')

            datafilelines = datafile.readlines()
            datafile.seek(0)
            datafile.truncate()

            for line in datafilelines:
                splitline = line.split(';')
                splitline[1] = str(float(splitline[1]) + masschange[title]/10**3)
                splitline[3] = str(unc.adduncert(float(splitline[3]),uncertainty[title]))
                splitline.append(str(count[title])+'+')
                unsplitline = splitline[0] + ';' + splitline[1] + ';' + splitline[2] + ';' + splitline[3] + ';' + splitline[4] + '\n'
                datafile.write(unsplitline)

def removeElements(elementName):
    try:
        elementName.remove("XX")
    except:
        pass
    try:
        elementName.remove("RF")
    except:
        pass
    try:
        elementName.remove("DB")
    except:
        pass
    try:
        elementName.remove("SG")
    except:
        pass
    try:
        elementName.remove("BH")
    except:
        pass
    try:
        elementName.remove("HS")
    except:
        pass
    try:
        elementName.remove("MT")
    except:
        pass
    try:
        elementName.remove("DS")
    except:
        pass
    try:
        elementName.remove("RG")
    except:
        pass
    try:
        elementName.remove("CN")
    except:
        pass
    try:
        elementName.remove("ED")
    except:
        pass
    try:
        elementName.remove("FL")
    except:
        pass
    try:
        elementName.remove("EF")
    except:
        pass
    try:
        elementName.remove("LV")
    except:
        pass
    try:
        elementName.remove("EH")
    except:
        pass
    try:
        elementName.remove("EI")
    except:
        pass
    return(elementName)
