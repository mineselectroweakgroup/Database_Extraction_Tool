from decimal import *
from functions import spinMatchFinder
from functions import levelExtract
from functions import NUCIDgen
 
    
class data:##This is the main data class.
    def __init__(self,ENSDF,ISOvar,option,energyLimit = 999999999, maxSpin = 9):
        ###maybe get rid of option, find out how energy limit and max spin are used

        ##Initialize Parameters
        self.data = []
        self.name = ISOvar
        self.op = option


        ## nucID is what is compared to the first 6 characters of the line to find the correct data
        nucID=self.name.upper()  
        if self.op == 'two':#FIXME Decay Data setup
            betaVariable = 'B-' #FIXME

            parent = ''
            daughter = ''
            Avalue = ''
            for char in nucID:
                if char.isnumeric():
                    Avalue = Avalue + char
                elif char.isalpha():
                    parent = parent + char
                        
            perTable = open("ElementList.txt","r")
            periodicTable = perTable.readline()
            periodicTable = periodicTable.split(',')
            for item in periodicTable:
                if item.upper() == parent:
                    index = periodicTable.index(item)
                    if betaVariable == "B+":
                        daughter = periodicTable[index-1].upper()
                    if betaVariable == "B-":
                        daughter = periodicTable[index+1].upper()

            parent = Avalue+parent
            daughter = NUCIDgen(Avalue+daughter)
            print(parent)
            print('|'+daughter+'|')
        else:
            nucID = NUCIDgen(nucID)


        ##open the appropriate ensdf file
        self.f = open("Data/"+str(ENSDF),'rU')


        linecount = 0 ## printing linecount can help locate problem-causing lines in the ensdf file
        desiredData = False

        for line in self.f:
            linecount+=1
            ## The line parsing algorithm is derived from the labeling system of the ensdf files
            ## See the endsf manual, pg. 22, for more information about how the lines of data are organized

            if (desiredData and line[0:6].strip() == ''):
            ## the loop must exit when the ensdf switches from evaluated data to experimental results
            ## this is indicated by an empty line in the ensdf file, which is detected here
                break     

            ## dsid is used in identifying decay data
            dsid = line[9:39].split(' ')

            if self.op == "two":#FIXME
                
                ## Locate identification record
                if (line[0:6] == daughter and line[6:9] == '   ' and dsid[0] == parent):
                    desiredData = True
                if desiredData == True:
                    if line[0:6] == '      ':
                        desiredData = False
                        continue
                    else:
                        if (line[0:6] == NUCIDgen(parent) and line[6:8]==' P'):
                            recordData = levelExtract(line,self.data)
                            if recordData == [-1]:
                                continue
                            if(float(recordData[1])<=energyLimit):
                                self.data.append(recordData)
                        elif (line[0:6] == daughter and line[6:8]==' L'):
                            recordData = levelExtract(line,self.data)
                            if recordData == [-1]:
                                continue
                            if(float(recordData[1])<=energyLimit):
                                self.data.append(recordData)
                            else:
                                break


            ## Options 1 and 3
            ## Identifies which lines in the data file have relevant data
            elif (line[6:8]==' L' and line[0:6]==nucID):
                #print(linecount,line[:-1])
                ## set desiredData bool so the program wil exit after reading adopted data
                desiredData = True
                ##[energy,jpi,uncert,hlife,dhlife] <- output of levelExtract
                recordData = levelExtract(line,self.data)                
                ## levelExtract passes error codes for continue
                if recordData == [-1]:
                    continue
                if(float(recordData[1])<=energyLimit):
                    ## include the data 
                    self.data.append(recordData)
                else:
                    break

                ## If no ground state energy is given, move on to the next isotope 
                if recordData[2]=='X':
                    break

    ## extraTitleText would be desired spin states, for example
    def export(self,fExtOption = '.dat',extraTitleText = ''): 
#            if(fExtOption==".dat"or fExtOption=="_Fil.dat"):##To make data files for use in gnuplot and plt file.
            fileName=str(self.name)+extraTitleText+fExtOption##creates filename
            fileName="Output/" + "gnuPlot/"+fileName.replace('/','_')
            datFile = open(fileName,'wb')##Creates a file with a valid file name.
            for i in range(len(self.data)):
                datFile.write(str.encode(str(self.data[i][0])+';'+str(self.data[i][1])+';'+str(self.data[i][2])+';'+str(self.data[i][3])+';'+str(self.data[i][4])+';'+str(self.data[i][5])+'\n'))


    def filterData(self,userInput,UI=False):
        ## no spin input
        if (userInput == ''):
            #print(self.data)
            if (not self.data):
                if(UI):
                    pass
                    ## Prints a statement telling user than no file was found
                    #print("Warning:No data filtered/selected for "+ self.name +".")
                self.data=[['NULL',0.0,"--",0.0,0.0,[0.0]]]##Enters a dummy entry to file with something.
                
        ## Filter by spin states
        else:
            if (self.data): ## If self.data has data in it
                newData = []
                groundSt = self.data[0]
                for i in range(1,len(self.data)): 
                    #print(self.name,self.data[i])
                    ## The spinMatchFinder will identify if the state is the desired spin
                    if any(spinMatchFinder(wantedString, self.data[i][2]) for wantedString in userInput.split(',')):
                        newData.append(self.data[i])
                self.data=newData##changes data to the new data.
                if (self.data):
                    self.data.insert(0,groundSt)
                else:
                    
                    if any(spinMatchFinder(wantedString,groundSt[2])for wantedString in userInput.split(',')):
                        self.data.append(groundSt)
                    else:
                        self.data = [['NULL',0.0,"--",0.0,0.0,0.0]]##Enters a dummy entry to file with something.

            else: ## If self.data is empty
                if(UI):
                    ## Prints a statement telling user than no file was found
                    pass
                    #print("Warning:No data filtered/selected for "+ self.name +".")#Prints a statement telling user than no file was found
                self.data=[['NULL',0.0,"--",0.0,0.0,0.0]]##Enters a dummy entry to file with something.

