import IsotopeDataExporting as ided
import os
import glob
import time
import sys
import renormalize as renorm

def function(option):
#Exports data requested by the user into text files (necessary to generate plots)
    userInput = ided.datExp(option,True,True)

#Prints the user input allowing user to make sure they inputted allowing user
#to check what they input against the plot they are viewing
#The sleep is a pause so the timestamps used work correctly


    renorm.renormalize(userInput[0],userInput[1],userInput[2],userInput[3])

    time.sleep(0.01)

#Makes plot (.012 s)
    ided.pltFileExp(option,userInput[6],userInput[4],userInput[0],userInput[1],userInput[2],userInput[7],userInput[3],True)


#This code creates the .git file which is the actual plot
    os.chdir("Output/gnuPlot")
    directory = os.getcwd()
    try:
        newest = max(glob.iglob(directory+"/*.plt"),key=os.path.getctime)
        newest = newest.replace(os.getcwd()+"/","")
        os.system("gnuplot "+newest)
    except:
        print('No new plot')
    
#This code puts restarts the program so it can be used again
    os.chdir("..")
    os.chdir("..")
    os.system("python3 Main.py "+option)
    newest = "Output/gnuPlot/"+newest.replace(".plt",".gif")
    if os.path.isfile(newest):
        os.system("rm "+newest)
    try:
        os.system("mv Output/gnuPlot/*.dat Output/gnuPlot/OutputData")
        os.system("mv Output/gnuPlot/*.plt Output/gnuPlot/OutputData")
    except:
        pass


option = sys.argv[-1]
function(option)
