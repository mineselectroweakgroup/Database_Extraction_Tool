from tkinter import *
root = Tk()
root.title("Data Extraction")
import sys
import os
import glob



class Application(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)

        self.create_widgets()
        self.grid()


        self.chemSymVar = StringVar()
        self.A = StringVar()

        self.spinVar = StringVar()
        

    def create_widgets(self):
        title = Frame(self)
        decay = Frame(self)
        out = Frame(self)
        title.pack(side = TOP)
        decay.pack(side = BOTTOM)
        out.pack(side = BOTTOM)


        decayLabel = Label(decay, text = "Evaluated Beta Decay Information")
        decayLabel.grid(columnspan = 3,row = 0)

        chemSymLabel = Label(decay, text = "Parent Nucleus (ex. Zn)")
        chemSymLabel.grid(row = 1, column = 0, sticky = W)
        ALabel = Label(decay, text = "Isotope (ex. 60)")
        ALabel.grid(row = 1, column = 1, sticky = W)

        spinLabel = Label(decay, text = "Spin (ex. 0+,3/2-...")
        spinLabel.grid(row = 1, column = 2, sticky = W)


        #Here I will set up all of the entry boxes for nucStruc
        #Same format

        self.chemSymEntry = Entry(decay)
        self.chemSymEntry.grid(row = 2, column = 0, sticky = W)
        self.AEntry = Entry(decay)
        self.AEntry.grid(row = 2, column = 1, sticky = W)

        self.spinEntry = Entry(decay)
        self.spinEntry.grid(row = 2, column = 2, sticky = W)



        #Setting up the submit buttons
        decaySubmit = Button(decay, text = "Submit", command = self.sendNucData)
        decaySubmit.grid(row = 5, column = 0)

        fullScreenSubmit = Button(decay, text = "Full Screen", command = self.fullScreenButton)
        fullScreenSubmit.grid(row = 5, column = 1)

        newChoiceSubmit = Button(decay, text = "Program Selection", command = self.newChoiceButton)
        newChoiceSubmit.grid(row = 5, column = 2)


        #Setting up the graph output box including the calling of the most
        #recent graph to the GUI
        self.outGraph = Canvas(out,width = 700, height = 500)
        self.outGraph.grid(row = 0, column = 0, sticky = W+E+N+S)

        os.chdir("Output/gnuPlot")
        work_path = os.getcwd()
        if os.listdir(work_path) == []:
            print("Directory Empty")
        elif os.listdir(work_path) == ["Ignore.txt"]:
            print("Directory Empty")
        else:
            self.directory=os.getcwd()
            self.newest = max(glob.iglob(self.directory+"/*"),key=os.path.getctime)
            self.newest = self.newest.replace(os.getcwd()+"/","")
            self.photo = PhotoImage(file=self.newest)
            self.outGraph.create_image(0,0,image=self.photo, anchor = "nw")
        os.chdir("..")
        os.chdir("..")

        self.pictureSpot = Canvas(title,width = 620, height = 100)
        self.pictureSpot.grid(row = 0, column = 0) 
        self.photo2 = PhotoImage(file = "eilonglogo.gif")
        self.pictureSpot.create_image(0,0,image = self.photo2, anchor = "nw")
            

    #Defining the functions that make the submit buttons do things. 
    def sendNucData(self):
        """Send user input to nuclear structure sorting function"""
        self.chemSymVar = self.chemSymEntry.get()
        self.A = self.AEntry.get()
        self.spinVar = self.spinEntry.get()
        root.destroy()#closes window

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

app = Application(root)
root.protocol("WM_DELETE_WINDOW",app.exitButton)
root.mainloop()

#Need to define a class for the variables output by the gui (the user inputs), to be used in the other scripts

class betaoutputs:
#These are the Nuclear Structure (ENSDF inputs) variables
    Z=app.chemSymVar
    A=app.A
    J=app.spinVar

    ##These if statements either kill the program or input preset values if the
    ##user leaves a section blank.
    if Z == '' or J == '' or A == '':
        print("YOU SUCK, FIGURE IT OUT")
        sys.exit()

