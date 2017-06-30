from decimal import *
from functions import spinMatchFinder
from functions import levelExtract
 
    
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
            ## this is indicated by an empty line in the ensdf file, which is detected here
            if (desiredData and line[0:6].strip() == ''):
                break     

             ## Identifies which lines in the data file have relevant data
            if (line[6:8]==' L' and line[0:6]==nucID):
                #print(linecount,line[:-1])

                ## set desiredData bool so the program wil exit after reading adopted data
                desiredData = True

                ##[energy,jpi,uncert,hlife,dhlife] <- output of levelExtract
                recordData = levelExtract(line,self.data)                


                if(float(recordData[0])<=energyLimit):
                    ## include the data #FIXME half lives not written to file
                    self.data.append(recordData)
                    #print(str(linecount)+' :'+str(self.data[-1]))
                else:
                    break

                ## If no ground state energy is given, move on to the next isotope #FIXME noGSE defined in levelextract
                if recordData[1]=='X':
                    break

    ## extraTitleText would be desired spin states, for example
    def export(self,fExtOption = '.dat',extraTitleText = ''): 
#            if(fExtOption==".dat"or fExtOption=="_Fil.dat"):##To make data files for use in gnuplot and plt file.
            fileName=str(self.name)+extraTitleText+fExtOption##creates filename
            fileName="Output/" + "gnuPlot/"+fileName.replace('/','_')
            datFile = open(fileName,'wb')##Creates a file with a valid file name.
            for i in range(len(self.data)):
                datFile.write(str.encode(str(self.name)+';'+str(self.data[i][0])+';'+str(self.data[i][1])+';'+str(self.data[i][2])+';'+str(self.data[i][3])+';'+str(self.data[i][4])+'\n'))


    def filterData(self,userInput,UI=False):
        ## no spin input
        if (userInput == ''):
            #print(self.data)
            if (not self.data):
                if(UI):
                    pass
                    ## Prints a statement telling user than no file was found
                    #print("Warning:No data filtered/selected for "+ self.name +".")
                self.data=[[0.0,"--",0.0,0.0,[0.0]]]##Enters a dummy entry to file with something.
                
        #if(self.op == 'EoL'):
        ## Filter by spin states
        else:
            if (self.data): ## If self.data has data in it
                newData = []
                groundSt = self.data[0]
                for i in range(1,len(self.data)): 
                    #print(self.name,self.data[i])
                    ## The spinMatchFinder will identify if the state is the desired spin
                    if any(spinMatchFinder(wantedString, self.data[i][1]) for wantedString in userInput.split(',')):
                        newData.append(self.data[i])
                self.data=newData##changes data to the new data.
                if (self.data):
                    self.data.insert(0,groundSt)
                else:
                    
                    if any(spinMatchFinder(wantedString,groundSt[1])for wantedString in userInput.split(',')):
                        self.data.append(groundSt)
                    else:
                        self.data = [[0.0,"--",0.0,0.0,0.0]]##Enters a dummy entry to file with something.

            else: ## If self.data is empty
                if(UI):
                    ## Prints a statement telling user than no file was found
                    pass
                    #print("Warning:No data filtered/selected for "+ self.name +".")#Prints a statement telling user than no file was found
                self.data=[[0.0,"--",0.0,0.0,0.0]]##Enters a dummy entry to file with something.

