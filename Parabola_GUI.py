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


        self.chemSymVar = StringVar()
        self.A = StringVar()
        self.T = StringVar()
        

    def create_widgets(self):
        decay = Frame(self)
        out = Frame(self)
        decay.pack(side = BOTTOM)
        out.pack(side = TOP)

        decay.configure(bg='#21314D')
        out.configure(bg='#21314D')


        decayLabel = Label(decay, text = "Extracted Mass Parabola Data",font=("Helvetica",13,"bold"),bg='#21314D',fg='#92A2BD')
        decayLabel.grid(columnspan = 3,row = 0)

        ALabel = Label(decay, text = "Mass",bg='#21314D',fg='#92A2BD',font=11)
        ALabel.grid(row = 1, column = 0, sticky = W)

        TLabel = Label(decay, text = "Temp (K)", bg = '#21314D', fg = '#92A2BD', font = 11)
        TLabel.grid(row = 1, column = 1 , sticky = W,padx=5)

        #Here I will set up all of the entry boxes for nucStruc
        #Same format

        self.AEntry = Entry(decay,highlightbackground="#21314D",width=10)
        self.AEntry.grid(row = 2, column = 0, sticky = W)
        self.TEntry = Entry(decay,highlightbackground="#21314D",width=10)
        self.TEntry.grid(row = 2, column = 1, sticky = W,padx=5)



        #Setting up the submit buttons
        decaySubmit = Button(decay, text = "Submit", command = self.sendNucData,bg='#92A2BD',fg='#21314D',highlightbackground="#21314D",font=11,width=6)
        decaySubmit.grid(rowspan = 2, row = 1, column = 2,sticky = S,padx=5)

        fullScreenSubmit = Button(decay, text = "Full", command = self.fullScreenButton,bg='#92A2BD',fg='#21314D',highlightbackground="#21314D",font=11,width=6)
        fullScreenSubmit.grid(row = 5, column = 0,pady = 5)

        newChoiceSubmit = Button(decay, text = "Main", command = self.newChoiceButton,bg='#92A2BD',fg='#21314D',highlightbackground="#21314D",font=11,width=6)
        newChoiceSubmit.grid(row = 5, column = 1,padx=5)

        exitButtonSubmit = Button(decay, text = "Exit", command = self.exitButton,bg='#92A2BD',fg='#21314D',highlightbackground="#21314D",font=11,width=6)
        exitButtonSubmit.grid(row=5,column=2,padx=5)


        #Setting up the graph output box including the calling of the most
        #recent graph to the GUI
        self.outGraph = Canvas(out,width = 840, height = 600)
        self.outGraph.grid(row = 0, column = 0, sticky = W+E+N+S)

        os.chdir("Output/gnuPlot")
        work_path = os.getcwd()
        if os.listdir(work_path) == []:
            print("Directory Empty")
        else:
            self.directory=os.getcwd()
            self.newest = max(glob.iglob(self.directory+"/*"),key=os.path.getctime)
            self.newest = self.newest.replace(os.getcwd()+"/","")
            if self.newest[-4:] != ".gif" or self.newest == "nuclearChart.gif":
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
                    self.photo = self.photo.zoom(1)
                    self.photo = self.photo.subsample(1)
                    self.outGraph.create_image(0,0,image=self.photo, anchor = "nw")
                except:
                    print("No Image to Display")
        os.chdir("..")
        os.chdir("..")
            

    #Defining the functions that make the submit buttons do things. 
    def sendNucData(self):
        """Send user input to nuclear structure sorting function"""
        self.A = self.AEntry.get()
        self.T = self.TEntry.get()
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
        newest = newest.replace(os.getcwd()+"/","").replace(".gif",".png")
        newest = "Large_"+newest
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

class parabolaoutputs:
#These are the Nuclear Structure (ENSDF inputs) variables
    periodicTable=open("ElementList.txt",'r')
    Z = periodicTable.readline()
    Z = Z.strip()
    A=app.A
    J=""
    T=app.T

    ##These if statements either kill the program or input preset values if the
    ##user leaves a section blank.
    if A == '':
        print("YOU SUCK, FIGURE IT OUT")
        sys.exit()
    if T == '':
        T = 0

