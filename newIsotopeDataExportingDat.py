##ENSDF File: Multiple Data PLT (for gnuplot) File Extractor
##By: Markus Garbiso
##Date Updated: April 26, 2017 by Peter Consalvi
##Date Updated: May 24, 2017 by Matthew Martin

import newDataClass as dc
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
        wantedSpins=str(guioutputs.J).replace(" ","")
        energyLim=int(guioutputs.E)
        elementName = elementName.replace(" ","")
        elementName = elementName.title()
        elementName = elementName.split(',')
        temperature = 0

    if option == "two":
        from Beta_GUI import betaoutputs
        elementName = str(betaoutputs.Z)
        lowerBound = int(betaoutputs.A)
        higherBound = int(betaoutputs.A)
        betaVariable = str(betaoutputs.B)
        energyLim = int(betaoutputs.E)
        massData = "YES"
        elementName = elementName.title()
        wantedSpins=str(betaoutputs.J).replace(" ","")
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
        elementName = elementName.replace(" ","")
        elementName = elementName.split(',')
        temperature = float(betaoutputs.temp)
        exitcount = 0

    if option == "three":
        from Parabola_GUI import parabolaoutputs
        elementName = str(parabolaoutputs.Z)
        lowerBound = int(parabolaoutputs.A)
        higherBound = int(parabolaoutputs.A)
        energyLim = 0.0
        massData = "YES"
        wantedSpins=str(parabolaoutputs.J).replace(" ","")
        elementName = elementName.replace(" ","")
        elementName = elementName.split(',')
        temperature = float(parabolaoutputs.T)
        exitcount = 0


    if(type(lowerBound) is int and type(higherBound) is int and type(energyLim) is int):
            tryAgainCounter=0
    
    #This loop goes through each wanted nuclei in the range of A values and makes the variable to be used (and iterated through) to from b in the a=b expression in data class.
    for element in elementName:
        for i in range(lowerBound,higherBound+1):
            itervar= str(i)+element
            indata=dc.data('ensdf.'+str(i).zfill(3),itervar,'EoL',energyLim)
            indata.filterData(wantedSpins,UI) #FIXME bring back functionality
            indata.export("_Fil.dat",wantedSpins)
            
                
            
    if UI:
        #readinput.message= "Data export complete"
        exit

    
    #If wanted this will return the user inputs for further use
    return [elementName,lowerBound,higherBound,wantedSpins,temperature,massData,energyLim]



       
#This function will create a plt file for use in gnuplot to plot data from a eiter filtered data files or the whoel data file. This function is best used if used with datExp.
def pltFileExp(option,energyLim,temperature,elementName,lowerBound,higherBound,Filter=False,wantedSpins='',UI=False,fileParsingFactor=0):

    fileParsingFactorStr="_every_"+str(fileParsingFactor)

    tryAgainCounter=1
    while(tryAgainCounter and UI):
        try:
            fileParsingFactor=int(1)
            fileParsingFactorStr="_every_"+str(fileParsingFactor)
            if(type(fileParsingFactor) is int):
                tryAgainCounter=0
        except:
            print("Invalid Input")


    elementnamestring = "".join(elementName)
    if len(elementnamestring) > 50:
        elementnamestring = "ALL"

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
                first_line = first_line.split(';')
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
            if os.path.isfile("Output/"+"gnuPlot/"+filenameopen):
                with open("Output/"+"gnuPlot/"+filenameopen, 'r') as datafile:
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
        if os.path.isfile("Output/"+"gnuPlot/"+filenameopen):
            if option == "one":
                fileName = str(elementnamestring)+"_"+str(lowerBound)+"to"+str(higherBound)+"_"+wantedSpins+"_"+str(energyLim)+".plt"
            elif option == "two":
                fileName = "Beta_"+str(lowerBound)+str(elementName[0])+str(elementName[1])+"_"+str(temperature)[:-2]+"K.plt"
            elif option == "three":
                fileName = "Parabola_"+str(lowerBound)+"_"+str(temperature)[:-2]+"K.plt"
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
                pltFile.write(str.encode("set ylabel \"Energy(keV)\"\n"))
                if option == "one":
                    pltFile.write(str.encode("set title \"Excited States of ^{"+str(lowerBound)+"}"+elementnamestring+" to ^{"+str(higherBound)+"}"+elementnamestring+" with "+wantedSpins+" Spins up to "+str(energyLim)+" keV\"\n"))
                elif option == "two":
                    pltFile.write(str.encode("set title \"Beta Decay Scheme for ^{"+str(lowerBound)+"}"+str(elementName[0])+" and ^{"+str(higherBound)+"}"+str(elementName[1])+" at "+str(temperature)+" K\\nup to "+str(energyLim)+" keV Excitation Energy\"\n"))
                elif option == "three":
                    pltFile.write(str.encode("set title \"Mass Parabola for A = "+str(lowerBound)+" at "+str(temperature)+" K\"\n"))
                else:
                    pltFile.write(str.encode("set title \"Energy levels of "+wantedSpins+" states for "+str(lowerBound)+elementnamestring+" through "+str(higherBound)+elementnamestring+"\"\n"))

        #This tells gnuplot that the delimiter of each column as ,
                pltFile.write(str.encode("set datafile sep ';'\n"))

                pltFile.write(str.encode("set pointsize 0.0001\n"))

                pltFile.write(str.encode('set label "* Extrapolated Mass" at graph 0.01, graph 0.97 left\n'))

                setLine="set xtics right rotate by 45 ("



        #This sets the x axis with the names of the isotpes wanted.
    rangecount = 0
    mostrecentrangecount = 0
    for element in elementName:
        for i in range(lowerBound+removecount[element],higherBound-removehighcount[element]+1,fileParsingFactor):
            rangecount = rangecount + 1
            datafile = open("Output/gnuPlot/"+str(i)+str(element)+wantedSpins.replace('/','_')+"_Fil.dat",'r')
            datafileline = datafile.readline().split(';')
            ionization = ""
            if option != "one":
                ionization = datafileline[4][:-1]
            if(i+fileParsingFactor>higherBound+rangecount):
                setLine=setLine+"\"^{"+str(i)+"}"+str(element)+" ^{"+ionization+"}\" "+str(i+1-lowerBound-removecount[element]+mostrecentrangecount)+")"
            else:
                setLine=setLine+"\"^{"+str(i)+"}"+str(element)+" ^{"+ionization+"}\" "+str(i+1-lowerBound-removecount[element]+mostrecentrangecount)+","
        mostrecentrangecount = rangecount


    try:
        pltFile.write(str.encode(setLine[:-1]+")"+"\n"))
        pltFile.write(str.encode("set xrange [0:"+str(rangecount+1)+"]\n"))
    except:
        pass
    
    itercount = 0
    mostrecentiter = 0
    for element in elementName:
        #This will write the plot coding for the labeling of each energy leven and a line that corrosponds to each one.

        for i in range(lowerBound + removecount[element],higherBound-removehighcount[element]+1,fileParsingFactor):
            if(itercount == 0):
                pltFile.write(str.encode(("plot \""+str(i)+str(element)+wantedSpins+"_Fil.dat\" using ("+str(i+1-lowerBound-removecount[element]+mostrecentiter)+"):2:3 with labels left point offset 0.2,0\n").replace('/', '_')))

                pltFile.write(str.encode(("replot \""+str(i)+str(element)+wantedSpins+"_Fil.dat\" using ("+str(i+1-lowerBound-removecount[element]+mostrecentiter)+"-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid\n").replace('/', '_')))                   

                pltFile.write(str.encode(("replot \""+str(i)+str(element)+wantedSpins+"_Fil.dat\" using ("+str(i+1-lowerBound-removecount[element]+mostrecentiter)+"-0.75):2:(0.75):(0) with vectors nohead linecolor -1\n").replace('/', '_')))
            
            else:
                pltFile.write(str.encode(("replot \""+str(i)+str(element)+wantedSpins+"_Fil.dat\" using ("+str(i+1-lowerBound-removecount[element]+mostrecentiter)+"):2:3 with labels left point offset 0.2,0\n").replace('/', '_')))

                pltFile.write(str.encode(("replot \""+str(i)+str(element)+wantedSpins+"_Fil.dat\" using ("+str(i+1-lowerBound-removecount[element]+mostrecentiter)+"-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid\n").replace('/', '_')))

                pltFile.write(str.encode(("replot \""+str(i)+str(element)+wantedSpins+"_Fil.dat\" using ("+str(i+1-lowerBound-removecount[element]+mostrecentiter)+"-0.75):2:(0.75):(0) with vectors nohead linecolor -1\n").replace('/', '_')))
                
            itercount = itercount + 1
        mostrecentiter = itercount   
                
    if UI:
        print("Program is finished plotting")
        #This defines the code required for the program to plot the information
        #as a .gif file.
        #Also in here is the font and font size for the .gif file
        #if os.path.isfile(fileName):
        try:
            pltFile.write(str.encode("set term png size 5600,4000\n"))
            fileName = fileName[15:].replace('.plt','.png')
            bigfileName = "Large_"+fileName.replace(".gif",".png")
            pltFile.write(str.encode("set title font \""+os.getcwd()+"/Helvetica.ttf, 95\"\n"))
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

            pltFile.write(str.encode("set term gif size 840,600\n"))
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
            pltFile.write(str.encode("set output "+"'"+fileName+"'"+"\n"))
            pltFile.write(str.encode("replot\n"))
            pltFile.write(str.encode("set term x11"))
        except:
            pass
        exit

    else:
        print("Nothing to plot")
        exit


#To make poster graphics, comment out the previous section and uncomment this. This will
#make the graphic significantly more detailed and large enough to not lose clarity on
#a poster. You will also need to switch the title font size line above for this purpose
#NOTE: This will screw up the resolution for the GUIs and only show part of the image
    '''
    if UI:
        print("Program is finished plotting")
        #This defines the code required for the program to plot the information
        #as a .gif file.
        #Also in here is the font and font size for the .gif file
        #if os.path.isfile(fileName):
        try:
            pltFile.write(str.encode("set term gif size 5600,4000\n"))
            fileName = fileName.replace('.plt','.gif')
            fileName = fileName[15:]
            if os.path.isfile(fileName):
                os.remove(fileName)
            if rangecount >= 20:
                pltFile.write(str.encode("set term gif enhanced font \""+os.getcwd()+"/Helvetica.ttf\" 56\n"))
            elif rangecount >= 15:
                pltFile.write(str.encode("set term gif enhanced font \""+os.getcwd()+"/Helvetica.ttf\" 64\n"))
            elif rangecount >= 10:
                pltFile.write(str.encode("set term gif enhanced font \""+os.getcwd()+"/Helvetica.ttf\" 70\n"))
            elif rangecount >= 5:
                pltFile.write(str.encode("set term gif enhanced font \""+os.getcwd()+"/Helvetica.ttf\" 80\n"))
            else:
                pltFile.write(str.encode("set term gif enhanced font \""+os.getcwd()+"/Helvetica.ttf\" 90\n"))
            pltFile.write(str.encode("set output "+"'"+fileName+"'"+"\n"))
            pltFile.write(str.encode("refresh\n"))
            pltFile.write(str.encode("set term x11"))
        except:
            pass
        exit
    
    else:
        print("Nothing to plot")
        exit
    '''
