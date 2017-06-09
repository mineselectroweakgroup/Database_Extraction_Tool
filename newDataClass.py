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
        ## This while loop makes sure that nucID has the correct whitespace to match the data file
        charIndex=0
        while(charIndex<3):
            if self.name[charIndex].isalpha():
                nucID=' '+nucID
            charIndex+=1

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

                ## set desiredData bool so the program wil exit after reading evaluated data
                desiredData = True

                ## finding the energy
                energy = line[9:19].strip()
                if 'E' in energy: ## This will convert scientific to decimal notation if needed
                    significand = float(energy[:energy.find('E')])
                    power = 10** float(energy[energy.find('E')+1:])
                    energy = str(significand * power)
                ## discard points where energy contains letters
                if not isNumber(energy):                    
                    continue


                ## Finding the uncertainty
                uncert = line[19:21].strip()
                print(uncert)
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
                            numberino = numberino[:-1-i] + numberino[-i:]
                        if (i < len(uncert)):
                            digit = int(numberino[-1-i])+int(uncert[-1-i])
                        else:
                            digit = int(numberino[-1-i])
                        topLimit = digit * (10**i) + topLimit
                    topLimit = str(topLimit)[:-decIndex]+'.'+str(topLimit)[-decIndex:]
                    uncert = str(Decimal(topLimit)-Decimal(energy))




                jpi = line[21:39].strip() ## ALL spin and pairity states
                jpi = '0+' #sets all spins to be 0+ for plot testing

                if(float(energy)<=energyLimit):
                    #include the data
                    self.data.append([energy,jpi,uncert])
                    print(str(linecount)+' :'+str(self.data[-1]))
                else:
                    break

    ## extraTitleText would be desired spin states, for example
    def export(self,fExtOption = '.dat',extraTitleText = ''): 
#            if(fExtOption==".dat"or fExtOption=="_Fil.dat"):##To make data files for use in gnuplot and plt file.
            fileName=str(self.name)+extraTitleText+fExtOption##creates filename
            fileName="Output/" + "gnuPlot/"+fileName.replace('/','_')
            datFile = open(fileName,'wb')##Creates a file with a valid file name.
            for i in range(len(self.data)):
                datFile.write(str.encode(str(self.name)+','+str(self.data[i][0])+','+str(self.data[i][1])+','+str(self.data[i][2]+'\n')))

