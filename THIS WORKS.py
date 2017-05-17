# -*- coding: utf-8 -*-
import dataClass as dc
import isotopeDataExportingDat as ided
from data_array import final
from searching_function import acquire


#Exports data requested by the user into text files (necessary to generate plots)
userInput = ided.datExp(True,True)


#Prints the user input allowing user to make sure they inputted allowing user
#to check what they input against the plot they are viewing
print userInput


#Makes plot
ided.pltFileExp(userInput[0],userInput[1],userInput[2],True,userInput[3],True)



#Problems:
#1. Click the submit button on the left and the GUI closes
#2. Any messages that appear in the shell should appear in textbox
#3. Plots do NOT appear inside GUI
#4. How to handle Theory and Sym inputs
#5. Formatting......
