# -*- coding: utf-8 -*-
import dataClass as dc
import isotopeDataExportingDat as ided
from data_array import final
from searching_function import acquire
userInput = ['',0,0,'',0]
import os
import glob

    #Exports data requested by the user into text files (necessary to generate plots)
userInput = ided.datExp(True,True)


    #Prints the user input allowing user to make sure they inputted allowing user
    #to check what they input against the plot they are viewing
print userInput
    
    #Makes plot
ided.pltFileExp(userInput[0],userInput[1],userInput[2],True,userInput[3],True)

#This code pulls up the plot in gnuplot and restarts the program
os.chdir("Output/gnuPlot")
directory = os.getcwd()
newest = max(glob.iglob(directory+"/*"),key=os.path.getctime)
newest = newest[55:]
os.system("gnuplot --persist "+newest)
os.chdir("/home/matmarti/Database_Extraction_Tool")
os.system("python THIS_WORKS.py")

#Problems:
#1. Click the submit button on the left and the GUI closes
#2. Any messages that appear in the shell should appear in textbox
#3. Plots do NOT appear inside GUI
#4. How to handle Theory and Sym inputs
#5. Formatting......

