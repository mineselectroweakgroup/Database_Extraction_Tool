#This script is a class which opens the GUI for the beta decay subscript of the program. A second class at the bottom contains
#the outputs of the GUI, and is used for passing information to other aspects of the program.

from tkinter import *
root = Tk()
root.title("Data Extraction")
import sys
import os
import glob


#Class used for the beta decay code
class Application(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.configure(bg='#21314D')

        self.create_widgets()
        self.grid()

        self.temp = StringVar()
        
    #This function creates the actual frame for the GUI including the buttons and input boxes
    def create_widgets(self):
        title = Frame(self)
        decay = Frame(self)
        out = Frame(self)
        title.pack(side = TOP)
        decay.pack(side = BOTTOM)
        out.pack(side = BOTTOM)

        title.configure(bg='#21314D')
        decay.configure(bg='#21314D')
        out.configure(bg='#21314D')


        #Set up labels for each section
        decayLabel = Label(decay, text = "Evaluated Beta Decay Information",font=("Helvetica",13,"bold"),bg='#21314D',fg='#92A2BD')
        decayLabel.grid(columnspan = 3,row = 0)

        #Setting up the submit buttons
        minusButton = Button(decay, text = "Beta -", command = self.minusFunc,bg='#92A2BD',fg='#21314D',highlightbackground="#21314D",font=11)
        minusButton.grid(row = 1, column = 0)

        plusButton = Button(decay, text = "Beta +", command = self.plusFunc,bg='#92A2BD',fg='#21314D',highlightbackground="#21314D",font=11)
        plusButton.grid(row = 1, column = 1)

        ECButton = Button(decay, text = "EC Decay", command = self.ECFunc,bg='#92A2BD',fg='#21314D',highlightbackground="#21314D",font=11)
        ECButton.grid(row = 1, column = 2)

        tempButton = Button(decay, text = "Temperature", command = self.tempFunc,bg='#92A2BD',fg='#21314D',highlightbackground="#21314D",font=11)
        tempButton.grid(columnspan = 2, row = 2, column = 0)

        self.tempEntry = Entry(decay,highlightbackground="#21314D")
        self.tempEntry.grid(columnspan = 2, row = 2, column = 1)

        fullScreenSubmit = Button(decay, text = "Full Screen", command = self.fullScreenButton,bg='#92A2BD',fg='#21314D',highlightbackground="#21314D",font=11)
        fullScreenSubmit.grid(row = 3, column = 0)

        newChoiceSubmit = Button(decay, text = "Program Selection", command = self.newChoiceButton,bg='#92A2BD',fg='#21314D',highlightbackground="#21314D",font=11)
        newChoiceSubmit.grid(row = 3, column = 1)

        exitButtonSubmit = Button(decay, text = "Exit", command = self.exitButton,bg='#92A2BD',fg='#21314D',highlightbackground="#21314D",font=11)
        exitButtonSubmit.grid(row=3,column=2)


        #Setting up the graph output box including the calling of the most
        #recent graph to the GUI
        self.outGraph = Canvas(out,width = 700, height = 500)
        self.outGraph.grid(row = 0, column = 0, sticky = W+E+N+S)

        os.chdir("Output/gnuPlot")
        work_path = os.getcwd()
        if os.listdir(work_path) == []:
            print("Directory Empty")
        else:
            self.directory=os.getcwd()
            self.newest = max(glob.iglob(self.directory+"/*"),key=os.path.getctime)
            self.newest = self.newest.replace(os.getcwd()+"/","")
            if self.newest[-4:] != ".gif":
                try:
                    self.newest = "nuclearChart.gif"
                    self.photo = PhotoImage(file=self.newest)
                    self.outGraph.create_image(0,0,image=self.photo, anchor = "nw")
                except:
                    print("No Image to Display")
            elif os.listdir(work_path) == ["Ignore.txt"]:
                print("Directory Empty")
            else:
                try:
                    self.photo = PhotoImage(file=self.newest)
                    self.outGraph.create_image(0,0,image=self.photo, anchor = "nw")
                except:
                    print("No Image to Display")
        os.chdir("..")
        os.chdir("..")

        #Sets up the group logo at the top of the GUI
        self.pictureSpot = Canvas(title,width = 620, height = 90)
        self.pictureSpot.grid(row = 0, column = 0) 
        self.photo2 = PhotoImage(file = "eilonglogo.gif")
        self.pictureSpot.create_image(0,0,image = self.photo2, anchor = "nw")
            

    #Defining the functions that make the submit buttons do things. 
    def minusFunc(self):
        os.system('python3 betaMinusperiodicTableDictionary.py')
        os.system('gnuplot nuclearChart.plt')
        os.system('okular nuclearChart.png')

    def plusFunc(self):
        os.system('python3 betaPlusperiodicTableDictionary.py')
        os.system('gnuplot nuclearChart.plt')
        os.system('okular nuclearChart.png')

    def ECFunc(self):
        os.system('python3 ECperiodicTableDictionary.py')
        os.system('gnuplot nuclearChart.plt')
        os.system('okular nuclearChart.png')

    def tempFunc(self):
        self.temp = self.tempEntry.get()
        os.system('python3 periodicTableDictionary.py')
        os.system('gnuplot nuclearChart.plt')
        os.system('okular nuclearChart.png')
        root.destroy()
        os.system('python3 Decay_Chart_GUI.py')

    def exitButton(self):
        self.exitcount = 1
        print("Thanks!")
        root.destroy()
        sys.exit()

    def fullScreenButton(self):
        os.chdir("Output/gnuPlot")
        directory = os.getcwd()
        newest = max(glob.iglob(directory+"/*"),key=os.path.getctime)
        newest = newest.replace(os.getcwd()+"/","")
        os.system("okular --presentation "+newest+" &")
        os.chdir("..")
        os.chdir("..")

    def newChoiceButton(self):
        self.chemSymVar = "Zn"
        self.A = 10
        self.spinVar = "0+"
        self.exitcount = 1
        root.destroy()
        os.system("python3 USE_THIS.py")
        sys.exit()

#This is the part of the script that actually runs the GUI
app = Application(root)
root.protocol("WM_DELETE_WINDOW",app.exitButton)
root.mainloop()

class outputs:
    T = app.temp
    if T == "":
        T = 0

