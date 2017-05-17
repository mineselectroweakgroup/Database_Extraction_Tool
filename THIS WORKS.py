# -*- coding: utf-8 -*-
import dataClass as dc
import isotopeDataExportingDat as ided
from data_array import final
from searching_function import acquire


#Exports data requested by the user into text files (necessary to generate plots)
userInput = ided.datExp(True,True)

print userInput

#Makes plot
ided.pltFileExp(userInput[0],userInput[1],userInput[2],True,userInput[3],True)



#Problems:
#1. Click the submit button on the left and the GUI closes
#2. Any messages that appear in the shell should appear in textbox
#3. Plots do NOT appear inside GUI
#4. Plots all data, should only output evaluated nuclear structure data
#5. Requires inputs into all Evaluated Nuclear Structure fields to produce plots
#6. How to handle Theory and Sym inputs
#7. Formatting......
