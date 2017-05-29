# -*- coding: utf-8 -*-
import dataClass as dc
import isotopeDataExportingDat as ided
from data_array import final
from searching_function import acquire
import mass_data as md
import os
import glob
import time
import sys




def function(option):

#Exports data requested by the user into text files (necessary to generate plots)
    userInput = ided.datExp(option,True,True)


#Prints the user input allowing user to make sure they inputted allowing user
#to check what they input against the plot they are viewing
#The sleep is a pause so the timestamps used work correctly
    print(userInput)
    time.sleep(0.01)

    md.addMass(userInput[0],userInput[1],userInput[2],userInput[3])

#Makes plot
    ided.pltFileExp(userInput[0],userInput[1],userInput[2],True,userInput[3],True)

#This code creates the .git file which is the actual plot
    os.chdir("Output/gnuPlot")
    directory = os.getcwd()
    newest = max(glob.iglob(directory+"/*"),key=os.path.getctime)
    newest = newest.replace(os.getcwd()+"/","")
    os.system("gnuplot "+newest)

#Optional code used to delete everything but the .git files.
#fileList = glob.glob("*.dat")
#for f in fileList:
    #os.remove(f)
#fileList = glob.glob("*.plt")
#for f in fileList:
    #os.remove(f)

#This code puts restarts the program so it can be used again    
    os.chdir("..")
    os.chdir("..")
    os.system("python3 THIS_WORKS.py "+option)


option = sys.argv[-1]
function(option)

#Problems:
#1. Click the submit button on the left and the GUI closes
#2. Any messages that appear in the shell should appear in textbox
#3. Plots do NOT appear inside GUI
#4. How to handle Theory and Sym inputs
#5. Formatting......

