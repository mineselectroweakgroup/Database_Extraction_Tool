##DATA Class
##By: Markus Garbiso
##Date Updated: May 6, 2017 by Peter Consalvi
##Date Updated: May 17, 2017 by Matthew Martin

##This function is used in the main __init__ function to parse through strings in each line of the file inorder to find the value of the spin that corresponds to energy of that line of that file.
def numberSlashBool(lineString,posTracker,trackChar):
    if(lineString.index(trackChar)-posTracker>-1):##This condition pertains to all characters that are allowed in a
        ##given spin
        if((lineString[lineString.index(trackChar)-posTracker]=='1' or lineString[lineString.index(trackChar)-posTracker]=='2' or lineString[lineString.index(trackChar)-posTracker]=='3' or lineString[lineString.index(trackChar)-posTracker]=='4' or lineString[lineString.index(trackChar)-posTracker]=='5' or lineString[lineString.index(trackChar)-posTracker]=='6' or lineString[lineString.index(trackChar)-posTracker]=='7' or lineString[lineString.index(trackChar)-posTracker]=='8' or lineString[lineString.index(trackChar)-posTracker]=='9' or lineString[lineString.index(trackChar)-posTracker]=='0' or lineString[lineString.index(trackChar)-posTracker]=='/'or lineString[lineString.index(trackChar)-posTracker]=='-'or lineString[lineString.index(trackChar)-posTracker]=='+'or lineString[lineString.index(trackChar)-posTracker]==')')):
            return True
    else:##This condtion is reached when the loop using this function reaches a character that could not be in a spin string.
        return False

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

class data:##This is the main data class
    def __init__(self,ENSDF,ISOvar,option = 'EoL',energyLimit=5000,maxSpin = 9): ##Initiator to take only lines that are determined by the filt (short for filter)

        ##Initialize Parameters
        filtDataSet = []
        self.data = []
        self.name = ISOvar
        self.op=option

        ##If there is a data file that matches the user's input then this program will try to extract the data.
        self.f = open("Data/"+str(ENSDF),'rU')
        ##Each line of the file is split into list so the code can parse through each line easier

        #Initializes a to be apple, a string that should not appear in the data file
        #This is used to stop the code after it goes through the first block
        a = 'apple'
        for line in self.f:
            line = line.split()

            ##Break function used to stop code after the evaluated nuclear data
            if len(line) == 0 and \
               a.lower() == b.lower():
                break

            ##Names for each entry which are used to filter which lines are used 
            if(len(line) >= 3): ##This makes sure not to take any lines that are emptry which will cause an error down the line.
                a = line[0] ##The first entry of each line, usually the filename. a will be used to double check to see if that line is valid.
                c = line[1] ##This second entry contains what type of data and information is in the list line. The ENSDF website has a complete list of
                            ##each line type. I used L since L lines have experimental data.

            ##This resets a to be apple every time there is a blank line
            ##This ensures that the first block wanted will be read rather than the first block in the file
            if(len(line) == 0):
                a = 'apple'

                
            b = str(ISOvar)
            ##This part of the code contains parsing algorithims to find wanted values,depending on what option is used.
            ##Marcus found that experimental data are one lines when c equal "L"


#This massive series of nested loops is what extracts the data of interest from the monster ensdf data files according to the user's inputs. 
            if(option == 'EoL' and a.lower() == b.lower() and c == "L"): 
                a = ''
                b = ''
                for i in range(3,len(line)): ##This loop will parse through each entry of line to find the spin corrospondin to the energy of that spin.
                    ##Intitialize the string used for the spin value and a temp string varible to take a string that has a spin, but may have
                    ##extra characters due to the incosistent file structure of ENSDF.
                    spinStr=''
                    unfilSpinStr=str(line[i])
                    
                    ##This if statement stops the code if the first character in the spin state is a J, which do not correspond to actual spin states
                    ##This corrects the 65Zn plotting 2+ states issue
                    if str(line[i][0]) == "J":
                        break
                    
                    oddANumberSingleDigitCheck=True
                    if(len(unfilSpinStr)>1 and not('X' in unfilSpinStr)and not('x' in unfilSpinStr) and not('Y' in unfilSpinStr)and not('y' in unfilSpinStr)):##Rarely, an entry will have pesky x and y characters which will break the program, so this if statment will not allow those statements. Also strings with lenths of 1 will break the program's algorithm.
                        for z in range(unfilSpinStr.count('+')+unfilSpinStr.count('-')):
                            if(':' in unfilSpinStr):
                                try:
                                    if('/' in str(line[2])):
                                        line[2]=str(line[2])
                                        line[2]=line[2][:line[2].find('/')]
                                    elif('+' in str(line[2])):
                                        line[2]=str(line[2])
                                        line[2]=line[2][:line[2].find('+')]
                                    elif( '-' in str(line[2])):
                                        line[2]=str(line[2])
                                        line[2]=line[2][:line[2].find('-')]
                                    ##print float(line[2])<=energyLimit,line[2]
                                    if(float(line[2])<=energyLimit):
                                        ##print unfilSpinStr
                                        upper=int(unfilSpinStr[unfilSpinStr.index(':')+1])
                                        if (unfilSpinStr[unfilSpinStr.index(':')-1]!='-' and unfilSpinStr[unfilSpinStr.index(':')-1]!='+'):
                                            lower=int(unfilSpinStr[unfilSpinStr.index(':')-1])
                                        else:
                                            lower=int(unfilSpinStr[unfilSpinStr.index(':')-2])

                                        if('-' in unfilSpinStr):
                                            for i in range(lower,upper+1):
                                                ##print [float(line[2]),str(i)+'-']
                                                filtDataSet.append([float(line[2]),"("+str(i)+'-'+")"])
                                        elif('+' in unfilSpinStr):
                                            for i in range(lower,upper+1):
                                                ##print [float(line[2]),str(i)+'+']
                                                filtDataSet.append([float(line[2]),"("+str(i)+'+'+")"])
                                except:
                                    print("Error with " + str(line[2])+ " " +unfilSpinStr + " at loop 0a")                                   
                            elif('+' in unfilSpinStr): ##For strings will + only but like the first case above for + and -.
                                posTracker=0
                                while(numberSlashBool(unfilSpinStr,posTracker,'+')):
                                    posTracker=posTracker+1
                                for j in range(unfilSpinStr.index('+')-posTracker+1,unfilSpinStr.index('+')+1):
                                    spinStr=spinStr+unfilSpinStr[j]
                                ##print(spinStr)    
                                if(('(' in unfilSpinStr or ')' in unfilSpinStr) and len(spinStr.replace("(","").replace(")",""))>1):
                                    unfilSpinStr.replace(spinStr,"")
                                    spinStr="("+spinStr.replace("(","").replace(")","")+")".replace("(","").replace(")","")+")"
                                    para = True
                                else:
                                    unfilSpinStr.replace(spinStr,"")
                                    para = False
                                    
                                ##print(spinStr + "test")
                                if(spinStr.replace("+","").replace("-","").replace("(","").replace(")","") and not('+' in spinStr and '-' in spinStr)):
                                    saneString=spinStr.replace("+","").replace("-","").replace("(","").replace(")","")
                                    if(eval(saneString)>maxSpin):
                                        try:
                                            if('/' in str(line[2])):
                                                line[2]=str(line[2])
                                                line[2]=line[2][:line[2].find('/')]
                                            elif('+' in str(line[2])):
                                                line[2]=str(line[2])
                                                line[2]=line[2][:line[2].find('+')]
                                            elif( '-' in str(line[2])):
                                                line[2]=str(line[2])
                                                line[2]=line[2][:line[2].find('-')]
                                            if(float(line[2])<=energyLimit and '/' in spinStr):
                                                if(eval(spinStr[:spinStr.index('/')].replace("(",""))<10 or oddANumberSingleDigitCheck):
                                                    if para:
                                                        filtDataSet.append([float(line[2]),"("+spinStr[-5]+spinStr[-4]+spinStr[-3]+spinStr[-2]+")"])
                                                    else:
                                                        filtDataSet.append([float(line[2]),spinStr[-4]+spinStr[-3]+spinStr[-2]+spinStr[-1]])
                                                else:
                                                    if para:
                                                        filtDataSet.append([float(line[2]),"("+spinStr[-6]+spinStr[-5]+spinStr[-4]+spinStr[-3]+spinStr[-2]+")"])
                                                    else:
                                                        filtDataSet.append([float(line[2]),spinStr[-5]+spinStr[-4]+spinStr[-3]+spinStr[-2]+spinStr[-1]])
                                            elif(float(line[2])<=energyLimit and hasNumbers(spinStr[-2]+spinStr[-1])):
                                                if para:
                                                    filtDataSet.append([float(line[2]),"("+spinStr[-2]+spinStr[-1]+")"])
                                                else:
                                                    filtDataSet.append([float(line[2]),spinStr[-2]+spinStr[-1]])
                                        except:
                                            print("Error with " + str(line[2])+ " " +spinStr + " at loop 2a")
                                    else:
                                        try:
                                            if('/' in str(line[2])):
                                                line[2]=str(line[2])
                                                line[2]=line[2][:line[2].find('/')]
                                            elif('+' in str(line[2])):
                                                line[2]=str(line[2])
                                                line[2]=line[2][:line[2].find('+')]
                                            elif( '-' in str(line[2])):
                                                line[2]=str(line[2])
                                                line[2]=line[2][:line[2].find('-')]
                                            if(float(line[2])<=energyLimit):
                                               filtDataSet.append([float(line[2]),spinStr])
                                            if('/' in spinStr):
                                                if(eval(spinStr[:spinStr.index('/')].replace("(",""))<10):
                                                    oddANumberSingleDigitCheck=True
                                                else:
                                                    oddANumberSingleDigitCheck=False
                                        except:
                                            print("Error with " + str(line[2])+ " " +str(spinStr) + " at loop 2b")

                                spinStr = ''
                            elif('-' in unfilSpinStr):##For strings will - only but like the first case above for + and -.
                                posTracker=0
                                while(numberSlashBool(unfilSpinStr,posTracker,'-')):
                                    posTracker=posTracker+1
                                for j in range(unfilSpinStr.index('-')-posTracker+1,unfilSpinStr.index('-')+1):
                                    spinStr=spinStr+unfilSpinStr[j]
                                
                                if(('(' in unfilSpinStr or ')' in unfilSpinStr) and len(spinStr.replace("(","").replace(")",""))>1):
                                    unfilSpinStr.replace(spinStr,"")
                                    spinStr="("+spinStr.replace("(","").replace(")","")+")".replace("(","").replace(")","")+")"
                                    para = True
                                else:
                                    unfilSpinStr.replace(spinStr,"")
                                    para = False
                                
                                if(spinStr.replace("+","").replace("-","").replace("(","").replace(")","") and not('+' in spinStr and '-' in spinStr)):
                                    saneString=spinStr.replace("+","").replace("-","").replace("(","").replace(")","")
                                    if(eval(saneString)>maxSpin):
                                        try:
                                            if('/' in str(line[2])):
                                                line[2]=str(line[2])
                                                line[2]=line[2][:line[2].find('/')]
                                            elif('+' in str(line[2])):
                                                line[2]=str(line[2])
                                                line[2]=line[2][:line[2].find('+')]
                                            elif( '-' in str(line[2])):
                                                line[2]=str(line[2])
                                                line[2]=line[2][:line[2].find('-')]
                                            if(float(line[2])<=energyLimit and '/' in spinStr):
                                                if(eval(spinStr[:spinStr.index('/')].replace("(",""))<10 or oddANumberSingleDigitCheck):
                                                    if para:
                                                        filtDataSet.append([float(line[2]),"("+spinStr[-5]+spinStr[-4]+spinStr[-3]+spinStr[-2]+")"])
                                                    else:
                                                        filtDataSet.append([float(line[2]),spinStr[-4]+spinStr[-3]+spinStr[-2]+spinStr[-1]])
                                                else:
                                                    if para:
                                                        filtDataSet.append([float(line[2]),"("+spinStr[-6]+spinStr[-5]+spinStr[-4]+spinStr[-3]+spinStr[-2]+")"])
                                                    else:
                                                        filtDataSet.append([float(line[2]),spinStr[-5]+spinStr[-4]+spinStr[-3]+spinStr[-2]+spinStr[-1]])
                                            elif(float(line[2])<=energyLimit and hasNumbers(spinStr[-2]+spinStr[-1])):
                                                if para:
                                                    filtDataSet.append([float(line[2]),"("+spinStr[-2]+spinStr[-1]+")"])
                                                else:
                                                    filtDataSet.append([float(line[2]),spinStr[-2]+spinStr[-1]])
                                        except:
                                            print("Error with " + str(line[2])+ " " +spinStr + " at loop 3a")
                                    else:
                                        try:
                                            if('/' in str(line[2])):
                                                line[2]=str(line[2])
                                                line[2]=line[2][:line[2].find('/')]
                                            elif('+' in str(line[2])):
                                                line[2]=str(line[2])
                                                line[2]=line[2][:line[2].find('+')]
                                            elif( '-' in str(line[2])):
                                                line[2]=str(line[2])
                                                line[2]=line[2][:line[2].find('-')]
                                            if(float(line[2])<=energyLimit):
                                               filtDataSet.append([float(line[2]),spinStr])
                                            if('/' in spinStr):
                                                if(eval(spinStr[:spinStr.index('/')].replace("(",""))<10):
                                                    oddANumberSingleDigitCheck=True
                                                else:
                                                    oddANumberSingleDigitCheck=False
                                        except:
                                            print("Error with " + str(line[2])+ " " +str(spinStr) + " at loop 3b")
                                spinStr = ''
                                
                
        ##This if loop rids the data list of redundant entries and saves data into
        ##the self.data list
        for i in filtDataSet:
              if i not in self.data:
                self.data.append(i)##Saves data into the self.data list
        self.f.close()##Closes the ENSDF file
        
    ##This function exports the data in the class into a data file. The output file is
    ##is sent to the Output file
    def export(self,fExtOption = ".txt",extraTitleText=""):
            if(self.op == 'EoL'):##for energies and spins
                if(fExtOption==".dat"or fExtOption=="_Fil.dat"):##To make data files for use in gnuplot and plt file.
                    fileName=str(self.name)+extraTitleText+fExtOption##creates filename
                    fileName="Output/" + "gnuPlot/"+fileName.replace('/','_')
                    datFile = open(fileName,'wb')##Creates a file with a valid file name.
                    for i in range(len(self.data)):##Write the line fro each entry and each entry is delimited by a ,
                        datFile.write(str(self.name)+','+str(self.data[i][0])+','+str(self.data[i][1])+'\n')
                        ###.dat is used for preparing data for gnuplot
                else:##This case is like the code above but for every other file type and is delimited by tabs.
                    fileName=str(self.name)+extraTitleText+fExtOption
                    fileName="Output/" + "gnuPlot/"+fileName.replace('/','_')
                    datFile = open(fileName,'wb')##Creates a file with a valid file name.
                    exportFile = open("Output/"+str(self.name)+extraTitleText+fExtOption,'wb')
                    for i in range(len(self.data)):
                        exportFile.write(str(self.name)+'\t'+str(self.data[i][0])+'\t'+str(self.data[i][1])+'\n')
                        ##.txt or any other file extension is used for preparing data for generic text file.    
            else:##Writes the each entry of our datalist with one entry per line.
                exportFile = open("Output/"+str(self.name)+".txt",'wb')
                for i in range(len(self.data)):
                    exportFile.write(str(self.name)+'\t'+str(self.data[i])+'\n')
                    ##Writes Energy Only
                    
    ##This functino allows the user to choose only wanted spins of a given data set. Note: This is only valid for the EoL option. The userinput must follow this
    ##syntax "0+,2+,3/2-" no quotations.
    def filterData(self,userInput,UI=False):
        if(self.op == 'EoL'):
            newData=[]##storage for new data
            for wantedString in userInput.split(","):##adds all the strings that are included in the userInput.
                for i in range(0,len(self.data)):
                    if(self.data[i][1]==wantedString or self.data[i][1]==("("+wantedString+")")):
                        newData.append(self.data[i])
            if(newData):
                self.data=newData##changes data to the new data.
            else:
                if(UI):
                    print "Warning:No data filtered/selected for "+ self.name +"."
                self.data=[[0.0,"NO_DATA"]]##Enters a dummy entry to file with something.
