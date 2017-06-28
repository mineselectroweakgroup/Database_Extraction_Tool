import newDataClass as dc
import newIsotopeDataExportingDat as ided
import mass_data as md
import os
import glob
import time
import sys
import ionization as addion
import renormalize as renorm

def function(option):

#Exports data requested by the user into text files (necessary to generate plots)
    userInput = ided.datExp(option,True,True)

#Prints the user input allowing user to make sure they inputted allowing user
#to check what they input against the plot they are viewing
#The sleep is a pause so the timestamps used work correctly

    if userInput[5] == "YES":
        md.addMass(userInput[0],userInput[1],userInput[2],userInput[3])

    addion.addIonization(userInput[0],userInput[1],userInput[2],userInput[3],userInput[4],userInput[5])
    renorm.renormalize(userInput[0],userInput[1],userInput[2],userInput[3])

    time.sleep(0.01)

#Makes plot
    ided.pltFileExp(option,userInput[6],userInput[4],userInput[0],userInput[1],userInput[2],True,userInput[3],True)



#This code creates the .git file which is the actual plot
    os.chdir("Output/gnuPlot")
    directory = os.getcwd()
    newest = max(glob.iglob(directory+"/*"),key=os.path.getctime)
    newest = newest.replace(os.getcwd()+"/","")
    os.system("gnuplot "+newest)

#Optional code used to delete everything but the .gif files.
#fileList = glob.glob("*.dat")
#for f in fileList:
    #os.remove(f)
#fileList = glob.glob("*.plt")
#for f in fileList:
    #os.remove(f)

#This code puts restarts the program so it can be used again    
    try:
        os.system("mv *.dat OutputData")
        os.system("mv *.plt OutputData")
    except:
        pass
    os.chdir("..")
    os.chdir("..")
    os.system("python3 THIS_WORKS.py "+option)
    newest = "Output/gnuPlot/"+newest.replace(".plt",".gif")
    if os.path.isfile(newest):
        os.system("rm "+newest)


        '''
        newestpng = newest.replace(".gif",".png")
        os.system("convert "+newest+ " "+ newestpng)
        os.system("rm "+newest)
        '''


option = sys.argv[-1]
function(option)

#Problems:
#1. Click the submit button on the left and the GUI closes
#2. Any messages that appear in the shell should appear in textbox
#3. Plots do NOT appear inside GUI
#4. How to handle Theory and Sym inputs
#5. Formatting......

