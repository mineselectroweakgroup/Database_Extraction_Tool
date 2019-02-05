import IsotopeDataExporting as ided
import os
import glob
import time
import sys
import renormalize as renorm

#common ancestor between beta (Will_Gammas, Will_noGUI and master)
#def function(option):

#beta (Will_Gammas, Will_noGUI and master)
#def function(option,user_args = None):
     ##FIXME only works if none of the GUI's pass a class instance to Main. If we pass instances of the Inputs class (CENDETcmd.py) to Main, then instead of checking if Null, check a membervariable such as user_args.GUI
     #if user_args == None:
         #UI = True
     #else:
         #UI = False

#yana
def startup(option, gif=""):
#Exports data requested by the user into text files (necessary to generate plots)

#yana
    userInput = ided.datExp(option,True,True, gif=gif)
#Will's
    #userInput = ided.datExp(option,user_args,UI)
#common ancestor
    #userInput = ided.datExp(option,True,True)

#Prints the user input allowing user to make sure they inputted allowing user
#to check what they input against the plot they are viewing
#The sleep is a pause so the timestamps used work correctly

    renorm.renormalize(userInput[0],userInput[1],userInput[2],userInput[3])

    time.sleep(0.01)

#Will uses another try loop
#Makes plot
    #try:
        #if user_args.checkplot():
            #ided.pltFileExp(option,userInput[6],userInput[4],userInput[0],userInput[1],userInput[2],userInput[7],userInput[3],UI,user_args)
    #except AttributeError: ## GUI used
        #ided.pltFileExp(option,userInput[6],userInput[4],userInput[0],userInput[1],userInput[2],userInput[7],userInput[3],UI)


#yana and common ancestor
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

#Will uses an if statement
    #This code creates the .git file which is the actual plot
    #if UI == True or user_args.checkplot():
        #os.chdir("Output/gnuPlot")
        #directory = os.getcwd()
    
#This code puts restarts the program so it can be used again
#yana and common ancestor
    os.chdir("..")
    os.chdir("..")

#yana
    gifFileName = "Output/gnuPlot/"+newest.replace(".plt",".gif")
    startup(option, gif=gifFileName)

#common ancestor
    #os.system("python3 Main.py "+option)
    #newest = "Output/gnuPlot/"+newest.replace(".plt",".gif")
    #if os.path.isfile(newest):
        #os.system("rm "+newest)
    #try:
        #os.system("mv Output/gnuPlot/*.dat Output/gnuPlot/OutputData")
        #os.system("mv Output/gnuPlot/*.plt Output/gnuPlot/OutputData")
    #except:
        #pass


#option = sys.argv[-1]
#function(option)

#Will's (double means it was already commented out)
        ##newest = max(glob.iglob(directory+"/*.plt"),key=os.path.getctime)
        ##newest = newest.replace(os.getcwd()+"/","")
        ##os.system("gnuplot %s >> /dev/null" % newest) ## >> supresses the gnuplot PNG unicode in the terminal
    
        #try:
            #newest = max(glob.iglob(directory+"/*.plt"),key=os.path.getctime)
            #newest = newest.replace(os.getcwd()+"/","")
            #os.system("gnuplot %s >> /dev/null" % newest) ## >> supresses the gnuplot PNG unicode in the terminal
        #except:
            #print('No new plot')
        #os.chdir('../..')
        #if UI:
    ##This code puts restarts the program so it can be used again
            #os.system("python3 Main.py "+option)
            #newest = "Output/gnuPlot/"+newest.replace(".plt",".gif")
            #if os.path.isfile(newest):
                #os.system("rm "+newest)
        #else:
            #pass
        #try:
            #os.system("mv Output/gnuPlot/*.dat Output/gnuPlot/OutputData")
            #os.system("mv Output/gnuPlot/*.plt Output/gnuPlot/OutputData")
        #except:
            #raise
    #else:
        #try:
            #os.system("mv Output/gnuPlot/*.dat Output/gnuPlot/OutputData")
        #except:
            raise
## CENDETcmd calls Main.function(...) on its own
## This will stop function(gui_option) from runnning when CENDETcmd imports this file
#gui_option = sys.argv[-1]
#if gui_option in ['one','two','three']:
    #function(gui_option)
#else:
    #pass
