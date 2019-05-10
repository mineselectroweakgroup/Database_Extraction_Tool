import IsotopeDataExporting as ided
import os
import glob
import time
import sys
import renormalize as renorm
import ErrorGUI

def startup(option, gif=""):
#Exports data requested by the user into text files (necessary to generate plots)
    userInput = ided.datExp(option,True,True, gif=gif)
#Prints the user input allowing user to make sure they inputted allowing user
#to check what they input against the plot they are viewing
#The sleep is a pause so the timestamps used work correctly
    if (ided.create_plot):
    
        renorm.renormalize(userInput[0],userInput[1],userInput[2],userInput[3])

        time.sleep(0.01)

#Makes plot
        ided.pltFileExp(option,userInput[6],userInput[4],userInput[0],userInput[1],userInput[2],userInput[7],userInput[3],True)

    else:
        print(ided.create_plot)
        ErrorGUI.App()
        if (ErrorGUI.buttonYes):
            os.system("python StartupQt.py")
            exit() 
        else:
            exit()


#This code creates the .git file which is the actual plot
    os.chdir("Output/gnuPlot")
    directory = os.getcwd()
    try:
        newest = max(glob.iglob(directory+"/*.plt"),key=os.path.getctime)
        newest = newest.replace(os.getcwd()+"/","")
        os.system("gnuplot "+newest)
    except:
        print('No new plot')

    #This code creates the .git file which is the actual plot
    
#This code puts restarts the program so it can be used again
    os.chdir("..")
    os.chdir("..")

    gifFileName = "Output/gnuPlot/"+newest.replace(".plt",".gif")
    startup(option, gif=gifFileName)
