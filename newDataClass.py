from decimal import *
from spinSearch import spinMatchFinder

class data:##This is the main data class.
    def __init__(self,ENSDF,ISOvar,option = 'EoL',energyLimit = 999999999, maxSpin = 9):
        ###maybe get rid of option, find out how energy limit and max spin are used

        ##Initialize Parameters
        self.data = []
        self.name = ISOvar
        self.op = option


        ## nucID is what is compared to the first 6 characters of the line to find the correct data
        nucID=self.name.upper()+" "
        ## This while loop makes sure that nucID has the correct leading whitespace to match the data file
        charIndex=0
        while(charIndex<3):
            if nucID[charIndex].isalpha():
                nucID=' '+nucID
            charIndex+=1
        ## if the element symbol is one letter, an additional space must be appended so len(nucID)==6
        if(len(nucID)<6):
            nucID=nucID+' '
            

        ##open the appropriate ensdf file
        self.f = open("Data/"+str(ENSDF),'rU')


        linecount = 0 ## printing linecount can help locate problem-causing lines in the ensdf file
        desiredData = False
        for line in self.f:
            linecount+=1
            ## The line parsing algorithm is derived from the labeling system of the ensdf files
            ## See the endsf manual, pg. 22, for more information about how the lines of data are organized

            ## the for loop must exit when the ensdf switches from evaluated data to experimental results
            ## this is indicated by an empty line in the ensdf file, which is detected her
            if (desiredData and line[0:6].strip() == ''):
                break     

             ## Identifies which lines in the data file have relevant data
            if (line[6:8]==' L' and line[0:6]==nucID):

                ## set desiredData bool so the program wil exit after reading adopted data
                desiredData = True

                ## finding the energy
                energy = line[9:19].strip()

                ## check if valid energy data (i.e. no letter at beginning or end)
                if (energy[0].isalpha() or energy[-1].isalpha()):
                    continue

                ## This will handle states with deduced energies enclosed in () 
                deducedEnergy = False
                if '(' in energy:
                    deducedEnergy = True
                    energy = energy.replace('(','')
                    energy = energy.replace(')','')
    
                if 'E' in energy: ## This will convert scientific to decimal notation if needed
                    significand = float(energy[:energy.find('E')])
                    power = 10** float(energy[energy.find('E')+1:])
                    energy = str(significand * power)

                
                ## Finding the uncertainty
                uncert = line[19:21].strip()
                ## Set unsert to 0 if no uncertainty is given.
                if (uncert == ''):
                    uncert = '0'
                ## Set uncert to 0 if not numeric 
                elif (not uncert.isnumeric()):
                    uncert = '0'

                elif ('.' in energy): ## Convert uncertainty to proper magnitude
                    numberino = energy
                    topLimit = 0
                    
                    for i in range(len(numberino)-1):
                        
                        if (numberino[-1-i] == '.'):
                            decIndex = i
                            if (decIndex == 0):
                                ## If the '.' is the last digit in the energy, numberino[-i:] will 
                                ## return the entire string, which is no bueno 
                                numberino = numberino[:-1-i]
                            else:
                                numberino = numberino[:-1-i] + numberino[-i:]
                        if (i < len(uncert)):
                            digit = int(numberino[-1-i])+int(uncert[-1-i])
                        else:
                            digit = int(numberino[-1-i])
                        topLimit = digit * (10**i) + topLimit
                    topLimit = str(topLimit)[:-decIndex]+'.'+str(topLimit)[-decIndex:]
                    uncert = str(Decimal(topLimit)-Decimal(energy))



                ## Finding ALL spin and pairity states (to be filtered later)
                jpi = line[21:39].strip() 
                ## indicating deduced energy
                if deducedEnergy:
                    jpi = jpi + '**'

                ## Finding stability info FIXME: this data is currently not used
                hlife = line[39:49].strip()
                # if stable, set to 10**9 year

                if(float(energy)<=energyLimit):
                    #include the data
                    self.data.append([energy,jpi,uncert])
                    #print(str(linecount)+' :'+str(self.data[-1]))
                else:
                    break

    ## extraTitleText would be desired spin states, for example
    def export(self,fExtOption = '.dat',extraTitleText = ''): 
#            if(fExtOption==".dat"or fExtOption=="_Fil.dat"):##To make data files for use in gnuplot and plt file.
            fileName=str(self.name)+extraTitleText+fExtOption##creates filename
            fileName="Output/" + "gnuPlot/"+fileName.replace('/','_')
            datFile = open(fileName,'wb')##Creates a file with a valid file name.
            for i in range(len(self.data)):
                datFile.write(str.encode(str(self.name)+';'+str(self.data[i][0])+';'+str(self.data[i][1])+';'+str(self.data[i][2])+'\n'))

    '''
    def spinMatchFinder(self,matchVal,checkVal):
        ## matchVal is the desired spin, checkVal is the spin to be checked for matchVal      
        tempList = checkVal.replace('**','').replace('&',',') 
        tempList = tempList.split(',')
              
        ## Look for parities that need to be distributed.
        if any((')+' in value or ')-' in value) for value in tempList):
            addPlus = False
            addMinus = False
            for j in range(len(tempList)): 
                if ')+' in tempList[j]:
                    addPlus = True
                    tempList[j] = tempList[j].replace('+','') 
                if ')-' in tempList[j]:  
                    addMinus = True
                    tempList[j] = tempList[j].replace('-','')

            ## Distribute the parities to each term
            for j in range(len(tempList)):
                if addPlus:
                    tempList[j] = tempList[j] + '+'
                if addMinus:
                    tempList[j] = tempList[j] + '-'

        ## Remove () and whitespace so that spins can be identified with ==
        for j in range(len(tempList)):
            tempList[j] = tempList[j].replace('(','')
            tempList[j] = tempList[j].replace(')','')
            tempList[j] = tempList[j].strip()
    
        ## Handing of ranges of spins (eg. JPI to J'PI', see ensdf manual pg. 46 for more info)
        if any(('TO' in value or ':' in value) for value in tempList):
            ## if a range is given, len(tempList) = 1 ALWAYS
            tempList[0] = tempList[0].replace('TO',':')
            [lhs,rhs] = tempList[0].split(':')
            
            ## JPI TO J'PI'
            if (('+' in lhs) or ('-' in lhs)) and (('+' in rhs) or ('-' in rhs)): 
                ## Note that lowJ and highJ are Fraction objects
                lowJ = getJ(lhs)
                lowPI = getPI(lhs)
                highJ = getJ(rhs)
                highPI = getPI(rhs) 
                ## jRange is a list of strings
                jRange = getJrange(lowJ,highJ)
                
                jRange[0] = jRange[0]+lowPI
                jRange[-1] = jRange[-1]+highPI
                tempList = jRange

            ## J TO J'PI
            elif ('+' in rhs) or ('-' in rhs):
                lowJ = getJ(lhs)
                highJ = getJ(rhs)
                highPI = getPI(rhs) 
                jRange = getJrange(lowJ,highJ)
                
                for jIndex in range(len(jRange)):
                    jRange[jIndex] = jRange[jIndex]+highPI
                tempList = jRange

            ## JPI TO J'
            elif ('+' in lhs) or ('-' in lhs):
                lowJ = getJ(lhs)
                lowPI = getPI(lhs)
                highJ = getJ(rhs) 
                jRange = getJrange(lowJ,highJ)
                
                jRange[0] = jRange[0]+lowPI
                tempList = jRange

            else: ## J TO J'
                lowJ = getJ(lhs)
                highJ = getJ(rhs) 
                jRange = getJrange(lowJ,highJ)
                tempList = jRange   

        ## assign + and - to states with no indicated pairity
        if (not tempList == ['']) and any(('+' not in value and '-' not in value) for value in tempList):
            j=0
            while (j < len(tempList)):
                if ('+' not in tempList[j] and '-' not in tempList[j]):
                    tempList.insert(j,tempList[j]+'-')
                    tempList[j+1] = tempList[j+1]+'+'
                j+=1

        if (matchVal in tempList):
            return True       
        else:
            ## Spin not found
            return False
    '''

    def filterData(self,userInput,UI=False):
        ## no spin input
        if (userInput == ''):
            #print(self.data)
            if (not self.data):
                if(UI):
                    pass
                    ## Prints a statement telling user than no file was found
                    #print("Warning:No data filtered/selected for "+ self.name +".")
                self.data=[[0.0,"--",0.0]]##Enters a dummy entry to file with something.
                
        #if(self.op == 'EoL'):
        ## Filter by spin states
        else:
            newData=[] ## storage for new data
            for wantedString in userInput.split(","):##adds all the strings that are included in the userInput.
                for i in range(0,len(self.data)): 
                    #print(self.name,self.data[i])
                    ## The spinMatchFinder will identify if the state is the desired spin
                    if(spinMatchFinder(wantedString, self.data[i][1])):
                        newData.append(self.data[i])
            if(newData):
                self.data=newData##changes data to the new data.
            else:
                if(UI):
                    ## Prints a statement telling user than no file was found
                    pass
                    #print("Warning:No data filtered/selected for "+ self.name +".")#Prints a statement telling user than no file was found
                self.data=[[0.0,"--",0.0]]##Enters a dummy entry to file with something.

