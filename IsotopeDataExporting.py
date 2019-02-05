import DataClass as dc
import os, sys
import re
import mass_data as md
import ionization as addion
import time
import Parabola_Qt, Beta_Qt, Nuc_Qt



#This function is used to bulk export a range of isotopes in a given A range.
#common ancestor of beta (Will_Gammas,Will_noGUI and master)
#def datExp(option,UI=False,Filter=False):

#beta (Will_Gammas,Will_noGUI and master)
#def datExp(option,user_ins, UI=False):

#gui_yana
def datExp(option,UI=False,Filter=False,gif=""):
#This uses the option from the first GUI to get inputs from the correct GUI. Some of the definitions here are
#used to maintain full use of Markus' code, such as the definition of higherBound in Beta_GUI
#common ancestor/Will use tryAgainCounter
    #tryAgainCounter=1
    if option == "one":

#gui_yana and common ancestor      
	Z, isoLo, isoHi, E, exitcount, mass, J = Nuc_Qt.getguioutputs(gif)
        elementName= str(Z)
        lowerBound = int(isoLo)
        higherBound = int(isoHi)
        energyLim = int(E)
        exitcount = int(exitcount)
        massData = str(mass)
        wantedSpins=str(J).replace(" ","")
        energyLim=int(E)
        elementName = elementName.replace(" ","")
        elementName = elementName.title()
        elementName = elementName.split(',')
        temperature = 0
        betaVariable = 'NULL' ## Required parameter of DataClass


#Will uses a try  statement
	#try:
            #from GUI import guioutputs
            #elementName= str(guioutputs.Z)
            #lowerBound = int(guioutputs.isoLow)
            #higherBound = int(guioutputs.isoUp)
            #energyLim = int(guioutputs.E)
            #exitcount = int(guioutputs.exitcount)
            #massData = False #str(guioutputs.mass)
            #wantedSpins=str(guioutputs.J).replace(" ","")
            #energyLim=int(guioutputs.E)
            #temperature = 0
        #except: #FIXME Errortype
        ## Catches Error from GUI


#Will uses the try and the following user_ins and finally
            #elementName= str(user_ins.Z)
            #lowerBound = int(user_ins.isoLow)
            #higherBound = int(user_ins.isoUp)
            #energyLim = int(user_ins.E)
            #exitcount = int(user_ins.exitcount)
            #massData = user_ins.mass
            #wantedSpins=str(user_ins.J).replace(" ","")
            #energyLim=int(user_ins.E)
            #temperature = 0
        #finally:
            #elementName = elementName.replace(" ","")
            #elementName = elementName.title()
            #elementName = elementName.split(',')
            #betaVariable = 'NULL' ## Required parameter of DataClass
            
        
    elif option == "two":

#yana/common ancestor
        Z, A, J, E, B, T = Beta_Qt.getbetaoutputs(gif)
        elementName = str(Z)
        lowerBound = int(A)
        higherBound = int(A)
        betaVariable = str(B)
        energyLim = int(E)
        massData = "YES"
        elementName = elementName.title()
        wantedSpins=str(J).replace(" ","")

#Common ancestor for and if loop
	''''
        perTable = open("ElementList.txt","r")
        periodicTable = perTable.readline()
        periodicTable = periodicTable.split(',')
        for item in periodicTable:
            if item == elementName:
                index = periodicTable.index(item)
                if betaVariable == "B+":
                    elementName = periodicTable[index-1] + "," + elementName
                if betaVariable == "B-":
                    elementName = elementName + "," + periodicTable[index+1]
        '''

#Will uses try statement
	#try:
            #from Beta_GUI import betaoutputs
            #elementName = str(betaoutputs.Z)
            #lowerBound = int(betaoutputs.A)
            #higherBound = int(betaoutputs.A)
            #betaVariable = str(betaoutputs.B)
            #energyLim = int(betaoutputs.E)
            #massData = True 
            #wantedSpins=str(betaoutputs.J).replace(" ","")
            #temperature = float(betaoutputs.temp)
        #except:
            #elementName = str(user_ins.Z)
            #FIXME Check what happes for a range of A
            #lowerBound = int(user_ins.isoLow)
            #higherBound = int(user_ins.isoUp)
            #betaVariable = str(user_ins.Beta)
            #energyLim = int(user_ins.E)
            #massData = user_ins.mass
            #wantedSpins=str(user_ins.J).replace(" ","")
            #temperature = float(user_ins.temp)
        #finally:
            #elementName = elementName.title()
            #elementName = elementName.replace(" ","")
            #elementName = elementName.split(',')
            #exitcount = 0

#yana and common ancestor
        elementName = elementName.replace(" ","")
        elementName = elementName.split(',')

#Will and common ancestor
	#temperature = floart(betaoutputs.temp)

        temperature = float(T)
        exitcount = 0

    elif option == "three":
        Z, A, J, T = Parabola_Qt.getparabolaoutputs(gif)
        elementName = str(Z)
        lowerBound = int(A)
        higherBound = int(A)
        energyLim = 0.0
        
#Will uses the following for massData
	#massData = True

	massData = "YES"
        wantedSpins=str(J).replace(" ","")
        elementName = elementName.replace(" ","")
        elementName = elementName.split(',')
        temperature = float(T)
        exitcount = 0
        betaVariable = 'NULL' ## Required parameter of DataClass

#yana comments out the tryAgainCounter and if statement
    #if(type(lowerBound) is int and type(higherBound) is int and type(energyLim) is int):

#Will added this comment
#FIXME not sure what tryAgainCounter actuall does, just plots?
            #tryAgainCounter=0

    ## Create dictionaries of ionization data
    addion.make_ion_dict(temperature)

    #This loop goes through each wanted nuclei in the range of A values and makes the variable to be used (and iterated through) to from b in the a=b expression in data class.
    for element in elementName:
        for i in range(lowerBound,higherBound+1):

            itervar= str(i)+element

            indata=dc.data('ensdf.'+str(i).zfill(3),itervar,option,betaVariable,energyLim)
            indata.filterData(wantedSpins,UI)

#Will uses the following if statement
            ## Include Atomic Mass Energy Data
            #if massData:
                #md.addMass(indata)
            
#yana and common ancestor
            ## Include Atomic Mass Energy Data
            if option == 'one':
                pass
            else:
                md.addMass(indata) 

            ## Include ionization effects
            addion.addIonization(indata) 

            ## export .dat file
            indata.export("_Fil.dat",wantedSpins)

    if UI:
        #readinput.message= "Data export complete"
        exit

    #If wanted this will return the user inputs for further use
    return [elementName,lowerBound,higherBound,wantedSpins,temperature,massData,energyLim,indata.decay]



       
#This function will create a plt file for use in gnuplot to plot data from a eiter filtered data files or the whoel data file. This function is best used if used with datExp.

#yana and common ancestor
def pltFileExp(option,energyLim,temperature,elementName,lowerBound,higherBound,decayType,wantedSpins='',UI=False,fileParsingFactor=0):

#Will uses a different def and then a try statement
#def pltFileExp(option,energyLim,temperature,elementName,lowerBound,higherBound,decayType,wantedSpins='',UI=False,userArgs=None,fileParsingFactor=0):
    
    #try:
        #makePNG = userArgs.png
        #makeGIF = userArgs.gif
    #except AtrributeError: ## GUI used
        #makePNG = True
        #makeGIF = True

    fileParsingFactorStr="_every_"+str(fileParsingFactor)

#Will prints the parsing factor for some reason
    #print(fileParsingFactor)

    tryAgainCounter=1

#Will comments out one of the while loops in favor of the other
#the following is yana and common ancestor
    while(tryAgainCounter and UI):
    #while(tryAgainCounter):
        try:
            fileParsingFactor=int(1)
            fileParsingFactorStr="_every_"+str(fileParsingFactor)
            if(type(fileParsingFactor) is int):
                tryAgainCounter=0
        except:
            print("Invalid Input")

#Will prints another parsing factor
    #print('@x2 %s'%fileParsingFactor)

    elementnamestring = "".join(elementName)
    if len(elementnamestring) > 50:
        elementnamestring = "ALL"

#These loops of (for element in elementName) go through the entire process for each element input. Multiple loops are used
#to ensure data is recorded properly for all elements
    removecount = {}
    removehighcount = {}
    create_file = False
    for element in elementName:
        ##This loop removes all datafiles below the first non-empty one
        removecount[element] = 0
        for i in range(lowerBound,higherBound+1,fileParsingFactor):
            filenameopen = (str(i)+str(element)+wantedSpins+"_Fil.dat").replace('/','_')
            with open("Output/gnuPlot/"+filenameopen, 'r') as datafile:
                first_line = datafile.readline().rstrip()
                first_line = first_line.split(';')

#Will and common ancestor
                #print(first_line)

                nodatatest = str(first_line[2][-2:])
            if (nodatatest == "--" or nodatatest == "-*"):
                os.remove("Output/"+"gnuPlot/"+filenameopen)
                removecount[element] = removecount[element] + 1
            else:
                break
        #This loop removes all datafiles above the last non-empty one
        removehighcount[element] = 0
        for i in range(higherBound,lowerBound-1,-fileParsingFactor):
            filenameopen = (str(i)+str(element)+wantedSpins+"_Fil.dat").replace('/','_')
            if os.path.isfile("Output/gnuPlot/"+filenameopen):
                with open("Output/gnuPlot/"+filenameopen, 'r') as datafile:
                    first_line = datafile.readline().rstrip()
                    first_line = first_line.split(';')
                    nodatatest = str(first_line[2][-2:])
                if (nodatatest == "--" or nodatatest == "-*"):
                    os.remove("Output/"+"gnuPlot/"+filenameopen)
                    removehighcount[element] = removehighcount[element] + 1
                else:
                    break

        #This if statement checks to see if there are any datafiles left to plot. If there are then it runs through the
        #plotting process. If there are none then it displays a statement telling the user that there is nothing to
        #plot and exits the program.
        filenameopen = (str(lowerBound+removecount[element])+str(element)+wantedSpins+"_Fil.dat").replace('/','_')
        fileNameBool = False
        #create_file =os.path.isfile("Output/"+"gnuPlot/"+filenameopen) 
        #if create_file :
        if os.path.isfile("Output/"+"gnuPlot/"+filenameopen):
            if option == "one":
                fileName = str(elementnamestring)+"_"+str(lowerBound)+"to"+str(higherBound)+"_"+wantedSpins+"_"+str(energyLim)+".plt"
                create_file = True
            elif option == "two":
                fileName = "Beta_"+str(lowerBound)+str(elementName[0])+"_"+str(temperature)[:-2]+"K.plt"
                create_file = True
            elif option == "three":
                fileName = "Parabola_"+str(lowerBound)+"_"+str(temperature)[:-2]+"K.plt"
                create_file = True

#Will has this fix me print
            #print(option) #FIXME option is reassigning somehow

            fileName= "Output/gnuPlot/" + fileName.replace('/','_')
            pltFile = open(fileName,'wb')
            

            infile = open(fileName,'r')
            if infile.readline() != "reset":
        # These following lines add the completely nessecary lines in the plt files
        #Reset gnuplot.
                pltFile.write(str.encode("reset\n"))

        #This removes the default legend in the final plot, because the legend is ugly and not useful in our case.
                pltFile.write(str.encode("unset key\n"))

        #This labels the y axis and the Title
                pltFile.write(str.encode("set ylabel \"Energy(keV)\"\n"))

#Will's pltFile.write
                #pltFile.write(str.encode("set term png\n"))

                if option == "one":
                    pltFile.write(str.encode("set title \"Excited States of ^{"+str(lowerBound)+"}"+elementnamestring+" to ^{"+str(higherBound)+"}"+elementnamestring+" with "+wantedSpins+" Spins up to "+str(energyLim)+" keV\"\n"))
                elif option == "two":
                    pltFile.write(str.encode("set title \"B^{"+decayType[-1]+"} Decay Scheme for ^{"+str(lowerBound)+"}"+str(elementName[0])+" at "+str(temperature)+" K\\nup to "+str(energyLim)+" keV Excitation Energy\"\n"))
                    
#yana and common ancestor have this commented out
		    #pltFile.write(str.encode("set title \"Beta Decay Scheme for ^{"+str(lowerBound)+"}"+str(elementName[0])+" and ^{"+str(higherBound)+"}"+str(elementName[1])+" at "+str(temperature)+" K\\nup to "+str(energyLim)+" keV Excitation Energy\"\n"))

                elif option == "three":
                    pltFile.write(str.encode("set title \"Mass Parabola for A = "+str(lowerBound)+" at "+str(temperature)+" K\"\n"))
                else:
                    pltFile.write(str.encode("set title \"Energy levels of "+wantedSpins+" states for "+str(lowerBound)+elementnamestring+" through "+str(higherBound)+elementnamestring+"\"\n"))

        #This tells gnuplot that the delimiter of each column as ,
                pltFile.write(str.encode("set datafile sep ';'\n"))

                pltFile.write(str.encode("set pointsize 0.0001\n"))

                pltFile.write(str.encode('set label "* Extrapolated Mass" at graph 0.01, graph 0.97 left\n'))

                setLine="set xtics right rotate by 45 ("


    ## Option 2 ##
    ## Generate a list of Isotopes for the x axis 
    if option == 'two':
        ## Create a dictionary to index each isotope for plotting
        isotopeLabels = {}
        ## Generate a list of Isotopes for the x axis
        labelsList = []
        numLabels = 0
        checkDaugther = False
        ## Create files for plotting the data and the decay arrows
        plotDataFile = open("Output/gnuPlot/DecayData_plot.dat","w+")
        arrowDataFile = open("Output/gnuPlot/ArrowData_plot.dat","w+")
        for element in elementName:
            for i in range(lowerBound+removecount[element],higherBound-removehighcount[element]+1,fileParsingFactor):
                datafile = open("Output/gnuPlot/"+str(i)+str(element)+wantedSpins.replace('/','_')+"_Fil.dat",'r')
                for line in datafile:
                    line = line.split(';')
                    
                    ## Build dictionary of isotopes
                    if line[0] not in isotopeLabels:
                        numLabels += 1
                        isotopeLabels[line[0]] = numLabels
                        labelsList.append([line[0],line[6]])
                        ionization = line[6].rstrip()
                        ## Create the axis label
                        Aval = ''
                        NameVal = ''
                        for char in line[0]:
                            if char.isnumeric():
                                Aval = Aval + char
                            else:
                                if len(NameVal) == 0:
                                    NameVal += char
                                else:
                                    NameVal += char.lower()
                            
                        setLine = setLine + '"^{%s}%s ^{%s}" %s,' % (Aval, NameVal, ionization, str(isotopeLabels[line[0]]))

                    ## index each state by isotope for plotting by prepending the index
                    lineToWrite = str(isotopeLabels[line[0]])
                    for value in line:
                        lineToWrite = lineToWrite + ';' + str(value)
                    plotDataFile.write(lineToWrite)

                    ## Define data for arrow file
                    if element.upper() in line[0]: ## Parent
                        arrowStart = [isotopeLabels[line[0]],line[1]] ## [x,y]
                    else: ## Daughter
                        arrowEnd = [isotopeLabels[line[0]],line[1]] ## [x,y]
                        arrowLine = str(arrowStart[0])+';'+str(arrowStart[1])+';'+str(arrowEnd[0])+';'+str(arrowEnd[1]) + ';'+str(line[3])
                        arrowDataFile.write(arrowLine+'\n')

        arrowDataFile.close()
        plotDataFile.close()       
        if create_file:
            setLine = setLine[:-1]+')\n'
            pltFile.write(str.encode(setLine))
            pltFile.write(str.encode("set xrange [0:"+str(len(isotopeLabels)+1)+"]\n"))
        #except:
        #    pltFile = open(fileName,'wb')
        #    pltFile.write(str.encode(setLine))
        #    pltFile.write(str.encode("set xrange [0:"+str(len(isotopeLabels)+1)+"]\n"))

            rangecount = len(isotopeLabels)

            ## Continue writing the .plt file
            pltFile.write(str.encode('plot "DecayData_plot.dat" using 1:3:4 with labels left point offset 0.2,0\n'))
            pltFile.write(str.encode('replot "DecayData_plot.dat" using ($1-0.375):3:(0.375):5 with boxxyerrorbars linecolor rgb \'black\' fillstyle solid\n'))
            pltFile.write(str.encode('replot "DecayData_plot.dat" using ($1-0.75):3:(0.75):(0) with vectors nohead linecolor -1\n'))
            pltFile.write(str.encode('replot "DecayData_plot.dat" using ($1-0.75):($3+$5):9 with labels left point offset 0,0.2\n'))
            pltFile.write(str.encode('replot "ArrowData_plot.dat" using 1:2:($3-$1-0.75):($4-$2) with vectors linecolor 1\n'))


            

    ## Options 1 and 3 ##
    #This sets the x axis with the names of the isotpes wanted.
    else:
        rangecount = 0
        mostrecentrangecount = 0
        for element in elementName:
            for i in range(lowerBound+removecount[element],higherBound-removehighcount[element]+1,fileParsingFactor):
                rangecount = rangecount + 1
                datafile = open("Output/gnuPlot/"+str(i)+str(element)+wantedSpins.replace('/','_')+"_Fil.dat",'r')
                datafileline = datafile.readline().split(';')
                ionization = ""
                if option != "one":
                    ionization = datafileline[6].rsplit() ## Remove Newline char
                if(i+fileParsingFactor>higherBound+rangecount):
                    setLine=setLine+"\"^{"+str(i)+"}"+str(element)+" ^{"+ionization+"}\" "+str(i+1-lowerBound-removecount[element]+mostrecentrangecount)+")"
                else:
                    setLine=setLine+"\"^{"+str(i)+"}"+str(element)+" ^{"+str(ionization)+"}\" "+str(i+1-lowerBound-removecount[element]+mostrecentrangecount)+","
            mostrecentrangecount = rangecount
        if create_file:
            setLine = setLine[:-1]+')\n'
            pltFile.write(str.encode(setLine))
            pltFile.write(str.encode("set xrange [0:"+str(rangecount+1)+"]\n"))
    
        itercount = 0
        mostrecentiter = 0
        for element in elementName:
            #This will write the plot coding for the labeling of each energy leven and a line that corrosponds to each one.

            for i in range(lowerBound + removecount[element],higherBound-removehighcount[element]+1,fileParsingFactor):
                if(itercount == 0): 
                    pltFile.write(str.encode(("plot \""+str(i)+str(element)+wantedSpins+"_Fil.dat\" using ("+str(i+1-lowerBound-removecount[element]+mostrecentiter)+"):2:3 with labels left point offset 0.2,0\n").replace('/', '_')))
            
                else:
                    pltFile.write(str.encode(("replot \""+str(i)+str(element)+wantedSpins+"_Fil.dat\" using ("+str(i+1-lowerBound-removecount[element]+mostrecentiter)+"):2:3 with labels left point offset 0.2,0\n").replace('/', '_')))

                pltFile.write(str.encode(("replot \""+str(i)+str(element)+wantedSpins+"_Fil.dat\" using ("+str(i+1-lowerBound-removecount[element]+mostrecentiter)+"-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid\n").replace('/', '_')))

                pltFile.write(str.encode(("replot \""+str(i)+str(element)+wantedSpins+"_Fil.dat\" using ("+str(i+1-lowerBound-removecount[element]+mostrecentiter)+"-0.75):2:(0.75):(0) with vectors nohead linecolor -1\n").replace('/', '_')))

                
                itercount = itercount + 1
            mostrecentiter = itercount   

#yana and common ancestor use if statement                
    if UI:
        print("Program is finished plotting")

#Will uses a try statement
    #try:
#    if UI:
        #This defines the code required for the program to plot the information
        #as a .gif file.
        #Also in here is the font and font size for the .gif file


#Will uses this for the file names and big files
        #fileName = fileName[15:]
        #gif_filename = fileName[:-4]+'.gif'
        #png_filename = fileName[:-4]+'.png'

        #if makePNG:
            #bigfileName = "Large_"+png_filename

#yana and common ancestor use a try statement instead
	#if os.path.isfile(fileName):
        try:
            pltFile.write(str.encode("set term png size 5600,4000\n"))

#yana and common ancestor's filenaming and big files
            fileName = fileName[15:].replace('.plt','.png')
            bigfileName = "Large_"+fileName.replace(".gif",".png")

            pltFile.write(str.encode("set title font \""+os.getcwd()+"/Helvetica.ttf, 95\"\n"))

#yana and common ancestor
#FIXME program stops here

            if os.path.isfile(bigfileName):
                os.remove(bigfileName)
            if rangecount >= 20:
                pltFile.write(str.encode("set term png enhanced font \""+os.getcwd()+"/Helvetica.ttf\" 56\n"))
            elif rangecount >= 15:
                pltFile.write(str.encode("set term png enhanced font \""+os.getcwd()+"/Helvetica.ttf\" 64\n"))
            elif rangecount >= 10:
                pltFile.write(str.encode("set term png enhanced font \""+os.getcwd()+"/Helvetica.ttf\" 70\n"))
            elif rangecount >= 5:
                pltFile.write(str.encode("set term png enhanced font \""+os.getcwd()+"/Helvetica.ttf\" 80\n"))
            else:
                pltFile.write(str.encode("set term png enhanced font \""+os.getcwd()+"/Helvetica.ttf\" 90\n"))
            
            pltFile.write(str.encode("set output "+"'"+bigfileName+"'"+"\n"))
            pltFile.write(str.encode("replot\n"))

#Will uses an if statement
        #if makeGIF:

            pltFile.write(str.encode("set term gif size 840,600\n"))

#yana and common ancestor except for pltFile (all)
            fileName = fileName.replace('.png','.gif')
            pltFile.write(str.encode("set title font \""+os.getcwd()+"/Helvetica.ttf, 15\"\n"))
            if os.path.isfile(fileName):
                os.remove(fileName)

            if rangecount >= 20:
                pltFile.write(str.encode("set term gif enhanced font \""+os.getcwd()+"/Helvetica.ttf\" 7\n"))
            elif rangecount >= 15:
                pltFile.write(str.encode("set term gif enhanced font \""+os.getcwd()+"/Helvetica.ttf\" 8\n"))
            elif rangecount >= 10:
                pltFile.write(str.encode("set term gif enhanced font \""+os.getcwd()+"/Helvetica.ttf\" 10\n"))
            elif rangecount >= 5:
                pltFile.write(str.encode("set term gif enhanced font \""+os.getcwd()+"/Helvetica.ttf\" 12\n"))
            else:
                pltFile.write(str.encode("set term gif enhanced font \""+os.getcwd()+"/Helvetica.ttf\" 15\n"))

#yana and common ancestor
            pltFile.write(str.encode("set output "+"'"+fileName+"'"+"\n"))

#Will
	    pltFile.write(str.encode("set output "+"'"+gif_filename+"'"+"\n"))

            pltFile.write(str.encode("replot\n"))
            pltFile.write(str.encode("set term x11"))
        except:

#yana
            print('Error generating .plt file: {0}'.format(sys.exc_info()))

#common ancestor
            #print('Error generating .plt file')

#Will also uses raise and another print no pltFile before except
	
	    #print('Error generating .plt file.')
            #raise
        exit

#Will doesn't include the final else
    else:
        print("Nothing to plot")
        exit
