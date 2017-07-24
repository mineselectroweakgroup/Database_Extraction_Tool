#This file adds the ionization energies for a given temperature.

import uncertainty as unc
import time
nonoElements =['Xx','Rf','Db','Sg','Bh','Hs','Mt','Ds','Rg','Cn','Ed','Fl','Ef','Lv','Eh','Ei']

energy ={}
masschange = {}
uncertainty = {}
count = {}

## Builds dictionary of ionization data
def make_ion_dict(temperature):
    start_t = time.time()
    ionizationFile = open("ionizationEnergy.txt","r")
    energyList = ionizationFile.readlines()
    kelvinToElectronVolts = 8.651738*10**(-5)
    mElectron = 510998.9461
    thermalE=temperature*kelvinToElectronVolts

    energyList = energyList[2:-1]

    for line in energyList:
        elementTitle = line[10:12].replace(" ","").upper()
        masschange[elementTitle] = 0
        uncertainty[elementTitle]= 0
        count[elementTitle] = 0
    
    for line in energyList:
        element = line[10:12].replace(" ","").upper()
        energy[element] = line[148:186].replace(" ","")
        if len(energy[element]) >= 2:
            if energy[element][-2] == ')':
                energy[element] = energy[element][1:-1].split('(')
                s = energy[element][0].find(".")
                decimals = energy[element][0][s+1:]
                energy[element][1] = energy[element][1].replace(")","").replace("(","")
                energy[element][0] = float(energy[element][0])
                energy[element][1] = float(energy[element][1])
            elif energy[element][0] == '(' or energy[element][0] == '[':
                energy[element] = energy[element][1:-1].split('(')
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
            if thermalE >= energy[element][0]:
                masschange[element] = masschange[element] + energy[element][0]
                uncertainty[element] = unc.adduncert(uncertainty[element],energy[element][1])
                count[element] = count[element] + 1
        uncertainty[element] = uncertainty[element]/1000

## Include ionization data
def addIonization(dataObj):
    for i in range(len(dataObj.data)):
        if any(elementName.upper() in dataObj.data[i][0] for elementName in nonoElements):
            ## The new removeElements(elementName)
            pass
        elif dataObj.data[i][0] == 'NULL':
            dataObj.data[i].insert(6,'0+')
        else:
            ## create elementLabel for the dictionaries to use
            elementLabel = ''
            for char in dataObj.data[i][0]:
                if char.isalpha():
                    elementLabel = elementLabel + char
            ## Preform Physics
            dataObj.data[i][1] = str(float(dataObj.data[i][1]) + masschange[elementLabel]/10**3)
            dataObj.data[i][3] = str(unc.adduncert(float(dataObj.data[i][3]),uncertainty[elementLabel]))
            ## Add ionization at index i = 6, even for decay data sets
            dataObj.data[i].insert(6,str(count[elementLabel])+'+')
