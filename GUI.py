from tkinter import *
import searching_function as sf
import isotopeDataExportingDat as ided
root = Tk()
root.title("Data Extraction")
import sys
import os
import glob


#Class used for the first function.
class Application(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)

        self.create_widgets()
        self.grid()



        #Here are the variable declarations for the Nuclear Structure section
        #Rows are seperated by newlines
        self.chemSymVar = StringVar()
        self.lowBoundIsoVar = StringVar()
        self.upBoundIsoVar = StringVar()

        self.spinVar = StringVar()
        self.upBoundEnergyVar = StringVar()
        self.massDataVar = StringVar()

        #Here are the variable declarations for the Decay section
        #Same formatting
        self.qLowVar = StringVar()
        self.qHighVar = StringVar()

        self.aLowVar = StringVar()
        self.aHighVar = StringVar()

        self.exitcount = 0
        

    def create_widgets(self):
        title = Frame(self)
        title.pack(side = TOP)


        #Here I am going to seperate the implementation of Peter's code,
        #my own, and the output text box by using 3 different frames
        nucStruc = Frame(self, padx = 10)
        decay = Frame(self, padx = 10)
        out = Frame(self, pady = 20)
        out.pack(side = BOTTOM)
        nucStruc.pack(side = LEFT)
        decay.pack(side = RIGHT)


        #Here I will set up and place all lables for the nucStruc frame
        #They will be seperated with newlines in this code to represent
        #different rows in the GUI
        nucStrucLable = Label(nucStruc, text = "Evaluated Nuclear Structure Extraction")
        nucStrucLable.grid(columnspan = 2,row = 0,sticky=W)

        chemSymLabel = Label(nucStruc, text = "Element (ex. Zn,Cu,...)")
        chemSymLabel.grid(row = 1, column = 0, sticky = W)
        lowBoundIsoLabel = Label(nucStruc, text = "Lower Bound Isotope")
        lowBoundIsoLabel.grid(row = 1, column = 1, sticky = W)
        upBoundIsoLabel = Label(nucStruc, text = "Upper Bound Isotope")
        upBoundIsoLabel.grid(row = 1, column = 2, sticky = W)

        spinLabel = Label(nucStruc, text = "Spin (ex. 0+,3/2-...")
        spinLabel.grid(row = 3, column = 0, sticky = W)
        upBoundEnergyLabel = Label(nucStruc, text = "Energy Bound (keV)")
        upBoundEnergyLabel.grid(row = 3, column = 1, sticky = W)

        self.checkVar = IntVar()
        self.checkVar = 0
        c = Checkbutton(nucStruc, text="Include Binding",variable=self.checkVar,command=self.checkfunction)
        c.grid(row=4,column=2)


        #Here I will set up and place all the labels for the decay frame
        #Same format as the previous section
        #I'm also going to configure the first column for asthetic purposes

        decay.columnconfigure(0, pad = 10)

        decayLabel = Label(decay, text = "Decay Information")
        decayLabel.grid(row = 0, column = 0, sticky = W)

        qLowLabel = Label(decay, text = "Q Low")
        qLowLabel.grid(row = 1, column = 0, sticky = W)
        qHighLabel = Label(decay, text = "Q High")
        qHighLabel.grid(row = 1, column = 1, sticky = W)

        aLowLabel = Label(decay, text = "A Low")
        aLowLabel.grid(row = 3, column = 0, sticky = W)
        aHighLabel = Label(decay, text = "A High")
        aHighLabel.grid(row = 3, column = 1, sticky = W)


        #Here I will set up all of the entry boxes for nucStruc
        #Same format

        self.chemSymEntry = Entry(nucStruc)
        self.chemSymEntry.grid(row = 2, column = 0, sticky = W)
        self.lowBoundIsoEntry = Entry(nucStruc)
        self.lowBoundIsoEntry.grid(row = 2, column = 1, sticky = W)
        self.upBoundIsoEntry = Entry(nucStruc)
        self.upBoundIsoEntry.grid(row = 2, column = 2, sticky = W)

        self.spinEntry = Entry(nucStruc)
        self.spinEntry.grid(row = 4, column = 0, sticky = W)
        self.upBoundEnergyEntry = Entry(nucStruc)
        self.upBoundEnergyEntry.grid(row = 4, column = 1, sticky = W)


        #Here I will set up all of the entry boxes for decay
        #Same format

        self.qLowEntry = Entry(decay)
        self.qLowEntry.grid(row = 2, column = 0, sticky = W)
        self.qHighEntry = Entry(decay)
        self.qHighEntry.grid(row = 2, column = 1, sticky = W)
        
        self.aLowEntry = Entry(decay)
        self.aLowEntry.grid(row = 4, column = 0, sticky = W)
        self.aHighEntry = Entry(decay)
        self.aHighEntry.grid(row = 4, column = 1, sticky = W)



        #Setting up the submit buttons
        nucStrucSubmit = Button(nucStruc, text = "Submit", command = self.sendNucData)
        nucStrucSubmit.grid(row = 5, column = 0, sticky = W)
        decaySubmit = Button(decay, text = "Submit", command = self.sendDecayData)
        decaySubmit.grid(row = 5, column = 0, sticky = W)

        exitSubmit = Button(out, text = "Exit", command = self.exitButton)
        exitSubmit.grid(row = 0, column = 2, sticky = W)
        fullScreenSubmit = Button(out, text = "Full Screen", command = self.fullScreenButton)
        fullScreenSubmit.grid(row = 1, column = 0)

        newChoiceSubmit = Button(out, text = "Program Selection", command = self.newChoiceButton)
        newChoiceSubmit.grid(row = 1, column = 1)



        #Setting up the output box with scrolling feature
        self.outText = Text(out)
        self.outText.grid(row = 0, column = 1, sticky = W+E+N+S)
        outScroll = Scrollbar(out)
        outScroll.grid(row = 0, column = 1, sticky = E+S+N)
        outScroll.config(command=self.outText.yview)
        self.outText.config(yscrollcommand=outScroll.set)

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
            try:
                self.directory=os.getcwd()
                self.newest = max(glob.iglob(self.directory+"/*.gif"),key=os.path.getctime)
                self.newest = self.newest.replace(os.getcwd()+"/","")
                self.photo = PhotoImage(file=self.newest)
                self.outGraph.create_image(0,0,image=self.photo, anchor = "nw")
            except:
                print("No Image to Display")
        os.chdir("..")
        os.chdir("..")

        self.pictureSpot = Canvas(title,width = 620, height = 100)
        self.pictureSpot.grid(row = 0) 
        self.photo2 = PhotoImage(file = "eilonglogo.gif")
        self.pictureSpot.create_image(0,0,image = self.photo2, anchor = "nw")


            

    #Defining the functions that make the submit buttons do things. 
    def sendNucData(self):
        """Send user input to nuclear structure sorting function"""
        self.outText.delete(0.0,END)
        self.chemSymVar = self.chemSymEntry.get()
        self.lowBoundIsoVar = self.lowBoundIsoEntry.get()
        self.upBoundIsoVar = self.upBoundIsoEntry.get()
        self.spinVar = self.spinEntry.get()
        self.upBoundEnergyVar = self.upBoundEnergyEntry.get()
        root.destroy()#closes window

    def sendDecayData(self):
        """Send user input to decay data sorting function"""
        self.outText.delete(0.0,END)
        self.qLowVar = self.qLowEntry.get()
        self.qHighVar = self.qHighEntry.get()
        self.aLowVar = self.aLowEntry.get()
        self.aHighVar = self.aHighEntry.get()

        self.outText.insert(0.0, sf.acquire(self.qLowVar,self.qHighVar,self.aLowVar,self.aHighVar,Theory = False,Sym = False))

    def exitButton(self):
        self.exitcount = 1
        print("Thanks!")
        root.destroy()

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

    def checkfunction(self):
        if self.checkVar == 0:
            self.checkVar = 1
        else:
            self.checkVar = 0

app = Application(root)
root.protocol("WM_DELETE_WINDOW",app.exitButton)
root.mainloop()

#Need to define a class for the variables output by the gui (the user inputs), to be used in the other scripts

class guioutputs:
#These are the Nuclear Structure (ENSDF inputs) variables
    Z=app.chemSymVar
    isoLow=app.lowBoundIsoVar
    J=app.spinVar
    isoUp=app.upBoundIsoVar
    E=app.upBoundEnergyVar
    exitcount=app.exitcount
    if app.checkVar == 1:
        mass = "YES"
    else:
        mass = "NO"

    ##These if statements either kill the program or input preset values if the
    ##user leaves a section blank.
    if exitcount == 1:
        sys.exit()
    if Z == '' or J == '':
        print("YOU SUCK, FIGURE IT OUT")
        sys.exit()
    if isoLow == '':
        isoLow = 1
    if isoUp == '':
        isoUp = 299
    if E == '':
        E = 9999999
    if mass.upper().replace(" ","") == "YES":
        mass = "YES"
    
    
#These are the Q and A variables for the mass extraction part the program
    Qlow= app.qLowVar
    Qhigh= app.qHighVar
    Alow= app.aLowVar 
    Ahigh= app.aHighVar

