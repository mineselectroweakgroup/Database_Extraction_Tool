from decimal import *
from functions import spinMatchFinder, levelExtract, NUCIDgen, Correct_Uncertainty
from uncertainty import multuncert

    
class data:##This is the main data class.
    def __init__(self,ENSDF,ISOvar,option,betaVar,energyLimit = 999999999):
        ###maybe get rid of option, find out how energy limit and max spin are used

        ##Initialize Parameters
        self.data = []
        self.name = ISOvar
        self.op = option
        self.decay = betaVar


        ## nucID is what is compared to the first 6 characters of the line to find the correct data
        nucID=self.name.upper()  
        if self.op == 'two':#FIXME Decay Data setup
            parent = ''
            daughter = ''
            Avalue = ''
            ## assign Avalue and parent values
            for char in nucID:
                if char.isnumeric():
                    Avalue = Avalue + char
                elif char.isalpha():
                    parent = parent + char
                        
            perTable = open("ElementList.txt","r")
            periodicTable = perTable.readline()
            periodicTable = periodicTable.split(',')
            periodicTable[-1] = periodicTable[-1][:-1]
            ## Assign daughter nucleus
            for item in periodicTable:
                if item.upper() == parent:
                    index = periodicTable.index(item)
                    if self.decay == "B+":
                        daughter = periodicTable[index-1].upper()
                        decayLabel = 'E'
                    elif self.decay == "B-":
                        daughter = periodicTable[index+1].upper()
                        decayLabel = 'B'
            parent = Avalue+parent
            daughter = NUCIDgen(Avalue+daughter)
            #print('Parent: '+ parent)
            #print('Daughter: '+daughter)
            nucID = daughter
        else:
            nucID = NUCIDgen(nucID)


        ##open the appropriate ensdf file
        self.f = open("Data/"+str(ENSDF),'rU')


        linecount = 0 ## printing linecount can help locate problem-causing lines in the ensdf file
        desiredData = False
        adoptedGammas = True
        needDecayRec = False
        need_ss_info = False

        for line in self.f:
            linecount+=1
            ## The line parsing algorithm is derived from the labeling system of the ensdf files
            ## See the endsf manual, pg. 22, for more information about how the lines of data are organized

            ## Check if line is an End Record (end of a data set)
            if (desiredData and line[0:6].strip() == ''):
                if option == 'two':
                    desiredData = False
                    if adoptedGammas: ## End of Adopted Gammas Dataset
                        adoptedGammas = False
                        ## adoptedLevelRec is used when reading the Decay Data Set
                        adoptedLevelRec = self.data[:]
                        self.data = []
                    continue
                else: ## Option 1 & 3
                    break

            ## dsid is used in identifying decay data
            dsid = line[9:39].split(' ')

            ## Locate the level records in the ADOPTED GAMMAS Dataset
            ## i.e. identifies which lines in the data file have relevant data
            if (adoptedGammas and line[6:8]==' L' and line[0:6]==nucID):
                #print(linecount,line[:-1])
                ## set desiredData bool so the program wil exit after reading adopted data
                desiredData = True
                ##[name,energy,jpi,uncert,hlife,dhlife] <- output of levelExtract
                recordData = levelExtract(line,self.data)                
                ## levelExtract passes error codes for continue
                if recordData == [-1]:
                    continue
                if(float(recordData[1])<=energyLimit):
                    ## include the data 
                    self.data.append(recordData)
                else:
                    if option == 'two':
                        continue
                    else:
                        break
                ## If no ground state energy is given, move on to the next isotope 
                if recordData[2]=='X':
                    print ('Missing ground state energy data for '+nucID)
                    break

            ## Get Decay Data ##
            if self.op == "two" and not adoptedGammas:
                
                ## Locate identification record for the decay dataset
                if (line[0:6] == daughter and line[6:9] == '   ' and dsid[0] == parent):
                    desiredData = True
                if desiredData == True:

                    ## Locate Parent Record and retrieve data
                    if (line[0:6] == NUCIDgen(parent) and line[6:8]==' P'):
                        recordData = levelExtract(line,self.data)
                        if recordData == [-1]:
                            continue
                        if(float(recordData[1])<=energyLimit):
                            self.data.append(recordData)

                    ## Locate the Normalization record for scaling branching ratios
                    if (line[0:6] == daughter and line[6:8] == ' N'):
                        ## See ensdf manual for more information on what these terms are (pg. 18)
                        BR = line[31:39].strip()
                        dBR = line[39:41].strip()
                        NB = line[41:49].strip()
                        dNB = line[49:55].strip()
                
                        if BR == '':
                            BR = '1'
                        if NB == '':
                            NB = '1'
                        #if dBR == '':
                        #    dBR = '0'
                        #else:
                        #    dBR = Correct_Uncertainty(BR,dBR)
                        if any(char.isalpha() for char in dNB):
                            d_scale_factor = dNB
                        elif dNB == '':
                            dNB = '0'
                            d_scale_factor = multuncert(float(NB),float(BR),float(dNB),float(dNB))
                        else:
                            dNB = Correct_Uncertainty(NB,dNB)
                            d_scale_factor = multuncert(float(NB),float(BR),float(dNB),float(dNB))

                        scale_factor = float(NB)*float(BR)

                    ## Locate the PN record to use instead of N record scaling
                    ## the N rec is only used if PN rec is empty
                    #FIXME get error & propagate
                    if (line[0:6] == daughter and line[6:8] == 'PN'):
                        NBBR = line[41:49].strip()
                        dNBBR = line[49:55].strip()
                        if not NBBR == '':
                            if dNBBR == '':
                                ## Use d_scale_factor from N record
                                pass
                            else:
                                d_scale_factor = ScaleUncert(NBBR,dNBBR)

                            scale_factor = float(NBBR)
                        ## Else: use scale_factor from N record 


                    ## Locate daughter Level Record
                    elif (line[0:6] == daughter and line[6:8]==' L'):
                        ## Get data from adoptedLevelRec     
                        recordData = levelExtract(line,self.data)
                        if recordData == [-1]:
                            continue
                        if(float(recordData[1])<=energyLimit):   
                            dataMatch = False
                            errorList = []
                            ## Frequently in the Decay Data Sets, the level records for the daughter isomers lack half life data, so that state's level record from the Adopted Gammas Data Set is used instead (all of the Gamma Level records are constained in adoptedLevelRec).

                            ## Find matching Adopted Gamma record
                            for record in adoptedLevelRec:
                                if Decimal(record[1]) == Decimal(recordData[1]):
                                    matchedRecord = record[:] ##Necessary string copy
                                    self.data.append(matchedRecord)
                                    dataMatch = True
                                    break
                                ## Sometimes the energy of a state differs between the Decay Data Set and the Adopted Data Set. A percent error (of energy) calculation is used to determine the closest Adopted Data Set level record for a given Decay Data Set level record.
                                else:
                                    errorPercent = abs((Decimal(record[1])-Decimal(recordData[1]))/Decimal(recordData[1])*Decimal('100'))
                                    errorList.append(errorPercent)
                            if not dataMatch:
                                ## MAXERROR is the maximum percent error with which a Decay Data Set state can be matched to an Adopted Gammas state.
                                MAXERROR = 1
                                minIndex = errorList.index(min(errorList))
                                if errorList[minIndex] < MAXERROR:
                                    minRec = adoptedLevelRec[minIndex]
                                    closestRec = minRec[:] ##Necessary string copy
                                    self.data.append(closestRec)
                                    ## Inform the user that a state has been imperfectly matched
                                    #print(recordData[0]+' state at '+recordData[1]+' keV matched to adopted level at '+adoptedLevelRec[minIndex][1]+' keV w/ error of '+str(round(errorList[minIndex],4))+'%.')
                                ## Case where the nearest Adopted Data Set level record is not within MAXERROR percent of the Decay Data Set level record.
                                else:
                                    #print('No adopted record found for '+recordData[0]+' at '+recordData[1]+' keV with under '+str(MAXERROR)+'% error.')
                                    self.data.append(recordData)
                            if needDecayRec == True:
                                ##no Decay record for previous daughter Level rec
                                self.data[-2].append('0')
                            needDecayRec = True
                            errorList = []
                        else:
                            continue
                    ## Identify decay record
                    elif(needDecayRec and line[0:6] == daughter and line[6:8]==' '+decayLabel):
                        ## Variables named *I are branching intensities
                        betaI = line[21:29].strip() ##Beta decay branching intensity
                        dbetaI = line[29:31].strip()
                        ## give uncertainty correct magnitude 
                        if any (char.isalpha() for char in dbetaI):
                            pass   
                        elif dbetaI == '':
                            pass
                        elif ('.' in betaI):
                            dbetaI = str(float(Correct_Uncertainty(betaI,dbetaI))*scale_factor)

                        ecI = line[31:39].strip() ##Electron Capture branching intensity
                        decI = line[39:41].strip()
                       
                        ## give uncertainty correct magnitude 
                        if any (char.isalpha() for char in decI):
                            pass   
                        elif decI == '':
                            pass
                        elif ('.' in ecI):
                            decI = str(float(Correct_Uncertainty(ecI,decI))*scale_factor)

                        ## get total branching intensity
                        if ecI == '' and betaI == '':
                            totBranchI = ''
                        elif ecI == '':
                            totBranchI = str(float(betaI)*scale_factor)
                        elif betaI == '':
                            totBranchI = str(float(ecI)*scale_factor)
                        else:
                            totBranchI = str((float(betaI) + float(ecI))*scale_factor)
                        needDecayRec = False
                        self.data[-1].append(totBranchI)


    def export(self,fExtOption = '.dat',extraTitleText = ''): 
#            if(fExtOption==".dat"or fExtOption=="_Fil.dat"):##To make data files for use in gnuplot and plt file.
            fileName=str(self.name)+extraTitleText+fExtOption##creates filename
            fileName="Output/" + "gnuPlot/"+fileName.replace('/','_')
            datFile = open(fileName,'wb')##Creates a file with a valid file name.
            for i in range(len(self.data)):
                lineToWrite = str(self.data[i][0])
                for j in range(1,len(self.data[i])):
                    lineToWrite = lineToWrite + ';' +str(self.data[i][j])
                lineToWrite = lineToWrite + '\n'
                datFile.write(str.encode(lineToWrite))

    ## Filters by desired spin states, if given
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
                self.data=newData[:]##changes data to the new data.
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

