##ENSDF File: Multiple Data PLT (for gnuplot) File Extractor
##By: Markus Garbiso
##Date Updated: April 26, 2017 by Peter Consalvi
##Date Updated: May 24, 2017 by Matthew Martin

import dataClass as dc
import os
import re



#This function is used to bulk export a range of isotopes in a given A range.
def datExp(option,UI=False,Filter=False):

#This uses the option from the first GUI to get inputs from the correct GUI. Some of the definitions here are
#used to maintain full use of Markus' code, such as the definition of higherBound in Beta_GUI
    tryAgainCounter=1
    if option == "one":
        from GUI import guioutputs
        elementName= str(guioutputs.Z)
        lowerBound = int(guioutputs.isoLow)
        higherBound = int(guioutputs.isoUp)
        energyLim = int(guioutputs.E)
        exitcount = int(guioutputs.exitcount)
        massData = str(guioutputs.mass)
        if(Filter):
            wantedSpins=str(guioutputs.J)
            energyLim=int(guioutputs.E)
        elementName = elementName.replace(" ","")
        elementName = elementName.split(',')

    if option == "two":
        from Beta_GUI import betaoutputs
        elementName = str(betaoutputs.Z)
        lowerBound = int(betaoutputs.A)
        higherBound = int(betaoutputs.A)
        betaVariable = str(betaoutputs.B)
        energyLim = 9999999
        massData = "YES"
        if(Filter):
            wantedSpins=str(betaoutputs.J)
        perTable = open("ElementList.txt","r")
        periodicTable = perTable.readline()
        periodicTable = periodicTable.split(',')
        for item in periodicTable:
            if item == elementName:
                index = periodicTable.index(item)
                if betaVariable == "Beta +":
                    elementName = periodicTable[index-1] + "," + elementName
                if betaVariable == "Beta -":
                    elementName = elementName + "," + periodicTable[index+1]
        elementName = elementName.replace(" ","")
        elementName = elementName.split(',')
        exitcount = 0

    if(type(lowerBound) is int and type(higherBound) is int and type(energyLim) is int):
            tryAgainCounter=0
    
    #This loop goes through each wanted nuclei in the range of A values and makes the variable to be used (and iterated through) to from b in the a=b expression in data class.
    for element in elementName:
        for i in range(lowerBound,higherBound+1):
            itervar= str(i)+element
            try:
                indata=dc.data('ensdf.'+str(i).zfill(3),itervar,'EoL',energyLim)
                if(Filter):
                    indata.filterData(wantedSpins,UI) 
                    indata.export("_Fil.dat",wantedSpins)
                else:
                    indata.export(".dat")
            except:
                if(UI):
                    ERROR="No file found for or error with " +'ensdf.'+str(i).zfill(3)##Allows the user to see if a specific ENSDF file is giving them trouble.
                    print(ERROR)
                
            
    if UI:
        #readinput.message= "Data export complete"
        exit

    
    #If wanted this will return the user inputs for further use
    return [elementName,lowerBound,higherBound,wantedSpins,exitcount,massData]



       
#This function will create a plt file for use in gnuplot to plot data from a eiter filtered data files or the whoel data file. This function is best used if used with datExp.
def pltFileExp(massInclude,elementName,lowerBound,higherBound,Filter=False,wantedSpins='',UI=False,fileParsingFactor=0):

    fileParsingFactorStr="_every_"+str(fileParsingFactor)

    if(Filter):#Program will ask the user if they only want to include only every other every single file or on and on.
               #Currently this parameter is fixed so the user does not have an option, its set to include every file.
        tryAgainCounter=1
        while(tryAgainCounter and UI):
            try:
                fileParsingFactor=int(1)
                fileParsingFactorStr="_every_"+str(fileParsingFactor)
                if(type(fileParsingFactor) is int):
                    tryAgainCounter=0
            except:
                print("Invalid Input")
    else:
        fileParsingFactor=1

    elementnamestring = "".join(elementName)

#These loops of (for element in elementName) go through the entire process for each element input. Multiple loops are used
#to ensure data is recorded properly for all elements
    removecount = {}
    removehighcount = {}
    for element in elementName:
        ##This loop removes all datafiles below the first non-empty one
        removecount[element] = 0
        for i in range(lowerBound,higherBound+1,fileParsingFactor):
            filenameopen = (str(i)+str(element)+wantedSpins+"_Fil.dat").replace('/','_')
            with open("Output/"+"gnuPlot/"+filenameopen, 'r') as datafile:
                first_line = datafile.readline().rstrip()
            nodatatest = str(first_line[-2:])
            if (nodatatest == "--" or nodatatest == "-*"):
                os.remove("Output/"+"gnuPlot/"+filenameopen)
                removecount[element] = removecount[element] + 1
            else:
                break
        #This loop removes all datafiles above the last non-empty one
        removehighcount[element] = 0
        for i in range(higherBound,lowerBound-1,-fileParsingFactor):
            filenameopen = (str(i)+str(element)+wantedSpins+"_Fil.dat").replace('/','_')
            if os.path.isfile("Output/"+"gnuPlot/"+filenameopen):
                with open("Output/"+"gnuPlot/"+filenameopen, 'r') as datafile:
                    first_line = datafile.readline().rstrip()
                nodatatest = str(first_line[-2:])
                if (nodatatest == "--" or nodatatest == "-*"):
                    os.remove("Output/"+"gnuPlot/"+filenameopen)
                    removehighcount[element] = removehighcount[element] + 1
                else:
                    break

        #This if statement checks to see if there are any datafiles left to plot. If there are then it runs through the
        #plotting process. If there are none then it displays a statement telling the user that there is nothing to
        #plot and exits the program.
        filenameopen = (str(lowerBound+removecount[element])+str(element)+wantedSpins+"_Fil.dat").replace('/','_')
        if os.path.isfile("Output/"+"gnuPlot/"+filenameopen):
            #plt file Naming
            if(Filter):
                fileName= str(lowerBound)+str(elementnamestring)+"_"+str(higherBound)+str(elementnamestring)+wantedSpins+fileParsingFactorStr+"_Fil.plt"        
                fileName= "Output/" + "gnuPlot/" + fileName.replace('/','_')
                pltFile = open(fileName,'wb')
            else:
                fileName= str(lowerBound)+str(elementnamestring)+"_"+str(higherBound)+str(element)+".plt"
                fileName= "Output/" + "gnuPlot/" + fileName.replace('/','_')
                pltFile = open(fileName,'wb')

            infile = open(fileName,'r')
            if infile.readline() != "reset":
        # These following lines add the completely nessecary lines in the plt files
        #Reset gnuplot.
                pltFile.write(str.encode("reset\n"))


        #This removes the default legend in the final plot, because the legend is ugly and not useful in our case.
                pltFile.write(str.encode("unset key\n"))

        #This labels the y axis and the Title
                if massInclude == "YES":
                    pltFile.write(str.encode("set ylabel \"Energy(MeV)\"\n"))
                else:
                    pltFile.write(str.encode("set ylabel \"Energy(keV)\"\n"))
                pltFile.write(str.encode("set title \"Energy levels of "+wantedSpins+" states for "+str(lowerBound)+elementnamestring+" through "+str(higherBound)+elementnamestring+"\"\n"))

        #This line Currently DOES NOT work but should make the graph greyscale.
                pltFile.write(str.encode("set palette gray\n"))

        #This tells gnuplot that the delimiter of each column as ,
                pltFile.write(str.encode("set datafile sep ','\n"))

                pltFile.write(str.encode("unset bars \n"))

                setLine="set xtics rotate by 45 offset -2.0,-1.4 ("
        else:
            fileName = "THIS FILE DOES NOT EXIST, MUAHAHAHAHAHAHAAHA"

        #This sets the x axis with the names of the isotpes wanted.
    rangecount = 0
    mostrecentrangecount = 0
    for element in elementName:
        for i in range(lowerBound+removecount[element],higherBound-removehighcount[element]+1,fileParsingFactor):
            rangecount = rangecount + 1
            if(i+fileParsingFactor>higherBound+rangecount):
                setLine=setLine+"\""+str(i)+str(element)+"\" "+str(i+1-lowerBound-removecount[element]+mostrecentrangecount)+")"
            else:
                setLine=setLine+"\""+str(i)+str(element)+"\" "+str(i+1-lowerBound-removecount[element]+mostrecentrangecount)+","
        mostrecentrangecount = rangecount

    if os.path.isfile(fileName):
        pltFile.write(str.encode(setLine[:-1]+")"+"\n"))
        pltFile.write(str.encode("set xrange [0:"+str(rangecount+1)+"]\n"))
    
    itercount = 0
    mostrecentiter = 0
    for element in elementName:
        #This will write the plot coding for the labeling of each energy leven and a line that corrosponds to each one.
        for i in range(lowerBound + removecount[element],higherBound-removehighcount[element]+1,fileParsingFactor):
            if(itercount == 0):
                if(Filter):
                    pltFile.write(str.encode(("plot \""+str(i)+str(element)+wantedSpins+"_Fil.dat\" using ("+str(i+1-lowerBound-removecount[element]+mostrecentiter)+"):2:3 with labels left point offset character " + str(fileParsingFactor) + ",character 0.2\n").replace('/', '_')))
                    pltFile.write(str.encode(("replot \""+str(i)+str(element)+wantedSpins+"_Fil.dat\" using ("+str(i+1-lowerBound-removecount[element]+mostrecentiter)+"):2:("+str(fileParsingFactor*0.5)+") with xerrorbars\n").replace('/', '_')))
                else:
                    pltFile.write(str.encode("plot \""+str(i)+str(element)+".dat\" using ("+str(i+1-lowerBound-removecount[element]+mostrecentiter)+"):2:3 with labels left point offset character " + str(fileParsingFactor) + ",character 0.2\n"))
                    pltFile.write(str.encode("replot \""+str(i)+str(element)+".dat\" using ("+str(i+1-lowerBound-removecount[element]+mostrecentiter)+"):2:("+str(fileParsingFactor*0.5)+") with xerrorbars\n"))
            else:
                if(Filter):
                    pltFile.write(str.encode(("replot \""+str(i)+str(element)+wantedSpins+"_Fil.dat\" using ("+str(i+1-lowerBound-removecount[element]+mostrecentiter)+"):2:3 with labels left point offset character " + str(fileParsingFactor) + ",character 0.2\n").replace('/', '_')))
                    pltFile.write(str.encode(("replot \""+str(i)+str(element)+wantedSpins+"_Fil.dat\" using ("+str(i+1-lowerBound-removecount[element]+mostrecentiter)+"):2:("+str(fileParsingFactor*0.5)+") with xerrorbars\n").replace('/', '_')))
                else:
                    pltFile.write(str.encode("replot \""+str(i)+str(element)+".dat\" using ("+str(i+1-lowerBound-removecount[element]+mostrecentiter)+"):2:3 with labels left point offset character " + str(fileParsingFactor) + ",character 0.2\n"))
                    pltFile.write(str.encode("replot \""+str(i)+str(element)+".dat\" using ("+str(i+1-lowerBound-removecount[element]+mostrecentiter)+"):2:("+str(fileParsingFactor*0.5)+") with xerrorbars\n"))
            itercount = itercount + 1
        mostrecentiter = itercount
            
                      
    if UI:
        print("Program is finished plotting")
        #This defines the code required for the program to plot the information
        #as a .gif file.
        #Also in here is the font and font size for the .gif file
        if os.path.isfile(fileName):
            fileName = fileName.replace('.plt','.gif')
            fileName = fileName[15:]
            if os.path.isfile(fileName):
                os.remove(fileName)
            if rangecount >= 20:
                pltFile.write(str.encode("set term gif font \""+os.getcwd()+"/Helvetica.ttf\" 6\n"))
            elif rangecount >= 15:
                pltFile.write(str.encode("set term gif font \""+os.getcwd()+"/Helvetica.ttf\" 7\n"))
            elif rangecount >= 10:
                pltFile.write(str.encode("set term gif font \""+os.getcwd()+"/Helvetica.ttf\" 9\n"))
            elif rangecount >= 5:
                pltFile.write(str.encode("set term gif font \""+os.getcwd()+"/Helvetica.ttf\" 12\n"))
            else:
                pltFile.write(str.encode("set term gif font \""+os.getcwd()+"/Helvetica.ttf\" 14\n"))
            pltFile.write(str.encode("set term gif size 700,500\n"))
            pltFile.write(str.encode("set output "+"'"+fileName+"'"+"\n"))
            pltFile.write(str.encode("replot\n"))
            pltFile.write(str.encode("set term x11"))
        exit

    
    else:
        print("Nothing to plot")
        exit
