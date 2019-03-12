from decimal import *
from functions import spinMatchFinder, levelExtract, NUCIDgen, Correct_Uncertainty
from uncertainty import multuncert
from RecordClasses import *

    
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
        self.f = open("ensdf_Data_Files/"+str(ENSDF),'rU')


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

                extractedData = levelExtract(line, self.data)
                ## The try/except checks if levelExtract is returning a continue code
                try:
                    ## assign data to LevelRecord class object
                    recordData = LevelRecord(*extractedData)
                except TypeError:
                    ## levelExtract passes error codes for continue
                    if extractedData == [-1]:
                        continue
                    else:
                        print('*** Improper initialization of LevelRecord object\n')
                        ##Deliberatly crash the program so that bugs can be found
                        float('crash')


                if(float(recordData.energy)<=energyLimit):
                    ## include the data 
                    self.data.append(recordData)
                    #recordData.print_record()
                else:
                    if option == 'two':
                        continue
                    else:
                        break
                ## If no ground state energy is given, move on to the next isotope 
                if recordData.jpi =='X':
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
                        extractedData = levelExtract(line, self.data)
                        ## The try/except checks if levelExtract is returning a continue code
                        try:
                            ## assign data to LevelRecord class object
                            recordData = LevelRecord(*extractedData)
                        except TypeError:
                            ## levelExtract passes error codes for continue
                            if extractedData == [-1]:
                                continue
                            else:
                                print('*** Improper initialization of LevelRecord object\n')
                                ##Deliberatly crash the program so that bugs can be found
                                float('crash')

                        if(float(recordData.energy)<=energyLimit):
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
                        extractedData = levelExtract(line, self.data)
                        ## The try/except checks if levelExtract is returning a continue code
                        try:
                            ## assign data to LevelRecord class object
                            recordData = LevelRecord(*extractedData)
                        except TypeError:
                            ## levelExtract passes error codes for continue
                            if extractedData == [-1]:
                                continue
                            else:
                                print('*** Improper initialization of LevelRecord object\n')
                                ##Deliberatly crash the program so that bugs can be found
                                float('crash')

                        if(float(recordData.energy)<=energyLimit):   
                            dataMatch = False
                            errorList = []
                            ## Frequently in the Decay Data Sets, the level records for the daughter isomers lack half life data, so that state's level record from the Adopted Gammas Data Set is used instead (all of the Gamma Level records are constained in adoptedLevelRec).

                            ## Find matching Adopted Gamma record
                            for record in adoptedLevelRec:
                                if Decimal(record.energy) == Decimal(recordData.energy):
                                    ### Here I got rid of a proper string copy ([:]) and am now just copying LevelRecord classes. This MAY cause problems if a state is in the decay data set twice, where modifying one instance of the class also changes the other (manifesting in the duplicate state having twice as much ionization or mass energy. #FIXME confirm that this class copy works for cases such as 38K which has an excited isomer that B decays
                                    matchedRecord = record ##Necessary string copy
                                    self.data.append(matchedRecord)
                                    dataMatch = True
                                    break
                                ## Sometimes the energy of a state differs between the Decay Data Set and the Adopted Data Set. A percent error (of energy) calculation is used to determine the closest Adopted Data Set level record for a given Decay Data Set level record.
                                else:
                                    errorPercent = abs((Decimal(record.energy)-Decimal(recordData.energy))/Decimal(recordData.energy)*Decimal('100'))
                                    errorList.append(errorPercent)
                            if not dataMatch:
                                ## MAXERROR is the maximum percent error with which a Decay Data Set state can be matched to an Adopted Gammas state.
                                MAXERROR = 1
                                minIndex = errorList.index(min(errorList))
                                if errorList[minIndex] < MAXERROR:
                                    minRec = adoptedLevelRec[minIndex]
                                    closestRec = minRec ##Necessary string copy #FIXME remove this?
                                    self.data.append(closestRec)
                                    ## Inform the user that a state has been imperfectly matched
                                    #print(recordData[0]+' state at '+recordData[1]+' keV matched to adopted level at '+adoptedLevelRec[minIndex][1]+' keV w/ error of '+str(round(errorList[minIndex],4))+'%.')
                                ## Case where the nearest Adopted Data Set level record is not within MAXERROR percent of the Decay Data Set level record.
                                else:
                                    #print('No adopted record found for '+recordData[0]+' at '+recordData[1]+' keV with under '+str(MAXERROR)+'% error.')
                                    self.data.append(recordData)
                            if needDecayRec == True:
                                ##no Decay record for previous daughter Level rec
                                decayRecData = DecayRecord(self.data[-2], '0','0', '0', '0', '0')
                                self.data[-2] = decayRecData
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

                        ## get total branching intensity FIXME error prop
                        if ecI == '' and betaI == '':
                            totBranchI = ''
                        elif ecI == '':
                            totBranchI = str(float(betaI)*scale_factor)
                        elif betaI == '':
                            totBranchI = str(float(ecI)*scale_factor)
                        else:
                            totBranchI = str((float(betaI) + float(ecI))*scale_factor)
                        needDecayRec = False
                        decayRecData = DecayRecord(self.data[-1], betaI, dbetaI, ecI, decI, totBranchI)
                        self.data[-1] = decayRecData



    def export(self,fExtOption = '.dat',extraTitleText = ''): 
        fileName=str(self.name)+extraTitleText+fExtOption##creates filename
        fileName="Output/" + "gnuPlot/"+fileName.replace('/','_')
        datFile = open(fileName,'wb')##Creates a file with a valid file name.
        for i in range(len(self.data)):

            lineToWrite = self.data[i].make_data_string()
            datFile.write(str.encode(lineToWrite))

    ## Filters by desired spin states, if given
    def filterData(self,userInput,UI=False):
        nullRecord = LevelRecord('NULL',0.0,"--",0.0,0.0,[0.0])
        ## no spin input
        if (userInput == ''):
            #print(self.data)
            if (not self.data):
                if(UI):
                    pass
                    ## Prints a statement telling user than no file was found
                    #print("Warning:No data filtered/selected for "+ self.name +".")
                self.data=[nullRecord]##Enters a dummy entry to file with something.
                
        ## Filter by spin states
        else:
            if (self.data): ## If self.data has data in it
                newData = []
                groundSt = self.data[0]
                for i in range(1,len(self.data)): 
                    #print(self.name,self.data[i])
                    ## The spinMatchFinder will identify if the state is the desired spin
                    if any(spinMatchFinder(wantedString, self.data[i].jpi) for wantedString in userInput.split(',')):
                        newData.append(self.data[i])
                self.data=newData[:]##changes data to the new data.
                if (self.data):
                    self.data.insert(0,groundSt)
                else:
                    if any(spinMatchFinder(wantedString,groundSt.jpi)for wantedString in userInput.split(',')):
                        self.data.append(groundSt)
                    else:
                        self.data = [nullRecord]##Enters a dummy entry to file with something.

            else: ## If self.data is empty
                if(UI):
                    ## Prints a statement telling user than no file was found
                    pass
                    #print("Warning:No data filtered/selected for "+ self.name +".")#Prints a statement telling user than no file was found
                self.data=[nullRecord]##Enters a dummy entry to file with something.

