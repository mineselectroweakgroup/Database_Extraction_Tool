## Will McD. 5/24/2018
## Provide structure to execute CENDET w/o using a gui

import argparse
import Main

class Inputs:
## this class stores the users input values.    
    def __init__(self):
        self.Z = "pb"
        self.isoLow = 1
        self.isoUp = 299  
        self.E = 2000
        self.exitcount = 0
        self.mass = "NO"
        self.J = "2+"


        #parser allows for easy dynamic handling of bash options
        parser = argparse.ArgumentParser()
        
        parser.add_argument("-x","--elements", help="Element labels of nuclei of interest.")
        parser.add_argument("-al", "--Alow", type=int, help="Minumun atomic mass.")
        parser.add_argument("-ah", "--Ahigh", type=int, help = "Maximum atomic manss.")
        parser.add_argument("-j", "--JPi", help = "Spin and pairity.")
        parser.add_argument("-e", "--energyMax", type=int, help = "Maximum level energy.")
        #parser.add_argument
        
        userin = parser.parse_args()
        
        print(userin)


user_ins = Inputs()
Main.function("one", user_ins)

## main_call is the fuction that calls Main.py
## written such that running CENDETcmd.py from the terminal calls Main.py first, and then creates an Input class instance and retrieves the user's arguments when CENDETcmd.py is executed for the second time from IsotopeDataExporting (near the top of file when parsing user inputs)
#def main_call():
#    def main_call():
#        print('second pass bioch')
#        user_ins = Inputs()
#    Main.function("one")
#
#main_call()
