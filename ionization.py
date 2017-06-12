
ionizationFile = open("ionizationEnergy.txt","r")
energyList = ionizationFile.readlines()
kelvinToElectronVolts = 8.651738*10**(-5)
mElectron = 510998.9461
T=522203.6
E=T*kelvinToElectronVolts
print(E)


energyofHydrogen = energyList[2][148:186]

energy ={}
masschange = {}

energyList = energyList[2:]
energyList = energyList[:-1]

for line in energyList:
    elementName = line[10:12].replace(" ","")
    masschange[elementName] = 0

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
            masschange[element] = masschange[element] + energy[element][0] - mElectron


print(energy['He'][0])
print(energy['He'][1])
print(masschange['He'])
