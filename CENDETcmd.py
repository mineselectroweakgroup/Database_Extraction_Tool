## Will McD. 5/24/2018
## Provide structure to execute CENDET w/o using a gui

import argparse
import sys
import Main

class Inputs:
## this class stores the users input values.    
    def __init__(self):
        #parser allows for easy dynamic handling of bash options
        parser = argparse.ArgumentParser()
        
        ## Set up optional arguments:
        parser.add_argument("-x", dest="elements", help="Element labels of nuclei of interest.")
        parser.add_argument("-a", help='Atomic mass(es).', metavar = 'Amin-Amax OR A')
        parser.add_argument("-j", default='', help = "Spin and parity.", metavar = 'JPi')
        parser.add_argument("-e", dest="maxEnergy", default=9999999, type=int, help = "Maximum level energy in keV.")
        parser.add_argument("-m", action='store_true', help = "Include AMCD mass-energy data")
        
        parser.add_argument('-B', dest='Beta', choices=['+','-'], help="Extract data from Beta+ or Beta-/EC decay record.")

        #FIXME change option for beta prgm

        userin = parser.parse_args()
        print(userin)




        ## Check if no arguments given, if so print the help message
        if len(sys.argv) == 1:
            parser.print_help()
            sys.exit()

        if userin.Beta == None:
            self.option = 'one'
        elif userin.Beta == '-':
            userin.Beta = 'B-'
            self.option = 'two'
        else:
            userin.Beta = 'B+'
            self.option = 'two'

        ## Check if element labels provided
        if userin.elements == None:
            ## Check entire periodic table
            perTabFile = open('ElementList.txt','r')  #FIXME get rid of elementLabels that wont be found (eg Xx)
            userin.elements = perTabFile.readline()
            #print(userin.elements)

        ## Get A_min and A_max from user's -a argument
        A_input = userin.a
        if A_input == None:
            A_min = 1
            A_max = 299
        elif '-' in A_input: ##Range of atomic masses given
            A_min = A_input[:A_input.find('-')]
            if A_min == '':
                A_min = 1
            A_max = A_input[A_input.find('-')+1:]
            if A_max == '':
                A_max = 299
        else: ##Single atomic mass given
            A_min = A_input
            A_max = A_input

        self.Z = userin.elements
        self.isoLow = A_min
        self.isoUp = A_max
        self.E = userin.maxEnergy
        self.J = userin.j
        self.exitcount = 0 #FIXME is this used? it is hardcoded to zero for prgm 2 & 3
        self.mass = userin.m #FIXME boolean instead of "NO"

        self.Beta = userin.Beta
        self.temp = 0 #FIXME new argument


user_ins = Inputs()
Main.function(user_ins.option, user_ins) ##FIXME dont need to pass option separately

## main_call is the fuction that calls Main.py
## written such that running CENDETcmd.py from the terminal calls Main.py first, and then creates an Input class instance and retrieves the user's arguments when CENDETcmd.py is executed for the second time from IsotopeDataExporting (near the top of file when parsing user inputs)
#def main_call():
#    def main_call():
#        print('second pass bioch')
#        user_ins = Inputs()
#    Main.function("one")
#
#main_call()
