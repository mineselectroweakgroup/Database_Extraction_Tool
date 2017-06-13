## Right now, this is imported by test.py look for all spin states of 65Zn up to 5000keV

from decimal import *

def isNumber(inputString):
    return not any(not (char.isdigit() or char == '.') for char in inputString)


class data:##This is the main data class.
    def __init__(self,ENSDF,ISOvar,option = 'EoL',energyLimit = 999999999, maxSpin = 9):
        ###maybe get rid of option, find out how energy limit and max spin are used

        ##Initialize Parameters
        #filtDataSet=[]
            ###may not need filt data set
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
                print(ENSDF,':',linecount)

                ## finding the energy
                energy = line[9:19].strip()

                ## check if valid energy data (i.e. no letter at beginning or end)
                if (energy[0].isalpha() or energy[-1].isalpha()):
                    continue
                    
                if 'E' in energy: ## This will convert scientific to decimal notation if needed
                    significand = float(energy[:energy.find('E')])
                    power = 10** float(energy[energy.find('E')+1:])
                    energy = str(significand * power)
                ## discard points where energy contains letters FIXME: this should not be necessary
                #if not isNumber(energy):                    
                    #continue


                ## Finding the uncertainty
                uncert = line[19:21].strip()
                #print(uncert)
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
                            #print(linecount,line,numberino,numberino[-i:])
                        if (i < len(uncert)):
                            #print(linecount,energy,numberino)
                            digit = int(numberino[-1-i])+int(uncert[-1-i])
                        else:
                            digit = int(numberino[-1-i])
                        topLimit = digit * (10**i) + topLimit
                    topLimit = str(topLimit)[:-decIndex]+'.'+str(topLimit)[-decIndex:]
                    uncert = str(Decimal(topLimit)-Decimal(energy))




                jpi = line[21:39].strip() ## ALL spin and pairity states
                #jpi = '0+' #sets all spins to be 0+ for plot testing

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



    def spinMatchFinder(self,matchVal,checkVal):
        ## matchVal is the desired spin, checkVal is the spin to be checked for matchVal
        tempList = checkVal.split(',')
        ## Look for parities that need to be distributed.
        if any((')+' in value or ')-' in value) for value in tempList):
            addPlus = False
            addMinus = False
            for j in range(len(tempList)): 
                if ')+' in tempList[j]:
                    addPlus = True
                    print('addPlus is True')
                    tempList[j] = tempList[j].replace('+','') 
                if ')-' in tempList[j]:  
                    addMinus = True
                    tempList[j] = tempList[j].replace('-','')

            if addMinus and addPlus: #FIXME check ALL isotopes in ALL datafiles
                print(self.data[i])
            ## Distribute the parities to each term
            for j in range(len(tempList)):
                if addPlus:
                    tempList[j] = tempList[j] + '+'
                if addMinus:
                    tempList[j] = tempList[j] + '-'

        ## Remove () so that spins can be identified with ==
        for j in range(len(tempList)):
            tempList[j] = tempList[j].replace('(','')
            tempList[j] = tempList[j].replace(')','')
        print(tempList)


        if (matchVal in checkVal.split(',')): #FIXME this will identify say 1/2- in 21/2-, probably
            return True
        else:
            ## Spin not found
            return False



    def filterData(self,userInput,UI=False):
        ## no spin input
        if (userInput == ''):
            #print(self.data)
            if (not self.data):
                if(UI):
                    ## Prints a statement telling user than no file was found
                    print("Warning:No data filtered/selected for "+ self.name +".")
                self.data=[[0.0,"--",0.0]]##Enters a dummy entry to file with something.
                
        #if(self.op == 'EoL'):
        ## Filter by spin states
        else:
            newData=[] ## storage for new data
            for wantedString in userInput.split(","):##adds all the strings that are included in the userInput.
                for i in range(0,len(self.data)): 
                    #print(self.data[i][1])
                    if(self.spinMatchFinder(wantedString, self.data[i][1])):
                        newData.append(self.data[i])
            if(newData):
                self.data=newData##changes data to the new data.
            else:
                if(UI):
                    print("Warning:No data filtered/selected for "+ self.name +".")#Prints a statement telling user than no file was found
                self.data=[[0.0,"--",0.0]]##Enters a dummy entry to file with something.

